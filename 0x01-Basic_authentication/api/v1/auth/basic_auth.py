#!/usr/bin/env python3
"""
BasicAuth class for the API
"""
from typing import Tuple, TypeVar
from api.v1.auth.auth import Auth
from models.user import User
import base64


class BasicAuth(Auth):
    """
    BasicAuth class to manage API basic authentication
    """
    def extract_base64_authorization_header(
            self,
            authorization_header: str,
            ) -> str:
        """
        returns the base64 par of the auth header
        for basic auth
        """
        if authorization_header is None:
            return None
        elif type(authorization_header) != str:
            return None
        elif not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str,
            ) -> str:
        """
        decodes a value of a base64 string
        """
        if base64_authorization_header is None:
            return None
        elif type(base64_authorization_header) != str:
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_str = decoded_bytes.decode('utf-8')
            return decoded_str
        except Exception:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str,
            ) -> str:
        """
        extracts the email and password from base64
        """
        if decoded_base64_authorization_header is None:
            return None, None
        elif type(decoded_base64_authorization_header) != str:
            return None, None
        elif ":" not in decoded_base64_authorization_header:
            return None, None
        credentials = decoded_base64_authorization_header.split(":")
        return credentials[0], credentials[1]

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str,
            ) -> TypeVar('User'):
        """
        returns the user instance based on the email and password
        """
        if user_email is None or type(user_email) != str:
            return None
        elif user_pwd is None or type(user_pwd) != str:
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None

        if not users:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None
