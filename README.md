# devops-labs

## Project: Flask CI/CD Demo

### Overview
A simple project to practice Flask + Docker + CI/CD.

- Docker containers successfully built and tested via GitHub Actions CI/CD
- Python 3.10 + Flask 2.3.3 + Pytest 7.4.0

### app.py
A simple Flask app to demonstrate build and deployment workflows.

By default, the app runs on 127.0.0.1 (localhost).
To allow LAN access, change host to 0.0.0.0 in app.run():
    app.run(host="0.0.0.0", port=5000)

### Dockerfile
Defines how to use Docker to build an image for the web app.

### flask_ci_cd.yaml
Defines the CI workflow for testing the app and building its Docker image.


