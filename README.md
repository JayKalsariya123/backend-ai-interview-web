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
    "role": "citizen" // Optional, defaults to "citizen"
  }
  ```
  For officer registration (admin only):
  ```json
  {
    "name": "Officer Name",
    "email": "officer@example.com",
    "phone": "1234567890",
    "password": "password123",
    "role": "officer",
    "department": "Water Department",
    "designation": "Junior Officer",
    "region": "Ahmedabad"
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

#### Get current user profile
- **URL**: `/api/auth/me`
- **Method**: `GET`
- **Headers**: `Authorization: Bearer jwt_token`
- **Response**:
  ```json
  {
    "success": true,
    "data": {
      "_id": "user_id",
      "name": "John Doe",
      "email": "john@example.com",
      "phone": "1234567890",
      "role": "citizen"
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

#### Forgot password
- **URL**: `/api/auth/forgot-password`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "email": "john@example.com"
  }
  ```
- **Response**:
  ```json
  {
    "success": true,
    "message": "Password reset instructions sent to your email"
  }
  ```

### Complaints

#### Create a new complaint
- **URL**: `/api/complaints`
- **Method**: `POST`
- **Headers**: `Authorization: Bearer jwt_token`
- **Content-Type**: `multipart/form-data` (for file uploads)
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
    },
    "attachments": [file1, file2] // Optional
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
      "attachments": ["url1", "url2"],
      "citizen": "user_id",
      "assignedTo": "officer_id",
      "createdAt": "timestamp"
    }
  }
  ```

#### Get all complaints
- **URL**: `/api/complaints`
- **Method**: `GET`
- **Headers**: `Authorization: Bearer jwt_token`
- **Query Parameters**:
  - `page`: Page number (default: 1)
  - `limit`: Items per page (default: 10)
  - `status`: Filter by status (pending, in-progress, resolved, rejected, escalated)
  - `category`: Filter by category
  - `priority`: Filter by priority
  - `search`: Search in title and description
- **Response**:
  ```json
  {
    "success": true,
    "count": 10,
    "pagination": {
      "page": 1,
      "limit": 10,
      "total": 50,
      "pages": 5
    },
    "data": [
      {
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
        "citizen": {
          "_id": "user_id",
          "name": "John Doe"
        },
        "assignedTo": {
          "_id": "officer_id",
          "name": "Officer Name"
        },
        "createdAt": "timestamp"
      }
    ]
  }
  ```

#### Get complaint by ID
- **URL**: `/api/complaints/:id`
- **Method**: `GET`
- **Headers**: `Authorization: Bearer jwt_token`
- **Response**:
  ```json
  {
    "success": true,
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
      "attachments": ["url1", "url2"],
      "citizen": {
        "_id": "user_id",
        "name": "John Doe"
      },
      "assignedTo": {
        "_id": "officer_id",
        "name": "Officer Name"
      },
      "comments": [
        {
          "user": {
            "_id": "user_id",
            "name": "John Doe"
          },
          "text": "Any updates?",
          "date": "timestamp"
        }
      ],
      "statusHistory": [
        {
          "status": "pending",
          "updatedBy": {
            "_id": "user_id",
            "name": "John Doe"
          },
          "comment": "Complaint registered",
          "date": "timestamp"
        }
      ],
      "createdAt": "timestamp"
    }
  }
  ```

#### Update complaint status
- **URL**: `/api/complaints/:id/status`
- **Method**: `PUT`
- **Headers**: `Authorization: Bearer jwt_token`
- **Request Body**:
  ```json
  {
    "status": "in-progress",
    "comment": "Working on it"
  }
  ```
- **Response**:
  ```json
  {
    "success": true,
    "message": "Complaint status updated successfully",
    "data": {
      "_id": "complaint_id",
      "status": "in-progress",
      "statusHistory": [
        {
          "status": "pending",
          "updatedBy": "user_id",
          "comment": "Complaint registered",
          "date": "timestamp"
        },
        {
          "status": "in-progress",
          "updatedBy": "officer_id",
          "comment": "Working on it",
          "date": "timestamp"
        }
      ]
    }
  }
  ```

#### Add comment to complaint
- **URL**: `/api/complaints/:id/comments`
- **Method**: `POST`
- **Headers**: `Authorization: Bearer jwt_token`
- **Request Body**:
  ```json
  {
    "text": "Any updates?"
  }
  ```
- **Response**:
  ```json
  {
    "success": true,
    "message": "Comment added successfully",
    "data": {
      "user": {
        "_id": "user_id",
        "name": "John Doe"
      },
      "text": "Any updates?",
      "date": "timestamp"
    }
  }
  ```

#### Escalate complaint
- **URL**: `/api/complaints/:id/escalate`
- **Method**: `POST`
- **Headers**: `Authorization: Bearer jwt_token`
- **Request Body**:
  ```json
  {
    "reason": "Unable to resolve at my level",
    "to": "officer_id"
  }
  ```
- **Response**:
  ```json
  {
    "success": true,
    "message": "Complaint escalated successfully",
    "data": {
      "_id": "complaint_id",
      "status": "escalated",
      "escalationLevel": 1,
      "assignedTo": {
        "_id": "officer_id",
        "name": "Senior Officer"
      }
    }
  }
  ```

### Users

#### Get all users (Admin only)
- **URL**: `/api/users`
- **Method**: `GET`
- **Headers**: `Authorization: Bearer jwt_token`
- **Query Parameters**:
  - `page`: Page number (default: 1)
  - `limit`: Items per page (default: 10)
  - `role`: Filter by role
  - `department`: Filter by department
  - `region`: Filter by region
  - `search`: Search in name and email
- **Response**:
  ```json
  {
    "success": true,
    "count": 10,
    "pagination": {
      "page": 1,
      "limit": 10,
      "total": 50,
      "pages": 5
    },
    "data": [
      {
        "_id": "user_id",
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "1234567890",
        "role": "citizen",
        "createdAt": "timestamp"
      }
    ]
  }
  ```

#### Get officers
- **URL**: `/api/users/officers`
- **Method**: `GET`
- **Headers**: `Authorization: Bearer jwt_token`
- **Query Parameters**:
  - `department`: Filter by department
  - `region`: Filter by region
- **Response**:
  ```json
  {
    "success": true,
    "count": 5,
    "data": [
      {
        "_id": "user_id",
        "name": "Officer Name",
        "email": "officer@example.com",
        "phone": "1234567890",
        "department": "Water Department",
        "designation": "Junior Officer",
        "region": "Ahmedabad"
      }
    ]
  }
  ```

### Departments

#### Create a new department (Admin only)
- **URL**: `/api/departments`
- **Method**: `POST`
- **Headers**: `Authorization: Bearer jwt_token`
- **Request Body**:
  ```json
  {
    "name": "Water Department",
    "description": "Handles water supply issues",
    "categories": ["water"],
    "head": "user_id",
    "regions": ["Ahmedabad", "Gandhinagar"],
    "contactEmail": "water@example.com",
    "contactPhone": "1234567890"
  }
  ```
- **Response**:
  ```json
  {
    "success": true,
    "message": "Department created successfully",
    "data": {
      "_id": "department_id",
      "name": "Water Department",
      "description": "Handles water supply issues",
      "categories": ["water"],
      "head": "user_id",
      "regions": ["Ahmedabad", "Gandhinagar"],
      "contactEmail": "water@example.com",
      "contactPhone": "1234567890",
      "isActive": true,
      "createdAt": "timestamp"
    }
  }
  ```

#### Get all departments
- **URL**: `/api/departments`
- **Method**: `GET`
- **Headers**: `Authorization: Bearer jwt_token`
- **Query Parameters**:
  - `page`: Page number (default: 1)
  - `limit`: Items per page (default: 10)
  - `isActive`: Filter by active status
  - `category`: Filter by category
  - `search`: Search in name
- **Response**:
  ```json
  {
    "success": true,
    "count": 5,
    "pagination": {
      "page": 1,
      "limit": 10,
      "total": 5,
      "pages": 1
    },
    "data": [
      {
        "_id": "department_id",
        "name": "Water Department",
        "description": "Handles water supply issues",
        "categories": ["water"],
        "head": {
          "_id": "user_id",
          "name": "Head Officer"
        },
        "officers": [
          {
            "_id": "user_id",
            "name": "Officer Name"
          }
        ],
        "regions": ["Ahmedabad", "Gandhinagar"],
        "contactEmail": "water@example.com",
        "contactPhone": "1234567890",
        "isActive": true,
        "createdAt": "timestamp"
      }
    ]
  }
  ```

### Analytics

#### Get dashboard statistics (Admin only)
- **URL**: `/api/analytics/dashboard`
- **Method**: `GET`
- **Headers**: `Authorization: Bearer jwt_token`
- **Response**:
  ```json
  {
    "success": true,
    "data": {
      "counts": {
        "complaints": {
          "total": 100,
          "pending": 20,
          "inProgress": 30,
          "resolved": 40,
          "escalated": 10
        },
        "users": {
          "total": 50,
          "citizens": 40,
          "officers": 9,
          "admins": 1
        },
        "departments": 5
      },
      "avgResolutionTimeHours": 48.5,
      "complaintsByCategory": [
        {
          "_id": "water",
          "count": 30
        },
        {
          "_id": "electricity",
          "count": 25
        }
      ],
      "complaintsByPriority": [
        {
          "_id": "high",
          "count": 40
        },
        {
          "_id": "medium",
          "count": 35
        }
      ],
      "complaintsByStatus": [
        {
          "status": "pending",
          "count": 20
        },
        {
          "status": "in-progress",
          "count": 30
        }
      ],
      "recentComplaints": [
        {
          "_id": "complaint_id",
          "title": "Water supply issue",
          "status": "pending",
          "createdAt": "timestamp"
        }
      ]
    }
  }
  ```

#### Export complaint data for Python analytics (Admin only)
- **URL**: `/api/analytics/export`
- **Method**: `GET`
- **Headers**: `Authorization: Bearer jwt_token`
- **Response**:
  ```json
  {
    "success": true,
    "count": 100,
    "data": [
      {
        "category": "water",
        "priority": "high",
        "status": "resolved",
        "created_date": "2023-05-01",
        "resolved_date": "2023-05-03",
        "resolution_time_hours": 48,
        "city": "Ahmedabad",
        "state": "Gujarat",
        "escalation_level": 0
      }
    ]
  }
  ```

## Contributors

- SSIP Gujarat Hackathon Team

## License

This project is licensed under the ISC License. 
