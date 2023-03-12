#!/usr/bin/python3

from flask import Flask
from flask import abort, jsonify, request

app = Flask(__name__)


users = {
        "777777": {"active": True, "userid": "777777", "email": "mendy@gmail.com"},
        "111111": {"active": True, "userid": "111111", "email": "chizaram@gmail.com"},
}

@app.route('/api/auth/<authID>', strict_slashes=False)
def authentication(authID):
    return jsonify({"api": "authentication service", "message": f"This is your user id {authID}"}), 200

@app.route('/oauth/token', methods=['POST', 'GET'], strict_slashes=False)
def oauth():
    token, tokenHint = request.form.get('token'), request.form.get('token_hint')
    if token in users:
        response = users[token]
        return jsonify(response), 200
    return jsonify({"active": False}), 401


if __name__ == '__main__':
    app.run('127.0.0.1', '5000')
