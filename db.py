from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from config import config

db_uri = 'mysql://{user}:{password}@{host}/{name}'.format(
                user=config['db']['user'],
                password=config['db']['password'],
                host=config['db']['host'],
                name=config['db']['name'])

Session = sessionmaker(autocommit=False,
                       autoflush=False,
                       bind=create_engine(db_uri))
session = scoped_session(Session)


def get_or_create(session, model, defaults=None, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance, False
    else:
        params = dict((k, v) for k, v in kwargs.iteritems() if not isinstance(v, ClauseElement))
        params.update(defaults or {})
        instance = model(**params)
        session.add(instance)
        return instance, True