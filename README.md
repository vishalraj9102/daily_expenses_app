Here's the updated `README.md` with PostgreSQL as the database and instructions for using **Postman** for API testing. I've also included some icons to make the file look visually appealing.

---

# 📝 Daily Expenses App

This is a **Daily Expenses Management Application** built using Flask that allows users to register, create expenses, and track their financial activities.

## ✨ Features
- **User Registration**: Register a new user with basic information.
- **Expense Management**: Create, manage, and retrieve expenses.
- **REST API**: RESTful API for user and expense operations.
- **Input Validation**: Validates request data using schema-based validation.

---

## 📚 Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Testing the API](#testing-the-api)
- [Contributing](#contributing)
- [License](#license)

---

## ⚙️ Prerequisites

Ensure you have the following installed:

- **Python 3.8+**
- **Flask**
- **PostgreSQL**
- **Postman** (for testing the API)

---

## 🛠 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/daily_expenses_app.git
   cd daily_expenses_app
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the project root with the following content:

   ```bash
   FLASK_ENV=development
   DATABASE_URI=postgresql://username:password@localhost/convin
   SECRET_KEY=your_secret_key
   ```

   - **DATABASE_URI**: Replace with your PostgreSQL database credentials.
   - **convin** is the database name.

---

Here’s the updated **Database Setup** section with the addition of the `flask db migrate` command.

---

## 🛠️ Database Setup

1. **Create PostgreSQL Database:**

   Open your PostgreSQL shell and create the database:

   ```sql
   CREATE DATABASE convin;
   ```

2. **Initialize migrations:**

   Run the following command to initialize database migrations:

   ```bash
   flask db init
   ```

3. **Generate migration script:**

   After setting up your models, create a migration script:

   ```bash
   flask db migrate
   ```

4. **Apply migrations:**

   Run the following command to apply the migration and set up your database schema:

   ```bash
   flask db upgrade
   ```

---

This guide now covers the entire migration process for setting up the database using **PostgreSQL**. Let me know if you'd like further adjustments!

## 🚀 Running the Application

1. **Run the Flask application:**

   ```bash
   flask run
   ```

   The app will be available at `http://127.0.0.1:5000/`.

---

## 🔗 API Endpoints

Here's the updated **API Endpoints** section in your `README.md`, incorporating both **User** and **Expense** APIs.

---

## 🔗 API Endpoints

### 🧑‍💻 User Endpoints

| Endpoint                  | Method | Description            | Request Body                                              |
|---------------------------|--------|------------------------|------------------------------------------------------------|
| `/user`                   | POST   | Register a new user     | `{ "name": "Test User", "email": "test@example.com", "password": "1234", "mobile": "9876543211" }` |
| `/user/<int:user_id>`      | GET    | Retrieve a user by ID   | N/A                                                        |

### 💸 Expense Endpoints

| Endpoint                             | Method | Description                    | Request Body                                              |
|--------------------------------------|--------|--------------------------------|------------------------------------------------------------|
| `/expense`                           | POST   | Add a new expense               | `{ "amount": 500, "split_method": "equal", "user_id": 1, "participants": [2, 3] }` |
| `/expenses/<int:user_id>`            | GET    | Retrieve expenses for a user    | N/A                                                        |
| `/balance_sheet/<int:user_id>`       | GET    | Download user's balance sheet   | N/A                                                        |

---

                                                    |

---

## 🔄 Testing the API with Postman

1. **User Registration**

   Open **Postman**, and make a `POST` request to register a new user:

   ```http
   POST /user
   Content-Type: application/json

   {
    "email": "Vishu1@example.com",
    "name": "Test User122",
    "mobile": "9112078572"
   }

   ```

2. **Create an Expense**

   Send a `POST` request to create a new expense:

   ```http
   POST /expense
   Content-Type: application/json

   {
    "amount": 300.0,
    "split_method": "exact",
    "user_id": 11,
    "participants": [2, 3, 6],
    "exact_splits": {
        "user2": 100.0,
        "user3": 150.0,
        "user6": 50.0
    },
    "percentage_splits": {
        "user2": 33,
        "user3": 50,
        "user6": 17
    },
    "description": "Team building event expenses"
}

   ```

3. **Get User Details**

   Send a `GET` request to fetch a user's details:

   ```http
   GET /user/1
   ```

4. **Get User Expenses**

   Send a `GET` request to retrieve the user's expenses:

   ```http
   GET /user/1/expenses
   ```

---

## 🤝 Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

### 📌 Notes

- The app currently supports PostgreSQL as the database.
- Authentication and Authorization features will be implemented in future updates.

---

