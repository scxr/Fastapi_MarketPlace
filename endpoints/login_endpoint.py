import os
import bcrypt
from fastapi import APIRouter, Request, Form, Depends, Response
from fastapi.templating import Jinja2Templates
from models.request_models import User_req
from fastapi_jwt_auth import AuthJWT
from fastapi.responses import JSONResponse
from db.functions import get_db
from db.base import SessionLocal, engine
from models.db_models import User
from .jwt_auth import encode_auth_token, decode_auth_token, jwt_required_wrap
from config import settings
router = APIRouter()

templates = Jinja2Templates(directory='templates')



@router.get('/login')                                  
async def login_get(request:Request):
    return templates.TemplateResponse('login.html', {'request':request})

@router.post('/login')
async def login_post(response: Response,username=Form(...), password=Form(...), db = Depends(get_db), Authorize: AuthJWT = Depends()):
    user_vals = db.query(User).filter(User.username == username).first()
    if user_vals is None:
        return {"error":"user not found"}
    if bcrypt.checkpw(password.encode(), user_vals.hashed_pword):
        access_token = Authorize.create_access_token(subject=username)
        Authorize.set_access_cookies(access_token)
        return {'access_token':access_token}
    else:
        return 'incorrect password'
        
@router.get('/test')
async def test(Authorise: AuthJWT = Depends()):
    Authorise.jwt_required()
    return 'hello'