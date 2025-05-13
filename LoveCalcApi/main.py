from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI(
    title="Love Calculator API",
    description="En API til at beregne kærligheds-kompatibilitet mellem to personer",
    version="1.0.0"
)

class Names(BaseModel):
    name1: str
    name2: str

def calculate_love_percentage(name1: str, name2: str) -> int:
    # Konverter navne til lowercase for konsistens
    combined_names = (name1.lower() + name2.lower()).strip()
    
    # Brug en deterministisk metode baseret på navnene
    random.seed(combined_names)
    
    # Generér et tal mellem 0-100
    love_percentage = random.randint(50, 100)  
    
    return love_percentage

def get_love_message(percentage: int) -> str:
    if percentage >= 90:
        return "Wow! I er det perfekte match!"
    elif percentage >= 80:
        return "Der er stærk kærlighed mellem jer!"
    elif percentage >= 70:
        return "I har gode chancer sammen!"
    elif percentage >= 60:
        return "Der er potentiale for kærlighed!"
    else:
        return "I kunne være gode venner!"

@app.get("/")
async def root():
    return {
        "message": "Velkommen til Love Calculator API!",
        "usage": "Send en POST request til /calculate med name1 og name2"
    }

@app.post("/calculate")
async def calculate_love(names: Names):
    if not names.name1 or not names.name2:
        raise HTTPException(status_code=400, detail="Begge navne skal være udfyldt")
    
    percentage = calculate_love_percentage(names.name1, names.name2)
    message = get_love_message(percentage)
    
    return {
        "name1": names.name1,
        "name2": names.name2,
        "percentage": percentage,
        "message": message
    } 