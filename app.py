import os
from flask import Flask, request, render_template
from PIL import Image
import numpy as np
from tensorflow import keras

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
MODEL_PATH = "best_model.keras"

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def validate_file(file):
    if not file:
        return False, "No file"
    if file.filename == '':
        return False, "Empty filename"
    if not allowed_file(file.filename):
        return False, "Invalid file type"
    return True, ""

def prepare_image(file, target_size=(224, 224)):
    img = Image.open(file.stream).convert('RGB')
    img = img.resize(target_size)
    arr = np.array(img) / 255.0
    arr = np.expand_dims(arr, axis=0)
    return arr

def load_model(model_path):
    try:
        if os.path.exists(model_path):
            model = keras.models.load_model(model_path)
            print("Model loaded successfully!")
            return model
        else:
            print(f"ERROR: File {model_path} not found!")
    except Exception as e:
        print(f"Error loading model: {e}")

def predict_image(img_array):
    model = load_model(MODEL_PATH)
    prediction = model.predict(img_array)
    score = float(prediction[0][0])
    if score > 0.5:
        return {
            "message": "It's a Dog!",
            "precentage": f"{score:.2%}",
            "css_class": "dog_bg.jpg"
        }
    else:
        return {
            "message": "It's a Cat!",
            "precentage": f"{(1 - score):.2%}",
            "css_class": "cat_bg.jpg"
        }

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files.get('file')

    valid, msg = validate_file(file)
    if not valid:
        return msg, 400

    img_array = prepare_image(file)
    result = predict_image(img_array)

    return render_template('result.html', prediction=result)
