class Course:
    def __init__(self, code, id_, description, u_rating, d_rating, u_rating_count, d_rating_count):
        """
        
        :param code: str 
        :param id_: int
        :param description: str
        """
        self.code = code
        self.id_ = id_
        self.description = description
        self.usefulness_rating = u_rating
        self.difficulty_rating = d_rating
        self.u_rating_count = u_rating_count
        self.d_rating_count = d_rating_count

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

    def get_usefulness_rating(self):
        return self.usefulness_rating

    def set_usefulness_rating(self, rating):
        self.usefulness_rating = rating

    def get_difficulty_rating(self):
        return self.difficulty_rating

    def set_difficulty_rating(self, rating):
        self.difficulty_rating = rating

    def get_u_rating_count(self):
        return self.u_rating_count

    def set_u_rating_count(self, count):
        self.u_rating_count = count

    def get_d_rating_count(self):
        return self.d_rating_count

    def set_d_rating_count(self, count):
        self.d_rating_count = count
