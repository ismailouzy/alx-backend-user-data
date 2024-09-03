#!/usr/bin/env python3
"""
BasicAuth class for the API
"""
from api.v1.auth.auth import Auth


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
        if authorization_head is None:
            return None
        elif type(authorization_head) != str:
            return None
        elif authorization_head.startwith('Basic '):
            return authorization_head[5:]
        else:
            return None
