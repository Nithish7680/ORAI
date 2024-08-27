import os

def run_app():
    # Set the environment variables for Flask
    os.environ.setdefault('FLASK_APP', 'app')
    os.environ.setdefault('FLASK_ENV', 'development')  # Set to 'production' for production

    # Import the Flask app after setting environment variables
    from app import app

    # Run the Flask application
    app.run(host="0.0.0.0", port=8000, debug=True)

if __name__ == "__main__":
    run_app()
