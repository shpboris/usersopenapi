from mongoengine import Document, StringField, IntField


class DbUser(Document):
    _id = IntField(required=True)
    name = StringField(required=True)
    unit = StringField(required=True)
    salary = IntField(required=True)
