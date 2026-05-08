from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Rule-based phishing detection
def detect_phishing(url):

    phishing_keywords = [
        "login",
        "verify",
        "secure",
        "account",
        "update",
        "bank",
        "paypal",
        "signin",
        "wallet",
        "free",
        "gift",
        "bonus",
        "claim",
        "bitcoin",
        "netflix",
        "amazon",
        "alert",
        "security",
        "confirm",
        "payment"
    ]

    suspicious_score = 0

    # Long URL
    if len(url) > 50:
        suspicious_score += 1

    # HTTP instead of HTTPS
    if url.startswith("http://"):
        suspicious_score += 1

    # Hyphen in domain
    if "-" in url:
        suspicious_score += 1

    # Too many dots
    if url.count(".") > 3:
        suspicious_score += 1

    # @ symbol
    if "@" in url:
        suspicious_score += 1

    # Check phishing keywords
    for word in phishing_keywords:
        if word in url.lower():
            suspicious_score += 1

    # Final decision
    if suspicious_score >= 3:
        return "PHISHING URL"
    else:
        return "SAFE URL"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    url = request.form['url']

    result = detect_phishing(url)

    return render_template(
        'result.html',
        prediction=result,
        url=url
    )

if __name__ == '__main__':
    app.run(debug=True)