import os
from flask import Flask, jsonify
from send_parallel import send_to_all_parallel_servers

REGISTER_SERVERS = os.getenv('SERVERS', None).split(',')
app = Flask(__name__)


@app.route('/register', methods=['POST'])
def register():
    return jsonify(send_to_all_parallel_servers(REGISTER_SERVERS, '/register')), 201


@app.route('/api/register', methods=['POST'])
def api_register():
    return "Registered!"


@app.route('/changePassword', methods=['POST'])
def change_password():
    return send_to_all_parallel_servers(REGISTER_SERVERS, '/changePassword'), 201


@app.route('/api/change_password', methods=['POST'])
def api_change_password():
    return 'Changed!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', threaded=True)
