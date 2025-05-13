# Love Calculator API

En sjov API til at beregne kærligheds-kompatibilitet mellem to personer! 💘

## Installation

1. Installer afhængigheder:
```bash
pip install -r requirements.txt
```

2. Start serveren:
```bash
uvicorn main:app --reload
```

API'en vil nu køre på `http://localhost:8000`

## Brug af API'en

### Endpoints

#### GET /
Returnerer velkomstbesked og grundlæggende instruktioner.

#### POST /calculate
Beregner kærligheds-kompatibilitet mellem to navne.

**Request Body:**
```json
{
    "name1": "Peter",
    "name2": "Maria"
}
```

**Response:**
```json
{
    "name1": "Peter",
    "name2": "Maria",
    "percentage": 85,
    "message": "Der er stærk kærlighed mellem jer! ❤️"
}
```

## Swagger Documentation
Du kan finde den komplette API-dokumentation på `/docs` endpointet (http://localhost:8000/docs). 