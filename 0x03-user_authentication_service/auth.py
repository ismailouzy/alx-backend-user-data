#!/usr/bin/env python3
"""Auth
"""

from db import DB
from user import User
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user with the given email and password."""
        # Check if the user already exists
        if self._db.find_user_by_email(email):
            raise ValueError(f"User {email} already exists")

        # Hash the password
        hashed_password = self._hash_password(password)

        # Create a new user and save to the database
        new_user = User(email=email, hashed_password=hashed_password)
        self._db.add_user(new_user)

        return new_user
