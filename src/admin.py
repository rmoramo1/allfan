import os
from flask_admin import Admin
from models import db, Nfl, Mbl, Nba, Nhl , Boxeo , Mma ,Nascar ,Nascar_drivers,Match_Ups_Nacar ,Golf ,Golfer ,News
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'slate'
    admin = Admin(app, name='Admin', template_mode='bootstrap3')

    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(Mbl, db.session))
    admin.add_view(ModelView(Nfl, db.session))
    admin.add_view(ModelView(Nba, db.session))
    admin.add_view(ModelView(Nhl, db.session))
    admin.add_view(ModelView(Boxeo, db.session))
    admin.add_view(ModelView(Mma, db.session))
    admin.add_view(ModelView(Nascar, db.session))
    admin.add_view(ModelView(Nascar_drivers, db.session))
    admin.add_view(ModelView(Golf, db.session))
    admin.add_view(ModelView(Golfer, db.session))
    admin.add_view(ModelView(News, db.session))
    admin.add_view(ModelView(Match_Ups_Nacar, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))