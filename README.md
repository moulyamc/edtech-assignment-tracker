# EdTech Assignment Tracker

A simplified fullstack project for an EdTech platform where teachers can post assignments and students can submit them.

## 🔧 Tech Stack

- **Backend:** FastAPI (Python)
- **Database:** SQLite (SQLAlchemy)
- **Frontend:** HTML, CSS, JavaScript
- **Auth:** JWT (Role-based: student & teacher)

---

## 📁 Project Structure

```
edtech_assignment_tracker/
├── backend/
│   ├── main.py
│   └── app/
│       ├── routers/
│       │   ├── auth.py
│       │   ├── assignments.py
│       │   └── submissions.py
│       ├── database/
│       │   ├── database.py
│       │   └── models.py
├── frontend/
│   ├── create_assignment.html
│   ├── submit_assignment.html
│   └── view_submissions.html
```

---

## 🚀 Getting Started

### 1. Setup Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Requirements

```bash
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose
```

### 3. Run the API

```bash
cd backend
uvicorn main:app --reload
```

Visit [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger API docs.

---

## 🌐 Frontend

Just open the HTML files in `frontend/` folder:
- `create_assignment.html` – Teacher creates assignment
- `submit_assignment.html` – Student submits assignment
- `view_submissions.html` – Teacher views submissions

---

## 🔐 Auth Strategy

- JWT token is required for protected routes
- Include `token` in the URL for now (for simplicity)
- Roles: `student`, `teacher`

---

## 🧪 Sample Usage

- **Signup:** `POST /signup`
- **Login:** `POST /login` → returns token
- **Create Assignment (teacher):** `POST /assignments`
- **Submit Assignment (student):** `POST /assignments/{id}/submit`
- **View Submissions (teacher):** `GET /assignments/{id}/submissions`

---

## 📝 Notes

- Simple structure for demo; you can add enhancements like:
  - File uploads
  - UI frameworks (React)
  - Persistent PostgreSQL DB
  - OAuth/SSO authentication

