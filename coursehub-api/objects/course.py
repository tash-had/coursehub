class Course:
    def __init__(self, code, id_, description, rating):
        """
        
        :param code: str 
        :param id_: int
        :param description: str 
        :param rating: int
        """
        self.code = code
        self.id_ = id_
        self.description = description
        self.rating = rating

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

    def get_rating(self):
        return self.rating

    def set_rating(self, rating):
        self.rating = rating
