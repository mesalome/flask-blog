# Flask Project README

This is a simple Flask project that serves as a starting point for your web application. 
It includes instructions on how to set up and run the project.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3 installed
- pip3 installed
- A code editor (e.g., Visual Studio Code, Sublime Text)

## Getting Started

To get this project up and running, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone <repository_url>
   cd <project_directory>
   ```

2. Create a virtual environment to isolate project dependencies:

   ```bash
   python3 -m venv .venv
   ```

3. Activate the virtual environment:

   On macOS and Linux:
   ```bash
   source .venv/bin/activate
   ```

   On Windows (Command Prompt):
   ```bash
   .venv\Scripts\activate
   ```

4. Install Flask and other project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   ```pip freeze > requirements.txt```


## Running the Application

To start the Flask application, run the following commands:

```bash
export FLASK_ENV=development
export FLASK_APP=run.py
flask --app app run --debug
```

Your Flask application should now be running at `http://127.0.0.1:5000/`.

## Project Structure

- `app/`: Contains the Flask application code.
- `templates/`: Store your HTML templates here.
- `static/`: Store static files (e.g., CSS, JavaScript) here.
- `start.sh`: A shell script to set environment variables and start the development server.

