#!/usr/bin/env python3
"""session auth
"""
from models.user import User
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """session auth class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """a method that creates a session id
        """
        if user_id is None:
            return None
        if type(user_id) != str:
            return None
        id = str(uuid.uuid4())
        self.user_id_by_session_id[id] = user_id
        return id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """gives the user id based on the session id
        """
        if session_id is None or type(session_id) != str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """returns a user based on a cookie value
        """
        cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie)
        return User.get(user_id)
