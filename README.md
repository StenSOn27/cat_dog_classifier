# Cat vs. Dog Classifier

A web application based on Flask and TensorFlow that classifies uploaded images as either a **Cat** or a **Dog**. The application uses a pre-trained Convolutional Neural Network (CNN) to make predictions and dynamically changes the background of the result page based on the classification result.

- **Google Colab Notebook:** https://colab.research.google.com/drive/1rlDI7RU-aSaSNQ3utAQzWxs2eW_pWcnh?usp=sharing
- **Dataset:** https://www.kaggle.com/datasets/ashfakyeafi/cat-dog-images-for-classification


## Screenshots

### Upload Page
<img width="1920" height="994" alt="зображення" src="https://github.com/user-attachments/assets/6c382206-4459-4445-a73a-b1b88e2425ee" />


### Cat Prediction
<img width="1920" height="994" alt="зображення" src="https://github.com/user-attachments/assets/9a28377c-65a4-4003-8a55-7bcf1456932c" />


### Dog Prediction
<img width="1920" height="994" alt="зображення" src="https://github.com/user-attachments/assets/f440827f-7a8e-42c1-bb39-ddeb69630186" />


## Tech Stack

- **Python 3**
- **Flask**
- **TensorFlow / Keras**
- **NumPy**
- **HTML/CSS**

---

## How to Run the Project

```
git clone https://github.com/StenSOn27/cat_dog_classifier.git
cd cat_dog_classifier

python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt

flask --app app run
```
