# 📰 Vistablog

**Vistablog** is a personal blog web application built with **Django**, featuring a responsive frontend and a simple backend system for managing blog posts across various categories.

---

## 🚀 Features

- 🧠 **Dynamic blog system** — Create and display posts under categories like Tech, Sport, Science, and People & Places.  
- 💻 **Responsive design** — Clean and modern UI that works across desktop and mobile devices.  
- 📂 **Organized layout** — Navbar with dropdown categories,  and a structured footer with quick links.  
- 🧰 **Contact form** — Email-based form validation with environment variable support.  

---

## 🏗️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (default, can be changed)
- **Version Control:** Git & GitHub

---

## ⚙️ Project Setup

Follow these steps to run **Vistablog** locally:

### 1️⃣ Clone the Repository 

git clone https://github.com/olalekan7857/Vistablog.git
cd Vistablog

2️⃣ Create and Activate a Virtual Environment
python -m venv .venv
# Activate on Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Database Migrations
python manage.py migrate

5️⃣ Start the Development Server
python manage.py runserver


Then visit: http://127.0.0.1:8000/

🔐 Environment Variables

Create a .env file in the project root and add:

EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_generated_app_password


Keep this file private — it’s already listed in .gitignore.

🖼️ Project Structure
Vistablog/
├── vistablog_project/
│   ├── manage.py
│   ├── vistablog/        # Main app
│   ├── templates/
│   ├── static/
│   └── ...
├── requirements.txt
├── .env
├── .gitignore
└── README.md

✨ Future Improvements

🔑 Add user authentication (register/login)


☁️ Deploy to a live hosting platform

🧑‍💻 Author

Olalekan Ibrahim
Full-Stack Developer | Django & Frontend Enthusiast
🌐 GitHub: olalekan7857
git clone https://github.com/olalekan7857/Vistablog.git
cd Vistablog
