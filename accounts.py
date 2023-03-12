#!/usr/bin/python3

from flask import Flask
from flask import jsonify, request

app = Flask(__name__)

accounts = {
        "777777": {"accountid": 45, "account number": "009823458745", "account balance": "45000"},
        "111111": {"accountid": 10, "account number": "002323765765", "account balance": "23000000"},
}

@app.route('/api/accounts/<accountId>', strict_slashes=False)
def account(accountId):
    userid = request.headers['x-userid']
    print(type(userid))
    if userid in accounts:
        account = accounts[userid]
        print(account)
        if str(account["accountid"]) == accountId:
            account['email'] = request.headers['x-useremail']
            return jsonify(account), 200
    return jsonify({"error": "Forbidden"}), 403


if __name__ == '__main__':
    app.run('127.0.0.1', '5001')
