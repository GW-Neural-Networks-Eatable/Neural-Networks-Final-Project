# https://stackoverflow.com/a/60137874
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
import cv2
import numpy as np

app = Flask(__name__)

model = load_model("models/eatable_model_reg.keras") # Load the model (regression version)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get the image from the form
    image = request.files["image"]

    # Load, resize, reshape the image for input to the model
    image = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)
    image = cv2.resize(image, (256, 256))
    image = image.reshape((1, 256, 256, 3))

    # Make a prediction
    prediction = model.predict(image)
    
    # Extract the prediction
    prediction = prediction[0][0]
    prediction = str("%.2f" % round(prediction, 2))

    # Return the prediction
    return jsonify({"prediction": prediction})
