BookShow Project Setup

This guide outlines how to set up your development environment for a this project.

Prerequisites:

Python (version 3.6 or later recommended) - https://www.python.org/downloads/
pip (package installer for Python) - Usually comes bundled with Python
Installation:

Python: If you don't have Python installed, download and install the latest version from the official website.

Virtual Environment (Recommended): It's highly recommended to create a virtual environment to isolate project dependencies. Refer to your operating system's documentation for creating virtual environments using venv or similar tools.

Activate Virtual Environment (if applicable): Activate your virtual environment using the appropriate command for your operating system.

pip: Verify pip installation by running pip --version in your terminal. If not installed, refer to Python documentation for installation instructions.

Dependencies:  Navigate to your project directory and install dependencies listed in your requirements.txt file using:

Bash
pip install -r requirements.txt
Use code with caution.
content_copy
Database Setup:

Migrations: Run the following commands to create database tables based on your Django models:

Bash
python manage.py makemigrations
python manage.py migrate
Use code with caution.
content_copy
Running the Development Server:

Start the development server to test your application locally:

Bash
python manage.py runserver
Use code with caution.
content_copy
This will typically start the server at http://127.0.0.1:8000/.

Additional Notes:

Create Django apps within your project directory for specific functionalities using python manage.py startapp myapp.
Refer to the official Django documentation for in-depth details and configuration: https://docs.djangoproject.com/en/5.0/
