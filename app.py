from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
import cv2
import numpy as np

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # or any {'0', '1', '2'}

app = Flask(__name__)

# Load the model (regression version)
model = load_model("eatable_model_reg.keras")

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get the data from the form
    image = request.files["image"]

    # Load the image for input to the model
    image = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)
    image = cv2.resize(image, (256, 256))
    image = image.reshape((1, 256, 256, 3))

    # Make a prediction
    prediction = model.predict(image)
    
    # Extract the prediction
    prediction = prediction[0][0]
    prediction = str(round(prediction, 2))

    # Return the prediction
    return jsonify({"prediction": prediction})
