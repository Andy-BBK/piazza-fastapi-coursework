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

Today I focused on setting up user registration and login for my Piazza API, using the process outlined in the week 4 lab as a guide. It felt like a natural next step for the project since it would introduce required depenendecies such as SQLalchemy (sqlite) and fit's perfectly with the purpose of Piazza which is centered around users.

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

Github commit:

Message: Added user registration and JWT authentication

link: https://github.com/Andy-BBK/piazza-fastapi-coursework/commit/1891141aab136bb98c1f56b081c3bd9f8bc45942

Commit author timestamp: 2026-11-15T20:02:49Z

Day 3 of development

Basic post model

Today I created a basic post model using the course model from week 3 as a guide and included an ID, author ID, title and body. Week 3 didn't cover foreign keys so I had to use the SQLalchemy documentation and google.

I added pydantic schemas for creating and returning post details.

I also created a post endpoint and reused my JWT authentication steps from day 3 to authorise and identify the user creating a post.

Tests completed:

- Used the docs page to test the creation of a page and got '201 created'

Problems

Had errors when trying to test post. Initally has “NameError: name 'current_user' is not defined” as I did not include this when defining my function. Also had NameError: name 'get_current_user' is not defined since I did not import this from security correctly. 

After sorting the above error codes I couldn't get authorisation to post even though I was able to log in and GET/profile/me returned status 200. This was because I mistakenly included 'Course' from week 3 in my db.add and db.refresh functions rather than posts.

References 
- Week 3 advanced cloud computing part 1-3
- Week 4  advanced cloud computing part 3
- https://docs.sqlalchemy.org/en/21/orm/basic_relationships.html

Github commit

Commit message: Add basic post creation for authenticated users

Commit URL: https://github.com/Andy-BBK/piazza-fastapi-coursework/commit/2e6e36b1ce1366b312d3b16fa21ac6915ca5a0f7

Author timestamp: 2026-11-17T03:01:05Z

Day 4 of development

GET/Post, Get/Post/{posts_id} and automated testing

Today I continued on from where I left of with the Post model and added endpoints to retrieve all posts and retrieve a post by it's ID. I used Week 3 part of the ACC /course routes as a basis adapting the my posts endpoints, which I tested using docs and acheived the correct status codes. This was relatively easy to do compared to the next tasks.

I also started to set up some automated tests in the same flow as the course, where weekend activity 3 focused on API testing with pytest and week 4 homework 1 focused on testing the authentication API. I left other elements of Post alone e.g. topics which I will implement another day.

In line with the course content I first created an application.py file so tests can create their own database, I then setup the conftest.py file for use of temporary SQlite databases. The most challeneging parts about this was adapting the application.py file to meet the Piazza requirments, particulalry because the course code does not include routers.

For the test I started with the /health endpoint which passed. I then used adapted code for password hashing, registration, login and JWT authenication. Using previous homework code to include tests for invalid tokens, expired tokens, duplicate registartion and incorrect login details.

Testing

Running pytest with the health endpoint resulted in:

1 passed, 1 warning.

After a google search on how to display a warning (pytest -W always) I got this ".venv/lib/python3.15/site-packages/fastapi/testclient.py:1
  /Users/andybenson/Documents/Piazza-coursework/.venv/lib/python3.15/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using httpx with starlette.testclient is deprecated; install httpx2 instead.
    from starlette.testclient import TestClient as TestClient  # noqa" which was fixed by updating the depreciated Starlette's TestClient to httpx

The final results using the authentication tests came back as:

12 passed in 0.51s

Problems and decisions

The major problem was adapting the application.py file. I initally included all the endpoints code from auth.py, posts.py, profile.py alongside the app.include_router(auth.router, prefix="/auth") etc, meaning I was doubling up on code. I pasted my code into Chatgpt and asked for help debugging in line with the AI use but not to give any code. With it's explanation I was able to refer back to the course content and see I only needed include_router() to access the code from here and included my .get("/") and .get("/health") endpoints. 

When updating main I didn't replace the previous code with just the application creation code so my main.py was creating the API twice, which I rectified. 

The only problem I had with conftest.py was a spelling mistake 'contest.py'.

Using the logic from the course I used a temporary SQLite database so test would not interfer with users and posts in my normal databse.

Refrences and assitance 

University teaching materials

Week 1 – FastAPI routes

Week 3 – SQLAlchemy models, database sessions, queries and Pydantic

Week 4 – Registration, password hashing and JWT authentication

External learning resources

KodeKloud, Python API Development with FastAPI — Get Post By ID (SQLAlchemy)

KodeKloud — FastAPI TestClient

KodeKloud — Setup Test Database

KodeKloud — Setup Test Database With Fixtures

AI assistance

I used ChatGPT to help understand the relationship between the application factory, database dependencies and pytest fixtures, and to help debug my code.

Github commit

Commit message:

Commit URL:

Author time stamp


