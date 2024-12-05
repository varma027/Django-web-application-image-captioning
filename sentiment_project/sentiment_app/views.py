from django.shortcuts import render
import joblib

# Create your views here.
import os
import pickle

# Load the model (ensure model path is correct)
with open('sentiment_app/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def home_view(request):
    return render(request, 'home.html')



# Load your trained model
model = joblib.load('model.pkl file path') #update the path here please


import joblib
import numpy as np
from django.shortcuts import render

# Load your trained model (make sure the path is correct)
model = joblib.load('model.pkl file path') #update the path here please

import joblib
import numpy as np
from django.shortcuts import render

# Load the trained model and the vectorizer
model = joblib.load('model.pkl file path') #update the path here please
vectorizer = joblib.load('model.pkl file path') #update the path here please

def result_view(request):
    if request.method == 'POST':
        # Get the user input from the form
        user_input = request.POST.get('text_input')

        # Transform the input data using the same vectorizer used during model training
        input_data = vectorizer.transform([user_input])  # Convert text to numerical data

        # Make the prediction using the transformed input data
        prediction = model.predict(input_data)

        # Return the prediction result to the template
        return render(request, 'result.html', {'prediction': prediction})

    return render(request, 'index.html')



# Load model and vectorizer
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
with open(model_path, 'rb') as model_file:
    model, vectorizer = pickle.load(model_file)

# View function to predict sentiment
def predict_sentiment(request):
    if request.method == 'POST':
        text = request.POST.get('text')  # Get text from user input
        # Convert the text to the same vector format as the training data
        text_vector = vectorizer.transform([text])
        # Predict sentiment
        sentiment = model.predict(text_vector)[0]
        return render(request, 'result.html', {'sentiment': sentiment})
    return render(request, 'home.html')
