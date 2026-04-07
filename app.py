from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Fishing AI Web Service!'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
    

from flask import Flask, jsonify, request
import os

