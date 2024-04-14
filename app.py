from flask import Flask, render_template, request, jsonify
import time
# from tensorflow.keras.models import load_model
# NOTE: the above import is not working

app = Flask(__name__)

# Load the model
# model = load_model("price_model")

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get the data from the form
    # image = request.files["image"]

    # Make a prediction
    # prediction = model.predict(image)

    # Return the prediction
    # Create fake JSON response, with price[0] and price[1]
    prediction = {
        "price": [10, 20]
    }

    # Wait 2 seconds to simulate a slow server
    time.sleep(2)

    return jsonify(prediction)
