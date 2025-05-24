import os
from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__)

# Define a dummy UPLOAD_FOLDER, even if not saving files, for consistency
app.config['UPLOAD_FOLDER'] = 'uploads'

# Load model and define class labels manually (based on training data)
# IMPORTANT: Ensure these class labels exactly match the keys in CLASS_DEFINITIONS below.
class_labels = ['class1', 'class2', 'class3', 'class4']

# Define your class mapping and explanations
# This dictionary maps the internal model output labels (e.g., 'class1')
# to user-friendly display names and detailed explanations.
CLASS_DEFINITIONS = {
    "class1": {
        "display_name": "Normal ECG",
        "explanation": """
            A **Normal** ECG indicates that the electrical activity of your heart appears to be within expected healthy parameters. This typically means:
            <ul>
                <li>A regular and consistent heart rhythm.</li>
                <li>Heart rate within a normal range (e.g., 60-100 beats per minute for adults at rest).</li>
                <li>The various wave patterns (P wave, QRS complex, T wave) are of normal shape, duration, and amplitude, reflecting healthy electrical depolarization and repolarization of the heart chambers.</li>
            </ul>
            <p>This is a positive indication; however, this analysis is not a substitute for a full medical evaluation. Regular check-ups are always recommended.</p>
        """
    },
    "class2": {
        "display_name": "Myocardial Infarction (Heart Attack)",
        "explanation": """
            The classification of **Myocardial Infarction (Heart Attack)** suggests that the ECG image exhibits patterns consistent with reduced or blocked blood flow to the heart muscle, potentially indicating damage. Key indicators often include:
            <ul>
                <li>Significant **ST-segment elevation or depression**, which points to acute myocardial injury.</li>
                <li>Presence of **pathological Q waves**, which can indicate previous heart muscle damage.</li>
                <li>**T-wave inversions** or other abnormalities, reflecting changes in the heart's repolarization.</li>
            </ul>
            <p class="warning">**Crucial Action Required:** This result warrants immediate medical attention. Please consult a healthcare professional without delay for further diagnosis and treatment. This AI analysis is a preliminary tool and not a definitive diagnosis.</p>
        """
    },
    "class3": {
        "display_name": "Abnormal Rhythm (Arrhythmia)",
        "explanation": """
            An **Abnormal Rhythm** (Arrhythmia) classification suggests that the heart's electrical activity is irregular. This could manifest as:
            <ul>
                <li>Heartbeats that are too fast (tachycardia), too slow (bradycardia), or irregular (e.g., atrial fibrillation, premature beats).</li>
                <li>Variations in the spacing between heartbeats or unusual wave patterns.</li>
            </ul>
            <p>While some arrhythmias are benign, others can be serious. It is highly recommended to discuss this result with a healthcare professional for proper evaluation and management.</p>
        """
    },
    "class4": {
        "display_name": "Other Cardiac Abnormality",
        "explanation": """
            The classification of **Other Cardiac Abnormality** indicates that the ECG image contains patterns that deviate from normal and don't neatly fit into the "Myocardial Infarction" or "Abnormal Rhythm" categories. This could potentially suggest:
            <ul>
                <li>Enlargement of heart chambers (e.g., ventricular hypertrophy).</li>
                <li>Electrolyte imbalances.</li>
                <li>Effects of certain medications.</li>
                <li>Or other structural or functional issues that require further investigation.</li>
            </ul>
            <p class="warning">**Follow-up Recommended:** It is important to consult with a healthcare professional for a comprehensive review of this finding and to determine the underlying cause.</p>
        """
    }
}

# Load the TensorFlow model
try:
    model = tf.keras.models.load_model("Vgg16_ecg_model.keras")
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    # Exit or handle error appropriately if model loading fails
    exit()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return render_template("result.html", error="No file part in the request.")
    
    file = request.files['file']
    
    if file.filename == '':
        return render_template("result.html", error="No selected file.")

    try:
        # Open, resize, and preprocess the image
        image = Image.open(file.stream).resize((224, 224)).convert('RGB')
        image = np.array(image) / 255.0  # Normalize pixel values to [0, 1]
        image = np.expand_dims(image, axis=0) # Add batch dimension (1, 224, 224, 3)

        # Make prediction
        prediction = model.predict(image)
        predicted_class_index = np.argmax(prediction[0])
        predicted_label_key = class_labels[predicted_class_index] # e.g., 'class1', 'class2'

        # Get the human-readable display name and explanation
        predicted_info = CLASS_DEFINITIONS.get(predicted_label_key, {
            "display_name": "Unknown Class",
            "explanation": "<p>No specific explanation available for this class. Please consult a medical professional.</p>"
        })
        predicted_label_display = predicted_info["display_name"]

        # Prepare probabilities for display
        # Create a dictionary where keys are original class labels and values are percentages
        probabilities = dict(zip(class_labels, [round(float(p) * 100, 2) for p in prediction[0]]))

        # Define the order of probabilities for consistent display in the HTML
        # This should match the order you want them to appear in the list
        probabilities_order = class_labels # Using class_labels as the order

        return render_template(
            "result.html",
            predicted_label_key=predicted_label_key,      # Internal key for conditional logic in HTML
            predicted_label_display=predicted_label_display, # User-friendly name for display
            probabilities=probabilities,                  # Dictionary of probabilities
            class_mapping={k: v["display_name"] for k, v in CLASS_DEFINITIONS.items()}, # Full mapping for probabilities list
            probabilities_order=probabilities_order       # Order for displaying probabilities
        )

    except Exception as e:
        # Catch any errors during image processing or prediction
        return render_template("result.html", error=f"An error occurred during prediction: {e}")

if __name__ == '__main__':
    # Create the uploads directory if it doesn't exist
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)