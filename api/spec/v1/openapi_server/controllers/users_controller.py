import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from api.spec.v1.openapi_server.models.user import User  # noqa: E501
from api.spec.v1.openapi_server import util


def create_user(user):  # noqa: E501
    """Create a new user

     # noqa: E501

    :param user: User object to be added
    :type user: dict | bytes

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        user = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'create_user response !'


def delete_user_by_id(user_id):  # noqa: E501
    """Delete a user by ID

     # noqa: E501

    :param id: ID of the user to delete
    :type id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'delete_user_by_id response !'


def get_user_by_id(user_id):  # noqa: E501
    """Get a user by ID

     # noqa: E501

    :param id: ID of the user to get
    :type id: int

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    return 'get_user_by_id response !'


def get_users():  # noqa: E501
    """Get all users

     # noqa: E501


    :rtype: Union[List[User], Tuple[List[User], int], Tuple[List[User], int, Dict[str, str]]
    """
    return 'get_users response !'


def update_user_by_id(user_id, user):  # noqa: E501
    """Update a user by ID

     # noqa: E501

    :param id: ID of the user to update
    :type id: int
    :param user: User object to be updated
    :type user: dict | bytes

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        user = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'update_user_by_id response !'
