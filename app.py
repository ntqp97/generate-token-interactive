from flask import Flask, request
import jwt
import os
import json
app = Flask(__name__)

@app.route('/generate-token-to-interactive', methods=['POST'])
def hello_world():
    list_token = []
    data = request.get_json()
    for profile in data:
        private_key = os.environ.get('private_key')
        token = jwt.encode(json.loads(profile), private_key, algorithm='ES256', )
        list_token.append(token)
    return {'token': list_token}
