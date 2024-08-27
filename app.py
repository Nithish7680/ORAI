from flask import Flask, request, jsonify, render_template
from datetime import datetime
import requests
from PIL import Image
import cv2
import numpy as np
from pyzbar.pyzbar import decode
from io import BytesIO

app = Flask(__name__)

@app.route("/")
def home():
    """Render the home page."""
    return render_template("home.html")

@app.route("/about/")
def about():
    """Render the about page."""
    return render_template("about.html")

@app.route("/contact/")
def contact():
    """Render the contact page."""
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name=None):
    """Render the hello page with optional name parameter."""
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    """Serve a static JSON file."""
    return app.send_static_file("data.json")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
