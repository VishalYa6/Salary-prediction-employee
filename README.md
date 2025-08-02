# Employee Salary Prediction Application

A full-stack web application for predicting employee salaries based on various factors such as experience, education level, job role, and industry.

## Project Structure

The project consists of two main components:

- **Backend**: A Python Flask application that provides a RESTful API for salary prediction using a machine learning model.
- **Frontend**: A React.js application that provides a user interface for entering employee details and viewing salary predictions.

## Features

- Predict employee salaries based on:
  - Years of experience
  - Education level
  - Job role
  - Industry
- Interactive web interface
- RESTful API for integration with other systems

## Prerequisites

- Python 3.7+
- Node.js 14+ and npm
- pip (Python package installer)

## Installation and Setup

### Backend Setup

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

5. Start the backend server:
   ```
   python app.py
   ```

   The backend server will start on http://localhost:5000.

### Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install the required packages:
   ```
   npm install
   ```

3. Start the frontend development server:
   ```
   npm start
   ```

   The frontend application will be available at http://localhost:3000.

## Using the Application

1. Ensure both the backend and frontend servers are running.
2. Open your web browser and navigate to http://localhost:3000.
3. Enter the employee details in the form:
   - Years of experience
   - Education level
   - Job role
   - Industry
4. Click the "Predict Salary" button.
5. View the predicted annual salary.

## API Documentation

### Predict Salary

- **URL**: `/api/predict`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "experience": 5,
    "education_level": 3,
    "role": 2,
    "industry": 1
  }
  ```
- **Response**:
  ```json
  {
    "predicted_salary": 85000.00,
    "status": "success"
  }
  ```

### Health Check

- **URL**: `/api/health`
- **Method**: `GET`
- **Response**: `{"status": "healthy"}`

## Model Information

The salary prediction model is a linear regression model trained on sample data. It uses the following features:

- Years of experience (float)
- Education level (integer: 1-5)
- Job role (integer: 1-5)
- Industry (integer: 1-5)

In a production environment, this model would be trained on a larger dataset and potentially use more sophisticated algorithms.

## Future Improvements

- Add user authentication
- Implement more sophisticated machine learning models
- Add data visualization for salary trends
- Allow users to save and compare multiple predictions
- Expand the dataset for more accurate predictions