import os
import redis
from flask import Flask, jsonify

app = Flask(__name__)

REDIS_URL = os.environ.get("REDIS_URL")

redis_client = None

if REDIS_URL:
    redis_client = redis.from_url(
        REDIS_URL,
        decode_responses=True,
        socket_connect_timeout=5
    )

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

@app.route("/health")
def health():
    if redis_client is None:
        return jsonify({
            "server": "online",
            "redis": "not_configured"
        }), 503

    try:
        redis_client.ping()
        return jsonify({
            "server": "online",
            "redis": "connected"
        })
    except Exception:
        app.logger.exception("Redis connection failed")
        return jsonify({
            "server": "online",
            "redis": "disconnected"
        }), 503

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
