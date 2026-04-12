from transformers import pipeline

# Initialize the NLP pipeline for Sentiment Analysis.
# The first time this code runs, it automatically downloads 
# the pretrained English sentiment model via HuggingFace!
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_project(text: str) -> dict:
    """
    Analyzes a resume project description and returns its strength,
    confidence score, and a beginner-friendly suggestion for improvement.
    """
    # The pipeline evaluates the sentence and returns a list containing a dict
    # Example output: [{'label': 'POSITIVE', 'score': 0.9998}]
    result = sentiment_pipeline(text)[0]
    
    label = result['label']
    confidence = round(result['score'], 2)
    
    if label == "POSITIVE":
        strength = "strong"
        suggestion = "Great project description! It highlights positive impact effectively."
    else:
        strength = "weak"
        suggestion = "Consider starting your description with stronger action verbs like: Developed, Engineered, Implemented, Optimized, or Designed."
        
    return {
        "project": text,
        "strength": strength,
        "confidence": confidence,
        "suggestion": suggestion
    }
