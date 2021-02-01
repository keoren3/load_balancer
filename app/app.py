import os
from flask import Flask, jsonify
from send_parallel import send_to_all_parallel_servers
from send_parallel import logging

REGISTER_SERVERS = os.getenv('SERVERS', '').split(',')

app = Flask(__name__)


@app.route('/register', methods=['POST'])
def register():
    logging.debug("Running /register API request")
    text, response_code = send_to_all_parallel_servers(REGISTER_SERVERS, '/register')
    return jsonify(text), response_code


@app.route('/changePassword', methods=['POST'])
def change_password():
    logging.debug("Running /changePassword API request")
    text, response_code = send_to_all_parallel_servers(REGISTER_SERVERS, '/changePassword')
    return jsonify(text), response_code


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', threaded=True)
