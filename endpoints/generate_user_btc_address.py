from fastapi import APIRouter, Request
from bit import Key
from fastapi.templating import Jinja2Templates
router = APIRouter()

templates = Jinja2Templates(directory='templates')

@router.get('/new_address')
async def new_addy_get(request: Request):
    return templates.TemplateResponse('new_address.html', {'request':Request})

@router.post('/new_address')
async def gen_new_addy(request:Request):
    key = Key()
    addy = key.to_wif()
    return templates.TemplateResponse('new_address.html', {'request':Request, 'priv':addy})