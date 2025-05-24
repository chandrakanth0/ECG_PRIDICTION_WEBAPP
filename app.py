from flask import Flask, request, jsonify, render_template
# import tensorflow as tf
import numpy as np
# from PIL import Image
import os

app = Flask(__name__)

# Load your model
# model = tf.keras.models.load_model("Vgg16_ecg_model.keras")

@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/predict', methods=['POST'])
# def predict():
#     file = request.files['file']
#     image = Image.open(file.stream).resize((224, 224))
#     image = np.array(image) / 255.0
#     image = image.reshape(1, 224, 224, 3)
#     prediction = model.predict(image)
#     result = "Positive" if prediction[0][0] > 0.5 else "Negative"
#     return jsonify({'result': result})

if __name__ == '__main__':
    app.run()
