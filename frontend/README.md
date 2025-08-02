# Salary Prediction Frontend

This is the frontend application for the Employee Salary Prediction system. It provides a user interface for entering employee details and viewing salary predictions.

## Features

- React-based user interface
- Form for entering employee details
- Display of predicted salary
- Responsive design using Bootstrap

## Prerequisites

- Node.js 14+ and npm

## Installation

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install the required packages:
   ```
   npm install
   ```

## Running the Application

To start the development server, run:
```
npm start
```

The application will be available at http://localhost:3000.

## Building for Production

To create a production build, run:
```
npm run build
```

This will create a `build` directory with optimized production files.

## Using the Application

1. Enter the employee's years of experience
2. Select the education level from the dropdown
3. Select the job role from the dropdown
4. Select the industry from the dropdown
5. Click the "Predict Salary" button
6. View the predicted annual salary

## Features Description

- **Years of Experience**: The number of years the employee has worked in their field
- **Education Level**: The highest level of education completed by the employee
  - High School
  - Bachelor's Degree
  - Master's Degree
  - PhD
  - Professional Degree
- **Job Role**: The employee's position in the company
  - Junior
  - Mid-level
  - Senior
  - Lead
  - Manager
- **Industry**: The sector in which the employee works
  - Technology
  - Finance
  - Healthcare
  - Education
  - Other