# NutriMoug 🥗

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

A personalized nutrition web app: track your meals, monitor your macros, plan your week and visualize your progress on an interactive dashboard.

Built as a tutored university project (Licence Informatique).

## ✨ Features

- **Account & profile** — sign up, log in, personal nutritional profile
- **Smart calculations** — daily calorie needs, macros (protein/carbs/fat), water intake, BMI
- **Recipes** — browse recipes, save your favorites
- **Meal planning** — organize your week of meals
- **Food journal** — log what you eat every day
- **Weight tracking** — follow your weight over time
- **Statistics** — charts and an interactive dashboard (Chart.js)

## 🛠️ Stack

- **Backend:** Python, Flask, mysql-connector-python
- **Database:** MySQL
- **Frontend:** HTML5, CSS3, JavaScript, Chart.js, Font Awesome

## 🚀 Getting started

**Prerequisites:** Python 3.10+, MySQL 8+

```bash
# 1. Clone the repo
git clone https://github.com/medreda091/Nutrimoug.git
cd Nutrimoug

# 2. Create a virtual environment and install dependencies
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 3. Configure your environment
cp .env.example .env
# then edit .env with your MySQL credentials and a secret key

# 4. Create the database (see database/ for the schema) and run
python app.py
```

Open http://localhost:5000 in your browser.

> 🔒 Configuration (database credentials, secret key) is loaded from environment variables — never commit your `.env` file.

## 📁 Project structure

```
├── app.py                 # Flask app entry point
├── config.py              # App configuration
├── database/              # MySQL connection layer
├── routes/                # Blueprints: auth, dashboard, journal, planning,
│                          #   poids, profil, favoris, recettes
├── services/              # Business logic: nutrition, menus, statistics
├── templates/             # Jinja2 templates
└── static/                # CSS, JS, images
```

## 👤 Author

**Reda Ait Smouguen** — Master 1 Computer Science @ Université Claude Bernard Lyon 1

- GitHub: [@medreda091](https://github.com/medreda091)
- LinkedIn: [reda-ait-smouguen](https://www.linkedin.com/in/reda-ait-smouguen-4b7b79200)
