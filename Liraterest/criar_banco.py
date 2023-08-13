from liraterest import app, database
from liraterest.models import Usuario, Foto

with app.app_context():

    database.create_all()