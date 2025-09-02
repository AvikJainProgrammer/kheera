from sqlalchemy import Column, Integer, String, Text, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    role = Column(String(50), default="member")
    created_at = Column(TIMESTAMP, server_default=func.now())

    tickets = relationship("Ticket", back_populates="assignee")

class Project(Base):
    __tablename__ = "projects"

    project_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    created_by = Column(Integer, ForeignKey("users.user_id"))
    created_at = Column(TIMESTAMP, server_default=func.now())

    tickets = relationship("Ticket", back_populates="project")

class Ticket(Base):
    __tablename__ = "tickets"

    ticket_id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.project_id"))
    title = Column(String(200), nullable=False)
    description = Column(Text)
    status = Column(String(50), default="To Do")
    priority = Column(String(20), default="Medium")
    assignee_id = Column(Integer, ForeignKey("users.user_id"))
    reporter_id = Column(Integer, ForeignKey("users.user_id"))
    parent_ticket_id = Column(Integer, ForeignKey("tickets.ticket_id"), nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    project = relationship("Project", back_populates="tickets")
    assignee = relationship("User", back_populates="tickets")

class Comment(Base):
    __tablename__ = "comments"

    comment_id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey("tickets.ticket_id"))
    user_id = Column(Integer, ForeignKey("users.user_id"))
    content = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
