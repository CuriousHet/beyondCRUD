from fastapi import FastAPI
from src.books.routes import book_router
from src.auth.routes import auth_router
from contextlib import asynccontextmanager
from src.db.main import init_db

@asynccontextmanager
async def life_span(app: FastAPI):
    print("Server is started...!!")
    await init_db()
    yield 
    print("Server has been stopped...!!")

version = "v1"

app = FastAPI(
    title="Bookly",
    description="A RESTFUL api for a book review web service",
    version=version,
    lifespan=life_span
)

app.include_router(book_router,prefix="/api/{version}/books",tags=['books'])
app.include_router(auth_router,prefix="/api/{version}/auth",tags=['auth'])