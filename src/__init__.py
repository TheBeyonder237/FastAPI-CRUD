from fastapi import FastAPI
from fastapi import status
from starlette.responses import JSONResponse

from src.books.routes import book_router
from src.auth.routes import auth_router
from src.db.main import init_db
from src.reviews.routes import review_router
from src.tags.routes import tags_router
from .errors import register_all_errors
from .middleware import register_middleware

from contextlib import asynccontextmanager


@asynccontextmanager
async def life_span(app: FastAPI):
    print(f"Server is starting ...")
    await init_db()
    yield
    print(f"server has been stopped")


version = "v1"


app = FastAPI(
    title="Books API",
    description="A REST API for a book review web service",
    version=version,
    docs_url=f"/api/{version}/docs",
    contact = {
        "email": "davidngoue@orizonne.net"
    },
    license = "MIT",
    redoc_url=f"/api/{version}/redoc",
)

register_all_errors(app)

register_middleware(app)
@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(book_router, prefix=f"/api/{version}/books", tags=['books'])
app.include_router(auth_router, prefix=f"/api/{version}/auth", tags=['auth'])
app.include_router(review_router, prefix=f"/api/{version}/reviews", tags=['reviews'])
app.include_router(tags_router, prefix=f"/api/{version}/tags", tags=['tags'])