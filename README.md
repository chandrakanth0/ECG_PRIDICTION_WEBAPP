# ECG_PREDICTION_WEBAPP 


# FOLDER STRUCTURE
ecg-heart-predictor/
├── app.py                  # Main Flask backend
├── your_model.h5           # Trained VGG16 model
├── requirements.txt        # Dependencies
├── render.yaml             # Render deployment config
├── static/
│   ├── css/
│   │   └── style.css       # Styling for index.html
│   └── js/
│       └── script.js       # JS for image upload/predict
├── templates/
│   └── index.html          # Flask looks here for Jinja/HTML
└── README.md               # Optional for project info
