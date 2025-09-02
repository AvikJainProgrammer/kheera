from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, Base, get_db

app = FastAPI()

# Create tables if not exists
Base.metadata.create_all(bind=engine)

# ---------- Users ----------
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip=skip, limit=limit)


# ---------- Projects ----------
@app.post("/projects/", response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return crud.create_project(db=db, project=project)

@app.get("/projects/", response_model=list[schemas.Project])
def read_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_projects(db, skip=skip, limit=limit)


# ---------- Tickets ----------
@app.post("/tickets/", response_model=schemas.Ticket)
def create_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    return crud.create_ticket(db=db, ticket=ticket)

@app.get("/tickets/", response_model=list[schemas.Ticket])
def read_tickets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_tickets(db, skip=skip, limit=limit)


# ---------- Comments ----------
@app.post("/comments/", response_model=schemas.Comment)
def create_comment(comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    return crud.create_comment(db=db, comment=comment)

@app.get("/comments/", response_model=list[schemas.Comment])
def read_comments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_comments(db, skip=skip, limit=limit)

# ---------- Users ----------
@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.update_user(db, user_id=user_id, user_update=user)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# ---------- Projects ----------
@app.put("/projects/{project_id}", response_model=schemas.Project)
def update_project(project_id: int, project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    db_project = crud.update_project(db, project_id=project_id, project_update=project)
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project

@app.delete("/projects/{project_id}", response_model=schemas.Project)
def delete_project(project_id: int, db: Session = Depends(get_db)):
    db_project = crud.delete_project(db, project_id=project_id)
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project


# ---------- Tickets ----------
@app.put("/tickets/{ticket_id}", response_model=schemas.Ticket)
def update_ticket(ticket_id: int, ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    db_ticket = crud.update_ticket(db, ticket_id=ticket_id, ticket_update=ticket)
    if not db_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return db_ticket

@app.delete("/tickets/{ticket_id}", response_model=schemas.Ticket)
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    db_ticket = crud.delete_ticket(db, ticket_id=ticket_id)
    if not db_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return db_ticket

# ---------- Comments ----------
@app.put("/comments/{comment_id}", response_model=schemas.Comment)
def update_comment(comment_id: int, comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    db_comment = crud.update_comment(db, comment_id=comment_id, comment_update=comment)
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment

@app.delete("/comments/{comment_id}", response_model=schemas.Comment)
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = crud.delete_comment(db, comment_id=comment_id)
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment
