import os
from flask_admin import Admin
from models import db, User, Casinos, Nfl, Mlb, Nba, Nhl, Boxeo, Mma, Nascar, Nascar_drivers, Moto_gp_drivers, Match_Ups_Nacar, Golf, Golfer, Ncaa_Baseball, Ncaa_Football, Ncaa_Basketball, Stats_nba_player, Stats_nba_team, Stats_mlb_team, Stats_mlb_player, Stats_nhl_team, Stats_nhl_player, Stats_box_fighter, Stats_mma_fighter, Stats_nfl_team, Stats_defensive_player_nfl, Stats_offensive_player_nfl, Stats_returning_player_nfl, Stats_kiking_player_nfl, Stats_punting_player_nfl, Soccer, Soccer_Tournament, Stats_Soccer_Team, Stats_Soccer_Player, Logos_NFL, Logos_NBA, Logos_MLB, Logos_NHL, Logos_SOCCER, Logos_Ncaa_Basketball , Logos_Ncaa_Football , Logos_Ncaa_Baseball , Props, Stats_ncaa_baseball_player,  Stats_ncaa_baseball_team, Stats_ncaa_football_team, Stats_defensive_player_ncca_football, Stats_offensive_player_ncaa_football, Stats_returning_player_ncaa_football, Stats_kiking_player_ncaa_football, Stats_punting_player_ncaa_football, Stats_ncaa_basket_team, Stats_ncaa_basket_player, Odds_to_win, Injuries , Futures , Moto_GP , Props_List , Stats_Nhl_Goalkeeper, WNba, Logos_WNBA ,Stats_wnba_player

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
    admin.add_view(ModelView(Moto_gp_drivers, db.session))
    admin.add_view(ModelView(Golf, db.session))
    admin.add_view(ModelView(Golfer, db.session))
    admin.add_view(ModelView(Match_Ups_Nacar, db.session))
    admin.add_view(ModelView(Stats_nba_player, db.session))
    admin.add_view(ModelView(Stats_nba_team, db.session))
    admin.add_view(ModelView(Stats_mlb_team, db.session))
    admin.add_view(ModelView(Stats_mlb_player, db.session))
    admin.add_view(ModelView(Stats_nhl_team, db.session))
    admin.add_view(ModelView(Stats_nhl_player, db.session))
    admin.add_view(ModelView(Stats_Nhl_Goalkeeper, db.session))
    admin.add_view(ModelView(Stats_box_fighter, db.session))
    admin.add_view(ModelView(Stats_mma_fighter, db.session))
    admin.add_view(ModelView(Stats_nfl_team, db.session))
    admin.add_view(ModelView(Stats_defensive_player_nfl, db.session))
    admin.add_view(ModelView(Stats_offensive_player_nfl, db.session))
    admin.add_view(ModelView(Stats_kiking_player_nfl, db.session))
    admin.add_view(ModelView(Stats_returning_player_nfl, db.session))
    admin.add_view(ModelView(Stats_punting_player_nfl, db.session))
    admin.add_view(ModelView(Casinos, db.session))
    admin.add_view(ModelView(Soccer_Tournament, db.session))
    admin.add_view(ModelView(Soccer, db.session))
    admin.add_view(ModelView(Stats_Soccer_Team, db.session))
    admin.add_view(ModelView(Stats_Soccer_Player, db.session))
    admin.add_view(ModelView(Logos_NFL, db.session))
    admin.add_view(ModelView(Logos_NBA, db.session))
    admin.add_view(ModelView(Logos_MLB, db.session))
    admin.add_view(ModelView(Logos_NHL, db.session))
    admin.add_view(ModelView(Logos_SOCCER, db.session))
    admin.add_view(ModelView(Logos_Ncaa_Basketball, db.session))
    admin.add_view(ModelView(Logos_Ncaa_Football, db.session))
    admin.add_view(ModelView(Logos_Ncaa_Baseball, db.session))
    admin.add_view(ModelView(Props, db.session))
    admin.add_view(ModelView(Stats_ncaa_baseball_player, db.session))
    admin.add_view(ModelView(Stats_ncaa_baseball_team, db.session))
    admin.add_view(ModelView(Stats_ncaa_football_team, db.session))
    admin.add_view(ModelView(Stats_defensive_player_ncca_football, db.session))
    admin.add_view(ModelView(Stats_offensive_player_ncaa_football, db.session))
    admin.add_view(ModelView(Stats_returning_player_ncaa_football, db.session))
    admin.add_view(ModelView(Stats_kiking_player_ncaa_football, db.session))
    admin.add_view(ModelView(Stats_punting_player_ncaa_football, db.session))
    admin.add_view(ModelView(Stats_ncaa_basket_team, db.session))
    admin.add_view(ModelView(Stats_ncaa_basket_player, db.session))
    admin.add_view(ModelView(Odds_to_win, db.session))
    admin.add_view(ModelView(Injuries, db.session))
    admin.add_view(ModelView(Futures, db.session))
    admin.add_view(ModelView(Moto_GP, db.session))
    admin.add_view(ModelView(Props_List, db.session))
    admin.add_view(ModelView(WNba, db.session))
    admin.add_view(ModelView(Logos_WNBA, db.session))
    admin.add_view(ModelView(Stats_wnba_player, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))
