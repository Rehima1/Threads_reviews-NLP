from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load("Threads_review.pkl")
vec = joblib.load("vectorizer.pkl")

print("Model and vectorizer loaded successfully.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        review_description = request.form.get('reviewDescription', '').strip()
        if not review_description:
            return jsonify({"error": "Review description cannot be empty."}), 400

        vec_text = vec.transform([review_description])
        sentiment_pred = model.predict(vec_text)
        sentiment = "Positive" if sentiment_pred[0] == 1 else "Negative"

        result = {
            "sentiment": sentiment,
            "source": request.form.get('source', ''),
            "rating": request.form.get('rating', ''),
            "review_description": review_description
        }
        return jsonify(result)

    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)