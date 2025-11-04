# src/evaluate.py
from sklearn.metrics import accuracy_score


def evaluate_model(model, X_val, y_val):
    preds = model.predict(X_val)
    return {"accuracy": accuracy_score(y_val, preds)}
