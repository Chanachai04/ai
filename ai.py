from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
import uvicorn

model_name = "Thaweewat/wangchanberta-hyperopt-sentiment-01"
tokenizer_name = "airesearch/wangchanberta-base-att-spm-uncased"

# โหลด tokenizer แบบ slow
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(tokenizer_name, use_fast=False)
print("Model and tokenizer loaded successfully")

sentiment_pipeline = pipeline(
    "text-classification",
    model=model,
    tokenizer=tokenizer
)

label_map = {
    "LABEL_0": "negative",
    "LABEL_1": "positive"
}

app = FastAPI(title="Thai Sentiment API")

class TextRequest(BaseModel):
    text: str

@app.get("/")
async def root():
    return {
        "message": "Thai Sentiment Analysis API",
        "status": "running",
        "endpoints": {
            "POST /sentiment": "Analyze sentiment of Thai text"
        }
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/sentiment")
async def analyze_sentiment(request: TextRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text is required.")
    
    result = sentiment_pipeline(request.text)[0]

    return {
        "text": request.text,
        "sentiment": label_map.get(result["label"], "unknown"),
        "confidence": round(result["score"], 4)
    }

if __name__ == "__main__":
    uvicorn.run("ai:app", host="0.0.0.0", port=5000, reload=True)
