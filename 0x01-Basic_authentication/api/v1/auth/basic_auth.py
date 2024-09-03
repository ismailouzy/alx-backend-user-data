#!/usr/bin/env python3
"""
BasicAuth class for the API
"""
from api.v1.auth.auth import Auth
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
