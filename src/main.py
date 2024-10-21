# API app initalizes here

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes import hello
from src.config.settings import get_settings


def create_application() -> FastAPI:
    settings = get_settings()
    
    app = FastAPI(
        title=settings.PROJECT_NAME,
        debug=settings.DEBUG
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    app.include_router(hello.router, prefix="/api/v1",tags=["home"])

    return app

app = create_application()