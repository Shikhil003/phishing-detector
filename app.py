from flask import Flask, render_template, request
import joblib
from url_feature_extraction import extract_features

app = Flask(__name__)

model = joblib.load("phishing_model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    url = request.form.get("url")
    if url:
        try:
            features = extract_features(url)
            features_scaled = scaler.transform([features])
            prediction = model.predict(features_scaled)[0]
            result = "✅ Legitimate Website" if prediction == 1 else "🚨 Phishing Website"
        except Exception as e:
            result = f"❌ Error: {str(e)}"
        return render_template("index.html", prediction=result, url=url)
    return render_template("index.html", prediction="❌ No URL provided")

if __name__ == '__main__':
    app.run(debug=True)