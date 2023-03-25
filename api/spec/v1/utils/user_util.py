from api.spec.v1.db_models.db_user import DbUser
from api.spec.v1.openapi_server.models.user import User


def get_db_user(user):
    return DbUser(_id=user.id, name=user.name, unit=user.unit, salary=user.salary)


def get_user(dbuser):
    return User(id=dbuser._id, name=dbuser.name, salary=dbuser.salary, unit=dbuser.unit)
