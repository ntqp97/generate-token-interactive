from flask import Flask, request
import jwt
import os
import json
app = Flask(__name__)

@app.route('/generate-token-to-interactive', methods=['POST'])
def hello_world():
    list_token = []
    data = request.get_json()
    for profile in data['profiles']:
        env = data.get('env', 'dev')
        if env == 'dev':
            private_key = os.environ.get('private_key_dev')
        if env == 'stg':
            private_key = os.environ.get('private_key_stg')
        if env == 'prd':
            private_key = os.environ.get('private_key_prd')
        token = jwt.encode(profile, private_key, algorithm='RS256', )
        list_token.append(token)
    return {'token': list_token}
