# Salary Prediction Backend

This is the backend service for the Salary Prediction application. It provides an API for predicting employee salaries based on various factors.

## Features

- RESTful API built with Flask
- Machine learning model for salary prediction
- Cross-origin resource sharing (CORS) support

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Installation

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Server

To start the server, run:
```
python app.py
```

The server will start on http://localhost:5000.

## API Endpoints

### Health Check
- URL: `/api/health`
- Method: `GET`
- Response: `{"status": "healthy"}`

### Predict Salary
- URL: `/api/predict`
- Method: `POST`
- Request Body:
  ```json
  {
    "experience": 5,
    "education_level": 3,
    "role": 2,
    "industry": 1
  }
  ```
- Response:
  ```json
  {
    "predicted_salary": 85000.00,
    "status": "success"
  }
  ```

## Feature Descriptions

- `experience`: Years of work experience (float)
- `education_level`: Education level (integer)
  - 1: High School
  - 2: Bachelor's
  - 3: Master's
  - 4: PhD
  - 5: Professional
- `role`: Job role (integer)
  - 1: Junior
  - 2: Mid-level
  - 3: Senior
  - 4: Lead
  - 5: Manager
- `industry`: Industry sector (integer)
  - 1: Tech
  - 2: Finance
  - 3: Healthcare
  - 4: Education
  - 5: Other