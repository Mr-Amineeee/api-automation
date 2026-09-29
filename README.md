# API Automation Testing

## Description

This project is an API automation testing framework built with Python, Requests, and Pytest. It tests REST API endpoints and validates their responses.

## Technologies

* Python
* Requests
* Pytest

## Installation & Run

### Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Run Tests

Run all tests with:

```bash
pytest -v
```

## Project Structure

```text
api_automation/
├── api_client.py
├── config.py
├── conftest.py
├── utils.py
├── requirements.txt
├── README.md
└── tests/
    ├── test_users.py
    └── test_posts.py
```

## Tests Covered

* Users API
* Posts API
* GET requests
* POST requests
* PUT requests
* DELETE requests
* Positive test cases
* Negative test cases

## Test Results

The project currently contains 9 automated tests, all passing successfully.
