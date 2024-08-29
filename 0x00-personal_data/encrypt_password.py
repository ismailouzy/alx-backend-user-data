#!/usr/bin/env python3
"""Password encryption and validation module"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt.
    """
    password_bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates that the provided password matches the hashed password.
    """
    password_bytes = password.encode('utf-8')

    return bcrypt.checkpw(password_bytes, hashed_password)
