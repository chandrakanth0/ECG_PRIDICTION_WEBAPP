from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np
from PIL import Image
import os

app = Flask(__name__)

# Load model and define class labels manually (based on training data)
model = tf.keras.models.load_model("Vgg16_ecg_model.keras")
class_labels = ['class1', 'class2', 'class3', 'class4']  # 🔁 Replace with actual class folder names

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    image = Image.open(file.stream).resize((224, 224)).convert('RGB')
    image = np.array(image) / 255.0
    image = image.reshape(1, 224, 224, 3)

    prediction = model.predict(image)
    predicted_class = np.argmax(prediction[0])
    predicted_label = class_labels[predicted_class]
    probabilities = dict(zip(class_labels, [round(float(p) * 100, 2) for p in prediction[0]]))  # in %

    return render_template("result.html", predicted_label=predicted_label, probabilities=probabilities)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
