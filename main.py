import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Zadanie 1

data = load_wine()
df = pd.DataFrame(data=data.data, columns=data.feature_names)
df['target'] = data.target

print("ZADANIE 1")
print(f"Pierwsze 5 wierszy:\n{df.head()}\n")
print(f"Rozmiar danych: {df.shape}")
print(f"Typy kolumn:\n{df.dtypes}\n")

# Zadanie 2
X = df.drop('target', axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("ZADANIE 2")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print("Raport klasyfikacji:")
print(classification_report(y_test, y_pred))

# Zadanie 3
model_name = 'model_v1.joblib'
joblib.dump(model, model_name)
print(f"Model zapisany jako {model_name} ")