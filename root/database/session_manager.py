"""
    SessionManager class
"""

import sqlalchemy.orm as sa_orm

class SessionManager:
    def __init__(self, _engine):
        self.session_factory = sa_orm.sessionmaker(bind=_engine)
        self.session = None

    def __enter__(self):
        self.session = self.session_factory()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.session.commit()
        else:
            self.session.rollback()
        self.session.close()
        self.session = None
