from flask import Flask, render_template, request, jsonify
from textblob import TextBlob
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend
import matplotlib.pyplot as plt
import base64
from io import BytesIO

app = Flask(__name__)

# Sentiment thresholds
POSITIVE_THRESHOLD = 0.1   # more sensitive
NEGATIVE_THRESHOLD = -0.1

# Neutral keywords
NEUTRAL_KEYWORDS = [
    "okay", "ok", "fine", "not bad", "average",
    "decent", "satisfactory", "alright", "normal", "so-so"
]

def analyze_sentiment_text(text):
    """Analyze sentiment using TextBlob"""
    if not text.strip():
        return {"error": "Please enter a review!"}

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    text_lower = text.lower()

    # Override for neutral keywords
    if any(word in text_lower for word in NEUTRAL_KEYWORDS):
        sentiment = "Neutral 😐"
        color = "#f59e42"
        data = {"Positive": 0, "Neutral": 100, "Negative": 0}
        polarity = 0.0  # Force display to 0 for mild reviews
    elif polarity > POSITIVE_THRESHOLD:
        sentiment = "Positive 😊"
        color = "#16a34a"
        data = {"Positive": 100, "Neutral": 0, "Negative": 0}
    elif polarity < NEGATIVE_THRESHOLD:
        sentiment = "Negative 😞"
        color = "#dc2626"
        data = {"Positive": 0, "Neutral": 0, "Negative": 100}
    else:
        sentiment = "Neutral 😐"
        color = "#f59e42"
        data = {"Positive": 0, "Neutral": 100, "Negative": 0}

    # Create chart
    chart_image = create_pie_chart(data)

    return {
        "sentiment": sentiment,
        "color": color,
        "polarity": round(polarity, 3),
        "chart": chart_image
    }

def create_pie_chart(data):
    """Create pie chart and return as base64"""
    labels = list(data.keys())
    sizes = list(data.values())
    color_map = {
        "Positive": "#16a34a",
        "Neutral": "#f59e42",
        "Negative": "#dc2626"
    }
    colors = [color_map[label] for label in labels]

    fig, ax = plt.subplots(figsize=(5, 5), dpi=80)
    wedges, texts, autotexts = ax.pie(
        sizes,
        colors=colors,
        autopct='%1.0f%%',
        startangle=90,
        textprops={'fontsize': 12, 'weight': 'bold', 'color': 'white'}
    )

    ax.set_title("Sentiment Analysis", fontsize=14, fontweight='bold', pad=20)

    # ✅ Legend below pie chart
    #ax.legend(
      #  labels,
      #  loc="lower center",
       # bbox_to_anchor=(0.5, -0.15),
       # ncol=3,
      #  frameon=False,
      #  fontsize=10
    #)

    plt.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', facecolor='white')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()
    plt.close(fig)

    return f"data:image/png;base64,{img_base64}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        text = data.get('text', '')
        result = analyze_sentiment_text(text)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
