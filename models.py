from sqlalchemy import Column, Integer, String, ForeignKey

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)

    # Unique email
    email = Column(String, unique=True, index=True, nullable=False)

    # Storage for hashed password
    hashed_password = Column(String, nullable=False)

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    title = Column(String, nullable=False)
    body = Column(String, nullable=False)