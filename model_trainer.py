import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
    return model

if __name__ == "__main__":
    df = pd.read_csv('feature_data.csv')
    X = df.drop('label', axis=1)
    y = df['label']
    model = train_model(X, y)
    import joblib
    joblib.dump(model, 'earthquake_model.pkl')