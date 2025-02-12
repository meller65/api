from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello from Render!"})

@app.route('/api/data')
def get_data():
    return jsonify({"data": ["apple", "banana", "cherry"]})

if __name__ == '__main__':
    app.run(hosts='0.0.0.0', port=5000)