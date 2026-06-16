# Expense Tracker Django Project

Expense Tracker is a basic Django web application that helps users manage their income and expenses. It allows users to add, view, edit, and delete transactions. The dashboard shows total income, total expense, and current balance.

## Features

* Add income and expense transactions
* View all transactions in a table
* Edit transaction details
* Delete transactions
* Calculate total income
* Calculate total expense
* Show current balance
* Django admin integration
* SQLite database

## Tech Stack

* Python
* Django
* SQLite
* HTML
* CSS
* Git and GitHub

## Project Structure

```text
expense_tracker/
│
├── expense_tracker/
│   ├── settings.py
│   ├── urls.py
│
├── tracker/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── templates/
│   └── static/
│
├── manage.py
├── requirements.txt
└── README.md
```

## How to Run This Project

1. Clone the repository

```bash
git clone https://github.com/pranjal3350/expense-tracker-django.git
```

2. Go inside the project folder

```bash
cd expense-tracker-django
```

3. Install required packages

```bash
pip install -r requirements.txt
```

4. Run migrations

```bash
python manage.py migrate
```

5. Create superuser

```bash
python manage.py createsuperuser
```

6. Run the server

```bash
python manage.py runserver
```

7. Open in browser

```text
http://127.0.0.1:8000/
```

## Current Status

This is the first working version of the project. It includes basic CRUD functionality and dashboard calculation.

## Upcoming Improvements

* Custom user login and register page
* Better UI design
* Category-wise filtering
* Monthly expense report
* Charts for income and expense
* Responsive design

## Author

Pranjal Dwivedi
