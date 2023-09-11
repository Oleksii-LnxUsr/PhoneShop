**PhoneShop**
Websit

# PhoneShop

PhoneShop is a simple e-commerce website for buying and selling mobile phones. This repository contains the source code for the PhoneShop project.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Images](#images)

## Features

- User authentication and registration.
- Browse and search for mobile phones.
- Add mobile phones to the shopping cart.
- Checkout and place orders.
- Admin panel for managing products and orders.
- Responsive design for mobile and desktop.

## Technologies Used

- Django: Backend web framework.
- HTML, CSS, JavaScript: Frontend development.
- SQLite: Database for development.
- PostgreSQL: Database for production (optional).
- Bootstrap: Frontend CSS framework.

## Getting Started

To run this project locally, follow these steps:

1. Clone this repository: `git clone https://github.com/JustWriteCode0/PhoneShop.git`
2. Change to the project directory: `cd PhoneShop`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Create and apply database migrations: `python manage.py makemigrations` and `python manage.py migrate`
5. Create a superuser for admin access: `python manage.py createsuperuser`
6. Start the development server: `python manage.py runserver`

## Usage

- Visit `http://localhost:8000` in your web browser to access the PhoneShop website.
- Use the admin panel at `http://localhost:8000/admin` to manage products and orders (login with superuser credentials created in step 5 of "Getting Started").

## Images
Catalog with all products

![Screenshot_1](https://github.com/JustWriteCode0/PhoneShop/assets/111213562/8f95b9ee-97e8-4b15-983f-feec1c4202f6)

Select products by company

![Screenshot_2](https://github.com/JustWriteCode0/PhoneShop/assets/111213562/6a69d522-a63c-4b65-8d71-bcde56d7ebd3)

Shopping cart with all the products you have selected, the quantity can be changed or deleted.

![Screenshot_4](https://github.com/JustWriteCode0/PhoneShop/assets/111213562/bce1bf2d-631c-4929-ba7e-267e5a0fec94)

Page with information about product with carousel

![Screenshot_8](https://github.com/JustWriteCode0/PhoneShop/assets/111213562/6ca05904-9e33-4bef-ab83-13858cbffee9)

You orders with status such as - preparing, in the way, delivered

![Screenshot_7](https://github.com/JustWriteCode0/PhoneShop/assets/111213562/c3f95ef8-0141-4a70-945c-5a2c788be6db)


