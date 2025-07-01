from flask import Flask, request, jsonify
from textblob import TextBlob
from googletrans import Translator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

# Initialize the VADER Sentiment Intensity Analyzer
analyzer = SentimentIntensityAnalyzer()

# Initialize the Google Translator
translator = Translator()

def analyze_sentiment(text: str, language: str = 'th'):
    """Analyze sentiment using TextBlob and VADER, after translating Thai to English."""
    
    # Translate text from Thai to English (if necessary)
    if language == 'th':
        translated_text = translator.translate(text, src='th', dest='en').text
    else:
        translated_text = text
    
    # Use TextBlob for sentiment analysis
    blob = TextBlob(translated_text)
    textblob_sentiment = blob.sentiment
    
    # Use VADER for sentiment analysis
    vader_score = analyzer.polarity_scores(translated_text)
    
    # Combine both sentiment scores for more insights
    sentiment = {
        'textblob': {
            'polarity': textblob_sentiment.polarity,
            'subjectivity': textblob_sentiment.subjectivity
        },
        'vader': vader_score
    }
    
    return sentiment

@app.route('/sentiment', methods=['POST'])
def sentiment_analysis():
    """Handle sentiment analysis API requests."""
    
    # Get text from the incoming request
    data = request.get_json()
    text = data.get('text', '')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    # Analyze sentiment
    sentiment = analyze_sentiment(text, language='th')
    
    return jsonify({
        'sentiment': sentiment
    })

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)