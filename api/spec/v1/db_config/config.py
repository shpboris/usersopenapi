from mongoengine import connect


def init():
    host = 'localhost'
    db_name = 'my-test'
    port = 27017
    connect(db=db_name, host=host, port=port)