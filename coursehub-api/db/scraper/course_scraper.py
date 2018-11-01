import requests
from db.database_manager import _CourseHubDatabaseInitializer


class _CourseScraper:

    def __init__(self):
        self.db_initializer = _CourseHubDatabaseInitializer()

    def get_org_names(self):
        request_url = "https://timetable.iit.artsci.utoronto.ca/api/orgs"
        response = requests.get(request_url).json()
        orgs_list = list(dict(response)["orgs"].keys())

        return orgs_list

    def populate_course_table(self, org_name="CSC"):
        """ If org_name is 'all', this function will populate table with all courses at UofT."""

        if org_name == "all":
            org_names = self.get_org_names()
        else:
            org_names = [org_name]

        for org in org_names:
            request_url = "https://timetable.iit.artsci.utoronto.ca/api/20189/courses?org=" + org
            response = requests.get(request_url).json()
            course_list = list(dict(response).values())
            for course in course_list:
                data = {
                    "course_id": course["courseId"],
                    "org_name": course["org"],
                    "course_title": course["courseTitle"],
                    "course_code": course["code"],
                    "course_description": course["courseDescription"]
                }
                self.db_initializer.insert_course(data)


if __name__ == "__main__":
    _CourseScraper().populate_course_table()
