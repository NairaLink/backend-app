#!/usr/bin/python3

from flask import Flask
from flask import jsonify, request

app = Flask(__name__)

cards = {
        "777777": {"cardid": 45, "card number": "009823458745", "card balance": "45000"},
        "111111": {"cardid": 10, "card number": "002323765765", "card balance": "23000000"},
}

@app.route('/api/cards/<cardId>', strict_slashes=False)
def card(cardId):
    userid = request.headers['x-userid']
    print(type(userid))
    if userid in cards:
        card = cards[userid]
        print(card)
        if str(card["cardid"]) == cardId:
            card['email'] = request.headers['x-useremail']
            return jsonify(card), 200
    return jsonify({"error": "Forbidden"}), 403


if __name__ == '__main__':
    app.run('127.0.0.1', '5001')
