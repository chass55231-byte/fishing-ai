from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route('/api/fish', methods=['GET'])
def get_fish():
    return jsonify({'fish': ['trout', 'salmon', 'tuna']})

@app.route('/api/fish', methods=['POST'])
def add_fish():
    data = request.get_json()
    return jsonify({'message': f'Fish {data.get("name")} added!'}), 201

if __name__ == '__main__':
    app.run(debug=True)