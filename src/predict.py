import joblib
from feature_extraction import extract_features

model = joblib.load("model/model.pkl")

def predict_url(url):
    features = extract_features(url)

    prediction = model.predict([features])

    return prediction[0]