#!/usr/bin/env python3
"""session authentication
"""

from flask import abort, jsonify, request
from models.user import User
from os import getenv
from api.v1.views import app_views


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """user login
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    users = User.search({"email": email})

    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)

    response = jsonify(user.to_json())
    session_name = getenv('SESSION_NAME')
    response.set_cookie(session_name, session_id)

    return response


@app_views.route(
        '/auth_session/logout',
        methods=['DELETE'], strict_slashes=False)
def logout():
    """
    Handle user logout
    """
    from api.vi.app import auth

    if auth.destroy_session(request):
        return jsonify({}), 200
    else:
        abort(404)
