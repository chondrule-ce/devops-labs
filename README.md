# devops-labs

## Project: Flask CI/CD Demo

### Overview
A simple project to practice Flask + Docker + CI/CD.

- Built and ran Docker containers on AMD64 architecture Windows system
- Python 3.10 + Flask 2.3.3 + Pytest 7.4.0

### app.py
By default, the app runs on 127.0.0.1 (localhost).
To allow LAN access, change host to 0.0.0.0 in app.run():
    app.run(host="0.0.0.0", port=5000)
