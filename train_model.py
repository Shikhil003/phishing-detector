# train_model.py
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
from preprocess import load_and_preprocess_data

# Load data
X_train, X_test, y_train, y_test, scaler = load_and_preprocess_data('Training_dataset.arff')

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save model and scaler
joblib.dump(model, 'phishing_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
