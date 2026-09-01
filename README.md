# Cartoon FastAPI + Python Frontend

A beginner-friendly project to learn REST APIs with FastAPI and a Python Tkinter frontend.

## 1. Create virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

## 2. Install requirements

```powershell
pip install -r requirements.txt
```

## 3. Start backend

From the project root:

```powershell
uvicorn backend.main:app --reload
```

Backend: http://127.0.0.1:8000
Swagger: http://127.0.0.1:8000/docs

## 4. Start Python frontend

Open another terminal, activate the same venv, then:

```powershell
python frontend/app.py
```

## How the Shinchan button works

1. You click **Shinchan**.
2. Python frontend sends `GET /shinchan`.
3. FastAPI matches `@app.get("/shinchan")`.
4. FastAPI returns a Python/Pydantic object which becomes JSON.
5. Frontend receives JSON and displays it.

Example response:

```json
{
    "name": "Shinchan",
    "age": 5,
    "show": "Crayon Shin-chan",
    "power": "Mischief"
}
```

## POST flow

Fill the form and click **POST Character**. The frontend sends JSON to `POST /character`, FastAPI validates it using the `Character` model, stores it in memory, and returns JSON.

Note: data is stored only in memory, so it resets when the backend restarts.
