# IT Support API

Backend REST API for an IT Help Desk system built with FastAPI and PostgreSQL.

The project is designed to manage support tickets, comments, users, and role-based workflows commonly found in internal IT support environments.

## Features

### Ticket Management

* Create support tickets
* Retrieve all tickets
* Retrieve a ticket by ID
* Update ticket status, priority, assignment, and category
* Track ticket ownership and lifecycle

### Comments System

* Add comments to a ticket
* Retrieve all comments associated with a ticket
* Preserve the original ticket description as part of the conversation history

### User Management

* User registration
* Password hashing with bcrypt
* User authentication via login
* Default role assignment (`user`)
* Support for multiple roles:

  * user
  * tech
  * admin

### Data Validation

* Request validation using Pydantic schemas
* UUID validation
* Enum validation for ticket priority values
* Optional fields handled safely during updates

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
```

### Comments

```http
GET    /tickets/{ticket_id}/comments
POST   /tickets/{ticket_id}/comments
```

## Future Improvements

* JWT authentication
* Role-based authorization
* Ticket history auditing
* Advanced filtering and pagination
* User profile management
* Automated tests
* Docker support
* API documentation improvements

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
