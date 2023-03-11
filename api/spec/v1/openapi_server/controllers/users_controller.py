import logging
import connexion
from api.spec.v1.openapi_server.models.user import User  # noqa: E501

users_global_dict = {}
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
    users_global_dict[user.id] = user
    logger.info("Completed create_user")
    return user, 201


def get_users():  # noqa: E501
    """Get all users

     # noqa: E501


    :rtype: Union[List[User], Tuple[List[User], int], Tuple[List[User], int, Dict[str, str]]
    """
    logger.info("Started get_users")
    res = []
    if users_global_dict:
        res = [user.to_dict() for user in users_global_dict.values()]
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
    user = users_global_dict[user_id].to_dict()
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
    users_global_dict[user.id] = user
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
    users_global_dict.pop(user_id)
    logger.info("Completed delete_user_by_id")


def validate_user_id(user_id, user_param=None):
    msg = None

    if user_id not in users_global_dict:
        msg = "User with id: " + str(user_id) + " not found"
    elif user_param is not None and user_id != user_param.id:
        msg = "id: " + str(user_id) + " in path variable doesn't match id: " \
              + str(user_param.id) + " in received object"
    if msg is not None:
        logger.error(msg)
        return False, msg
    return True, None