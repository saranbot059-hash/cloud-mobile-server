from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "app": "Cloud Mobile",
        "status": "Connected"
    })

@app.route("/apps")
def apps():
    return jsonify({
        "apps": []
    })
