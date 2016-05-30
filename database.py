from sqlalchemy.orm import scoped_session, sessionmaker
from flaskapp import app, Base, User, session, engine, Directory
import time


def initdb():
    Base.metadata.create_all(bind=engine)
    # log.info('tables created')
    mkusr()
    mkdir()
    # log.info('user created')


def deldb():
    Base.metadata.drop_all(bind=engine)


def mkusr():
    u = User()
    u.id = 1
    u.email = 'kurohai@gmail.com'
    u.username = 'kurohai'
    u.name = 'Kurohai'
    u.password = 'lol'
    u.admin = True

    session.add(u)
    session.commit()

def mkdir():
    d = Directory()
    d.name = 'test'
    d.path = 'd:/dropbox/'
    session.add(d)
    session.commit()

if __name__ == '__main__':
    deldb()
    initdb()
