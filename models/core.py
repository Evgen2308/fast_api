from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base

from .database import Base

# Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")
    tokens = relationship("Token", back_populates="user")


# class Token(Base):
#     __tablename__ = "tokens"
#     id = Column(Integer, primary_key=True, index=True)
#     access_token = Column(String, unique=True, index=True)
#
#     user_id = Column(Integer, ForeignKey("users.id"))
#     user = relationship("User", back_populates="tokens")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
