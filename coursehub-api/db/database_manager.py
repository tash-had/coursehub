"""Basic DataBase for a comment"""

import sqlite3
from sqlite3 import Error


class DatabaseManager:
    """ The medium through which one should communicate to the db """
    def __init__(self, db_name="coursehub.db"):
        import os
        base_path = os.path.dirname(os.path.abspath(__file__)) + "/"
        self._db_path = base_path + db_name
        self.db_conn = sqlite3.connect(self._db_path)
        if self.db_conn is None:
            raise sqlite3.DatabaseError("Could not establish a connection to the database.")

    def create_table(self, instructions):
        """ create a table from the create_table_sql statement
        :param instructions: a CREATE TABLE statement
        :return:
        """
        try:
            c = self.db_conn.cursor()
            return c.execute(instructions)
        except Error as e:
            print(e)
        return None


class CommentdatabaseWorker(DatabaseManager):
    """Contains the functions to add to and retrieve from the database"""

    def __init__(self):
        DatabaseManager.__init__(self)

    def insert_comment(self, data):
        """ Insert data into the comments table

        :param dict data: Keys: [id, course_id, comment, timestamp, votes]
        :return:
        """

        comment_id = data["id"]
        course_id = data["course_id"]
        comment = data["comment"]
        time = data["timestamp"]
        votes = data["votes"]

        input_data = [comment_id, course_id, comment, time, votes]

        c = self.db_conn.cursor()
        c.execute('insert into comments (id, course_id, commment, timestamp, votes) values (?,?,?,?,?)', input_data)
        self.db_conn.commit()
        c.close()

    def get_comments_for_course(self, course_id):
        """
        Get all comments for a specific course

        :param str course_id: course we are retrieving data for
        :return:
        """
        cur = self.db_conn.cursor()
        cur.execute("SELECT * FROM comments WHERE course_id=?", [course_id])

        results = cur.fetchall()
        if results is None:
            return []
        return results

    def get_comment_by_id(self, comment_id):
        """Return the comment in the database that corresponds to comment_id.

        :param comment_id:
        :return:
        """
        cur = self.db_conn.cursor()
        comment = cur.execute('SELECT * FROM comments WHERE id=?', comment_id).fetchone()

        cur.close()
        return comment

    def upvote(self, comment_id):
        """

        :param comment_id:
        :return: new score
        """
        # update the comment with comment_id by a value of 1

        cur = self.db_conn.cursor()
        current_votes = cur.execute('SELECT votes FROM comments WHERE id=?', comment_id).fetchone()
        update = cur.execute('UPDATE comments SET votes=? WHERE id=?', [current_votes[0] + 1, comment_id]).fetchone()
        self.db_conn.commit()

        return update[0]

    def downvote(self, comment_id):
        """

        :param comment_id:
        :return: new score
        """
        # update the comment with comment_id by decreasing by a value of 1

        cur = self.db_conn.cursor()
        current_votes = cur.execute('SELECT votes FROM comments WHERE id=?', comment_id).fetchone()
        update = cur.execute('UPDATE comments SET votes=? WHERE id=?', [current_votes[0] - 1, comment_id]).fetchone()
        self.db_conn.commit()

        return update[0]


class CoursedatabaseWorker(DatabaseManager):
    """Updates and gets course information in the course database"""
    def __init__(self):
        DatabaseManager.__init__(self)

    def get_course_data(self, course_code):
        """
        Query courses based on course code

        :param str course_code: course we are retrieving
        :return:
        """
        cur = self.db_conn.cursor()
        cur.execute("SELECT * FROM courses WHERE course_code=?", [course_code])

        results = cur.fetchall()
        cur.close()
        if results is None:
            return []
        return results

    def update_rating(self, course_id, new_workload, new_recommend):
        """Update the rating for course with course_id

        :param course_id: id of the course whos rating we want to update
        :param new_workload:
        :param new_recommend:
        :return: the udpated rating for that course
        """

        cur = self.db_conn.cursor()
        current_workload_rating = cur.execute("SELECT workload_rating FROM courses WHERE course_id=?",
                                              ([course_id])).fetchone()
        current_recommend_rating = cur.execute("SELECT recommendation_rating FROM courses WHERE course_id=?",
                                              ([course_id])).fetchone()
        current_num_ratings = cur.execute("SELECT num_ratings FROM courses WHERE course_id=?", ([course_id])).fetchone()

        updated_workload_rating = int(current_workload_rating[0]) * current_num_ratings[0] + new_workload \
                         / current_num_ratings[0] + 1
        updated_recommend_rating = int(current_recommend_rating[0]) * current_num_ratings[0] + new_recommend \
                         / current_num_ratings[0] + 1

        cur.execute("UPDATE courses SET workload_rating=? WHERE course_id=?", ([updated_workload_rating, course_id]))
        cur.execute("UPDATE courses SET recommendation_rating=? WHERE course_id=?", ([updated_recommend_rating,
                                                                                      course_id]))
        cur.execute("UPDATE courses SET num_ratings=? WHERE course_id=?", ([current_num_ratings[0] + 1, course_id]))

        self.db_conn.commit()

        results = cur.fetchall()
        cur.close()

        return results

    def get_courses_that_match(self, match):
        """Get all the courses in the database that string match with match

        :param match:
        :return: list of tuples
        """
        cur = self.db_conn.cursor()
        results = cur.execute('SELECT * FROM courses WHERE course_code LIKE %?%', match).fetchall()
        cur.close()

        return results


class _CourseHubDatabaseInitializer:
    """ A set of functions to help setup the database. Use cautiously. """

    def __init__(self, drop_courses_table=False):
        self.db_manager = DatabaseManager()
        if drop_courses_table:
            conn = self.db_manager.db_conn
            conn.execute("DROP TABLE courses")
            conn.close()

        self.create_tables()

    def set_course_ratings(self, tuple_of_info):
        """Initally sets the course rating using the information gathered from the course evals.

        :param tuple_of_info: tuple that contains workload_rating, recomendation_rating, num_ratings and course code
        :return:
        """
        # set the database values using info in the tuple
        cur = self.db_manager.db_conn.cursor()
        workload = tuple_of_info[0]
        recommend = tuple_of_info[1]
        total = tuple_of_info[2]
        course = tuple_of_info[3]
        cur.execute('UPDATE course SET workload_rating = ? WHERE code = ?', [workload, course])
        cur.execute('UPDATE course SET recommendation_rating = ? WHERE code = ?', [recommend, course])
        cur.execute('UPDATE course SET num_ratings = ? WHERE code = ?', total)
        combined_rating = (workload + recommend) / 2
        cur.execute('UPDATE course SET overall_rating = ? over WHERE code = ?', [combined_rating, course])

        self.db_manager.db_conn.commit()
        cur.close()

    def insert_course(self, data):
        """ Insert data into the table

        :param dict data: Keys: [courseId, org_name, course_title, code, course_description]
        :return:
        """

        course_id = data["course_id"]
        org_name = data["org_name"]
        course_title = data["course_title"]
        code = data["course_code"]
        course_description = data["course_description"]

        input_data = [course_id, code, course_description, course_title, org_name, 0, 0, 0, 0]

        c = self.db_manager.db_conn.cursor()
        course_exists = c.execute('SELECT * FROM courses WHERE id = ?', [str(course_id)])

        # NOTE: this will makesure the same course in two different sections don't both get added.
        if course_exists.fetchall() is None:
            c.execute('insert into courses values (?,?,?,?,?,?,?,?,?)', input_data)

        self.db_manager.db_conn.commit()
        c.close()

    def create_tables(self):
        """ Creates the comment and course tables in the db """

        comment_table = """  CREATE TABLE IF NOT EXISTS comments(
            id text PRIMARY KEY,
            course_id text,
            comment text,
            timestamp integer,
            votes integer);
        """

        course_table = """
        CREATE TABLE IF NOT EXISTS courses(
            id text PRIMARY KEY,
            course_code text,
            course_description text,
            course_title text,
            org_name text,
            workload_rating float,
            recommendation_rating float,
            overall_rating float,
            num_ratings integer);
        """
        self.db_manager.create_table(comment_table)
        self.db_manager.create_table(course_table)
