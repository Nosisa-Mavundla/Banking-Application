# 🏦 Banking Application

A web-based banking application built with **Python, Flask, and SQLite**. Users can register for an account if they don't already have one, log in securely, access a personalized dashboard, and perform basic banking operations.

---

## 📌 Overview

The system provides users with a centralized interface for managing their bank account. Current focus areas:

- User registration & login
- Session management
- Protected dashboard access
- Banking operations (deposit, withdraw, transfer)
- Transaction history
- Store and manage user data using a relational database, applying CRUD and SQL concepts practically
- System analysis and design techniques applied throughout development

The project is being developed incrementally, following a structured **SDLC**, using an **Agile methodology** with iterative development cycles to progressively build and refine features.

---

## 🛠️ Technology Stack

| Technology     | Purpose                     |
| -------------- | --------------------------- |
| **Python**     | Backend programming         |
| **Flask**      | Web application framework   |
| **SQLite**     | Relational database         |
| **SQL**        | Queries and data management |
| **HTML/CSS**   | Structure and styling       |
| **Jinja2**     | Dynamic HTML templating     |
| **Git/GitHub** | Version control             |

---

## 💳 Core Features

**User Registration** — create an account with full name, email, and password.

**User Login** — authenticate with email and password; redirects to dashboard on success.

**Dashboard** — personalized view with navigation to: Deposit, Withdraw, Transfer, Transaction History, Logout.

**Deposit Funds** _(planned)_ — validates amount, updates balance, records transaction.

**Withdraw Funds** _(planned)_ — withdraws funds subject to sufficient balance.

**Transfer Funds** _(planned)_ — validates recipient, balance, and amount, then updates both accounts.

**Transaction History** _(planned)_ — view past deposits, withdrawals, and transfers.

---

## 🗄️ Database Design

**Users table:**

| Column      | Description             |
| ----------- | ----------------------- |
| `id`        | Unique user identifier  |
| `full_name` | User's full name        |
| `email`     | User's email address    |
| `password`  | User password           |
| `balance`   | Current account balance |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate into the project

```bash
cd banking-app
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

The application will then be available locally through the Flask development server.

---

## 👩🏽‍💻 Author

**Nosisa Mavundla**
BCom Information Systems & Technology

Built as part of my software development portfolio to strengthen skills in Python, Flask, databases, system analysis, and application development.
