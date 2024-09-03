#!/usr/bin/env python3
"""
Auth class for the API
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Auth class to manage API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns the authorization header from the request
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user
        """
        return None
