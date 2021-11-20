from app import app
from models import Clubs, Matches, db

#drop and create tables
db.drop_all()
db.create_all()
