from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

try:
    sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
except Exception as e:
    print(f"Error loading model: {e}")
    sentiment_pipeline = None

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    text_input = ""
    if request.method == "POST":
        text_input = request.form.get("text_to_analyze", "")
        if text_input and sentiment_pipeline:
            prediction = sentiment_pipeline(text_input)
            label = prediction['label']
            score = prediction['score'] * 100
            result = {"label": label, "confidence": f"{score:.2f}%"}
            
    return render_template("index.html", result=result, text_input=text_input)

if __name__ == "__main__":
    app.run(debug=True)
