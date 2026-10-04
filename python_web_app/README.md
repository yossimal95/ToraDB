# ToraDB - Python Web Interface

This directory contains a complete implementation of the ToraDB project using **Python**, featuring an embedded database (SQLite) and an interactive web user interface.
The project allows for easy management, browsing, and editing of data regarding Torah characters and their sources in a user-friendly way.

## ✨ Features

- **Browsing:** Easily navigate through the list of characters, their aliases, and family relationships (marriages, etc.).
- **Create:** Add new characters, aliases, and relationships to the database directly through the UI.
- **Update:** Seamlessly edit details of existing characters.
- **Search & Filter:** Quick search capabilities to find specific characters.
- **Clean Architecture:** Separation of concerns with distinct layers for API, Data Access, and Frontend.

## 🛠️ Tech Stack

- **Backend:** Python (Flask)
- **Database:** SQLite (with built-in SQL scripts and procedures structure)
- **Frontend:** HTML, CSS, JavaScript

## 🚀 How to Run

To run the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yossimal95/ToraDB.git
   cd ToraDB/python_web_app
   ```

2. **Create a virtual environment (Recommended):**
   ```bash
   python -m venv venv
   # Mac/Linux
   source venv/bin/activate
   # Windows
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```
   *The server will run locally, and you can access it in your browser at: `http://localhost:5000` (or another configured port).*

## 📁 Directory Structure

- `app.py` - The main application runner and API definitions.
- `DB/` - Contains the SQLite database file (`torah.db`).
- `infrastructure/` - Data access layer and query execution functions.
- `static/` - Frontend assets (HTML, CSS, JS).
- `requirements.txt` - Required Python packages.

---
*This project is designed to make Torah data accessible in a modern, developer-friendly, and end-user-friendly format.*
