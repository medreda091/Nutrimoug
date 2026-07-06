# NutriMoug

NutriMoug est une application web de nutrition personnalisée développée dans le cadre d'un projet tutoré en Licence Informatique à l'Université Lumière Lyon 2.

L'application permet aux utilisateurs de calculer leurs besoins nutritionnels, suivre leur alimentation, organiser leurs repas et visualiser leur progression grâce à un tableau de bord interactif.

---

## Fonctionnalités

- Création de compte utilisateur
- Connexion et déconnexion
- Gestion du profil nutritionnel
- Calcul automatique des besoins caloriques
- Calcul des protéines, glucides et lipides
- Calcul de la consommation quotidienne d'eau
- Calcul de l'Indice de Masse Corporelle (IMC)
- Recommandation de menus personnalisés
- Consultation de recettes
- Ajout de recettes aux favoris
- Création d'un planning hebdomadaire des repas
- Journal alimentaire
- Suivi de l'évolution du poids
- Statistiques nutritionnelles
- Tableau de bord interactif

---

## Technologies utilisées

### Backend

- Python
- Flask

### Base de données

- MySQL

### Frontend

- HTML5
- CSS3
- JavaScript

### Bibliothèques

- Chart.js
- Font Awesome

---

## Structure du projet

```text
Nutrimoug/

├── database/
│   └── db.py
│
├── routes/
│   ├── auth.py
│   ├── dashboard.py
│   ├── favoris.py
│   ├── journal.py
│   ├── planning.py
│   ├── poids.py
│   └── profil.py
│
├── services/
│   ├── menus.py
│   ├── nutrition.py
│   ├── recettes.py
│   └── statistiques.py
│
├── static/
│   ├── assets/
│   ├── css/
│   └── js/
│
├── templates/
│   ├── components/
│   ├── dashboard/
│   ├── dashboard.html
│   ├── index.html
│   ├── login.html
│   └── register.html
│
├── app.py
└── README.md
```

---

## Installation

### 1. Cloner le projet

```bash
git clone https://github.com/medreda091/Nutrimoug.git
```

### 2. Accéder au dossier

```bash
cd Nutrimoug
```

### 3. Installer les dépendances

```bash
pip install flask
pip install mysql-connector-python
```

### 4. Configurer la base de données

Créer une base de données MySQL puis importer le fichier SQL du projet.

Modifier ensuite les informations de connexion dans :

```text
database/db.py
```

### 5. Lancer l'application

```bash
python app.py
```

Ouvrir ensuite votre navigateur à l'adresse :

```text
http://127.0.0.1:5000
```

---

## Modules de l'application

### Authentification

- Inscription
- Connexion
- Déconnexion

### Tableau de bord

- Calories journalières
- IMC
- Consommation d'eau
- Objectifs nutritionnels

### Nutrition

- Calories
- Protéines
- Glucides
- Lipides
- Recommandations personnalisées

### Recettes

Chaque recette contient :

- Calories
- Protéines
- Glucides
- Lipides
- Ingrédients
- Étapes de préparation
- Temps de préparation
- Nombre de portions

### Favoris

Les utilisateurs peuvent enregistrer leurs recettes préférées.

### Planning hebdomadaire

Organisation des repas de la semaine avec attribution des recettes aux différents repas.

### Journal alimentaire

Enregistrement des aliments consommés afin de suivre l'apport nutritionnel quotidien.

### Suivi du poids

Ajout de nouvelles mesures et consultation de l'historique.

### Statistiques

Visualisation de l'évolution du poids à l'aide de graphiques interactifs.

---

## Perspectives d'amélioration

- Génération automatique de menus avec l'intelligence artificielle
- Sécurisation des mots de passe par hachage
- Export des statistiques au format PDF
- Notifications de rappel
- Version responsive pour mobile
- Intégration d'une API nutritionnelle
- Tableau de bord administrateur

---

## Auteur

**Mohamed Reda Ait Smouguen**

Projet tutoré réalisé dans le cadre de la Licence Informatique.

Université Lumière Lyon 2

---

