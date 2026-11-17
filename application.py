from fastapi import FastAPI

import models
from database import engine
from routers import auth, profile, posts


def create_app(db_engine=engine):
    models.Base.metadata.create_all(bind=db_engine)
    app = FastAPI()

    app.include_router(auth.router, prefix="/auth")
    app.include_router(profile.router, prefix="/profile")
    app.include_router(posts.router)

    @app.get("/")
    def home():
        return{"message": "Welcome to Piazza API"}


    @app.get("/health")
    def health():
        return {"message": "Piazza API working"}

    return app