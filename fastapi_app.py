from fastapi import FastAPI
from pydantic import BaseModel
from tools.diagnosis_tools import get_diagnosis
from tools.pubmed_fetcher import fetch_pubmed_articles_with_metadata
from tools.summarizer import summarize_text
from tools.symptom_extracter import extract_symptoms

app= FastAPI()

class SymptomInput(BaseModel):
    description:str

@app.post("/diagnosis")
def diagnose_patient(data:SymptomInput):
    symptoms= extract_symptoms(data.description)
    diagnosis=get_diagnosis(symptoms)
    pubmed_raw=fetch_pubmed_articles_with_metadata(" ".join(symptoms))
    summary= summarize_text(pubmed_raw[:3000])

    return{
        "symptoms":symptoms,
        "diagnosis":diagnosis,
        "pubmed_summary":summary
    }

#python -m uvicorn fastapi_app:app --reload --port 8080
