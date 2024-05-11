import pandas as pd
from scipy.fft import fft

def extract_features(dataframe):
    features = {}
    for axis in ['x', 'y', 'z']:
        axis_data = dataframe[axis]
        features[f'{axis}_mean'] = axis_data.mean()
        features[f'{axis}_std'] = axis_data.std()
        features[f'{axis}_fft'] = fft(axis_data).real[:10]  # Get the first 10 FFT components
    return features

if __name__ == "__main__":
    df = pd.read_csv('real_time_data.csv')
    features = extract_features(df)
    print(features)