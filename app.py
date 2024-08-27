from flask import Flask, request, jsonify, render_template
from datetime import datetime
from io import BytesIO
import requests
from PIL import Image
from pyzbar.pyzbar import decode 
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

@app.route('/decode-barcode', methods=['POST'])
def decode_barcode():
    data = request.get_json()
    

    # if 'url' not in data:
    #     return jsonify({"error": "Missing 'url' key in JSON body"}), 400
    # image_url = "https://fpi.branding-element.com/prod/34782/WA_PUBLIC_ATTACHMENT/88d9ce69_903b_4a6e_bde6_45dd214d407d.jpeg-QsUGG.jpeg"
    image_url = data['url']
    

    try:
        
        response = requests.get(image_url)
        response.raise_for_status() 

        
        img_bytes = BytesIO(response.content)
        img_pil = Image.open(img_bytes)

        results = decode(img_pil)

        if not results:
            return jsonify({"error": "No barcodes or QR codes found in the image"}), 404

        barcode = results[0]
        decoded_data = {
            "Code": barcode.data.decode('utf-8'),
            "type": barcode.type
        }
        return jsonify(decoded_data)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Request error: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
