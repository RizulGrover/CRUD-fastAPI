
# FastAPI CRUD App

A beginner-friendly yet production-style FastAPI CRUD application that allows creating, reading, updating, and deleting user feedback. Built with **FastAPI**, **SQLAlchemy**, **SQLite**, and deployed on **Render**.

---

## Features

- Create new feedback entries
- View all feedback
- View a single feedback item
- Update feedback
- Delete feedback
- Auto-generated timestamps
- Rating-based status (Positive / Negative)
- Built with clean architecture and Pydantic validation
- Interactive API documentation with Swagger UI

---

## Tech Stack

| Component | Technology |
|----------|------------|
| Backend API | FastAPI |
| ORM | SQLAlchemy |
| Database | SQLite |
| Schema Validation | Pydantic |
| Deployment | Render |
| Docs | Swagger / ReDoc |

---

## Project Structure

```
fastapi-crud-app/
│
├── main.py
├── models.py
├── schemas.py
├── database.py
├── requirements.txt
└── Procfile
```

---

##  Run Locally

### 1️ Clone the repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2️ Create Virtual Environment (Optional but recommended)
Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️ Start the Server
```bash
uvicorn main:app --reload
```

### 5️ Open in Browser
- Swagger UI → http://127.0.0.1:8000/docs  
- ReDoc UI → http://127.0.0.1:8000/redoc  


## API Routes

| METHOD | ENDPOINT | DESCRIPTION |
|--------|----------|-------------|
| POST | `/feedbacks` | Create feedback |
| GET | `/feedbacks` | Get all feedback |
| GET | `/feedbacks/{id}` | Get one feedback |
| PUT | `/feedbacks/{id}` | Update feedback |
| DELETE | `/feedbacks/{id}` | Delete feedback |

### Example Request (POST `/feedbacks`)
```json
{
  "username": "Rohit",
  "rating": 9,
  "comment": "Excellent API!"
}
```

---

## Contribution

You are welcome to:

✔ Open issues  
✔ Suggest features  
✔ Fork and submit PRs  

---

