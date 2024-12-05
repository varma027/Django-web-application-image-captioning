import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Step 1: Prepare training data
# Example texts and their corresponding sentiment labels
data = [
    ("I love this product", "positive"),
    ("This is a terrible product", "negative"),
    ("It's okay, nothing special", "neutral"),
    ("I am so happy with this", "positive"),
    ("I hate this", "negative"),
    ("Not bad, could be better", "neutral")
]

# Separate texts and labels
texts, labels = zip(*data)

# Step 2: Convert text into a numerical format
vectorizer = TfidfVectorizer()  # Converts text into TF-IDF weighted vectors
X = vectorizer.fit_transform(texts)

# Step 3: Train a machine learning model
model = MultinomialNB()  # Naive Bayes classifier
model.fit(X, labels)  # Train the model

# Step 4: Save the model and vectorizer to files
with open('model.pkl', 'wb') as model_file:
    pickle.dump((model, vectorizer), model_file)

print("Model trained and saved to 'model.pkl'")
