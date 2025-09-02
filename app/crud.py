from sqlalchemy.orm import Session
from . import models, schemas

# ---------- Users ----------
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


# ---------- Projects ----------
def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def get_projects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Project).offset(skip).limit(limit).all()


# ---------- Tickets ----------
def create_ticket(db: Session, ticket: schemas.TicketCreate):
    db_ticket = models.Ticket(**ticket.dict())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

def get_tickets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Ticket).offset(skip).limit(limit).all()


# ---------- Comments ----------
def create_comment(db: Session, comment: schemas.CommentCreate):
    db_comment = models.Comment(**comment.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_comments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Comment).offset(skip).limit(limit).all()

# ---------- Users ----------
def update_user(db: Session, user_id: int, user_update: schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not db_user:
        return None
    for key, value in user_update.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not db_user:
        return None
    db.delete(db_user)
    db.commit()
    return db_user


# ---------- Projects ----------
def update_project(db: Session, project_id: int, project_update: schemas.ProjectCreate):
    db_project = db.query(models.Project).filter(models.Project.project_id == project_id).first()
    if not db_project:
        return None
    for key, value in project_update.dict().items():
        setattr(db_project, key, value)
    db.commit()
    db.refresh(db_project)
    return db_project

def delete_project(db: Session, project_id: int):
    db_project = db.query(models.Project).filter(models.Project.project_id == project_id).first()
    if not db_project:
        return None
    db.delete(db_project)
    db.commit()
    return db_project


# ---------- Tickets ----------
def update_ticket(db: Session, ticket_id: int, ticket_update: schemas.TicketCreate):
    db_ticket = db.query(models.Ticket).filter(models.Ticket.ticket_id == ticket_id).first()
    if not db_ticket:
        return None
    for key, value in ticket_update.dict().items():
        setattr(db_ticket, key, value)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

def delete_ticket(db: Session, ticket_id: int):
    db_ticket = db.query(models.Ticket).filter(models.Ticket.ticket_id == ticket_id).first()
    if not db_ticket:
        return None
    db.delete(db_ticket)
    db.commit()
    return db_ticket

# ---------- Comments ----------
def update_comment(db: Session, comment_id: int, comment_update: schemas.CommentCreate):
    db_comment = db.query(models.Comment).filter(models.Comment.comment_id == comment_id).first()
    if not db_comment:
        return None
    for key, value in comment_update.dict().items():
        setattr(db_comment, key, value)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def delete_comment(db: Session, comment_id: int):
    db_comment = db.query(models.Comment).filter(models.Comment.comment_id == comment_id).first()
    if not db_comment:
        return None
    db.delete(db_comment)
    db.commit()
    return db_comment

