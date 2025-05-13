from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Love Calculator API",
    description="An API to calculate love compatibility between two people",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins in development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Access environment variables
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG", "False") == "True"  # Convert the DEBUG value to a boolean
API_KEY = os.getenv("API_KEY")

class Names(BaseModel):
    name1: str
    name2: str

def calculate_love_percentage(name1: str, name2: str) -> int:
    # Convert names to lowercase for consistency
    combined_names = (name1.lower() + name2.lower()).strip()
    
    # Use a deterministic method based on the names
    random.seed(combined_names)
    
    # Generate a "love percentage" between 0-100
    love_percentage = random.randint(50, 100)  # Keep it positive! 😊
    
    return love_percentage

def get_love_message(percentage: int) -> str:
    if percentage >= 90:
        return "Wow! You are a perfect match!"
    elif percentage >= 80:
        return "There is a strong love between you!"
    elif percentage >= 70:
        return "You could be good friends!"
    elif percentage >= 60:
        return "There is potential for love!"
    else:
        return "You could be good friends!"

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Love Calculator API!",
        "usage": "Send a POST request to /calculate with name1 and name2",
        "documentation": "/docs"
    }

@app.post("/calculate")
async def calculate_love(names: Names):
    if not names.name1 or not names.name2:
        raise HTTPException(status_code=400, detail="Both names must be filled")
    
    percentage = calculate_love_percentage(names.name1, names.name2)
    message = get_love_message(percentage)
    
    return {
        "name1": names.name1,
        "name2": names.name2,
        "percentage": percentage,
        "message": message
    }

@app.get("/healthz")
async def health_check():
    return {"status": "healthy"}
