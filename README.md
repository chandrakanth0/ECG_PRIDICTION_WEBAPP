# ECG Heart Predictor WebApp

A modern web application leveraging deep learning (VGG16) to analyze Electrocardiogram (ECG) images for early detection of heart abnormalities, including Myocardial Infarction (MI). Built with Flask for backend, HTML/CSS/JS for frontend, and designed for easy deployment (e.g., Render.com).

---

## Project Structure



ecg-heart-predictor/
├── app.py                  # Main Flask backend server
├── Vgg16_ecg_model.keras   # Pretrained VGG16 model weights file
├── requirements.txt        # Python dependencies
├── render.yaml             # Render.com deployment config
├── static/
│   ├── css/
│   │   └── style.css       # Stylesheet for the frontend
│   └── js/
│       └── script.js       # JavaScript for image upload & prediction
├── templates/
│   └── index.html  and result.html        # HTML template rendered by Flask
└── README.md               # Project documentation (this file)



---

## Features

- Upload ECG image files (`.png`, `.jpg`, `.jpeg`) via a user-friendly web interface.
- AI-powered prediction model based on transfer learning (VGG16) to detect cardiac conditions.
- Real-time display of prediction results with clear UI feedback.
- Loading spinner animation during prediction processing.
- Responsive design for mobile and desktop.
- Easily deployable to cloud platforms such as Render.com using `render.yaml`.

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- `pip` package manager

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/chandrakanth0/ECG_PRIDICTION_WEBAPP.git
   cd ECG_PRIDICTION_WEBAPP


2. **Create and activate a virtual environment (recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```


---

## Usage

1. **Run the Flask app locally:**

   ```bash
   python app.py
   ```

2. **Open your browser and visit:**

   ```
   http://127.0.0.1:5000
   ```

3. **Upload your ECG image and click “Analyze ECG” to get prediction results.**

---

## Deployment

### Deploying on Render.com

* The `render.yaml` configuration file is preconfigured for automatic deployment.
* Push your repository to GitHub or any Git provider connected with Render.
* Create a new Web Service on Render and link your repository.
* Render will detect `render.yaml` and deploy your Flask app with all dependencies.

---

## Model Details

* The prediction model is based on VGG16 architecture, pretrained on ImageNet and fine-tuned for ECG image classification.
* Input images are resized and normalized before prediction.
* The output is a classification label indicating the presence or absence of cardiac abnormalities such as Myocardial Infarction.

---

## File Details

* `app.py`: Flask backend server handling routes, file upload, and prediction logic.
* `your_model.h5`: Pretrained Keras model weights (update with your model).
* `requirements.txt`: List of all Python packages required.
* `render.yaml`: Deployment configuration for Render.com.
* `templates/index.html`: Frontend UI with Jinja2 templating.
* `static/css/style.css`: Styling for a clean, modern look.
* `static/js/script.js`: JavaScript to manage image upload and dynamic frontend behaviors.

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## License

NILL
---

## Acknowledgments

* Based on VGG16 deep learning architecture.
* Inspired by advances in AI for medical imaging.
* Thanks to the Flask and Render.com communities for excellent tools.

---

## Contact

Developed by Chandrakanth S , Vaishnavi B K, Nandana T S 
Email: [chandrakanthchandru0799@gmail.com](mailto:chandrakanthchandru0799@gmail.com)
GitHub: [https://github.com/chandrakanth0](https://github.com/chandrakanth0)

```

---
