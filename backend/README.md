# 📘 Project API Documentation

Welcome to the internal API documentation for our backend project. This API is built using **Laravel PHP** and **MySQL**, providing essential services for user authentication, wallet management, and subscription purchases.

![Laravel Logo](https://laravel.com/img/logomark.min.svg)

## ⚙️ Tech Stack

### Backend Framework
- **Laravel**: A PHP framework that enables efficient development with expressive syntax and a strong ecosystem.
- **Database**: MySQL, used for secure data storage and efficient querying.
- **ORM**: Eloquent ORM, providing a fluent interface for database operations.

### Core Libraries
- **Laravel Passport**: Provides secure OAuth2-based token authentication for managing API access.
- **Laravel Wallet**: Manages user wallet functionality, enabling balance tracking and transaction handling.
- **Validation & Middleware**: Laravel’s native validation and middleware ensure secure, reliable request handling.

---

## Key Functionalities

1. **User Authentication & Authorization**  
   - Handles user registration, login, and token management using **Laravel Passport**.
   
2. **Profile Management**  
   - Allows users to view and manage their profile data.
   
3. **Wallet Operations**  
   - Provides endpoints for checking wallet balances, depositing funds, and managing transactions.

4. **Subscription Plan Management**  
   - Users can view and purchase available plans, utilizing funds from their wallet.

5. **Error Handling**  
   - Comprehensive validation and error responses for smooth troubleshooting and secure operation.

---

## Postman Documentation

For easy testing and integration within the organization, here is the link to the **Postman Collection** with pre-configured endpoints:

🔗 **[Postman Collection - Internal Use Only](https://www.postman.com/your-internal-link-here)**

Import the collection into Postman and set up the environment variables as required for secure testing.

---

## Security and Access

Since this is a private API, security is a top priority. **Laravel Passport** provides token-based authentication, while role-based middleware ensures restricted access to sensitive endpoints. All data transfers are encrypted via HTTPS, and session management is carefully monitored.

---

For further details on each endpoint, refer to the sections below.

# API Documentation

This document outlines the available API endpoints for your Laravel PHP & MySQL project, with detailed descriptions for each endpoint.

### Base URL

All endpoints are prefixed with `/api/v1/`.

---

## Authentication Endpoints

### 1. Login

- **URL**: `/api/v1/login`
- **Method**: `POST`
- **Description**: Authenticates a user and returns a token for subsequent requests.
  
#### Request Parameters

| Parameter | Type   | Description            |
|-----------|--------|------------------------|
| `email`   | string | User's email address   |
| `password`| string | User's password        |

#### Example Request

```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

#### Success Response

- **Status**: `200 OK`

```json
{
  "success": true,
  "token": "your-access-token",
  "user": {
    "id": 1,
    "name": "John Doe",
    "email": "user@example.com"
  }
}
```

#### Error Response

- **Status**: `401 Unauthorized`

```json
{
  "success": false,
  "message": "Invalid credentials"
}
```

---

### 2. Register

- **URL**: `/api/v1/register`
- **Method**: `POST`
- **Description**: Registers a new user and returns authentication details.

#### Request Parameters

| Parameter      | Type   | Description           |
|----------------|--------|-----------------------|
| `name`         | string | User's full name      |
| `email`        | string | User's email address  |
| `password`     | string | User's password       |
| `password_confirmation` | string | Must match `password` |

#### Example Request

```json
{
  "name": "Jane Doe",
  "email": "jane@example.com",
  "password": "password123",
  "password_confirmation": "password123"
}
```

#### Success Response

- **Status**: `201 Created`

```json
{
  "success": true,
  "token": "your-access-token",
  "user": {
    "id": 2,
    "name": "Jane Doe",
    "email": "jane@example.com"
  }
}
```

#### Error Response

- **Status**: `422 Unprocessable Entity`

```json
{
  "success": false,
  "message": "Validation errors",
  "errors": {
    "email": ["The email has already been taken."]
  }
}
```

---

### 3. Refresh Token

- **URL**: `/api/v1/refresh`
- **Method**: `POST`
- **Description**: Refreshes the access token and returns a new one.

#### Success Response

- **Status**: `200 OK`

```json
{
  "success": true,
  "token": "new-access-token"
}
```

---

### 4. Logout

- **URL**: `/api/v1/logout`
- **Method**: `POST`
- **Description**: Logs out the user, invalidating the token.

#### Success Response

- **Status**: `200 OK`

```json
{
  "success": true,
  "message": "Logged out successfully"
}
```

---

## User Endpoints

### 5. Get User Details

- **URL**: `/api/v1/user`
- **Method**: `GET`
- **Description**: Returns the authenticated user's profile details.
- **Headers**: `Authorization: Bearer <token>`

#### Success Response

- **Status**: `200 OK`

```json
{
  "success": true,
  "user": {
    "id": 1,
    "name": "John Doe",
    "email": "user@example.com",
    "created_at": "2023-01-01T12:00:00Z"
  }
}
```

---

## Wallet Endpoints

### 6. View Wallet Balance

- **URL**: `/api/v1/wallet`
- **Method**: `GET`
- **Description**: Returns the current balance of the user's wallet.
- **Headers**: `Authorization: Bearer <token>`

#### Success Response

- **Status**: `200 OK`

```json
{
  "success": true,
  "balance": 150.00
}
```

---

### 7. Deposit into Wallet

- **URL**: `/api/v1/wallet/deposit`
- **Method**: `POST`
- **Description**: Allows the user to deposit a specified amount into their wallet.
  
#### Request Parameters

| Parameter | Type    | Description          |
|-----------|---------|----------------------|
| `amount`  | decimal | Amount to deposit    |

#### Example Request

```json
{
  "amount": 50.00
}
```

#### Success Response

- **Status**: `200 OK`

```json
{
  "success": true,
  "balance": 200.00,
  "message": "Deposit successful"
}
```

#### Error Response

- **Status**: `400 Bad Request`

```json
{
  "success": false,
  "message": "Invalid deposit amount"
}
```

---

## Plans Endpoints

### 8. List Available Plans

- **URL**: `/api/v1/plans`
- **Method**: `GET`
- **Description**: Retrieves a list of available plans.

#### Success Response

- **Status**: `200 OK`

```json
{
  "success": true,
  "plans": [
    {
      "id": 1,
      "name": "Basic Plan",
      "price": 100.00,
      "description": "Access to basic features"
    },
    {
      "id": 2,
      "name": "Premium Plan",
      "price": 200.00,
      "description": "Access to premium features"
    }
  ]
}
```

---

### 9. Purchase a Plan

- **URL**: `/api/v1/plans/{plan_id}/purchase`
- **Method**: `POST`
- **Description**: Purchases a specific plan for the user.

#### URL Parameters

| Parameter | Type    | Description            |
|-----------|---------|------------------------|
| `plan_id` | integer | ID of the plan to purchase |

#### Success Response

- **Status**: `200 OK`

```json
{
  "success": true,
  "message": "Plan purchased successfully",
  "plan": {
    "id": 1,
    "name": "Basic Plan",
    "price": 100.00
  }
}
```

#### Error Response

- **Status**: `400 Bad Request`

```json
{
  "success": false,
  "message": "Insufficient wallet balance"
}
```

---

## Error Handling

All API responses include a `success` boolean to indicate if the request was successful. In case of errors, the API will return a relevant HTTP status code and an error message to help with troubleshooting.

| Status Code | Description                       |
|-------------|-----------------------------------|
| 200         | Request was successful            |
| 201         | Resource was created successfully |
| 400         | Bad request, invalid parameters   |
| 401         | Unauthorized, invalid credentials |
| 422         | Validation error                  |

--- 
