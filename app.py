# app.py
import os, time, socket, redis
from flask import Flask, jsonify

app = Flask(__name__)

def get_redis():
    return redis.Redis(
        host=os.environ.get("REDIS_HOST", "localhost"),
        port=int(os.environ.get("REDIS_PORT", 6379)),
        socket_connect_timeout=2
    )

@app.route("/")
def index():
    return jsonify({"status": "ok", "tests": ["/ping", "/rw", "/latency", "/auth"]})

@app.route("/ping")
def ping():
    try:
        r = get_redis()
        result = r.ping()
        return jsonify({"ping": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/rw")
def read_write():
    try:
        r = get_redis()
        r.set("test_key", "hello")
        val = r.get("test_key")
        return jsonify({"set": "ok", "get": val.decode()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/latency")
def latency():
    try:
        r = get_redis()
        times = []
        for _ in range(20):
            start = time.monotonic()
            r.ping()
            times.append((time.monotonic() - start) * 1000)
        return jsonify({
            "min_ms": round(min(times), 2),
            "max_ms": round(max(times), 2),
            "avg_ms": round(sum(times)/len(times), 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/auth")
def auth_check():
    try:
        r = get_redis()
        # Zkusí připojení bez hesla – pokud projde, DB nemá auth
        r.ping()
        return jsonify({"auth_required": False, "note": "Connected without password"})
    except redis.AuthenticationError:
        return jsonify({"auth_required": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))