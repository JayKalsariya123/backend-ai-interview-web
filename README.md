# Comprehensive Complaint Redressal System

A robust backend system for automating grievance logging, ensuring transparency, and providing real-time tracking of complaints.

## Features

- **Multi-Channel Complaint Registration**
  - Web Portal
  - WhatsApp Bot
  - QR Code (Pre-filled Form)
  - Helpdesk

- **Real-time Notifications**
  - SMS alerts via Twilio
  - WhatsApp messages
  - Email notifications
  - In-app notifications

- **Automated Escalation**
  - Configurable escalation thresholds
  - Multi-level escalation hierarchy
  - Automatic assignment to higher authorities

- **Complaint Tracking & Reopening**
  - Real-time status updates
  - Detailed timeline view
  - Ability to reopen resolved complaints

- **Role-Based Access**
  - Citizen: Register, track, and reopen complaints
  - Officer: View, respond, and resolve assigned complaints
  - Admin (District Collector): Monitor escalations, analyze trends, and reassign cases

- **Dashboard & Analytics**
  - Real-time reports on complaint types
  - Resolution time analysis
  - Department-wise performance metrics
  - Python-based data analysis

- **Security & Performance Optimizations**
  - Rate-limiting
  - JWT authentication
  - Input validation
  - Async task queues

## Tech Stack

- **Backend**: Node.js + Express.js
- **Database**: MongoDB (NoSQL)
- **Authentication**: JWT (Secure role-based access)
- **Messaging**: Twilio (SMS), WhatsApp API
- **Task Queue**: BullMQ (Auto-escalation & notifications)
- **Data Analytics**: Python (pandas, Matplotlib)

## Installation

### Prerequisites

- Node.js (v14 or higher)
- MongoDB
- Redis (for BullMQ)
- Python 3.7+ (for analytics)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/complaint-redressal-system.git
   cd complaint-redressal-system
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

3. Install Python dependencies (for analytics):
   ```bash
   cd analytics
   pip install -r requirements.txt
   cd ..
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. Start the server:
   ```bash
   npm start
   ```

## API Endpoints

### Authentication

- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Login user
- `GET /api/auth/me` - Get current user profile
- `PUT /api/auth/me` - Update user profile
- `PUT /api/auth/change-password` - Change password
- `POST /api/auth/forgot-password` - Request password reset
- `PUT /api/auth/reset-password/:resetToken` - Reset password

### Complaints

- `POST /api/complaints` - Create a new complaint
- `GET /api/complaints` - Get all complaints (filtered by user role)
- `GET /api/complaints/:id` - Get complaint by ID
- `PUT /api/complaints/:id/status` - Update complaint status
- `PUT /api/complaints/:id/assign` - Assign complaint to officer
- `PUT /api/complaints/:id/escalate` - Escalate complaint
- `PUT /api/complaints/:id/reopen` - Reopen complaint
- `PUT /api/complaints/:id/feedback` - Add feedback to complaint
- `GET /api/complaints/track/:complaintId` - Track complaint by ID
- `GET /api/complaints/stats` - Get complaint statistics

### Notifications

- `GET /api/notifications` - Get user notifications
- `GET /api/notifications/unread-count` - Get unread notification count
- `GET /api/notifications/:id` - Get notification by ID
- `PUT /api/notifications/:id/read` - Mark notification as read
- `PUT /api/notifications/read-all` - Mark all notifications as read
- `DELETE /api/notifications/:id` - Delete notification
- `PUT /api/notifications/preferences` - Update notification preferences

### Dashboard

- `GET /api/dashboard/overview` - Get dashboard overview
- `GET /api/dashboard/trends` - Get complaint trends
- `GET /api/dashboard/department-performance` - Get department performance
- `GET /api/dashboard/officer-performance` - Get officer performance
- `GET /api/dashboard/advanced-analytics` - Get advanced analytics
- `GET /api/dashboard/category-distribution` - Get category distribution

### Webhooks

- `POST /api/webhooks/whatsapp` - WhatsApp webhook endpoint

## Project Structure

```
complaint-redressal-system/
├── analytics/                  # Python analytics scripts
│   ├── dashboard.py            # Dashboard API
│   ├── generate_insights.py    # Data analysis script
│   ├── report_generator.py     # PDF report generator
│   └── requirements.txt        # Python dependencies
├── config/                     # Configuration files
│   ├── bull.js                 # BullMQ configuration
│   ├── constants.js            # System constants
│   └── db.js                   # Database configuration
├── controllers/                # API controllers
│   ├── authController.js       # Authentication controller
│   ├── complaintController.js  # Complaint controller
│   ├── dashboardController.js  # Dashboard controller
│   ├── notificationController.js # Notification controller
│   └── whatsappController.js   # WhatsApp integration
├── middleware/                 # Express middleware
│   ├── auth.js                 # Authentication middleware
│   ├── errorHandler.js         # Error handling middleware
│   ├── rateLimiter.js          # Rate limiting middleware
│   ├── roleCheck.js            # Role-based access control
│   └── validator.js            # Input validation
├── models/                     # MongoDB models
│   ├── ActivityLog.js          # Activity log model
│   ├── Complaint.js            # Complaint model
│   ├── Department.js           # Department model
│   ├── Notification.js         # Notification model
│   └── User.js                 # User model
├── queues/                     # BullMQ queues
│   ├── escalationQueue.js      # Escalation queue
│   ├── notificationQueue.js    # Notification queue
│   └── processors/             # Queue processors
│       ├── escalationProcessor.js # Escalation processor
│       └── notificationProcessor.js # Notification processor
├── routes/                     # API routes
│   ├── authRoutes.js           # Authentication routes
│   ├── complaintRoutes.js      # Complaint routes
│   ├── dashboardRoutes.js      # Dashboard routes
│   ├── notificationRoutes.js   # Notification routes
│   └── webhookRoutes.js        # Webhook routes
├── scripts/                    # Utility scripts
│   └── run-analytics.js        # Script to run analytics
├── services/                   # Service layer
│   ├── emailService.js         # Email service
│   ├── smsService.js           # SMS service
│   └── whatsappService.js      # WhatsApp service
├── utils/                      # Utility functions
│   ├── generators.js           # ID and token generators
│   ├── helpers.js              # Helper functions
│   ├── logger.js               # Logging utility
│   ├── responseFormatter.js    # API response formatter
│   └── validationSchemas.js    # Validation schemas
├── .env.example                # Example environment variables
├── .gitignore                  # Git ignore file
├── app.js                      # Express app setup
├── package.json                # Node.js dependencies
├── README.md                   # Project documentation
└── server.js                   # Server entry point
```

## Scheduled Jobs

- **Escalation Check**: Runs every hour to check for complaints that need escalation
- **Reminder Notifications**: Runs every 2 hours to send reminders for approaching deadlines
- **Analytics Generation**: Runs daily to generate fresh insights and reports

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- SSIP Gujarat for the opportunity to develop this solution
- All contributors who participated in this project
