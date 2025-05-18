# NOTIFICATION-SERVICE
A robust and modular notification system built using **Flask** and **Node.js**, enabling the delivery of notifications via Email, SMS, and In-App methods. The service uses  a React-based user interface.


## 🔧 Features

- Send notifications through:
  - Email (via SMTP)
  - SMS (via Twilio)
  - In-App (file-based or database)
-  Retrieve user-specific notifications
-  Automatic retry mechanism for failed deliveries
-  API documentation via Swagger UI



## 🛠️ Technology Stack

- **Flask (Python):** Core API for notifications
- **Node.js (Express):** Auxiliary services & retry logic
- **React.js:** Frontend dashboard
- **Twilio:** SMS delivery service
- **Google SMTP:** Email dispatch
- **dotenv:** Environment variable management



## 📋 Prerequisites

-Python installed on the system
-PostgreSQL set up and running on the system
-Git for version control



## 🚀 Getting Started

### 1️⃣ Clone the Repository


`git clone https://github.com/ManasRaj15/Notification-Service
cd Notification-Service`


### 2️⃣ Set Up Python Environment


`python -m venv venv
venv\Scripts\activate`


###  3️⃣ Install Python Dependencies


`pip install -r requirements.txt`


### Database Setup

Start PostgreSQL service and create a database named notificationdb


`psql -U postgres`

`postgres=# CREATE DATABASE notificationdb;
CREATE DATABASE`

`postgres=# CREATE USER <username> WITH PASSWORD '<password>';
CREATE ROLE`

`postgres=# GRANT ALL PRIVILEGES ON DATABASE notificationdb TO <username>;
GRANT`


### 🔐 Environment Variables

Create a .env file in the project root and configure:


`DATABASE_URL=postgresql+asyncpg://<username>:<password>@localhost:5432/notificationdb`

✉️ Email Configuration

`EMAIL_FROM=<your-email>@gmail.com
EMAIL_USERNAME=<your-email>@gmail.com
EMAIL_PASSWORD=16 digit Google App Password
EMAIL_HOST=smtp.gmail.com  
EMAIL_PORT=587`


📱 Twilio SMS Configuration

`TWILIO_ACCOUNT_SID=<From Twilio Account Dashboard>
TWILIO_AUTH_TOKEN=<From Twilio Account Dashboard>
TWILIO_PHONE_NUMBER=+123456789`

###  Ensure environment variables are correctly set to prevent runtime errors.


### Run Locally

Open command prompt in the project directory and run the following command to start the API

 `uvicorn app.main:app --reload`

 By default it will run on http://127.0.0.1:8000


### Run the API

Send Notification
POST /notifications

Example :

`{
  "user_id": 1,
  "type": "email",
  "email": "<receiver email>",
  "message": "Notification"
}`

`{
  "user_id": 2,
  "type": "sms",
  "phone": "<receiver phone number>",
  "message": "Notification"
}`

Get Notifications
GET /users/{user_id}/notifications

Example Response:

`[
  {
    "user_id": 1,
    "type": "email",
    "message": "Test Message",
    "status": "sent",
    "created_at": "2025-05-18T14:00:00Z",
    "id": "507f191e810c19729de860ea"
  }
]`


### 🧪 API Documentation

Access the Swagger UI at: http://127.0.0.1:5000/docs
Use it to explore, test, and validate API endpoints.


### 🛠 Troubleshooting

| Problem                      | Suggested Fix                                          |
| ---------------------------- | ------------------------------------------------------ |
| DATABASE_URL/Connection error| Check .env file & restart PostgreSQL service        |
| Email/SMS not sent           | Check SMTP and Twilio credentials in `.env`            |
| Frontend not displaying data | Confirm backend servers are active and CORS is enabled |
| React build fails            | Reinstall `node_modules` or clear cache                |

