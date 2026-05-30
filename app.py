# app.py
import os, time, redis
from flask import Flask, jsonify

app = Flask(__name__)

def get_redis(password=None):
    return redis.Redis(
        host=os.environ.get("REDIS_HOST", "localhost"),
        port=int(os.environ.get("REDIS_PORT", 6379)),
        password=password,
        socket_connect_timeout=2
    )

@app.route("/")
def index():
    return jsonify({"tests": ["/ping", "/rw", "/latency", "/auth", "/auth-strict"]})

@app.route("/ping")
def ping():
    try:
        return jsonify({"ping": get_redis().ping()})
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
        get_redis().ping()
        return jsonify({"auth_required": False, "note": "Connected without password"})
    except redis.AuthenticationError:
        return jsonify({"auth_required": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/auth-strict")
def auth_strict():
    try:
        get_redis(password="wrong_password_xyz").ping()
        return jsonify({"auth_required": False, "note": "PING succeeded with wrong password"})
    except redis.AuthenticationError as e:
        return jsonify({"auth_required": True, "note": str(e)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/db-info")
def db_info():
    try:
        r = get_redis()
        keys = r.keys("*")
        info = r.info("server")
        return jsonify({
            "keys": [k.decode() for k in keys],
            "version": info.get("redis_version"),
            "uptime_seconds": info.get("uptime_in_seconds"),
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))