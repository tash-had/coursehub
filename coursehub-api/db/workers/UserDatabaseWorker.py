from db.database_manager import DatabaseManager


class UserDatabaseWorker(DatabaseManager):
    """Contains the functions for the User database"""

    def __init__(self):
        DatabaseManager.__init__(self)
