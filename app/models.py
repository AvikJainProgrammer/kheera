from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .database import Base
import enum


class TicketStatus(str, enum.Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    CLOSED = "closed"


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)

    # Relationships
    reported_tickets = relationship(
        "Ticket",
        foreign_keys="Ticket.reporter_id",
        back_populates="reporter"
    )
    assigned_tickets = relationship(
        "Ticket",
        foreign_keys="Ticket.assignee_id",
        back_populates="assignee"
    )
    comments = relationship("Comment", back_populates="author")


class Project(Base):
    __tablename__ = "projects"

    project_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(Text)

    # Relationships
    tickets = relationship("Ticket", back_populates="project", cascade="all, delete-orphan")


class Ticket(Base):
    __tablename__ = "tickets"

    ticket_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    status = Column(Enum(TicketStatus), default=TicketStatus.OPEN, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    project_id = Column(Integer, ForeignKey("projects.project_id"), nullable=False)
    reporter_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    assignee_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)

    # Relationships
    project = relationship("Project", back_populates="tickets")
    reporter = relationship(
        "User",
        foreign_keys=[reporter_id],
        back_populates="reported_tickets"
    )
    assignee = relationship(
        "User",
        foreign_keys=[assignee_id],
        back_populates="assigned_tickets"
    )
    comments = relationship("Comment", back_populates="ticket", cascade="all, delete-orphan")


class Comment(Base):
    __tablename__ = "comments"

    comment_id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey("tickets.ticket_id"), nullable=False)
    author_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    ticket = relationship("Ticket", back_populates="comments")
    author = relationship("User", back_populates="comments")
