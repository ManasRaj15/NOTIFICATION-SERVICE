from databases import Database
from app.config import settings

database = Database(settings.DATABASE_URL)