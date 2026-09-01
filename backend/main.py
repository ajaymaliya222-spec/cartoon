from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Cartoon API", version="1.0.0")

class Character(BaseModel):
    name: str
    age: int
    show: str
    power: str

characters = {
    "shinchan": Character(name="Shinchan", age=5, show="Crayon Shin-chan", power="Mischief"),
    "doraemon": Character(name="Doraemon", age=10, show="Doraemon", power="Anywhere Door"),
    "ben10": Character(name="Ben 10", age=10, show="Ben 10", power="Omnitrix"),
}

@app.get("/")
def home():
    return {"message": "Cartoon API is running", "endpoints": ["/shinchan", "/doraemon", "/ben10", "/characters", "/character"]}

@app.get("/shinchan")
def shinchan():
    return characters["shinchan"]

@app.get("/doraemon")
def doraemon():
    return characters["doraemon"]

@app.get("/ben10")
def ben10():
    return characters["ben10"]

@app.get("/characters")
def get_all_characters():
    return characters

@app.post("/character")
def add_character(character: Character):
    key = character.name.lower().replace(" ", "")
    characters[key] = character
    return {"message": "Character added successfully", "character": character}
