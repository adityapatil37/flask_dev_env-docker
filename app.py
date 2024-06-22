from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Configurations
app.config['MONGO_URI'] = 'mongodb://mongo:27017/flaskdb'

# Initialize MongoDB client
client = MongoClient(app.config['MONGO_URI'])
db = client.get_default_database()

@app.route('/')
def index():
    return jsonify({"message": "Hello, World!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
