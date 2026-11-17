from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import models
import schemas
from database import get_db
from security import get_current_user

router = APIRouter()

@router.post(
    "/posts", response_model=schemas.PostResponse,status_code=201)
def create_post(post_data: schemas.PostCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    # post_data has already been checked by Pydantic.

    post = models.Post(
        author_id=current_user.id,
        title=post_data.title,
        body=post_data.body
    )

    try:
        db.add(post)
        db.commit()
        db.refresh(post)
        return post

    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Post code already exists")

@router.get("/posts", response_model=list[schemas.PostResponse])
def get_posts(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):

    posts = db.query(models.Post).all()
    return posts

@router.get("/posts/{posts_id}", response_model=schemas.PostResponse)
def get_course(posts_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)
):
   
    posts = db.query(models.Post).filter(models.Post.id == posts_id).first()

    if posts is None:
        raise HTTPException(status_code=404, detail="Post not found")

    return posts   