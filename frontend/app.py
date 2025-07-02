from flask import Flask, render_template
import requests, os

BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:8000")

app = Flask(__name__)

@app.route("/")
def index():
    resp = requests.get(f"{BACKEND_URL}/api/items")
    items = resp.json() if resp.ok else []
    return render_template("index.html", items=items)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
