import os
from flask_admin import Admin
from models import db,User, Nfl, Mlb, Nba, Nhl , Boxeo , Mma ,Nascar ,Nascar_drivers,Match_Ups_Nacar ,Golf ,Golfer ,News,Ncaa_Baseball,Ncaa_Football,Ncaa_Basketball,Champions_League,Confederations_Cup,W_C_Qualifying,CONCACAF,England_Premier_League,Europa_League,International_Friendlies,France_League,Bundesliga,International_Matches,Italia_Serie_A,Mx_Expansion,Mx_Apertura,Spain_Primera_Liga,USA_MLS,Brazil_Serie_A,Colombia_Primera_A
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'slate'
    admin = Admin(app, name='Admin', template_mode='bootstrap3')

    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Mlb, db.session))
    admin.add_view(ModelView(Ncaa_Baseball, db.session))
    admin.add_view(ModelView(Nfl, db.session))
    admin.add_view(ModelView(Ncaa_Football, db.session))
    admin.add_view(ModelView(Nba, db.session))
    admin.add_view(ModelView(Ncaa_Basketball, db.session))
    admin.add_view(ModelView(Nhl, db.session))
    admin.add_view(ModelView(Boxeo, db.session))
    admin.add_view(ModelView(Mma, db.session))
    admin.add_view(ModelView(Nascar, db.session))
    admin.add_view(ModelView(Nascar_drivers, db.session))
    admin.add_view(ModelView(Golf, db.session))
    admin.add_view(ModelView(Golfer, db.session))
    admin.add_view(ModelView(News, db.session))
    admin.add_view(ModelView(Match_Ups_Nacar, db.session))
    admin.add_view(ModelView(Champions_League, db.session))
    admin.add_view(ModelView(Confederations_Cup, db.session))
    admin.add_view(ModelView(W_C_Qualifying, db.session))
    admin.add_view(ModelView(CONCACAF, db.session))
    admin.add_view(ModelView(England_Premier_League, db.session))
    admin.add_view(ModelView(Europa_League, db.session))
    admin.add_view(ModelView(International_Friendlies, db.session))
    admin.add_view(ModelView(France_League, db.session))
    admin.add_view(ModelView(Bundesliga, db.session))
    admin.add_view(ModelView(International_Matches, db.session))
    admin.add_view(ModelView(Italia_Serie_A, db.session))
    admin.add_view(ModelView(Mx_Expansion, db.session))
    admin.add_view(ModelView(Mx_Apertura, db.session))
    admin.add_view(ModelView(Spain_Primera_Liga, db.session))
    admin.add_view(ModelView(USA_MLS, db.session))
    admin.add_view(ModelView(Brazil_Serie_A, db.session))
    admin.add_view(ModelView(Colombia_Primera_A, db.session))


    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))