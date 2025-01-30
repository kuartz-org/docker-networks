from flask import Flask
import psycopg2

app = Flask(__name__)

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="mydatabase",
            user="user",
            password="password",
            host="db"
        )
        return conn
    except Exception as e:
        return str(e)

@app.route("/")
def home():
    conn = connect_db()
    if isinstance(conn, str):
        return f"Database Connection Error: {conn}", 500
    return "Hello from API! Connected to the database 🎉"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
