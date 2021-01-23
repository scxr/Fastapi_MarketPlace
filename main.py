from fastapi import FastAPI, Request
from endpoints import (login_endpoint, 
    register_endpoint, 
    generate_user_btc_address,
    create_listing,
    view_items)
from db.base import engine
import uvicorn
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from models import db_models
from fastapi.templating import Jinja2Templates
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from config import settings_jwt
from pydantic import BaseModel, BaseSettings
import os
db_models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
class Settings(BaseModel):
    authjwt_secret_key: str = "thisisasecrettest1234"
    authjwt_token_location: set = {"cookies"} 

@AuthJWT.load_config
def get_config():
    return Settings()

@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return RedirectResponse(url="/login")
app.include_router(
    login_endpoint.router
)
app.include_router(
    register_endpoint.router
)

app.include_router(
    generate_user_btc_address.router
)

app.include_router(
    create_listing.router
)

app.include_router(
    view_items.router
)

uvicorn.run(app)
