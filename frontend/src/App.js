import React, { useState } from 'react';
import { Container, Row, Col, Form, Button, Card, Alert } from 'react-bootstrap';
import axios from 'axios';

function App() {
  // State for form inputs
  const [experience, setExperience] = useState('');
  const [educationLevel, setEducationLevel] = useState('1');
  const [role, setRole] = useState('1');
  const [industry, setIndustry] = useState('1');

  // State for prediction result
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      // Validate experience input
      if (isNaN(experience) || experience === '') {
        throw new Error('Experience must be a valid number');
      }

      // Prepare data for API request
      const data = {
        experience: parseFloat(experience),
        education_level: parseInt(educationLevel),
        role: parseInt(role),
        industry: parseInt(industry)
      };

      // Make API request to backend
      const response = await axios.post('http://127.0.0.1:5000/api/predict', data);

      // Check if response contains the expected data
      if (response.data && response.data.predicted_salary !== undefined) {
        // Update prediction state with result
        setPrediction(response.data.predicted_salary);
      } else {
        throw new Error('Invalid response from server');
      }
    } catch (err) {
      setError(err.message || 'An error occurred while making the prediction');
    } finally {
      setLoading(false);
    }
  };

  // Format salary as currency
  const formatSalary = (salary) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      minimumFractionDigits: 0,
      maximumFractionDigits: 0
    }).format(salary);
  };

  return (
    <Container className="py-5">
      <h1 className="app-title">Employee Salary Prediction</h1>

      <Row>
        <Col md={8} className="mx-auto">
          <Card className="mb-4">
            <Card.Header>Enter Employee Details</Card.Header>
            <Card.Body>
              <Form onSubmit={handleSubmit}>
                <Form.Group className="mb-3">
                  <Form.Label>Years of Experience</Form.Label>
                  <Form.Control 
                    type="number" 
                    step="0.1"
                    min="0"
                    placeholder="Enter years of experience" 
                    value={experience} 
                    onChange={(e) => setExperience(e.target.value)}
                    required
                  />
                  <Form.Text className="text-muted">
                    Enter the number of years of work experience
                  </Form.Text>
                </Form.Group>

                <Form.Group className="mb-3">
                  <Form.Label>Education Level</Form.Label>
                  <Form.Select 
                    value={educationLevel} 
                    onChange={(e) => setEducationLevel(e.target.value)}
                  >
                    <option value="1">High School</option>
                    <option value="2">Bachelor's Degree</option>
                    <option value="3">Master's Degree</option>
                    <option value="4">PhD</option>
                    <option value="5">Professional Degree</option>
                  </Form.Select>
                </Form.Group>

                <Form.Group className="mb-3">
                  <Form.Label>Job Role</Form.Label>
                  <Form.Select 
                    value={role} 
                    onChange={(e) => setRole(e.target.value)}
                  >
                    <option value="1">Junior</option>
                    <option value="2">Mid-level</option>
                    <option value="3">Senior</option>
                    <option value="4">Lead</option>
                    <option value="5">Manager</option>
                  </Form.Select>
                </Form.Group>

                <Form.Group className="mb-3">
                  <Form.Label>Industry</Form.Label>
                  <Form.Select 
                    value={industry} 
                    onChange={(e) => setIndustry(e.target.value)}
                  >
                    <option value="1">Technology</option>
                    <option value="2">Finance</option>
                    <option value="3">Healthcare</option>
                    <option value="4">Education</option>
                    <option value="5">Other</option>
                  </Form.Select>
                </Form.Group>

                <Button 
                  variant="primary" 
                  type="submit" 
                  className="w-100" 
                  disabled={loading}
                >
                  {loading ? 'Predicting...' : 'Predict Salary'}
                </Button>
              </Form>
            </Card.Body>
          </Card>

          {error && (
            <Alert variant="danger">
              {error}
            </Alert>
          )}

          {prediction !== null && !error && (
            <Card className="prediction-result">
              <Card.Body className="text-center">
                <h4>Predicted Annual Salary</h4>
                <div className="prediction-value">
                  {formatSalary(prediction)}
                </div>
                <p className="mt-3 text-muted">
                  This prediction is based on the provided employee details and historical salary data.
                </p>
              </Card.Body>
            </Card>
          )}
        </Col>
      </Row>
    </Container>
  );
}

export default App;
