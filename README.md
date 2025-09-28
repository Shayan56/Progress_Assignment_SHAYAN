# 🛠️ DevSecOps CI/CD Pipeline Project

[![Python CI/CD DevSecOps](https://github.com/Shayan56/Progress_Assignment_SHAYAN/actions/workflows/ci.yml/badge.svg)](https://github.com/Shayan56/Progress_Assignment_SHAYAN/actions/workflows/ci.yml)

## 📌 Objective
Demonstrate DevSecOps principles by setting up an automated **CI/CD pipeline** for a simple web API or CLI app.  
The pipeline ensures code quality, runs tests, and performs static security analysis.

---

## ⚙️ Setup Steps

### 1. Application
- Type: Simple web API / CLI app (Python example)  
- Code location: `/app/`

### 2. CI/CD Pipeline
Configured using **GitHub Actions**.

#### Workflow Steps
1. **Linting**  
   Checks code formatting and style using `flake8` (Python) or `eslint` (JavaScript).

2. **Unit Tests**  
   Runs automated tests with `pytest` or equivalent testing framework.

3. **Static Code Analysis / Security Checks**  
   Tools used: `Bandit`, `CodeQL`, or `SonarCloud` to detect vulnerabilities and enforce coding standards.

#### GitHub Actions Workflow Example
```yaml
name: CI/CD Pipeline

on: [push, pull_request]

jobs:
  build-and-test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: 3.11
    - name: Install dependencies
      run: pip install -r requirements.txt
    - name: Lint code
      run: flake8 .
    - name: Run tests
      run: pytest
    - name: Security scan with Bandit
      run: bandit -r .
3. Badges

Build & CI Status:


🛠️ Challenges & Assumptions

Pipeline triggers on push and pull requests.

Dependency security warnings handled manually.

Limited test coverage for demo purposes.

🤖 Use of AI Tooling

ChatGPT assisted in:

Generating GitHub Actions workflow boilerplate

Suggesting security and static analysis tools

Writing README structure and workflow instructions

📌 Reflection

Learned to implement automated CI/CD pipelines with quality and security gates.

Gained experience integrating linting, testing, and static analysis.

Tricky part: configuring multiple tools in one workflow and fixing initial pipeline errors.

### 📌 Reflection

- Learned to implement automated **CI/CD pipelines** with quality and security gates.  
- Gained experience integrating **linting, testing, and static analysis**.  
- Tricky part: configuring multiple tools in one workflow and fixing initial pipeline errors.  
