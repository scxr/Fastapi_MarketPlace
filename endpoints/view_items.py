from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from db.functions import get_db
from models.db_models import Items
templates = Jinja2Templates(directory='templates')

router = APIRouter()

@router.get('/view_all_items')
async def get_all_items(request: Request, db: Session = Depends(get_db)):
    items = db.query(Items).all()
    return templates.TemplateResponse('view_listings.html', {'request':request, 'items':items})