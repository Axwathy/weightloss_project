# Weight Loss Management Website

A web-based **Weight Loss Management System** developed using Django and MySQL/MariaDB. The application allows users to create an account, log in, and manage their weight records.

## Project Overview

The Weight Loss Management Website helps users maintain and track their weight records. Users can securely register and log in to the system, add their weight, and manage previously added records.

The project was developed as a Django web application with a database backend.

## Technologies Used

* **Frontend:** HTML, CSS, Bootstrap
* **Backend:** Python, Django
* **Database:** MySQL/MariaDB
* **Database Tool:** XAMPP/phpMyAdmin
* **Version Control:** Git and GitHub

## Features

* User registration
* User login and logout
* User authentication
* Add weight records
* Automatically store the current date
* View weight records
* Edit weight records
* Delete weight records
* User-specific weight management
* Django admin panel
* MySQL/MariaDB database integration

## Project Structure

```text
weightloss_project/
│
├── WeightLossProject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── tracker/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   └── ...
│
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Requirements

Before running the project, install the following:

* Python 3
* Django
* MySQL or MariaDB
* XAMPP
* Git

## Installation and Setup

### 1. Clone the Repository

Open your terminal or PowerShell and run:

```bash
git clone https://github.com/Axwathy/weightloss_project.git
```

Move into the project folder:

```bash
cd weightloss_project
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

If the `requirements.txt` file is not available, install Django manually:

```bash
pip install django
```

### 4. Start MySQL/MariaDB

Open XAMPP Control Panel and start:

* Apache, if required
* MySQL

Create a database named:

```text
weightloss_db
```

The database can be created using phpMyAdmin.

### 5. Configure Environment Variables

Create a file named `.env` inside the project root folder.

Use the following format:

```env
DB_NAME=weightloss_db
DB_USER=your_database_username
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=3306
```

Replace the username and password with the database credentials available on your computer.

**Important:** Do not upload the `.env` file to GitHub because it contains private database credentials. Use `.env.example` as a reference.

### 6. Apply Database Migrations

Run:

```bash
python manage.py makemigrations
```

Then:

```bash
python manage.py migrate
```

### 7. Create an Admin User

To access the Django admin panel, run:

```bash
python manage.py createsuperuser
```

Enter the required username, email address, and password.

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open the following URL in your browser:

```text
http://127.0.0.1:8000/
```

## Admin Panel

The Django admin panel is available at:

```text
http://127.0.0.1:8000/admin/
```

Log in using the superuser account created with:

```bash
python manage.py createsuperuser
```

## Application URLs

| Page          | URL             |
| ------------- | --------------- |
| Home          | `/`             |
| Register      | `/register/`    |
| Login         | `/login/`       |
| Logout        | `/logout/`      |
| Add Weight    | `/add-weight/`  |
| View Weight   | `/view-weight/` |
| Edit Weight   | `/edit/<id>/`   |
| Delete Weight | `/delete/<id>/` |
| Admin Panel   | `/admin/`       |

## How the Application Works

1. A new user registers on the website.
2. The user logs in using their username and password.
3. The logged-in user can add their weight.
4. The current date is automatically stored with the weight record.
5. The user can view their weight records.
6. The user can edit or delete their records.
7. The Django admin can manage the application through the admin panel.

## Database

The project uses MySQL/MariaDB for storing application data.

The database contains information related to:

* User accounts
* Weight records
* Weight entry dates
* User-specific weight information

## Security Notes

* User authentication is handled by Django.
* The `.env` file is excluded from GitHub using `.gitignore`.
* Database credentials should not be shared publicly.
* Use a separate database password for development and production.
* `DEBUG = True` should not be used in a production environment.

## Future Improvements

* Add weight progress charts
* Add date-range filtering
* Add BMI calculation
* Add weight goals
* Add progress reports
* Add email reminders
* Improve mobile responsiveness
* Deploy the project online

## Author

**Aswathy**

## GitHub Repository

[Weight Loss Management Website](https://github.com/Axwathy/weightloss_project)
