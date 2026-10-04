# TorahDB - Python Web Interface
<img width="1208" height="213" alt="image" src="https://github.com/user-attachments/assets/6c804191-d4bc-4867-8a13-8b5c4bc8df94" />

This directory contains a complete implementation of the TorahDB project using **Python**, featuring an embedded database (SQLite) and an interactive web user interface.
The project allows for easy management, browsing, and editing of data regarding Torah characters and their sources in a user-friendly way.

## ✨ Features

- **Browsing:** Easily navigate through the list of characters, their aliases, and family relationships (marriages, etc.).
- **Create:** Add new characters, aliases, and relationships to the database directly through the UI.
- **Update:** Seamlessly edit details of existing characters.
- **Search & Filter:** Quick search capabilities to find specific characters.
- **Clean Architecture:** Separation of concerns with distinct layers for API, Data Access, and Frontend.
<img width="617" height="614" alt="image" src="https://github.com/user-attachments/assets/0efd5f60-2122-49ef-afe0-992d2287089a" />

## 🛠️ Tech Stack

- **Backend:** Python (Flask)
- **Database:** SQLite (with built-in SQL scripts and procedures structure)
- **Frontend:** HTML, CSS, JavaScript

## 🚀 How to Run

To run the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yossimal95/TorahDB.git
   cd TorahDB/python_web_app
   ```

2. **Install dependencies:**
   ```bash
   pip install flask
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```
   *The server will run locally, and you can access it in your browser at: `http://localhost:5000` (or another configured port).*

## 📁 Directory Structure

- `app.py` - The main application runner and server configuration.
- `db/` - Contains the SQLite database file (`torah.db`).
- `api/` - API endpoints and route handlers for frontend-backend communication.
- `infrastructure/` - Data access layer and query execution functions.
- `static/` - Frontend assets (HTML, CSS, JS).
