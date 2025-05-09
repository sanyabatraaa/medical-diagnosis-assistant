import re

def extract_symptoms(text: str) -> list[str]:
    symptom_keywords = [
        "headache", "fever", "nausea", "fatigue", "pain", "cough", "sore throat", "runny nose",
        "congestion", "dizziness", "vomiting", "diarrhea", "chills", "sweating", "rash",
        "shortness of breath", "difficulty breathing", "muscle ache", "joint pain", "chest pain",
        "abdominal pain", "loss of appetite", "weight loss", "blurred vision", "sneezing",
        "itching", "swelling", "insomnia", "anxiety", "depression", "palpitations"
    ]
    
    # Join symptoms for use in regex; escape symptoms with spaces
    pattern = r"\b(" + "|".join(re.escape(symptom) for symptom in symptom_keywords) + r")\b"
    symptoms = re.findall(pattern, text.lower())
    return list(set(symptoms))
