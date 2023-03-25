import logging

import connexion

from api.spec.v1.db_models.db_user import DbUser
from api.spec.v1.openapi_server.models.user import User  # noqa: E501
from api.spec.v1.utils.user_util import get_db_user
from api.spec.v1.utils.user_util import get_user

logger = logging.getLogger()


def create_user(user=None):  # noqa: E501
    """Create a new user

     # noqa: E501

    :param user: User object to be added
    :type user: dict | bytes

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    logger.info("Started create_user")
    user = User.from_dict(connexion.request.get_json())
    db_user = get_db_user(user)
    db_user.save()
    logger.info("Completed create_user")
    return user, 201


def get_users():  # noqa: E501
    """Get all users

     # noqa: E501


    :rtype: Union[List[User], Tuple[List[User], int], Tuple[List[User], int, Dict[str, str]]
    """
    logger.info("Started get_users")
    users = []
    for dbuser in DbUser.objects():
        users.append(get_user(dbuser))
    res = [user.to_dict() for user in users]
    logger.info("Completed get_users")
    return res


def get_user_by_id(user_id):  # noqa: E501
    """Get a user by ID

     # noqa: E501

    :param user_id: ID of the user to get
    :type user_id: int

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    logger.info("Started get_user_by_id")
    ok, msg = validate_user_id(user_id)
    if not ok:
        return msg, 400
    dbuser = DbUser.objects.get(_id=user_id)
    user = get_user(dbuser).to_dict()
    logger.info("Completed get_user_by_id")
    return user


def update_user_by_id(user_id, user=None):  # noqa: E501
    """Update a user by ID

     # noqa: E501

    :param user_id: ID of the user to update
    :type user_id: int
    :param user: User object to be updated
    :type user: dict | bytes

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    logger.info("Started update_user_by_id")
    user = User.from_dict(connexion.request.get_json())
    ok, msg = validate_user_id(user_id, user)
    if not ok:
        return msg, 400
    db_user = get_db_user(user)
    db_user.save()
    logger.info("Completed update_user_by_id")


def delete_user_by_id(user_id):  # noqa: E501
    """Delete a user by ID

     # noqa: E501

    :param user_id: ID of the user to delete
    :type user_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    logger.info("Started delete_user_by_id")
    ok, msg = validate_user_id(user_id)
    if not ok:
        return msg, 400
    DbUser.objects(_id=user_id).delete()
    logger.info("Completed delete_user_by_id")


def validate_user_id(user_id, user_param=None):
    msg = None
    try:
        DbUser.objects.get(_id=user_id)
    except Exception as e:
        msg = "User with id: " + str(user_id) + " not found"
    if user_param is not None and user_id != user_param.id:
        msg = "id: " + str(user_id) + " in path variable doesn't match id: " \
              + str(user_param.id) + " in received object"
    if msg is not None:
        logger.error(msg)
        return False, msg
    return True, None