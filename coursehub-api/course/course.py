class Course:
    def __init__(self, code, id_, description, title, org_name):
        """
        
        :param code: str 
        :param id_: int
        :param description: str
        :param ratings: dict
        """
        self.code = code
        self.id_ = id_
        self.description = description
        self.title = title
        self.org_name = org_name
        # self.ratings = ratings
        # self.overall_rating = overall_rating
        # self.rating_count = rating_count

    def get_code(self):
        return self.code

    def set_code(self, code):
        self.code = code

    def get_id(self):
        return self.id_

    def set_id(self, id_):
        self.id_ = id_

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_ratings(self):
        return self.ratings

    def set_ratings(self, ratings):
        self.ratings = ratings

    def get_rating_count(self):
        return self.rating_count

    def set_rating_count(self, count):
        self.rating_count = count

    def get_overall_rating(self):
        return self.overall_rating
                                             
    def set_overall_rating(self, rating):
        self.overall_rating = rating
