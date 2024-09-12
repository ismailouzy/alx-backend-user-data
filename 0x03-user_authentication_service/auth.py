#!/usr/bin/env python3
"""Auth
"""

from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
import uuid


def _hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


def _generate_uuid() -> str:
    """Generates a new UUID and returns its string representation."""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user with the given email and password."""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            new_user = self._db.add_user(email, _hash_password(password))
            return new_user
        else:
            raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate login credentials.
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                encoded_password = password.encode('utf-8')
                hashed_password = user.hashed_password
                password_matches = bcrypt.checkpw(
                    encoded_password, hashed_password
                )
                if password_matches:
                    return True
            return False
        except Exception:
            return False
