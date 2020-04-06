# Course Text Updates

A Django web application for notifying you when your class opens up for VCCCD community colleges.

## Setup
These setup instructions are intended for MacOS.


```bash
# Create a virtual environment
virtualenv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Migrate database
python manage.py migrate

# Start the server
python manage.py runserver
```

The app should now be viewable in a browser window at `http://localhost:8000/courses/`.