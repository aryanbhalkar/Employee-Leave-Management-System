# ☁️ Employee Leave Management System

A fully serverless **Employee Leave Management System** built on AWS using event-driven architecture. The application allows employees to submit leave requests, upload supporting documents, receive real-time notifications, and track leave status while enabling managers to approve or reject requests through secure REST APIs.

---

## 📌 Project Overview

This project demonstrates how to build a scalable and serverless application using core AWS services. It eliminates server management by leveraging AWS Lambda and integrates multiple AWS services to provide a secure and reliable leave management workflow.

---

## 🏗️ Architecture

![Architecture](architecture/architecture-diagram.png)

---

## 🚀 Features

- Apply for leave using REST API
- Upload supporting documents to Amazon S3
- Store leave requests in Amazon DynamoDB
- Approve or reject leave requests
- Check leave status
- Real-time email notifications using Amazon SNS
- Serverless architecture
- Centralized logging and monitoring with Amazon CloudWatch
- IAM-based secure permissions

---

# ⚙️ AWS Services Used

| Service | Purpose |
|----------|---------|
| AWS Lambda | Executes application logic |
| Amazon API Gateway | Exposes REST APIs |
| Amazon DynamoDB | Stores leave request data |
| Amazon S3 | Stores leave documents |
| Amazon SNS | Sends email notifications |
| Amazon CloudWatch | Logs and monitoring |
| AWS IAM | Access control and permissions |

---

# 📂 Project Structure

```text
employee-leave-management-system/
│
├── README.md
├── architecture/
│     architecture-diagram.png
│
├── lambda/
│     lambda_function.py
│
├── api/
│     api-endpoints.md
│
├── postman/
│     EmployeeLeaveAPI.postman_collection.json
│
├── screenshots/
│
├── docs/
│     deployment-guide.md
│
└── LICENSE
```

---

# 🔄 Project Workflow

```text
Employee
     │
     ▼
Amazon API Gateway
     │
     ▼
AWS Lambda
     │
     ├────────► Amazon DynamoDB
     │
     ├────────► Amazon S3
     │
     ├────────► Amazon SNS
     │
     ▼
Amazon CloudWatch

Manager

     │
Approve / Reject Leave

     ▼

AWS Lambda

     ▼

DynamoDB Status Updated

     ▼

SNS Email Notification
```

---

# 📡 REST API Endpoints

## Apply Leave

```http
POST /leave/apply
```

## Check Leave Status

```http
GET /leave/status?leaveId={leaveId}
```

## Update Leave Status

```http
PUT /leave/update
```

---

# 🧾 Sample Request

```json
{
    "employeeName":"Aryan Bhalkar",
    "employeeEmail":"aryan@example.com",
    "leaveType":"Sick Leave",
    "startDate":"2026-07-01",
    "endDate":"2026-07-03",
    "reason":"High Fever"
}
```

---

# ✅ Sample Response

```json
{
    "message":"Leave request submitted successfully",
    "leaveId":"7ef3c7d2",
    "status":"PENDING"
}
```

---

# 📸 Project Screenshots

## Architecture

![Architecture](screenshots/architecture.png)

---

## AWS Lambda

![Lambda](screenshots/lambda-overview.png)

---

## API Gateway

![API Gateway](screenshots/api-gateway.png)

---

## DynamoDB

![DynamoDB](screenshots/dynamodb.png)

---

## Amazon S3

![S3](screenshots/s3-bucket.png)

---

## Amazon SNS

![SNS](screenshots/sns-topic.png)

---

## CloudWatch Logs

![CloudWatch](screenshots/cloudwatch.png)

---

## Successful API Response

![Postman](screenshots/postman-apply.png)

---

# 📊 Data Stored in DynamoDB

| Attribute |
|-----------|
| leaveId |
| employeeName |
| employeeEmail |
| leaveType |
| startDate |
| endDate |
| reason |
| status |
| documentUrl |
| createdAt |

---

# 📈 Key Learning Outcomes

- Serverless Application Development
- REST API Design
- Event-Driven Architecture
- AWS IAM Permissions
- DynamoDB CRUD Operations
- Amazon S3 Object Storage
- SNS Email Notifications
- CloudWatch Monitoring & Logging
- AWS Service Integration
- API Testing using Postman

---

# 🔮 Future Improvements

- Amazon Cognito Authentication
- Frontend hosted on Amazon S3
- Manager Dashboard
- Leave History Dashboard
- Pre-signed S3 Upload URLs
- AWS Step Functions Approval Workflow
- CI/CD using GitHub Actions
- Infrastructure as Code using AWS CloudFormation or Terraform

---

# 📖 Deployment Guide

Complete deployment steps are available here:

```
docs/deployment-guide.md
```

---

# 📬 Postman Collection

Import the Postman collection from:

```
postman/EmployeeLeaveAPI.postman_collection.json
```

---

# 👨‍💻 Author

**Aryan Bhalkar**

Aspiring Cloud & FinOps Engineer

AWS | Azure | Cloud Infrastructure | Serverless Computing

LinkedIn:
www.linkedin.com/in/aryan-bhalkar-37162524a

---

## ⭐ If you found this project useful, consider giving it a Star.
