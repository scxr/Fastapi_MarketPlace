from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from models.db_models import Items
from db.functions import get_db
from db.base import SessionLocal, engine
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT
templates = Jinja2Templates(directory='templates')

router = APIRouter()

@router.get('/create_listing')
async def create_listing_get(request: Request):
    return templates.TemplateResponse('create_listing.html', {'request':request})

@router.post('/create_listing')
async def create_listing_post(item_name=Form(...), item_price=Form(...), db: Session = Depends(get_db), Authorise :AuthJWT = Depends()):
    Authorise.jwt_required()
    user = Authorise.get_jwt_subject()
    new_item = Items()
    new_item.owner = user
    new_item.item_name = item_name
    new_item.item_price = item_price
    db.add(new_item)
    db.commit()
    return 'item added successfully'