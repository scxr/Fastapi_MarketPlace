from pydantic import BaseConfig, BaseModel

class settings(BaseConfig):
    DATABASE_URI = 'sqlite:///./database.db'

class settings_jwt(BaseModel):
    AUTHJWT_SECRET_KEY: str = 'andioop'