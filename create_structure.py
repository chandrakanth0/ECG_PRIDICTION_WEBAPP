import os

# Define folder structure (relative to current dir)
folders = [
    "static/css",
    "static/js",
    "templates"
]

# Define files to create
files = {
    "app.py": "# Flask app will go here\n",
    "requirements.txt": "Flask\ntensorflow\nnumpy\nPillow\n",
    "render.yaml": """\
services:
  - type: web
    name: ecg-heart-predictor
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python app.py
    plan: free
""",
    "static/css/style.css": "/* Add your styles here */\n",
    "static/js/script.js": "// JavaScript to handle file upload and prediction\n",
    "templates/index.html": """\
<!DOCTYPE html>
<html>
<head>
  <title>ECG Heart Disease Predictor</title>
  <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
  <h1>ECG-based Heart Disease Prediction</h1>
  <p>This application uses deep learning (VGG19) to predict the likelihood of heart disease from ECG signal images.</p>
  <form id="uploadForm" enctype="multipart/form-data">
    <input type="file" name="file" id="fileInput" />
    <button type="button" onclick="uploadImage()">Predict</button>
  </form>
  <p id="result"></p>
  <script src="/static/js/script.js"></script>
</body>
</html>
"""
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files with content
for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ Project files and folders created successfully inside 'ecg-heart-predictor/'")
