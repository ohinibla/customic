### Customic Interview Task

This project provides a simple REST API for generating and managing t-shirt mockups.  
It includes endpoints for authentication, mockup generation, task status tracking, and listing all created mockups.  
The API is built with **Django** and **Django REST Framework**, and uses **Celery** and **Redis** for asynchronous task processing.

(.http file included — working demo available at [https://webapp.albiniho.com:8443](https://webapp.albiniho.com:8443))

## Prerequisites

- docker compose
- curl (for testing API requests)

## Installation

1. **Clone the repository**  

```bash
git clone https://github.com/ohinibla/customic.git
cd customic
```

2. **Run docker compose**
```bash
docker compose up
```

# API Usage 

## 1.Generate a mockup
Navigate to http://127.0.0.1:8000/api/token/

```bash
curl -s -X POST http://localhost:8000/api/token/ \
     -H "Content-Type: application/json" \
     -H "Accept: application/json" \
     -d '{"username": "admin", "password": "test"}'
```

## 2. Generate a mockup
Navigate to http://localhost:8000/api/v1/mockups/generate/

```bash
curl -s -X POST http://localhost:8000/api/v1/mockups/generate/ \
     -H "Content-Type: application/json" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN" \
     -d '{"text": "new_text"}'
```

##  3.Get status of the generated mockup
Navigate to http://localhost:8000/api/v1/tasks/$TASK_ID/

```bash
curl -s -X GET http://localhost:8000/api/v1/tasks/$TASK_ID/ \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```

## 4.List all mockups
Navigate to http://localhost:8000/api/v1/mockups/

```bash
curl -s -X GET http://localhost:8000/api/v1/mockups/ \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```

