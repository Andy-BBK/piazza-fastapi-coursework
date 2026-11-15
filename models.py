from sqlalchemy import Column, Integer, String

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)

    # Unique email
    email = Column(String, unique=True, index=True, nullable=False)

    # Storage for hashed password
    hashed_password = Column(String, nullable=False)