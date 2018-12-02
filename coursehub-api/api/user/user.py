class User:
    def __init__(self, id, username, email, picture):
        self.id = id
        self.username = username
        self.email = email
        self.picture = picture
        self.comment_history = []
