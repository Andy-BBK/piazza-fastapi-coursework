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

Github commit:

Commit message:

Commit URL:

Author timestamp: