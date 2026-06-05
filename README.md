# IT Support API

Backend REST API for an IT Help Desk system built with FastAPI and PostgreSQL.

The project is designed to manage support tickets, comments, users, and role-based workflows commonly found in internal IT support environments.

## Features

### Authentication & Authorization

- User registration (default role assignment `user`)
- User login with JWT authentication
- Password hashing with bcrypt
- Role-based access control (RBAC) ???
- Protected routes

### User Management

* User registration
* Get all users (Admin only)
- Get user by ID (Admin only)
- Change user roles (Admin only)

### Ticket Management

* Create support tickets
* Get tickets with pagination
- Role-based ticket visibility
* Get ticket by ID
* Update ticket status, priority, assignment, and category
- Assign tickets to technicians
* Track ticket ownership and lifecycle

### Comments

* Add comments to a ticket
* Retrieve all comments associated with a ticket
* Preserve the original ticket description as part of the conversation history

### Ticket History

- Every ticket update is automatically recorded
- Tracked fields include: status, priority, assigned technician,category
- Each history record stores: cahnged field, previous and new value, user who performed the change, timestamp

### Data Validation

* Request validation using Pydantic schemas
* UUID validation
* Enum validation for ticket priority and status values
* Optional fields handled safely during updates

## Roles

### User

- Create tickets
- View own tickets
- View own ticket history
- Add comments to own tickets

### Tech

- View all tickets
- Update tickets
- Assign tickets to themselves
- View ticket history

### Admin

- Full access to tickets
- Assign tickets to any technician
- Manage users
- Change user roles

## Tech Stack

### Backend

* Python
* FastAPI

### Database

* PostgreSQL

### Authentication

* Passlib
* bcrypt

### Validation

* Pydantic

## API Documentation

Interactive API documentation is available through FastAPI Swagger UI:

http://localhost:8000/docs

## Project Structure

```text
app/
├── controllers/
├── queries/
├── routes/
├── schemas/
├── utils/
└── db/
```

### Architecture

The project follows a layered architecture:

```text
Routes
   ↓
Controllers
   ↓
Queries
   ↓
PostgreSQL
```

#### Routes

Handle HTTP requests and responses.

#### Controllers

Contain application logic and coordinate operations.

#### Queries

Execute SQL statements and interact with the database.

#### Schemas

Validate incoming request data using Pydantic.

#### Utils

Reusable helper functions such as password hashing and authentication utilities.

## Database Design

Main entities:

### Users

Stores application users and roles.

### Tickets

Stores support requests and their lifecycle.

### Comments

Stores ticket conversations and updates.

### Categories

Stores ticket classification categories.

### Ticket History

Reserved for future audit logging and change tracking.

## Current Endpoints

### Authentication

```http
POST /auth/register
POST /auth/login
```

### Tickets

```http
GET    /tickets
GET    /tickets/{id}
POST   /tickets
PUT    /tickets/{id}
GET    /tickets/{id}/history
```

### Comments

```http
GET    /tickets/{ticket_id}/comments
POST   /tickets/{ticket_id}/comments
```

### Users

```http
GET    /users
GET    /users/{id}
PATCH  /users/{user_id}/role
```

## Future Improvements

* User activation and deactivation
- Automated test with pytest
- Frontend application with React
- Dashboard and statistics
- Docker support


## Learning Goals

This project was created as a learning exercise to strengthen backend development skills using:

* FastAPI
* PostgreSQL
* SQL
* Authentication and security concepts
* REST API design
* Layered backend architecture
* Professional project organization

## Current Status

The project is in an early development stage.  
Initial backend structure and database configuration are being implemented.

```
```
