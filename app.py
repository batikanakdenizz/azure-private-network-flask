from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "App is running"})


@app.route("/hello")
def hello():
    db_host = os.getenv("DB_HOST", "not-set")
    db_name = os.getenv("DB_NAME", "not-set")
    app_env = os.getenv("APP_ENV", "development")

    return jsonify(
        {
            "message": "Hello from Azure-ready Flask app!",
            "environment": app_env,
            "db_host": db_host,
            "db_name": db_name,
        }
    )


@app.route("/db-test")
def db_test():

    db_host = os.getenv("DB_HOST")
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_port = os.getenv("DB_PORT", "5432")

    try:
        conn = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password,
            port=db_port,
        )

        conn.close()

        return jsonify(
            {"status": "success", "message": "Database connection successful"}
        )

    except Exception as e:

        return jsonify({"status": "error", "message": str(e)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
