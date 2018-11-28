from db.database_manager import DatabaseManager


class _CourseHubDatabaseInitializer:
    """ A set of functions to help setup the database. Use cautiously. """

    def __init__(self, drop_courses_table=False):
        self.db_manager = DatabaseManager()
        if drop_courses_table:
            conn = self.db_manager.db_conn
            conn.execute("DROP TABLE courses")
            conn.close()

        self.create_tables()

    def set_course_ratings(self, data):
        """Initally sets the course rating using the information gathered from the course evals.

        :param data: dictionary that contains course code as key to a tuple with ratings
        :return:
        """
        # set the database values using info in the tuple
        cur = self.db_manager.db_conn.cursor()
        for key in data.keys():
            tuple_of_info = data[key]
            workload = tuple_of_info[0]
            recommend = tuple_of_info[1]
            total = tuple_of_info[2]
            cur.execute('UPDATE courses SET workload_rating = ? WHERE course_code = ?', [workload, key])
            cur.execute('UPDATE courses SET recommendation_rating = ? WHERE course_code = ?', [recommend, key])
            cur.execute('UPDATE courses SET num_ratings = ? WHERE course_code = ?', [total, key])
            combined_rating = (workload + recommend) / 2
            cur.execute('UPDATE courses SET overall_rating = ? WHERE course_code = ?', [combined_rating, key])
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
        if course_exists.fetchall() == []:
            c.execute('insert into courses (id, course_code, course_description, course_title, org_name,'
                      'workload_rating, recommendation_rating, overall_rating, num_ratings) values (?,?,?,?,?,?,?,?,?)',
                      input_data)

        self.db_manager.db_conn.commit()
        c.close()

    def create_tables(self):
        """ Creates the comment and course tables in the db """

        comment_table = """  CREATE TABLE IF NOT EXISTS comments(
             id text PRIMARY KEY,
             course_id text,
             comment text,
             timestamp integer,
             votes integer,
             root boolean,
             children text,
             user_id text);
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

        user_table = """
                 CREATE TABLE IF NOT EXISTS users(
                     id text PRIMARY KEY,
                     picture text,
                     username text,
                     email text);
                 """

        user_to_comment_table = """
                 CREATE TABLE IF NOT EXISTS user_to_comment(
                     user_id text,
                     comment_id text,
                     upvote_or_downvote text);
                         """
        user_to_course_table = """
                 CREATE TABLE IF NOT EXISTS user_to_course(
                     user_id text,
                     course_id text,
                     workload_rating float,
                     recommendation_rating float);
                         """

        self.db_manager.create_table(comment_table)
        self.db_manager.create_table(course_table)
        self.db_manager.create_table(user_table)
        self.db_manager.create_table(user_to_comment_table)
        self.db_manager.create_table(user_to_course_table)
