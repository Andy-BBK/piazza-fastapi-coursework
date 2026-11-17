Piazza API: Advanced Cloud Computing Coursework

Project goal 

Piazza is a discussion platform where registered users publish posts by topic, react and comment. Expired posts remain readable but accept no further interactions.

The main technologies used are:

Python and FastAPI to create the API.
Pydantic for validation of user input.
SQLAlchemy to create and work with databases and SQLite for data storage of user information.
JWT bearer authentication for user authentication.
pytest and FastAPI TestClient.
Docker and Docker Hub.
Google Cloud and Kubernetes.

Requirements

- Python 3.10 or later
- pip
- Python editor, VS Code was used for this project

Installation

Create a virtual environment:

python -m venv .venv

Activate it on Windows PowerShell:

.venv\Scripts\Activate.ps1

Or on macOS/Linux:

source .venv/bin/activate

Install the dependencies:

python -m pip install -r requirements.txt

Before starting the app a JWT_SECRET variable is needed for signing authenitcation tokens:

Generate a secret using:

python -c "import secrets; print(secrets.token_hex(32))"

Copy the result into an environment variable in the terminal where you run Uvicorn.

On macOS/Linux:

export JWT_SECRET="paste-your-generated-value-here"

On Windows PowerShell:

$env:JWT_SECRET = "paste-your-generated-value-here"

Start the application:

uvicorn main:app --reload

Testing

Open the API documentation at:

http://127.0.0.1:8000/docs

The page above will allow you to test application features manually, pytest automated tests will be included in the future.

API endpoints

GET/ - welcome message
GET/health - status of Piazza working
POST/auth/register - register a user
POST/auth/login - login and get JWT token
GET/profile/me - retrieve authenticated user details
POST/posts - create a simple post for an authenticated user

