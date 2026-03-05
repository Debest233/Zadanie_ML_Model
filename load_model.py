import joblib
import pandas as pd
from sklearn.datasets import load_wine

# Wczytanie modelu
model = joblib.load('model_v1.joblib')
print("Model wczytany poprawnie")

data = load_wine()
sample_df = pd.DataFrame([data.data[0]], columns=data.feature_names)

prediction = model.predict(sample_df)
print(f"Predykcja dla przykładowego rekordu: {prediction[0]} (Prawidłowa klasa: {data.target[0]})")