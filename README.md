# ReviewSense – Sentiment Analysis

ReviewSense is a Python-based web application developed as part of a Machine Intelligence mini project. It analyzes customer reviews and classifies them into three sentiment categories: **Positive, Negative, and Neutral**.

The application uses Natural Language Processing (NLP) with TextBlob to identify the sentiment of text and Matplotlib to generate visual representations of the analysis.

## Features

- Analyze customer reviews.
- Classify reviews as Positive, Negative, or Neutral.
- Calculate sentiment polarity scores.
- Display sentiment analysis results.
- Generate pie charts for sentiment visualization.
- Simple and user-friendly web interface.

## Technologies Used

- **Python** – Core programming language
- **Flask** – Backend web framework
- **TextBlob** – Natural Language Processing and sentiment analysis
- **Matplotlib** – Data visualization
- **HTML** – Frontend structure
- **CSS** – Styling
- **JavaScript** – Frontend interaction

## How It Works

1. The user enters a customer review.
2. The review is sent to the Flask backend.
3. TextBlob analyzes the text and calculates its polarity.
4. The application classifies the sentiment.
5. Matplotlib generates a pie chart.
6. The sentiment result and chart are displayed on the webpage.

## Sentiment Categories

| Sentiment | Description |
|---|---|
| Positive | Indicates positive opinions or feedback |
| Negative | Indicates negative opinions or feedback |
| Neutral | Indicates neutral or balanced opinions |

## Project Structure

```text
ReviewSense-Sentiment-Analysis/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd ReviewSense-Sentiment-Analysis
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in your browser

```text
http://127.0.0.1:5000
```

## Future Enhancements

- Improve sentiment classification accuracy.
## Application Screenshots

### Homepage
![Homepage](screenshots/homepage.png)

### Positive Sentiment
![Positive Result](screenshots/positive-result.png)

### Negative Sentiment
![Negative Result](screenshots/negative-result.png)

### Neutral Sentiment
![Neutral Result](screenshots/neutral-result.png)