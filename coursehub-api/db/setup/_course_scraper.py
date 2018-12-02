import requests

import re
from db.setup._course_evals_parser import find_course_ratings


class _CourseScraper:

    def __init__(self, db_initializer):
        self.db_initializer = db_initializer

    def get_org_names(self):
        request_url = "https://timetable.iit.artsci.utoronto.ca/api/orgs"
        response = requests.get(request_url).json()
        return dict(response)["orgs"]

    def get_course_code_prefix_list(self, org_full_name):
        prefix_list = re.findall('\(.*?\)', org_full_name)
        return [i.replace("(", "").replace(")", "") for i in prefix_list]

    def _populate_course_ratings(self, org_full_name):
        course_code_prefix_list = self.get_course_code_prefix_list(org_full_name)
        for code in course_code_prefix_list:
            self.db_initializer.set_course_ratings(find_course_ratings(code))

    def populate_course_table(self, org_code="CSC"):
        """ If org_name is 'all', this function will populate table with all courses at UofT."""

        org_code_to_name_dict = self.get_org_names()

        if org_code == "all":
            org_code_list = org_code_to_name_dict.keys()
        else:
            org_code_list = [org_code]

        for org in org_code_list:
            request_url = "https://timetable.iit.artsci.utoronto.ca/api/20189/courses?org=" + org
            response = requests.get(request_url).json()
            course_list = list(dict(response).values())
            for course in course_list:
                data = {
                    "course_id": course["courseId"],
                    "org_name": course["org"],
                    "course_title": course["courseTitle"],
                    "course_code": course["code"],
                    "course_description": course["courseDescription"],
                    "prerequisite": course["prerequisite"],
                    "corequisite": course["corequisite"],
                    "exclusion": course["exclusion"],
                    "breadth": course["breadthCategories"]
                }
                self.db_initializer.insert_course(data)

            org_full_name = org_code_to_name_dict[org]
            self._populate_course_ratings(org_full_name)