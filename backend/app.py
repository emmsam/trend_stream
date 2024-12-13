from flask import Flask
from scheduler import start_scheduler
from init_db import init_db

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Trending Tracker!"

if __name__ == "__main__":
    init_db()  # Initialize the database
    start_scheduler()  # Start the scheduler
    app.run(debug=True)
