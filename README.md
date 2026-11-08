Piaza API: Advanced Cloud Computing Coursework

Project goal 

Piazza is a discussion platform where registered users publish posts by topic, react and comment. Expired posts remain readable but accept no further interactions.

The main technologies used are:

Python and FastAPI.
Pydantic for validation.
SQLAlchemy and SQLite for data storage.
JWT bearer authentication.
pytest and FastAPI TestClient.
Docker and Docker Hub.
Google Cloud and Kubernetes.

Requirements

- Python 3.10 or later
- Python editor, VS Code was used for this project

How to install dependencies

Create a virtual environment:

python -m venv .venv

Activate it on Windows PowerShell:

.venv\Scripts\Activate.ps1

Or on macOS/Linux:

source .venv/bin/activate

Install the dependencies:

python -m pip install -r requirements.txt

Start the application:

uvicorn main:app --reload

