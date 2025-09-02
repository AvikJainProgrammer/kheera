from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .models import TicketStatus

# ---------- Users ----------
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    user_id: int

    class Config:
        orm_mode = True


# ---------- Projects ----------
class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    project_id: int

    class Config:
        orm_mode = True


# ---------- Tickets ----------
class TicketBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[TicketStatus] = TicketStatus.OPEN

class TicketCreate(TicketBase):
    project_id: int
    reporter_id: int
    assignee_id: Optional[int] = None

class Ticket(TicketBase):
    ticket_id: int
    project_id: int
    reporter_id: int
    assignee_id: Optional[int]
    created_at: datetime

    class Config:
        orm_mode = True


# ---------- Comments ----------
class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    ticket_id: int
    author_id: int

class Comment(CommentBase):
    comment_id: int
    ticket_id: int
    author_id: int
    created_at: datetime

    class Config:
        orm_mode = True
