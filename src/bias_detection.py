from sklearn.ensemble import RandomForestClassifier
import numpy as np

def train_bias_model(X, y):
    model = RandomForestClassifier()
    model.fit(X, y)
    return model

def detect_bias(model, features):
    prediction = model.predict([features])
    if prediction[0] == 1:
        return "High-risk market pattern detected"
    else:
        return "Market pattern appears stable"