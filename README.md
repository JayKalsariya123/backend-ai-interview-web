# Comprehensive Complaint Redressal System - Backend

A state-level student project developed for SSIP Gujarat Hackathon. This backend system provides a complete solution for complaint registration, tracking, escalation, and resolution.

## Features

- **Complaint Registration**: Citizens can file complaints via Web Form or WhatsApp chatbot
- **Complaint Tracking**: Real-time status updates via SMS/WhatsApp
- **Auto-Escalation**: Complaints are automatically escalated if unresolved within specified timeframes
- **Role-Based Access Control**: Different access levels for citizens, officers, and administrators
- **Analytics Dashboard API**: Generate and visualize complaint statistics

## Tech Stack

- **Backend**: Node.js + Express.js
- **Database**: MongoDB
- **Authentication**: JWT-based role management
- **Notifications**: Twilio (SMS) + WhatsApp API
- **Queue Management**: BullMQ (for complaint escalation)
- **Analytics**: Python script with pandas and Matplotlib

## Project Structure

```
├── config/             # Configuration files
├── controllers/        # Request handlers
├── middlewares/        # Custom middleware functions
├── models/             # Database models
├── routes/             # API routes
├── services/           # Business logic
├── utils/              # Utility functions
├── analytics/          # Python scripts for data analysis
├── .env                # Environment variables
├── package.json        # Project dependencies
└── server.js           # Entry point
```

## Setup Instructions

1. **Clone the repository**
   ```
   git clone <repository-url>
   cd complaint-redressal-system
   ```

2. **Install dependencies**
   ```
   npm install
   ```

3. **Configure environment variables**
   - Copy `.env.example` to `.env`
   - Update the variables with your credentials

4. **Start MongoDB**
   - Make sure MongoDB is running on your system

5. **Run the server**
   ```
   # Development mode
   npm run dev
   
   # Production mode
   npm start
   ```

6. **Setup Python analytics (optional)**
   ```
   cd analytics
   pip install -r requirements.txt
   ```

## API Documentation

### Authentication

#### Register a new user
- **URL**: `/api/auth/register`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "1234567890",
    "password": "password123",
    "role": "citizen"
  }
  ```
- **Response**:
  ```json
  {
    "success": true,
    "message": "User registered successfully",
    "data": {
      "user": {
        "_id": "user_id",
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "1234567890",
        "role": "citizen"
      },
      "token": "jwt_token"
    }
  }
  ```

#### Login
- **URL**: `/api/auth/login`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "email": "john@example.com",
    "password": "password123"
  }
  ```
- **Response**:
  ```json
  {
    "success": true,
    "message": "Login successful",
    "data": {
      "user": {
        "_id": "user_id",
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "1234567890",
        "role": "citizen"
      },
      "token": "jwt_token"
    }
  }
  ```

#### Change password
- **URL**: `/api/auth/change-password`
- **Method**: `PUT`
- **Headers**: `Authorization: Bearer jwt_token`
- **Request Body**:
  ```json
  {
    "currentPassword": "password123",
    "newPassword": "newpassword123"
  }
  ```
- **Response**:
  ```json
  {
    "success": true,
    "message": "Password updated successfully"
  }
  ```

### Complaints

#### Create a new complaint
- **URL**: `/api/complaints`
- **Method**: `POST`
- **Headers**: `Authorization: Bearer jwt_token`
- **Request Body**:
  ```json
  {
    "title": "Water supply issue",
    "description": "No water supply for the last 2 days",
    "category": "water",
    "priority": "high",
    "location": {
      "address": "123 Main St",
      "city": "Ahmedabad",
      "state": "Gujarat",
      "pincode": "380001"
    }
  }
  ```
- **Response**:
  ```json
  {
    "success": true,
    "message": "Complaint registered successfully",
    "data": {
      "_id": "complaint_id",
      "title": "Water supply issue",
      "description": "No water supply for the last 2 days",
      "category": "water",
      "priority": "high",
      "status": "pending",
      "location": {
        "address": "123 Main St",
        "city": "Ahmedabad",
        "state": "Gujarat",
        "pincode": "380001"
      },
      "citizen": "user_id",
      "assignedTo": "officer_id",
      "createdAt": "timestamp"
    }
  }
  ```

#### Fetch complaints
- **URL**: `/api/complaints`
- **Method**: `GET`
- **Headers**: `Authorization: Bearer jwt_token`
- **Response**:
  ```json
  {
    "success": true,
    "data": [
      {
        "_id": "complaint_id",
        "title": "Water supply issue",
        "status": "pending",
        "priority": "high",
        "createdAt": "timestamp"
      }
    ]
  }
  ```

