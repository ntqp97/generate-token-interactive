from flask import Flask, request
import jwt
import os
app = Flask(__name__)

@app.route('/generate-token-to-interactive', methods=['POST'])
def hello_world():
    data = request.get_json()
    private_key = os.environ.get('private_key')
    token = jwt.encode(data, private_key, algorithm='ES256', )
    return {'token': token}
