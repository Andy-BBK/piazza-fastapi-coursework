Piazza coursework log

Date: 8th November 2026

Work done:

- I created my pizza-coursework folder on my mac and opened it in VS code.
- I set up a Python virtual environment (using .venv/bin/activate etc).
- I set up a requirements.txt file to add the FastAPI and Uvicorn dependecies.
- I created the main.py file to create a welcome and health endpoint and tested them locally.
- I added a .gitignore file, initial README and development log file.

Decisions 

Used the steps outlined in Week 1's lab to create the inital app and ensure that I was able to create virtual environments and make sure my installed packages were working. Also, to start of small and not focus on thing's like including the database too early.

Problems

I had problems when trying to use the pip module to install packages. Bug was caused by a missmatch of python interpreataion which I fixed by deactivating my venv.

Sources and assistance

- Week 1 advanced cloud computing 
- Week 3 and 4 advanced cloud computing
- Assignment briefing 

GitHub Commit

Message: Initial set up of Piazza endpoints, dependencies, README, development log and gitignore files.

Link: https://github.com/Andy-BBK/piazza-fastapi-coursework/commit/acb45a49bd22bfce5502c1dcbfca3b76acff9583

Day 2 of development

Date: 15th November 2026

User registration and login

Todaay I focused on setting up user registration and login for my Piazza API, using the process outlined in the week 4 lab as a guide. It felt like a natural next step for the project since it would introduce required depenendecies such as SQLalchemy (sqlite) and fit's perfectly with the purpose of Piazza which is centered around users.

Firstly, I created a SQLite database using SQLAlchemy and added the User model outlined in Week 4 to store usernames, emails and hashed passwords. I also introduced Pydantic schemas so I could validate user details when they registered or logged in.

Within a routers folder I added registration and login endpoints, making sure that users couldn't register with an already existing email address. Logging in used password hashing and JWT functions also outlined in week 4, so that users can log in and receive an access token.

I used a profile endpoint to test/practise using JWT authentications.

Tests completed:

- Registering a new user.
- Trying to register a new user with an already existing email.
- Logging in using correct and incorrect passwords.
- Accessing the profile endpoint with and without a valid token.
- Checking is user information was stored in my database.

All tests passed and returned the expected status codes, which I took screenshots off.

Decisions

I created a routers folder because it was outlined in wek4 but also because Week 1 states it's better to have one to keep my code clean and group related endpoints. 

Problems

I didn't encounter any problems today.


References 

- Week 1 advanced cloud computing
- Week 3 advanced cloud computing
- Week 4 advanced cloud computing
- Google AI for helping with Git commands and pushing coursework files to my online repository