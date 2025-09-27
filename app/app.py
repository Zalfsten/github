import os
from datetime import datetime

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify(
        {
            "message": "Hello World from Dummy Python App!",
            "version": os.environ.get("APP_VERSION", "development"),
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "environment": os.environ.get("FLASK_ENV", "production"),
            "python_version": "3.13",
            "package_manager": "uv",
        }
    )


@app.route("/health")
def health():
    return jsonify({"status": "healthy", "service": "dummy-python-app"})


@app.route("/info")
def info():
    return jsonify(
        {
            "name": "Dummy Python Application",
            "description": "A simple Flask application for Docker CI/CD testing",
            "endpoints": ["/", "/health", "/info"],
            "port": 8080,
            "package_manager": "uv",
        }
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)  # nosec B104
