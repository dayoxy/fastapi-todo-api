# FastAPI Todo API

```markdown
# 📝 FastAPI Todo App API

A full-featured Todo REST API built with **FastAPI**, **SQLAlchemy**, and **JWT authentication**, ready for deployment on **Render** using Docker.

---

## 🚀 Features

- ✅ JWT-based user registration & login
- ✅ Secure token-based authentication
- ✅ Create, read, and manage todo items
- ✅ SQLite database with SQLAlchemy ORM
- ✅ Dockerized and ready for cloud deployment
- ✅ Auto-generated Swagger docs

---

## 📁 Project Structure

```

fastapi-todo-api/
├── app/
│   ├── **init**.py
│   ├── main.py          # FastAPI app & routes
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── database.py      # DB config
│   ├── auth.py          # JWT logic
│   └── crud.py          # DB operations
├── Dockerfile
├── requirements.txt
├── render.yaml
└── README.md

````

---

## 🛠️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/dayoxy/fastapi-todo-api.git
cd fastapi-todo-api
````

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app locally

```bash
uvicorn app.main:app --reload
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🔐 Authentication

### Register a user

`POST /register`

```json
{
  "username": "yourname",
  "password": "yourpassword"
}
```

### Login to get a token

`POST /token` (uses `application/x-www-form-urlencoded`)

Returns:

```json
{
  "access_token": "jwt-token-string",
  "token_type": "bearer"
}
```

Use the token in the **Authorize** section of Swagger UI or set header manually:

```
Authorization: Bearer <your-token>
```

---

## 🧱 API Endpoints

| Method | Endpoint    | Description      |
| ------ | ----------- | ---------------- |
| POST   | `/register` | Register user    |
| POST   | `/token`    | Get JWT token    |
| GET    | `/users/me` | Get current user |
| POST   | `/todos/`   | Create a todo    |
| GET    | `/todos/`   | List all todos   |

---

## 🐳 Docker Setup

Build and run with Docker:

```bash
docker build -t fastapi-todo .
docker run -d -p 8000:8000 fastapi-todo
```

Then go to: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🌍 Deploying to Render

1. Push your code to GitHub
2. Go to [https://render.com](https://render.com)
3. Click **New Web Service**
4. Select the repo, use Docker, and deploy

✅ The app will be live at: `https://your-app.onrender.com`

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).

---

## 🙌 Contributions Welcome!

Feel free to fork, submit issues, or make pull requests.

---

```

---

Would you like me to include a **license** file or a **sample `.env` file** too?
```
