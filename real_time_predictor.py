import pandas as pd
import joblib
from feature_extractor import extract_features

model = joblib.load('earthquake_model.pkl')

def predict_real_time(dataframe):
    features = extract_features(dataframe)
    X = pd.DataFrame([features])
    prediction = model.predict(X)
    return prediction

if __name__ == "__main__":
    df = pd.read_csv('real_time_data.csv')
    prediction = predict_real_time(df)
    print(f'Prediction: {"Earthquake" if prediction[0] == 1 else "No Earthquake"}')