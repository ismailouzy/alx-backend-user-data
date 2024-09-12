#!/usr/bin/env python3
"""auth
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """
    generates a salt
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed
