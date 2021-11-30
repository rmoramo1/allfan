"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Casinos, Nfl, Mlb, Nba, Nhl, Boxeo, Mma, Nascar, Nascar_drivers, Match_Ups_Nacar, Golf, Golfer, News, Ncaa_Baseball, Ncaa_Football, Ncaa_Basketball, Champions_League, Confederations_Cup, W_C_Qualifying, CONCACAF, Europa_League, International_Friendlies, France_League, Bundesliga, International_Matches, Italia_Serie_A, Mx_Expansion, Mx_Apertura, Spain_Primera_Liga, USA_MLS, Brazil_Serie_A, Colombia_Primera_A, Stats_nba_player, Stats_nba_team, Stats_mlb_team, Stats_nhl_team, Stats_nhl_player, Stats_box_fighter, Stats_mma_fighter, Stats_nfl_team, Stats_defensive_player_nfl, Stats_offensive_player_nfl, Stats_returning_player_nfl, Stats_kiking_player_nfl, Stats_punting_player_nfl, Costa_Rica_PD

from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from flask_jwt_extended import JWTManager

# from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)
# Handle/serialize errors like a JSON object


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code
# generate sitemap with all your endpoints


@app.route('/')
def sitemap():
    return generate_sitemap(app)

# obtener usuario de base de datos y crea token


@app.route('/login', methods=['POST'])
def login():
    name = request.json.get("name", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    print(name)
    print(moneyLineAway)
    user = User.query.filter_by(name=name, moneyLineAway=moneyLineAway).first()
    # valida si estan vacios los ingresos
    if user is None:
        return jsonify({"msg": "Bad mail or moneyLineAway"}), 401
    # crear token login
    access_token = create_access_token(identity=name)
    return jsonify({"token": access_token, "username": user.name})
# ----------------------------------------------------------------------------


@app.route("/casinos", methods=["GET"])
def casinos():
    if request.method == "GET":
        records = Casinos.query.all()
        return jsonify([Casinos.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ----------------------------------------------------------------------------


@app.route("/mlb", methods=["GET"])
def mlb():
    if request.method == "GET":
        records = Mlb.query.all()
        return jsonify([Mlb.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------


@app.route("/ncaa_football", methods=["GET"])
#   @limiter.limit("12 per hour")
def ncaa_football():
    if request.method == "GET":
        records = Ncaa_Football.query.all()
        return jsonify([Ncaa_Football.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------


@app.route("/nfl", methods=["GET"])
def nfl():
    if request.method == "GET":
        records = Nfl.query.all()
        return jsonify([Nfl.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------


@app.route("/ncaa_baseball", methods=["GET"])
#   @limiter.limit("12 per hour")
def ncaa_baseball():
    if request.method == "GET":
        records = Ncaa_Baseball.query.all()
        return jsonify([Ncaa_Baseball.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------


@app.route("/nba", methods=["GET"])
def nba():
    if request.method == "GET":
        records = Nba.query.all()
        return jsonify([Nba.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------


@app.route("/ncaa_basketball", methods=["GET"])
#   @limiter.limit("12 per hour")
def ncaa_basketball():
    if request.method == "GET":
        records = Ncaa_Basketball.query.all()
        return jsonify([Ncaa_Basketball.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------


@app.route("/nhl", methods=["GET"])
def nhl():
    if request.method == "GET":
        records = Nhl.query.all()
        return jsonify([Nhl.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------


@app.route("/boxeo", methods=["GET"])
def boxeo():
    if request.method == "GET":
        records = Boxeo.query.all()
        return jsonify([Boxeo.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------


@app.route("/mma", methods=["GET"])
def mma():
    if request.method == "GET":
        records = Mma.query.all()
        return jsonify([Mma.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------


@app.route("/nascar", methods=["GET"])
def nascar():
    if request.method == "GET":
        records = Nascar.query.all()
        return jsonify([Nascar.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------


@app.route("/nascar_drivers", methods=["GET"])
def nascar_drivers():
    if request.method == "GET":
        records = Nascar_drivers.query.all()
        return jsonify([Nascar_drivers.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # ---------------------------------------------------------------------------


@app.route("/match_ups_nascar", methods=["GET"])
def match_ups_nascar():
    if request.method == "GET":
        records = Match_Ups_Nacar.query.all()
        return jsonify([Match_Ups_Nacar.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # ---------------------------------------------------------------------------


@app.route("/golf", methods=["GET"])
def golf():
    if request.method == "GET":
        records = Golf.query.all()
        return jsonify([Golf.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # ---------------------------------------------------------------------------


@app.route("/golfer", methods=["GET"])
def golfer():
    if request.method == "GET":
        records = Golfer.query.all()
        return jsonify([Golfer.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # ---------------------------------------------------------------------------


@app.route("/confederations_cup", methods=["GET"])
def confederations_cup():
    if request.method == "GET":
        records = Confederations_Cup().query.all()
        return jsonify([Confederations_Cup.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # ---------------------------------------------------------------------------


@app.route("/champions_league", methods=["GET"])
def champions_league():
    if request.method == "GET":
        records = Champions_League().query.all()
        return jsonify([Champions_League.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # ---------------------------------------------------------------------------


@app.route("/w_c_qualifying", methods=["GET"])
def w_c_qualifying():
    if request.method == "GET":
        records = W_C_Qualifying().query.all()
        return jsonify([W_C_Qualifying.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # ---------------------------------------------------------------------------


@app.route("/CONCACAF", methods=["GET"])
def CONCACAF():
    if request.method == "GET":
        records = CONCACAF().query.all()
        return jsonify([CONCACAF.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # ---------------------------------------------------------------------------


@app.route("/england_premier_league", methods=["GET"])
def england_premier_league():
    if request.method == "GET":
        records = England_Premier_League().query.all()
        return jsonify([England_Premier_League.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # ---------------------------------------------------------------------------


@app.route("/europa_league", methods=["GET"])
def europa_league():
    if request.method == "GET":
        records = Europa_League().query.all()
        return jsonify([Europa_League.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # ---------------------------------------------------------------------------


@app.route("/international_friendlies", methods=["GET"])
def international_friendlies():
    if request.method == "GET":
        records = International_Friendlies().query.all()
        return jsonify([International_Friendlies.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # ---------------------------------------------------------------------------


@app.route("/france_league", methods=["GET"])
def france_league():
    if request.method == "GET":
        records = France_League().query.all()
        return jsonify([France_League.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # ---------------------------------------------------------------------------


@app.route("/bundesliga", methods=["GET"])
def bundesliga():
    if request.method == "GET":
        records = Bundesliga().query.all()
        return jsonify([Bundesliga.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # ---------------------------------------------------------------------------


@app.route("/international_matches", methods=["GET"])
def international_matches():
    if request.method == "GET":
        records = International_Matches().query.all()
        return jsonify([International_Matches.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # ---------------------------------------------------------------------------


@app.route("/italia_serie_A", methods=["GET"])
def italia_serie_A():
    if request.method == "GET":
        records = Italia_Serie_A().query.all()
        return jsonify([Italia_Serie_A.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # ---------------------------------------------------------------------------


@app.route("/mx_expansion", methods=["GET"])
def mx_expansion():
    if request.method == "GET":
        records = Mx_Expansion().query.all()
        return jsonify([Mx_Expansion.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # ---------------------------------------------------------------------------


@app.route("/mx_apertura", methods=["GET"])
def mx_apertura():
    if request.method == "GET":
        records = Mx_Apertura().query.all()
        return jsonify([Mx_Apertura.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # ---------------------------------------------------------------------------


@app.route("/spain_primera_liga", methods=["GET"])
def spain_primera_liga():
    if request.method == "GET":
        records = Spain_Primera_Liga().query.all()
        return jsonify([Spain_Primera_Liga.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # ---------------------------------------------------------------------------


@app.route("/USA_MLS", methods=["GET"])
def USA_MLS():
    if request.method == "GET":
        records = USA_MLS().query.all()
        return jsonify([USA_MLS.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # ---------------------------------------------------------------------------


@app.route("/brazil_serie_A", methods=["GET"])
def brazil_serie_A():
    if request.method == "GET":
        records = Brazil_Serie_A().query.all()
        return jsonify([Brazil_Serie_A.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # ---------------------------------------------------------------------------


@app.route("/colombia_primera_A", methods=["GET"])
def colombia_primera_A():
    if request.method == "GET":
        records = Colombia_Primera_A().query.all()
        return jsonify([Colombia_Primera_A.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # ---------------------------------------------------------------------------


@app.route("/stats_nba_player", methods=["GET"])
def stats_nba_player():
    if request.method == "GET":
        records = Stats_nba_player().query.all()
        return jsonify([Stats_nba_player.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # --------------------------------------------------------------------


@app.route("/stats_mlb_team", methods=["GET"])
def stats_mlb_team():
    if request.method == "GET":
        records = Stats_mlb_team().query.all()
        return jsonify([Stats_mlb_team.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # --------------------------------------------------------------------


@app.route("/stats_mlb_player", methods=["GET"])
def stats_mlb_player():
    if request.method == "GET":
        records = Stats_mlb_player().query.all()
        return jsonify([Stats_mlb_player.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # --------------------------------------------------------------------


@app.route("/stats_nhl_team", methods=["GET"])
def stats_nhl_team():
    if request.method == "GET":
        records = Stats_nhl_team().query.all()
        return jsonify([Stats_nhl_team.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # --------------------------------------------------------------------


@app.route("/stats_nhl_player", methods=["GET"])
def stats_nhl_player():
    if request.method == "GET":
        records = Stats_nhl_player().query.all()
        return jsonify([Stats_nhl_player.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # --------------------------------------------------------------------


@app.route("/stats_box_fighter", methods=["GET"])
def stats_box_fighter():
    if request.method == "GET":
        records = Stats_box_fighter().query.all()
        return jsonify([Stats_box_fighter.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # --------------------------------------------------------------------


@app.route("/stats_mma_fighter", methods=["GET"])
def stats_mma_fighter():
    if request.method == "GET":
        records = Stats_mma_fighter().query.all()
        return jsonify([Stats_mma_fighter.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # --------------------------------------------------------------------


@app.route("/stats_nfl_team", methods=["GET"])
def stats_nfl_team():
    if request.method == "GET":
        records = Stats_nfl_team().query.all()
        return jsonify([Stats_nfl_team.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # --------------------------------------------------------------------


@app.route("/stats_defensive_player_nfl", methods=["GET"])
def stats_defensive_player_nfl():
    if request.method == "GET":
        records = Stats_defensive_player_nfl().query.all()
        return jsonify([Stats_defensive_player_nfl.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # --------------------------------------------------------------------


@app.route("/stats_offensive_player_nfl", methods=["GET"])
def stats_offensive_player_nfl():
    if request.method == "GET":
        records = Stats_offensive_player_nfl().query.all()
        return jsonify([Stats_offensive_player_nfl.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # --------------------------------------------------------------------


@app.route("/stats_returning_player_nfl", methods=["GET"])
def stats_returning_player_nfl():
    if request.method == "GET":
        records = Stats_returning_player_nfl().query.all()
        return jsonify([Stats_returning_player_nfl.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # --------------------------------------------------------------------


@app.route("/stats_kiking_player_nfl", methods=["GET"])
def stats_kiking_player_nfl():
    if request.method == "GET":
        records = Stats_kiking_player_nfl().query.all()
        return jsonify([Stats_kiking_player_nfl.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # --------------------------------------------------------------------


@app.route("/stats_punting_player_nfl", methods=["GET"])
def stats_punting_player_nfl():
    if request.method == "GET":
        records = Stats_punting_player_nfl().query.all()
        return jsonify([Stats_punting_player_nfl.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # --------------------------------------------------------------------


@app.route("/news", methods=["GET"])
def news():
    if request.method == "GET":
        records = News().query.all()
        return jsonify([News.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})

# --------------------------post methot--------------------------------------------


@app.route('/casinos', methods=['POST'])
def createCasino():
    name = request.json.get("name", None)

    # busca team en BBDD
    casinos = Casinos.query.filter_by(name=name).first()
    # the team was not found on the database
    if casinos:
        return jsonify({"msg": "Casino already exists", "Casino": casinos.name}), 401
    else:
        # crea casino nuevo
        # crea registro nuevo en BBDD de
        casinos = Casinos(
            name=name,
        )
        db.session.add(casinos)
        db.session.commit()
        return jsonify({"msg": "casino created successfully"}), 200


@app.route('/mlb', methods=['POST'])
def createGameMlb():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    status = request.json.get("status", None)
    away = request.json.get("away", None)
    pitcher_a = request.json.get("pitcher_a", None)
    home = request.json.get("home", None)
    pitcher_h = request.json.get("pitcher_h", None)
    rl_away = request.json.get("rl_away", None)
    rl_home = request.json.get("rl_home", None)
    juice_rl_away = request.json.get("juice_rl_away", None)
    juice_rl_home = request.json.get("juice_rl_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)
    # --------------------------------------------------------------
    rl_away_f5 = request.json.get("rl_away_f5", None)
    rl_home_f5 = request.json.get("rl_home_f5", None)
    juice_rl_away_f5 = request.json.get("juice_rl_away_f5", None)
    juice_rl_home_f5 = request.json.get("juice_rl_home_f5", None)
    moneyLineAway_f5 = request.json.get("moneyLineAway_f5", None)
    moneyLineHome_f5 = request.json.get("moneyLineHome_f5", None)
    total_f5 = request.json.get("total_f5", None)
    juice_total_over_f5 = request.json.get("juice_total_over_f5", None)
    juice_total_under_f5 = request.json.get("juice_total_under_f5", None)
    tt_away_f5 = request.json.get("tt_away_f5", None)
    juice_over_away_f5 = request.json.get("juice_over_away_f5", None)
    juice_under_away_f5 = request.json.get("juice_under_away_f5", None)
    juice_over_home_f5 = request.json.get("juice_over_home_f5", None)
    juice_under_home_f5 = request.json.get("juice_under_home_f5", None)
    fs_away_f5 = request.json.get("fs_away_f5", None)
    fs_home_f5 = request.json.get("fs_home_f5", None)
    sa_1inning = request.json.get("sa_1inning", None)
    sh_1inning = request.json.get("sh_1inning", None)
    sa_2inning = request.json.get("sa_2inning", None)
    sh_2inning = request.json.get("sh_2inning", None)
    sa_3inning = request.json.get("sa_3inning", None)
    sh_3inning = request.json.get("sh_3inning", None)
    sa_4inning = request.json.get("sa_4inning", None)
    sh_4inning = request.json.get("sh_4inning", None)
    sa_5inning = request.json.get("sa_5inning", None)
    sh_5inning = request.json.get("sh_5inning", None)
    sa_6inning = request.json.get("sa_6inning", None)
    sh_6inning = request.json.get("sh_6inning", None)
    sa_7inning = request.json.get("sa_7inning", None)
    sh_7inning = request.json.get("sh_7inning", None)
    sa_8inning = request.json.get("sa_8inning", None)
    sh_8inning = request.json.get("sh_8inning", None)
    sa_9inning = request.json.get("sa_9inning", None)
    sh_9inning = request.json.get("sh_9inning", None)
    sa_10inning = request.json.get("sa_10inning", None)
    sh_10inning = request.json.get("sh_10inning", None)
    sa_11inning = request.json.get("sa_11inning", None)
    sh_11inning = request.json.get("sh_11inning", None)
    sa_12inning = request.json.get("sa_12inning", None)
    sh_12inning = request.json.get("sh_12inning", None)
    sa_13inning = request.json.get("sa_13inning", None)
    sh_13inning = request.json.get("sh_13inning", None)
    sa_14inning = request.json.get("sa_14inning", None)
    sh_14inning = request.json.get("sh_14inning", None)
    sa_15inning = request.json.get("sa_15inning", None)
    sh_15inning = request.json.get("sh_15inning", None)
    sa_16inning = request.json.get("sa_16inning", None)
    sh_16inning = request.json.get("sh_16inning", None)
    sa_17inning = request.json.get("sa_17inning", None)
    sh_17inning = request.json.get("sh_17inning", None)
    sa_18inning = request.json.get("sa_18inning", None)
    sh_18inning = request.json.get("sh_18inning", None)
    sa_19inning = request.json.get("sa_19inning", None)
    sh_19inning = request.json.get("sh_19inning", None)
    sa_20inning = request.json.get("sa_20inning", None)
    sh_20inning = request.json.get("sh_20inning", None)
    sa_21inning = request.json.get("sa_21inning", None)
    sh_21inning = request.json.get("sh_21inning", None)
    sa_22inning = request.json.get("sa_22inning", None)
    sh_22inning = request.json.get("sh_22inning", None)
    sa_23inning = request.json.get("sa_23inning", None)
    sh_23inning = request.json.get("sh_23inning", None)
    sa_24inning = request.json.get("sa_24inning", None)
    sh_24inning = request.json.get("sh_24inning", None)
    sa_25inning = request.json.get("sa_25inning", None)
    sh_25inning = request.json.get("sh_25inning", None)
    # valida si estan vacios los ingresos

    # busca mlb en BBDD
    mlb = Mlb.query.filter_by(home=home, away=away, date=date).first()
    # the mlb was not found on the database
    if mlb:
        return jsonify({"msg": "Mlb already exists", "status": mlb.status}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        mlb = Mlb(
            date=date, hour=hour, status=status, away=away, pitcher_a=pitcher_a, home=home, pitcher_h=pitcher_h,
            rl_away=rl_away, rl_home=rl_home, juice_rl_away=juice_rl_away, juice_rl_home=juice_rl_home,         moneyLineAway=moneyLineAway, moneyLineHome=moneyLineHome, total=total, juice_total_over=juice_total_over, juice_total_under=juice_total_under, tt_away=tt_away, juice_over_away=juice_over_away, juice_under_away=juice_under_away, tt_home=tt_home, juice_over_home=juice_over_home, juice_under_home=juice_under_home, final_score_away=final_score_away, final_score_home=final_score_home, rl_away_f5=rl_away_f5, rl_home_f5=rl_home_f5, juice_rl_away_f5=juice_rl_away_f5, juice_rl_home_f5=juice_rl_home_f5, moneyLineAway_f5=moneyLineAway_f5, moneyLineHome_f5=moneyLineHome_f5, total_f5=total_f5, juice_total_over_f5=juice_total_over_f5, juice_total_under_f5=juice_total_under_f5, tt_away_f5=tt_away_f5, juice_over_away_f5=juice_over_away_f5, juice_under_away_f5=juice_under_away_f5, juice_over_home_f5=juice_over_home_f5, juice_under_home_f5=juice_under_home_f5, fs_away_f5=fs_away_f5, fs_home_f5=fs_home_f5, sa_1inning=sa_1inning, sh_1inning=sh_1inning, sa_2inning=sa_2inning, sh_2inning=sh_2inning, sa_3inning=sa_3inning, sh_3inning=sh_3inning, sa_4inning=sa_4inning, sh_4inning=sh_4inning, sa_5inning=sa_5inning, sh_5inning=sh_5inning, sa_6inning=sa_6inning, sh_6inning=sh_6inning, sa_7inning=sa_7inning, sh_7inning=sh_7inning, sa_8inning=sa_8inning, sh_8inning=sh_8inning, sa_9inning=sa_9inning, sh_9inning=sh_9inning, sa_10inning=sa_10inning, sh_10inning=sh_10inning, sa_11inning=sa_11inning, sh_11inning=sh_11inning, sa_12inning=sa_12inning, sh_12inning=sh_12inning, sa_13inning=sa_13inning, sh_13inning=sh_13inning, sa_14inning=sa_14inning, sh_14inning=sh_14inning, sa_15inning=sa_15inning, sh_15inning=sh_15inning, sa_16inning=sa_16inning, sh_16inning=sh_16inning, sa_17inning=sa_17inning, sa_18inning=sa_18inning, sa_19inning=sa_19inning, sa_20inning=sa_20inning, sa_21inning=sa_21inning, sa_22inning=sa_22inning, sa_23inning=sa_23inning, sa_24inning=sa_24inning, sa_25inning=sa_25inning)
        db.session.add(mlb)
        db.session.commit()
        return jsonify({"msg": "User created successfully"}), 200


@app.route('/nba', methods=['POST'])
def createGameNba():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    status = request.json.get("status", None)
    away = request.json.get("away", None)
    home = request.json.get("home", None)
    spread_away = request.json.get("spread_away", None)
    spread_home = request.json.get("spread_home", None)
    juice_spread_away = request.json.get("juice_spread_away", None)
    juice_spread_home = request.json.get("juice_spread_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)
    # --------------------------------------------------------------
    first_half_spread_away = request.json.get("first_half_spread_away", None)
    first_half_spread_home = request.json.get("first_half_spread_home", None)
    first_half_juice_spread_away = request.json.get(
        "first_half_juice_spread_away", None)
    first_half_juice_spread_home = request.json.get(
        "first_half_juice_spread_home", None)
    first_half_moneyLineAway = request.json.get(
        "first_half_moneyLineAway", None)
    first_half_moneyLineHome = request.json.get(
        "first_half_moneyLineHome", None)
    first_half_total = request.json.get("first_half_total", None)
    fh_juice_over = request.json.get("fh_juice_over", None)
    fh_juice_under = request.json.get("fh_juice_under", None)
    first_half_tt_away = request.json.get("first_half_tt_away", None)
    first_half_juice_over_away = request.json.get(
        "first_half_juice_over_away", None)
    first_half_juice_under_away = request.json.get(
        "first_half_juice_under_away", None)
    first_half_tt_home = request.json.get("first_half_tt_home", None)
    first_half_juice_over_home = request.json.get(
        "first_half_juice_over_home", None)
    first_half_juice_under_home = request.json.get(
        "first_half_juice_under_home", None)
    first_half_final_score_away = request.json.get(
        "first_half_final_score_away", None)
    first_half_final_score_home = request.json.get(
        "first_half_final_score_home", None)
    #-----------------------------------------------------------------------
    second_half_spread_away = request.json.get("second_half_spread_away", None)
    second_half_spread_home = request.json.get("second_half_spread_home", None)
    second_half_juice_spread_away = request.json.get(
        "second_half_juice_spread_away", None)
    second_half_juice_spread_home = request.json.get(
        "second_half_juice_spread_home", None)
    second_half_moneyLineAway = request.json.get(
        "second_half_moneyLineAway", None)
    second_half_moneyLineHome = request.json.get(
        "second_half_moneyLineHome", None)
    second_half_total = request.json.get("sa_4inning", None)
    sh_juice_over = request.json.get("sh_juice_over", None)
    sh_juice_under = request.json.get("sh_juice_under", None)
    second_half_tt_away = request.json.get("second_half_tt_away", None)
    second_half_juice_over_away = request.json.get(
        "second_half_juice_over_away", None)
    second_half_juice_under_away = request.json.get(
        "second_half_juice_under_away", None)
    second_half_tt_home = request.json.get("second_half_tt_home", None)
    second_half_juice_over_home = request.json.get(
        "second_half_juice_over_home", None)
    second_half_juice_under_home = request.json.get(
        "second_half_juice_under_home", None)
    second_half_final_score_away = request.json.get(
        "second_half_final_score_away", None)
    second_half_final_score_home = request.json.get(
        "second_half_final_score_home", None)
    #----------------------
    q1_half_spread_away = request.json.get("q1_half_spread_away", None)
    q1_half_spread_home = request.json.get("q1_half_spread_home", None)
    q1_half_juice_spread_away = request.json.get(
        "q1_half_juice_spread_away", None)
    q1_half_juice_spread_home = request.json.get(
        "q1_half_juice_spread_home", None)
    q1_half_moneyLineAway = request.json.get("q1_half_moneyLineAway", None)
    q1_half_moneyLineHome = request.json.get("q1_half_moneyLineHome", None)
    q1_half_total = request.json.get("q1_half_total", None)
    q1_juice_over = request.json.get("q1_juice_over", None)
    q1_juice_under = request.json.get("q1_juice_under", None)
    q1_half_tt_away = request.json.get("q1_half_tt_away", None)
    q1_half_juice_over_away = request.json.get("q1_half_juice_over_away", None)
    q1_half_juice_under_away = request.json.get(
        "q1_half_juice_under_away", None)
    q1_half_tt_home = request.json.get("q1_half_tt_home", None)
    q1_half_juice_over_home = request.json.get("q1_half_juice_over_home", None)
    q1_half_juice_under_home = request.json.get(
        "q1_half_juice_under_home", None)
    q1_half_final_score_away = request.json.get(
        "q1_half_final_score_away", None)
    q1_half_final_score_home = request.json.get(
        "q1_half_final_score_home", None)

    # busca mlb en BBDD
    nba = Nba.query.filter_by(home=home, away=away, date=date).first()
    # the mlb was not found on the database
    if nba:
        return jsonify({"msg": "Mlb already exists", "status": nba.status}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        nba = Nba(
            date=date,
            hour=hour,
            status=status,
            away=away,
            home=home,
            spread_away=spread_away,
            spread_home=spread_home,
            juice_spread_away=juice_spread_away,
            juice_spread_home=juice_spread_home,
            moneyLineAway=moneyLineAway,
            moneyLineHome=moneyLineHome,
            total=total,
            juice_total_over=juice_total_over,
            juice_total_under=juice_total_under,
            tt_away=tt_away,
            juice_over_away=juice_over_away,
            juice_under_away=juice_under_away,
            tt_home=tt_home,
            juice_over_home=juice_over_home,
            juice_under_home=juice_under_home,
            final_score_away=final_score_away,
            final_score_home=final_score_home,
            first_half_spread_away=first_half_spread_away,
            first_half_spread_home=first_half_spread_home,
            first_half_juice_spread_away=first_half_juice_spread_away,
            first_half_juice_spread_home=first_half_juice_spread_home,
            first_half_moneyLineAway=first_half_moneyLineAway,
            first_half_moneyLineHome=first_half_moneyLineHome,
            first_half_total=first_half_total,
            fh_juice_over=fh_juice_over,
            fh_juice_under=fh_juice_under,
            first_half_tt_away=first_half_tt_away,
            first_half_juice_over_away=first_half_juice_over_away, first_half_juice_under_away=first_half_juice_under_away, first_half_tt_home=first_half_tt_home, first_half_juice_over_home=first_half_juice_over_home,
            first_half_juice_under_home=first_half_juice_under_home,
            first_half_final_score_away=first_half_final_score_away,
            first_half_final_score_home=first_half_final_score_home, second_half_spread_away=second_half_spread_away,
            second_half_spread_home=second_half_spread_home,
            second_half_juice_spread_away=second_half_juice_spread_away,
            second_half_juice_spread_home=second_half_juice_spread_home,
            second_half_moneyLineAway=second_half_moneyLineAway,
            second_half_moneyLineHome=second_half_moneyLineHome,
            second_half_total=second_half_total,
            sh_juice_over=sh_juice_over,
            sh_juice_under=sh_juice_under,
            second_half_tt_away=second_half_tt_away,
            second_half_juice_over_away=second_half_juice_over_away,
            second_half_juice_under_away=second_half_juice_under_away,
            second_half_tt_home=second_half_tt_home,
            second_half_juice_over_home=second_half_juice_over_home,
            second_half_juice_under_home=second_half_juice_under_home,
            second_half_final_score_away=second_half_final_score_away,
            second_half_final_score_home=second_half_final_score_home,
            q1_half_spread_away=q1_half_spread_away,
            q1_half_spread_home=q1_half_spread_home,
            q1_half_juice_spread_away=q1_half_juice_spread_away,
            q1_half_juice_spread_home=q1_half_juice_spread_home,
            q1_half_moneyLineAway=q1_half_moneyLineAway,
            q1_half_moneyLineHome=q1_half_moneyLineHome,
            q1_half_total=q1_half_total,
            q1_juice_over=q1_juice_over,
            q1_juice_under=q1_juice_under,
            q1_half_tt_away=q1_half_tt_away,
            q1_half_juice_over_away=q1_half_juice_over_away,
            q1_half_juice_under_away=q1_half_juice_under_away,
            q1_half_tt_home=q1_half_tt_home,
            q1_half_juice_over_home=q1_half_juice_over_home,
            q1_half_juice_under_home=q1_half_juice_under_home,
            q1_half_final_score_away=q1_half_final_score_away,
            q1_half_final_score_home=q1_half_final_score_home
        )
        db.session.add(nba)
        db.session.commit()
        return jsonify({"msg": "Game created successfully"}), 200


@app.route('/nhl', methods=['POST'])
def createGameNhl():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    status = request.json.get("status", None)
    away = request.json.get("away", None)
    home = request.json.get("home", None)
    puck_line_away = request.json.get("puck_line_away", None)
    puck_line_home = request.json.get("puck_line_home", None)
    juice_puck_away = request.json.get("juice_puck_away", None)
    juice_puck_home = request.json.get("juice_puck_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)
    # --------------------------------------------------------------
    puck_away_1Q = request.json.get("puck_away_1Q", None)
    puck_home_1Q = request.json.get("puck_home_1Q", None)
    juice_puck_away_1Q = request.json.get("juice_puck_away_1Q", None)
    juice_puck_home_1Q = request.json.get("juice_puck_home_1Q", None)
    moneyLineAway_1Q = request.json.get("moneyLineAway_1Q", None)
    moneyLineHome_1Q = request.json.get("moneyLineHome_1Q", None)
    total_1Q = request.json.get("total_1Q", None)
    Q1_juice_over = request.json.get("Q1_juice_over", None)
    Q1_juice_under = request.json.get("Q1_juice_under", None)
    tt_away_1Q = request.json.get("tt_away_1Q", None)
    juice_over_away_1Q = request.json.get("juice_over_away_1Q", None)
    juice_under_away_1Q = request.json.get("juice_under_away_1Q", None)
    tt_home_1Q = request.json.get("tt_home_1Q", None)
    juice_over_home_1Q = request.json.get("juice_over_home_1Q", None)
    juice_under_home_1Q = request.json.get("juice_under_home_1Q", None)
    sa_1Q = request.json.get("sa_1Q", None)
    sh_1Q = request.json.get("sh_1Q", None)
    sa_2Q = request.json.get("sa_2Q", None)
    sh_2Q = request.json.get("sh_2Q", None)
    sa_3Q = request.json.get("sa_3Q", None)
    sh_3Q = request.json.get("sh_3Q", None)

    # busca mlb en BBDD
    nhl = Nhl.query.filter_by(home=home, away=away, date=date).first()
    # the mlb was not found on the database
    if nhl:
        return jsonify({"msg": "Mlb already exists", "status": nhl.status}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        nhl = Nhl(
            date=date,
            hour=hour,
            status=status,
            away=away,
            preview=preview,
            img_preview=img_preview,
            home=home,
            puck_line_away=puck_line_away,
            puck_line_home=puck_line_home,
            juice_puck_away=juice_puck_away,
            juice_puck_home=juice_puck_home,
            moneyLineAway=moneyLineAway,
            moneyLineHome=moneyLineHome,
            total=total,
            juice_total_over=juice_total_over,
            juice_total_under=juice_total_under,
            tt_away=tt_away,
            juice_over_away=juice_over_away,
            juice_under_away=juice_under_away,
            tt_home=tt_home,
            juice_over_home=juice_over_home,
            juice_under_home=juice_under_home,
            final_score_away=final_score_away,
            final_score_home=final_score_home,
            puck_away_1Q=puck_away_1Q,
            puck_home_1Q=puck_home_1Q,
            juice_puck_away_1Q=juice_puck_away_1Q,
            juice_puck_home_1Q=juice_puck_home_1Q,
            moneyLineAway_1Q=moneyLineAway_1Q,
            moneyLineHome_1Q=moneyLineHome_1Q,
            total_1Q=total_1Q,
            Q1_juice_over=Q1_juice_over,
            Q1_juice_under=Q1_juice_under,
            tt_away_1Q=tt_away_1Q,
            juice_over_away_1Q=juice_over_away_1Q, juice_under_away_1Q=juice_under_away_1Q,
            tt_home_1Q=tt_home_1Q,
            juice_over_home_1Q=juice_over_home_1Q,
            juice_under_home_1Q=juice_under_home_1Q,
            sa_1Q=sa_1Q,
            sh_1Q=sh_1Q,
            sa_2Q=sa_2Q,
            sh_2Q=sh_2Q,
            sa_3Q=sa_3Q,
            sh_3Q=sh_3Q,
        )
        db.session.add(nhl)
        db.session.commit()
        return jsonify({"msg": "Game created successfully"}), 200


@app.route('/nfl', methods=['POST'])
def createGameNfl():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    week = request.json.get("week", None)
    status = request.json.get("status", None)
    casino = request.json.get("casino", None)
    rotation_home = request.json.get("rotation_home", None)
    rotation_away = request.json.get("rotation_away", None)
    away = request.json.get("away", None)
    home = request.json.get("home", None)
    spread_away = request.json.get("spread_away", None)
    spread_home = request.json.get("spread_home", None)
    juice_spread_away = request.json.get("juice_spread_away", None)
    juice_spread_home = request.json.get("juice_spread_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)
    # --------------------------------------------------------------
    first_half_spread_away = request.json.get("first_half_spread_away", None)
    first_half_spread_home = request.json.get("first_half_spread_home", None)
    first_half_juice_spread_away = request.json.get(
        "first_half_juice_spread_away", None)
    first_half_juice_spread_home = request.json.get(
        "first_half_juice_spread_home", None)
    first_half_moneyLineAway = request.json.get(
        "first_half_moneyLineAway", None)
    first_half_moneyLineHome = request.json.get(
        "first_half_moneyLineHome", None)
    first_half_total = request.json.get("first_half_total", None)
    fh_juice_total_over = request.json.get("fh_juice_total_over", None)
    fh_juice_total_under = request.json.get("fh_juice_total_under", None)
    first_half_tt_away = request.json.get("first_half_tt_away", None)
    first_half_juice_over_away = request.json.get(
        "first_half_juice_over_away", None)
    first_half_juice_under_away = request.json.get(
        "first_half_juice_under_away", None)
    first_half_tt_home = request.json.get("first_half_tt_home", None)
    first_half_juice_over_home = request.json.get(
        "first_half_juice_over_home", None)
    first_half_juice_under_home = request.json.get(
        "first_half_juice_under_home", None)
    first_half_final_score_away = request.json.get(
        "first_half_final_score_away", None)
    first_half_final_score_home = request.json.get(
        "first_half_final_score_home", None)
    # --------------
    second_half_spread_away = request.json.get("second_half_spread_away", None)
    second_half_spread_home = request.json.get("second_half_spread_home", None)
    second_half_juice_spread_away = request.json.get(
        "second_half_juice_spread_away", None)
    second_half_juice_spread_home = request.json.get(
        "second_half_juice_spread_home", None)
    second_half_moneyLineAway = request.json.get(
        "second_half_moneyLineAway", None)
    second_half_moneyLineHome = request.json.get(
        "second_half_moneyLineHome", None)
    second_half_total = request.json.get("second_half_total", None)
    sh_juice_total_over = request.json.get("sh_juice_total_over", None)
    sh_juice_total_under = request.json.get("sh_juice_total_under", None)
    second_half_tt_away = request.json.get("second_half_tt_away", None)
    second_half_juice_over_away = request.json.get(
        "second_half_juice_over_away", None)
    second_half_juice_under_away = request.json.get(
        "second_half_juice_under_away", None)
    second_half_tt_home = request.json.get("second_half_tt_home", None)
    second_half_juice_over_home = request.json.get(
        "second_half_juice_over_home", None)
    second_half_juice_under_home = request.json.get(
        "second_half_juice_under_home", None)
    second_half_final_score_away = request.json.get(
        "second_half_final_score_away", None)
    second_half_final_score_home = request.json.get(
        "second_half_final_score_home", None)
    # ------
    q1_half_spread_away = request.json.get("q1_half_spread_away", None)
    q1_half_spread_home = request.json.get("q1_half_spread_home", None)
    q1_half_juice_spread_away = request.json.get(
        "q1_half_juice_spread_away", None)
    q1_half_juice_spread_home = request.json.get(
        "q1_half_juice_spread_home", None)
    q1_half_moneyLineAway = request.json.get("q1_half_moneyLineAway", None)
    q1_half_moneyLineHome = request.json.get("q1_half_moneyLineHome", None)
    q1_half_total = request.json.get("q1_half_total", None)
    q1_juice_over = request.json.get("q1_juice_over", None)
    q1_juice_under = request.json.get("q1_juice_under", None)
    q1_half_tt_away = request.json.get("q1_half_tt_away", None)
    q1_half_juice_over_away = request.json.get("q1_half_juice_over_away", None)
    q1_half_juice_under_away = request.json.get(
        "q1_half_juice_under_away", None)
    q1_half_tt_home = request.json.get("q1_half_tt_home", None)
    q1_half_juice_over_home = request.json.get("q1_half_juice_over_home", None)
    q1_half_juice_under_home = request.json.get(
        "q1_half_juice_under_home", None)
    q1_half_final_score_away = request.json.get(
        "q1_half_final_score_away", None)
    q1_half_final_score_home = request.json.get(
        "q1_half_final_score_home", None)
    # --------
    q2_half_spread_away = request.json.get("q2_half_spread_away", None)
    q2_half_spread_home = request.json.get("q2_half_spread_home", None)
    q2_half_juice_spread_away = request.json.get(
        "q2_half_juice_spread_away", None)
    q2_half_juice_spread_home = request.json.get(
        "q2_half_juice_spread_home", None)
    q2_half_moneyLineAway = request.json.get("q2_half_moneyLineAway", None)
    q2_half_moneyLineHome = request.json.get("q2_half_moneyLineHome", None)
    q2_half_total = request.json.get("q2_half_total", None)
    q2_juice_over = request.json.get("q2_juice_over", None)
    q2_juice_under = request.json.get("q2_juice_under", None)
    q2_half_tt_away = request.json.get("q2_half_tt_away", None)
    q2_half_juice_over_away = request.json.get("q2_half_juice_over_away", None)
    q2_half_juice_under_away = request.json.get(
        "q2_half_juice_under_away", None)
    q2_half_tt_home = request.json.get("q2_half_tt_home", None)
    q2_half_juice_over_home = request.json.get("q2_half_juice_over_home", None)
    q2_half_juice_under_home = request.json.get(
        "q2_half_juice_under_home", None)
    q2_half_final_score_away = request.json.get(
        "q2_half_final_score_away", None)
    q2_half_final_score_home = request.json.get(
        "q2_half_final_score_home", None)
    # --------------
    q3_half_spread_away = request.json.get("q3_half_spread_away", None)
    q3_half_spread_home = request.json.get("q3_half_spread_home", None)
    q3_half_juice_spread_away = request.json.get(
        "q3_half_juice_spread_away", None)
    q3_half_juice_spread_home = request.json.get(
        "q3_half_juice_spread_home", None)
    q3_half_moneyLineAway = request.json.get("q3_half_moneyLineAway", None)
    q3_half_moneyLineHome = request.json.get("q3_half_moneyLineHome", None)
    q3_half_total = request.json.get("q3_half_total", None)
    q3_juice_over = request.json.get("q3_juice_over", None)
    q3_juice_under = request.json.get("q3_juice_under", None)
    q3_half_tt_away = request.json.get("q3_half_tt_away", None)
    q3_half_juice_over_away = request.json.get("q3_half_juice_over_away", None)
    q3_half_juice_under_away = request.json.get(
        "q3_half_juice_under_away", None)
    q3_half_tt_home = request.json.get("q3_half_tt_home", None)
    q3_half_juice_over_home = request.json.get("q3_half_juice_over_home", None)
    q3_half_juice_under_home = request.json.get(
        "q3_half_juice_under_home", None)
    q3_half_final_score_away = request.json.get(
        "q3_half_final_score_away", None)
    q3_half_final_score_home = request.json.get(
        "q3_half_final_score_home", None)
    # --------------
    q4_half_spread_away = request.json.get("q4_half_spread_away", None)
    q4_half_spread_home = request.json.get("q4_half_spread_home", None)
    q4_half_juice_spread_away = request.json.get(
        "q4_half_juice_spread_away", None)
    q4_half_juice_spread_home = request.json.get(
        "q4_half_juice_spread_home", None)
    q4_half_moneyLineAway = request.json.get("q4_half_moneyLineAway", None)
    q4_half_moneyLineHome = request.json.get("q4_half_moneyLineHome", None)
    q4_half_total = request.json.get("q4_half_total", None)
    q4_juice_over = request.json.get("q4_juice_over", None)
    q4_juice_under = request.json.get("q4_juice_under", None)
    q4_half_tt_away = request.json.get("q4_half_tt_away", None)
    q4_half_juice_over_away = request.json.get("q4_half_juice_over_away", None)
    q4_half_juice_under_away = request.json.get(
        "q4_half_juice_under_away", None)
    q4_half_tt_home = request.json.get("q4_half_tt_home", None)
    q4_half_juice_over_home = request.json.get("q4_half_juice_over_home", None)
    q4_half_juice_under_home = request.json.get(
        "q4_half_juice_under_home", None)
    q4_half_final_score_away = request.json.get(
        "q4_half_final_score_away", None)
    q4_half_final_score_home = request.json.get(
        "q4_half_final_score_home", None)
    # busca mlb en BBDD
    nfl = Nfl.query.filter_by(home=home, away=away, date=date).first()
    # the mlb was not found on the database
    if nfl:
        return jsonify({"msg": "Nfl game already exists", "status": nfl.status}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        nfl = Nfl(
            date=date,
            hour=hour,
            week=week,
            status=status,
            casino=casino,
            rotation_away=rotation_away,
            rotation_home=rotation_home,
            away=away,
            home=home,
            spread_away=spread_away,
            spread_home=spread_home,
            juice_spread_away=juice_spread_away,
            juice_spread_home=juice_spread_home,
            moneyLineAway=moneyLineAway,
            moneyLineHome=moneyLineHome,
            total=total,
            juice_total_over=juice_total_over,
            juice_total_under=juice_total_under,
            tt_away=tt_away,
            juice_over_away=juice_over_away,
            juice_under_away=juice_under_away,
            tt_home=tt_home,
            juice_over_home=juice_over_home,
            juice_under_home=juice_under_home,
            final_score_away=final_score_away,
            final_score_home=final_score_home,
            # --
            first_half_spread_away=first_half_spread_away,
            first_half_spread_home=first_half_spread_home,
            first_half_juice_spread_away=first_half_juice_spread_away,
            first_half_juice_spread_home=first_half_juice_spread_home,
            first_half_moneyLineAway=first_half_moneyLineAway,
            first_half_moneyLineHome=first_half_moneyLineHome,
            first_half_total=first_half_total,
            fh_juice_total_over=fh_juice_total_over,
            fh_juice_total_under=fh_juice_total_under,
            first_half_tt_away=first_half_tt_away,
            first_half_juice_over_away=first_half_juice_over_away,
            first_half_juice_under_away=first_half_juice_under_away,
            first_half_tt_home=first_half_tt_home,
            first_half_juice_over_home=first_half_juice_over_home,
            first_half_juice_under_home=first_half_juice_under_home,
            first_half_final_score_away=first_half_final_score_away,
            first_half_final_score_home=first_half_final_score_home,
            # --
            second_half_spread_away=second_half_spread_away,
            second_half_spread_home=second_half_spread_home,
            second_half_juice_spread_away=second_half_juice_spread_away,
            second_half_juice_spread_home=second_half_juice_spread_home,
            second_half_moneyLineAway=second_half_moneyLineAway,
            second_half_moneyLineHome=second_half_moneyLineHome,
            second_half_total=second_half_total,
            sh_juice_total_over=sh_juice_total_over,
            sh_juice_total_under=sh_juice_total_under,
            second_half_tt_away=second_half_tt_away,
            second_half_juice_over_away=second_half_juice_over_away,
            second_half_juice_under_away=second_half_juice_under_away,
            second_half_tt_home=second_half_tt_home,
            second_half_juice_over_home=second_half_juice_over_home,
            second_half_juice_under_home=second_half_juice_under_home,
            second_half_final_score_away=second_half_final_score_away,
            second_half_final_score_home=second_half_final_score_home,
            # --
            q1_half_spread_away=q1_half_spread_away,
            q1_half_spread_home=q1_half_spread_home,
            q1_half_juice_spread_away=q1_half_juice_spread_away,
            q1_half_juice_spread_home=q1_half_juice_spread_home,
            q1_half_moneyLineAway=q1_half_moneyLineAway,
            q1_half_moneyLineHome=q1_half_moneyLineHome,
            q1_half_total=q1_half_total,
            q1_juice_over=q1_juice_over,
            q1_juice_under=q1_juice_under,
            q1_half_tt_away=q1_half_tt_away,
            q1_half_juice_over_away=q1_half_juice_over_away,
            q1_half_juice_under_away=q1_half_juice_under_away,
            q1_half_tt_home=q1_half_tt_home,
            q1_half_juice_over_home=q1_half_juice_over_home,
            q1_half_juice_under_home=q1_half_juice_under_home,
            q1_half_final_score_away=q1_half_final_score_away,
            q1_half_final_score_home=q1_half_final_score_home,
            # ---
            q2_half_spread_away=q2_half_spread_away,
            q2_half_spread_home=q2_half_spread_home,
            q2_half_juice_spread_away=q2_half_juice_spread_away,
            q2_half_juice_spread_home=q2_half_juice_spread_home,
            q2_half_moneyLineAway=q2_half_moneyLineAway,
            q2_half_moneyLineHome=q2_half_moneyLineHome,
            q2_half_total=q2_half_total,
            q2_juice_over=q2_juice_over,
            q2_juice_under=q2_juice_under,
            q2_half_tt_away=q2_half_tt_away,
            q2_half_juice_over_away=q2_half_juice_over_away,
            q2_half_juice_under_away=q2_half_juice_under_away,
            q2_half_tt_home=q2_half_tt_home,
            q2_half_juice_over_home=q2_half_juice_over_home,
            q2_half_juice_under_home=q2_half_juice_under_home,
            q2_half_final_score_away=q2_half_final_score_away,
            q2_half_final_score_home=q2_half_final_score_home,
            # ---
            q3_half_spread_away=q3_half_spread_away,
            q3_half_spread_home=q3_half_spread_home,
            q3_half_juice_spread_away=q3_half_juice_spread_away,
            q3_half_juice_spread_home=q3_half_juice_spread_home,
            q3_half_moneyLineAway=q3_half_moneyLineAway,
            q3_half_moneyLineHome=q3_half_moneyLineHome,
            q3_half_total=q3_half_total,
            q3_juice_over=q3_juice_over,
            q3_juice_under=q3_juice_under,
            q3_half_tt_away=q3_half_tt_away,
            q3_half_juice_over_away=q3_half_juice_over_away,
            q3_half_juice_under_away=q3_half_juice_under_away,
            q3_half_tt_home=q3_half_tt_home,
            q3_half_juice_over_home=q3_half_juice_over_home,
            q3_half_juice_under_home=q3_half_juice_under_home,
            q3_half_final_score_away=q3_half_final_score_away,
            q3_half_final_score_home=q3_half_final_score_home,
            # ---
            q4_half_spread_away=q4_half_spread_away,
            q4_half_spread_home=q4_half_spread_home,
            q4_half_juice_spread_away=q4_half_juice_spread_away,
            q4_half_juice_spread_home=q4_half_juice_spread_home,
            q4_half_moneyLineAway=q4_half_moneyLineAway,
            q4_half_moneyLineHome=q4_half_moneyLineHome,
            q4_half_total=q4_half_total,
            q4_juice_over=q4_juice_over,
            q4_juice_under=q4_juice_under,
            q4_half_tt_away=q4_half_tt_away,
            q4_half_juice_over_away=q4_half_juice_over_away,
            q4_half_juice_under_away=q4_half_juice_under_away,
            q4_half_tt_home=q4_half_tt_home,
            q4_half_juice_over_home=q4_half_juice_over_home,
            q4_half_juice_under_home=q4_half_juice_under_home,
            q4_half_final_score_away=q4_half_final_score_away,
            q4_half_final_score_home=q4_half_final_score_home
        )
        db.session.add(nfl)
        db.session.commit()
        return jsonify({"msg": "Game created successfully"}), 200


@app.route('/boxeo', methods=['POST'])
def createBoxFight():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    week = request.json.get("week", None)
    status = request.json.get("status", None)
    event = request.json.get("event", None)
    rounds = request.json.get("rounds", None)
    location_Fight = request.json.get("location_Fight", None)
    fighter_One = request.json.get("fighter_One", None)
    money_Line_One = request.json.get("money_Line_One", None)
    fighter_Two = request.json.get("fighter_Two", None)
    money_Line_Two = request.json.get("money_Line_Two", None)
    winner = request.json.get("winner", None)
    finish_by = request.json.get("finish_by", None)
    r1_result = request.json.get("r1_result", None)
    r2_result = request.json.get("r2_result", None)
    r3_result = request.json.get("r3_result", None)
    r4_result = request.json.get("r4_result", None)
    r5_result = request.json.get("r5_result", None)
    r6_result = request.json.get("r6_result", None)
    r7_result = request.json.get("r7_result", None)
    r8_result = request.json.get("r8_result", None)
    r9_result = request.json.get("r9_result", None)
    r10_result = request.json.get("r10_result", None)
    r11_result = request.json.get("r11_result", None)
    r12_result = request.json.get("r12_result", None)
    r13_result = request.json.get("r13_result", None)
    r14_result = request.json.get("r14_result", None)
    r15_result = request.json.get("moneyLineHome_1Q", None)

    # busca mlb en BBDD
    boxeo = Boxeo.query.filter_by(
        fighter_One=fighter_One, fighter_Two=fighter_Two, date=date).first()
    # the mlb was not found on the database
    if boxeo:
        return jsonify({"msg": "Pelea de Box already exists", "status": boxeo.event}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        boxeo = Boxeo(
            date=date,
            hour=hour,
            week=week,
            status=status,
            event=event,
            rounds=rounds,
            location_Fight=location_Fight,
            fighter_One=fighter_One,
            money_Line_One=money_Line_One,
            fighter_Two=fighter_Two,
            money_Line_Two=money_Line_Two,
            winner=winner,
            finish_by=finish_by,
            r1_result=r1_result,
            r2_result=r2_result,
            r3_result=r3_result,
            r4_result=r4_result,
            r5_result=r5_result,
            r6_result=r6_result,
            r7_result=r7_result,
            r8_result=r8_result,
            r9_result=r9_result,
            r10_result=r10_result,
            r11_result=r11_result,
            r12_result=r12_result,
            r13_result=r13_result,
            r14_result=r14_result,
            r15_result=r15_result
        )
        db.session.add(boxeo)
        db.session.commit()
        return jsonify({"msg": "Fight created successfully"}), 200


@app.route('/mma', methods=['POST'])
def createMmaFight():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    week = request.json.get("week", None)
    status = request.json.get("status", None)
    event = request.json.get("event", None)
    rounds = request.json.get("rounds", None)
    location_Fight = request.json.get("location_Fight", None)
    fighter_One = request.json.get("fighter_One", None)
    money_Line_One = request.json.get("money_Line_One", None)
    fighter_Two = request.json.get("fighter_Two", None)
    money_Line_Two = request.json.get("money_Line_Two", None)
    winner = request.json.get("winner", None)
    finish_by = request.json.get("finish_by", None)
    r1_result = request.json.get("r1_result", None)
    r2_result = request.json.get("r2_result", None)
    r3_result = request.json.get("r3_result", None)
    r4_result = request.json.get("r4_result", None)
    r5_result = request.json.get("r5_result", None)
    r6_result = request.json.get("r6_result", None)
    r7_result = request.json.get("r7_result", None)
    r8_result = request.json.get("r8_result", None)
    r9_result = request.json.get("r9_result", None)
    r10_result = request.json.get("r10_result", None)
    r11_result = request.json.get("r11_result", None)
    r12_result = request.json.get("r12_result", None)
    r13_result = request.json.get("r13_result", None)
    r14_result = request.json.get("r14_result", None)
    r15_result = request.json.get("moneyLineHome_1Q", None)

    # busca mlb en BBDD
    mma = Mma.query.filter_by(fighter_One=fighter_One,
                              fighter_Two=fighter_Two, date=date).first()
    # the mlb was not found on the database
    if mma:
        return jsonify({"msg": "Pelea de Box already exists", "status": mma.event}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        mma = Mma(
            date=date,
            hour=hour,
            week=week,
            status=status,
            event=event,
            rounds=rounds,
            location_Fight=location_Fight,
            fighter_One=fighter_One,
            money_Line_One=money_Line_One,
            fighter_Two=fighter_Two,
            money_Line_Two=money_Line_Two,
            winner=winner,
            finish_by=finish_by,
            r1_result=r1_result,
            r2_result=r2_result,
            r3_result=r3_result,
            r4_result=r4_result,
            r5_result=r5_result,
            r6_result=r6_result,
            r7_result=r7_result,
            r8_result=r8_result,
            r9_result=r9_result,
            r10_result=r10_result,
            r11_result=r11_result,
            r12_result=r12_result,
            r13_result=r13_result,
            r14_result=r14_result,
            r15_result=r15_result
        )
        db.session.add(mma)
        db.session.commit()
        return jsonify({"msg": "Fight created successfully"}), 200


@app.route('/nascar', methods=['POST'])
def createNacarRun():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    week = request.json.get("week", None)
    status = request.json.get("status", None)
    race = request.json.get("race", None)
    track = request.json.get("track", None)
    rounds = request.json.get("rounds", None)
    country = request.json.get("country", None)
    location = request.json.get("location", None)
    place1 = request.json.get("place1", None)
    place2 = request.json.get("place2", None)
    place3 = request.json.get("place3", None)

    # busca mlb en BBDD
    nascar = Nascar.query.filter_by(
        race=race, place1=place1, date=date).first()
    # the mlb was not found on the database
    if nascar:
        return jsonify({"msg": "Pelea de Box already exists", "status": nascar.event}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        nascar = Nascar(
            date=date,
            hour=hour,
            week=week,
            status=status,
            race=race,
            track=track,
            country=country,
            location=location,
            place1=place1,
            place2=place2,
            place3=place3,
        )
        db.session.add(nascar)
        db.session.commit()
        return jsonify({"msg": "Fight created successfully"}), 200


@app.route('/nascar_drivers', methods=['POST'])
def createNacarDrivers():
    name = request.json.get("name", None)
    country = request.json.get("country", None)
    birth = request.json.get("birth", None)
    sponsor = request.json.get("sponsor", None)
    engine = request.json.get("engine", None)
    number_car = request.json.get("number_car", None)
    rank = request.json.get("rank", None)
    starts = request.json.get("starts", None)
    poles = request.json.get("poles", None)
    top5 = request.json.get("top5", None)
    top10 = request.json.get("top10", None)
    laps_lead = request.json.get("laps_lead", None)
    pts = request.json.get("pts", None)
    AVG_laps = request.json.get("AVG_laps", None)
    AVG_finish = request.json.get("AVG_finish", None)

    # busca mlb en BBDD
    nascar_drivers = Nascar_drivers.query.filter_by(
        engine=engine, number_car=number_car, name=name).first()
    # the mlb was not found on the database
    if nascar_drivers:
        return jsonify({"msg": "Nascar Driver already exists", "name": nascar_drivers.name}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        nascar_drivers = Nascar_drivers(
            name=name,
            country=country,
            birth=birth,
            sponsor=sponsor,
            engine=engine,
            number_car=number_car,
            rank=rank,
            poles=poles,
            top5=top5,
            top10=top10,
            laps_lead=laps_lead,
            pts=pts,
            AVG_laps=AVG_laps,
            AVG_finish=AVG_finish,
        )
        db.session.add(nascar_drivers)
        db.session.commit()
        return jsonify({"msg": "Nascar Driver created successfully"}), 200


@app.route('/match_ups_nascar', methods=['POST'])
def createNacarMatch():
    name1 = request.json.get("name1", None)
    mu1 = request.json.get("mu1", None)
    name2 = request.json.get("name2", None)
    mu2 = request.json.get("mu2", None)

    # busca mlb en BBDD
    match_ups_nascar = Match_Ups_Nacar.query.filter_by(
        name1=name1, name2=name2).first()
    # the mlb was not found on the database
    if match_ups_nascar:
        return jsonify({"msg": "Nascar Driver already exists", "name1": match_ups_nascar.name1}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        match_ups_nascar = Match_Ups_Nacar(
            name1=name1,
            mu1=mu1,
            name2=name2,
            mu2=mu2,
        )
        db.session.add(match_ups_nascar)
        db.session.commit()
        return jsonify({"msg": "Nascar Driver created successfully"}), 200


@app.route('/golf', methods=['POST'])
def createGolfMatch():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    week = request.json.get("week", None)
    status = request.json.get("status", None)
    event = request.json.get("event", None)
    location = request.json.get("location", None)
    place1 = request.json.get("place1", None)
    place2 = request.json.get("place2", None)
    place3 = request.json.get("place3", None)

    # busca mlb en BBDD
    golf = Golf.query.filter_by(
        date=date, event=event).first()
    # the mlb was not found on the database
    if golf:
        return jsonify({"msg": "Nascar Driver already exists", "name1": golf.event}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        golf = Golf(
            date=date,
            hour=hour,
            week=week,
            status=status,
            event=event,
            location=location,
            place1=place1,
            place2=place2,
            place3=place3,
        )
        db.session.add(golf)
        db.session.commit()
        return jsonify({"msg": "Nascar Driver created successfully"}), 200


@app.route('/golfer', methods=['POST'])
def createGoler():
    name = request.json.get("name", None)
    country = request.json.get("country", None)
    swing = request.json.get("swing", None)
    birth = request.json.get("birth", None)
    cuts = request.json.get("cuts", None)
    top10 = request.json.get("top10", None)
    w = request.json.get("w", None)
    rnds = request.json.get("rnds", None)
    holes = request.json.get("holes", None)
    avg = request.json.get("avg", None)

    # busca mlb en BBDD
    golfer = Golfer.query.filter_by(name=name, birth=birth).first()
    # the mlb was not found on the database
    if golfer:
        return jsonify({"msg": "Nascar Driver already exists", "name1": golfer.cuts}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        golfer = Golfer(
            name=name,
            country=country,
            swing=swing,
            birth=birth,
            cuts=cuts,
            top10=top10,
            w=w,
            rnds=rnds,
            holes=holes,
            avg=avg
        )
        db.session.add(golfer)
        db.session.commit()
        return jsonify({"msg": "Nascar Driver created successfully"}), 200


@app.route('/ncaa_basketball', methods=['POST'])
def createGameNcaaBasket():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    status = request.json.get("status", None)
    away = request.json.get("away", None)
    home = request.json.get("home", None)
    spread_away = request.json.get("spread_away", None)
    spread_home = request.json.get("spread_home", None)
    juice_spread_away = request.json.get("juice_spread_away", None)
    juice_spread_home = request.json.get("juice_spread_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)
    # --------------------------------------------------------------
    first_half_spread_away = request.json.get("first_half_spread_away", None)
    first_half_spread_home = request.json.get("first_half_spread_home", None)
    first_half_juice_spread_away = request.json.get(
        "first_half_juice_spread_away", None)
    first_half_juice_spread_home = request.json.get(
        "first_half_juice_spread_home", None)
    first_half_moneyLineAway = request.json.get(
        "first_half_moneyLineAway", None)
    first_half_moneyLineHome = request.json.get(
        "first_half_moneyLineHome", None)
    first_half_total = request.json.get("first_half_total", None)
    fh_juice_over = request.json.get("fh_juice_over", None)
    fh_juice_under = request.json.get("fh_juice_under", None)
    first_half_tt_away = request.json.get("first_half_tt_away", None)
    first_half_juice_over_away = request.json.get(
        "first_half_juice_over_away", None)
    first_half_juice_under_away = request.json.get(
        "first_half_juice_under_away", None)
    first_half_tt_home = request.json.get("first_half_tt_home", None)
    first_half_juice_over_home = request.json.get(
        "first_half_juice_over_home", None)
    first_half_juice_under_home = request.json.get(
        "first_half_juice_under_home", None)
    first_half_final_score_away = request.json.get(
        "first_half_final_score_away", None)
    first_half_final_score_home = request.json.get(
        "first_half_final_score_home", None)
    second_half_spread_away = request.json.get("second_half_spread_away", None)
    second_half_spread_home = request.json.get("second_half_spread_home", None)
    second_half_juice_spread_away = request.json.get(
        "second_half_juice_spread_away", None)
    second_half_juice_spread_home = request.json.get(
        "second_half_juice_spread_home", None)
    second_half_moneyLineAway = request.json.get(
        "second_half_moneyLineAway", None)
    second_half_moneyLineHome = request.json.get(
        "second_half_moneyLineHome", None)
    second_half_total = request.json.get("sa_4inning", None)
    sh_juice_over = request.json.get("sh_juice_over", None)
    sh_juice_under = request.json.get("sh_juice_under", None)
    second_half_tt_away = request.json.get("second_half_tt_away", None)
    second_half_juice_over_away = request.json.get(
        "second_half_juice_over_away", None)
    second_half_juice_under_away = request.json.get(
        "second_half_juice_under_away", None)
    second_half_tt_home = request.json.get("second_half_tt_home", None)
    second_half_juice_over_home = request.json.get(
        "second_half_juice_over_home", None)
    second_half_juice_under_home = request.json.get(
        "second_half_juice_under_home", None)
    second_half_final_score_away = request.json.get(
        "second_half_final_score_away", None)
    second_half_final_score_home = request.json.get(
        "second_half_final_score_home", None)
    q1_half_spread_away = request.json.get("q1_half_spread_away", None)
    q1_half_spread_home = request.json.get("q1_half_spread_home", None)
    q1_half_juice_spread_away = request.json.get(
        "q1_half_juice_spread_away", None)
    q1_half_juice_spread_home = request.json.get(
        "q1_half_juice_spread_home", None)
    q1_half_moneyLineAway = request.json.get("q1_half_moneyLineAway", None)
    q1_half_moneyLineHome = request.json.get("q1_half_moneyLineHome", None)
    q1_half_total = request.json.get("q1_half_total", None)
    q1_juice_over = request.json.get("q1_juice_over", None)
    q1_juice_under = request.json.get("q1_juice_under", None)
    q1_half_tt_away = request.json.get("q1_half_tt_away", None)
    q1_half_juice_over_away = request.json.get("q1_half_juice_over_away", None)
    q1_half_juice_under_away = request.json.get(
        "q1_half_juice_under_away", None)
    q1_half_tt_home = request.json.get("q1_half_tt_home", None)
    q1_half_juice_over_home = request.json.get("q1_half_juice_over_home", None)
    q1_half_juice_under_home = request.json.get(
        "q1_half_juice_under_home", None)
    q1_half_final_score_away = request.json.get(
        "q1_half_final_score_away", None)
    q1_half_final_score_home = request.json.get(
        "q1_half_final_score_home", None)

    # busca mlb en BBDD
    ncaa_basketball = Ncaa_basketball.query.filter_by(
        home=home, away=away, date=date).first()
    # the mlb was not found on the database
    if ncaa_basketball:
        return jsonify({"msg": "Mlb already exists", "status": ncaa_basketball.status}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        ncaa_basketball = Ncaa_basketball(
            date=date,
            hour=hour,
            status=status,
            away=away,
            home=home,
            spread_away=spread_away,
            spread_home=spread_home,
            juice_spread_away=juice_spread_away,
            juice_spread_home=juice_spread_home,
            moneyLineAway=moneyLineAway,
            moneyLineHome=moneyLineHome,
            total=total,
            juice_total_over=juice_total_over,
            juice_total_under=juice_total_under,
            tt_away=tt_away,
            juice_over_away=juice_over_away,
            juice_under_away=juice_under_away,
            tt_home=tt_home,
            juice_over_home=juice_over_home,
            juice_under_home=juice_under_home,
            final_score_away=final_score_away,
            final_score_home=final_score_home,
            first_half_spread_away=first_half_spread_away,
            first_half_spread_home=first_half_spread_home,
            first_half_juice_spread_away=first_half_juice_spread_away,
            first_half_juice_spread_home=first_half_juice_spread_home,
            first_half_moneyLineAway=first_half_moneyLineAway,
            first_half_moneyLineHome=first_half_moneyLineHome,
            first_half_total=first_half_total,
            fh_juice_over=fh_juice_over,
            fh_juice_under=fh_juice_under,
            first_half_tt_away=first_half_tt_away,
            first_half_juice_over_away=first_half_juice_over_away, first_half_juice_under_away=first_half_juice_under_away, first_half_tt_home=first_half_tt_home, first_half_juice_over_home=first_half_juice_over_home,
            first_half_juice_under_home=first_half_juice_under_home,
            first_half_final_score_away=first_half_final_score_away,
            first_half_final_score_home=first_half_final_score_home, second_half_spread_away=second_half_spread_away,
            second_half_spread_home=second_half_spread_home,
            second_half_juice_spread_away=second_half_juice_spread_away,
            second_half_juice_spread_home=second_half_juice_spread_home,
            second_half_moneyLineAway=second_half_moneyLineAway,
            second_half_moneyLineHome=second_half_moneyLineHome,
            second_half_total=second_half_total,
            sh_juice_over=sh_juice_over,
            sh_juice_under=sh_juice_under,
            second_half_tt_away=second_half_tt_away,
            second_half_juice_over_away=second_half_juice_over_away,
            second_half_juice_under_away=second_half_juice_under_away,
            second_half_tt_home=second_half_tt_home,
            second_half_juice_over_home=second_half_juice_over_home,
            second_half_juice_under_home=second_half_juice_under_home,
            second_half_final_score_away=second_half_final_score_away,
            second_half_final_score_home=second_half_final_score_home,
            q1_half_spread_away=q1_half_spread_away,
            q1_half_spread_home=q1_half_spread_home,
            q1_half_juice_spread_away=q1_half_juice_spread_away,
            q1_half_juice_spread_home=q1_half_juice_spread_home,
            q1_half_moneyLineAway=q1_half_moneyLineAway,
            q1_half_moneyLineHome=q1_half_moneyLineHome,
            q1_half_total=q1_half_total,
            q1_juice_over=q1_juice_over,
            q1_juice_under=q1_juice_under,
            q1_half_tt_away=q1_half_tt_away,
            q1_half_juice_over_away=q1_half_juice_over_away,
            q1_half_juice_under_away=q1_half_juice_under_away,
            q1_half_tt_home=q1_half_tt_home,
            q1_half_juice_over_home=q1_half_juice_over_home,
            q1_half_juice_under_home=q1_half_juice_under_home,
            q1_half_final_score_away=q1_half_final_score_away,
            q1_half_final_score_home=q1_half_final_score_home
        )
        db.session.add(ncaa_basketball)
        db.session.commit()
        return jsonify({"msg": "Game created successfully"}), 200


@app.route('/ncaa_baseball', methods=['POST'])
def createGameNcaaBaseBall():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    status = request.json.get("status", None)
    away = request.json.get("away", None)
    pitcher_a = request.json.get("pitcher_a", None)
    home = request.json.get("home", None)
    pitcher_h = request.json.get("pitcher_h", None)
    rl_away = request.json.get("rl_away", None)
    rl_home = request.json.get("rl_home", None)
    juice_rl_away = request.json.get("juice_rl_away", None)
    juice_rl_home = request.json.get("juice_rl_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)
    # --------------------------------------------------------------
    rl_away_f5 = request.json.get("rl_away_f5", None)
    rl_home_f5 = request.json.get("rl_home_f5", None)
    juice_rl_away_f5 = request.json.get("juice_rl_away_f5", None)
    juice_rl_home_f5 = request.json.get("juice_rl_home_f5", None)
    moneyLineAway_f5 = request.json.get("moneyLineAway_f5", None)
    moneyLineHome_f5 = request.json.get("moneyLineHome_f5", None)
    total_f5 = request.json.get("total_f5", None)
    juice_total_over_f5 = request.json.get("juice_total_over_f5", None)
    juice_total_under_f5 = request.json.get("juice_total_under_f5", None)
    tt_away_f5 = request.json.get("tt_away_f5", None)
    juice_over_away_f5 = request.json.get("juice_over_away_f5", None)
    juice_under_away_f5 = request.json.get("juice_under_away_f5", None)
    juice_over_home_f5 = request.json.get("juice_over_home_f5", None)
    juice_under_home_f5 = request.json.get("juice_under_home_f5", None)
    fs_away_f5 = request.json.get("fs_away_f5", None)
    fs_home_f5 = request.json.get("fs_home_f5", None)
    sa_1inning = request.json.get("sa_1inning", None)
    sh_1inning = request.json.get("sh_1inning", None)
    sa_2inning = request.json.get("sa_2inning", None)
    sh_2inning = request.json.get("sh_2inning", None)
    sa_3inning = request.json.get("sa_3inning", None)
    sh_3inning = request.json.get("sh_3inning", None)
    sa_4inning = request.json.get("sa_4inning", None)
    sh_4inning = request.json.get("sh_4inning", None)
    sa_5inning = request.json.get("sa_5inning", None)
    sh_5inning = request.json.get("sh_5inning", None)
    sa_6inning = request.json.get("sa_6inning", None)
    sh_6inning = request.json.get("sh_6inning", None)
    sa_7inning = request.json.get("sa_7inning", None)
    sh_7inning = request.json.get("sh_7inning", None)
    sa_8inning = request.json.get("sa_8inning", None)
    sh_8inning = request.json.get("sh_8inning", None)
    sa_9inning = request.json.get("sa_9inning", None)
    sh_9inning = request.json.get("sh_9inning", None)
    sa_10inning = request.json.get("sa_10inning", None)
    sh_10inning = request.json.get("sh_10inning", None)
    sa_11inning = request.json.get("sa_11inning", None)
    sh_11inning = request.json.get("sh_11inning", None)
    sa_12inning = request.json.get("sa_12inning", None)
    sh_12inning = request.json.get("sh_12inning", None)
    sa_13inning = request.json.get("sa_13inning", None)
    sh_13inning = request.json.get("sh_13inning", None)
    sa_14inning = request.json.get("sa_14inning", None)
    sh_14inning = request.json.get("sh_14inning", None)
    sa_15inning = request.json.get("sa_15inning", None)
    sh_15inning = request.json.get("sh_15inning", None)
    sa_16inning = request.json.get("sa_16inning", None)
    sh_16inning = request.json.get("sh_16inning", None)
    sa_17inning = request.json.get("sa_17inning", None)
    sh_17inning = request.json.get("sh_17inning", None)
    sa_18inning = request.json.get("sa_18inning", None)
    sh_18inning = request.json.get("sh_18inning", None)
    sa_19inning = request.json.get("sa_19inning", None)
    sh_19inning = request.json.get("sh_19inning", None)
    sa_20inning = request.json.get("sa_20inning", None)
    sh_20inning = request.json.get("sh_20inning", None)
    sa_21inning = request.json.get("sa_21inning", None)
    sh_21inning = request.json.get("sh_21inning", None)
    sa_22inning = request.json.get("sa_22inning", None)
    sh_22inning = request.json.get("sh_22inning", None)
    sa_23inning = request.json.get("sa_23inning", None)
    sh_23inning = request.json.get("sh_23inning", None)
    sa_24inning = request.json.get("sa_24inning", None)
    sh_24inning = request.json.get("sh_24inning", None)
    sa_25inning = request.json.get("sa_25inning", None)
    sh_25inning = request.json.get("sh_25inning", None)

    # busca mlb en BBDD
    ncaa_baseball = Ncaa_baseball.query.filter_by(
        home=home, away=away, date=date).first()
    # the ncaa_baseball was not found on the database
    if ncaa_baseball:
        return jsonify({"msg": "ncaa_baseball already exists", "status": ncaa_baseball.status}), 401
    else:
        # crea ncaa_baseball nuevo
        # crea registro nuevo en BBDD de
        ncaa_baseball = Ncaa_baseball(
            date=date, hour=hour, status=status, away=away, pitcher_a=pitcher_a, home=home, pitcher_h=pitcher_h,
            rl_away=rl_away, rl_home=rl_home, juice_rl_away=juice_rl_away, juice_rl_home=juice_rl_home, moneyLineAway=moneyLineAway, moneyLineHome=moneyLineHome, total=total, juice_total_over=juice_total_over, juice_total_under=juice_total_under, tt_away=tt_away, juice_over_away=juice_over_away, juice_under_away=juice_under_away, tt_home=tt_home, juice_over_home=juice_over_home, juice_under_home=juice_under_home, final_score_away=final_score_away, final_score_home=final_score_home, rl_away_f5=rl_away_f5, rl_home_f5=rl_home_f5, juice_rl_away_f5=juice_rl_away_f5, juice_rl_home_f5=juice_rl_home_f5, moneyLineAway_f5=moneyLineAway_f5, moneyLineHome_f5=moneyLineHome_f5, total_f5=total_f5, juice_total_over_f5=juice_total_over_f5, juice_total_under_f5=juice_total_under_f5, tt_away_f5=tt_away_f5, juice_over_away_f5=juice_over_away_f5, juice_under_away_f5=juice_under_away_f5, juice_over_home_f5=juice_over_home_f5, juice_under_home_f5=juice_under_home_f5, fs_away_f5=fs_away_f5, fs_home_f5=fs_home_f5, sa_1inning=sa_1inning, sh_1inning=sh_1inning, sa_2inning=sa_2inning, sh_2inning=sh_2inning, sa_3inning=sa_3inning, sh_3inning=sh_3inning, sa_4inning=sa_4inning, sh_4inning=sh_4inning, sa_5inning=sa_5inning, sh_5inning=sh_5inning, sa_6inning=sa_6inning, sh_6inning=sh_6inning, sa_7inning=sa_7inning, sh_7inning=sh_7inning, sa_8inning=sa_8inning, sh_8inning=sh_8inning, sa_9inning=sa_9inning, sh_9inning=sh_9inning, sa_10inning=sa_10inning, sh_10inning=sh_10inning, sa_11inning=sa_11inning, sh_11inning=sh_11inning, sa_12inning=sa_12inning, sh_12inning=sh_12inning, sa_13inning=sa_13inning, sh_13inning=sh_13inning, sa_14inning=sa_14inning, sh_14inning=sh_14inning, sa_15inning=sa_15inning, sh_15inning=sh_15inning, sa_16inning=sa_16inning, sh_16inning=sh_16inning, sa_17inning=sa_17inning, sa_18inning=sa_18inning, sa_19inning=sa_19inning, sa_20inning=sa_20inning, sa_21inning=sa_21inning, sa_22inning=sa_22inning, sa_23inning=sa_23inning, sa_24inning=sa_24inning, sa_25inning=sa_25inning)
        db.session.add(ncaa_baseball)
        db.session.commit()
        return jsonify({"msg": "User created successfully"}), 200


@app.route('/ncaa_football', methods=['POST'])
def createGameNcaa_football():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    week = request.json.get("week", None)
    status = request.json.get("status", None)
    away = request.json.get("away", None)
    home = request.json.get("home", None)
    spread_away = request.json.get("spread_away", None)
    spread_home = request.json.get("spread_home", None)
    juice_spread_away = request.json.get("juice_spread_away", None)
    juice_spread_home = request.json.get("juice_spread_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)
    # --------------------------------------------------------------
    first_half_spread_away = request.json.get("first_half_spread_away", None)
    first_half_spread_home = request.json.get("first_half_spread_home", None)
    first_half_juice_spread_away = request.json.get(
        "first_half_juice_spread_away", None)
    first_half_juice_spread_home = request.json.get(
        "first_half_juice_spread_home", None)
    first_half_moneyLineAway = request.json.get(
        "first_half_moneyLineAway", None)
    first_half_moneyLineHome = request.json.get(
        "first_half_moneyLineHome", None)
    first_half_total = request.json.get("first_half_total", None)
    fh_juice_total_over = request.json.get("fh_juice_total_over", None)
    fh_juice_total_under = request.json.get("fh_juice_total_under", None)
    first_half_tt_away = request.json.get("first_half_tt_away", None)
    first_half_juice_over_away = request.json.get(
        "first_half_juice_over_away", None)
    first_half_juice_under_away = request.json.get(
        "first_half_juice_under_away", None)
    first_half_tt_home = request.json.get("first_half_tt_home", None)
    first_half_juice_over_home = request.json.get(
        "first_half_juice_over_home", None)
    first_half_juice_under_home = request.json.get(
        "first_half_juice_under_home", None)
    first_half_final_score_away = request.json.get(
        "first_half_final_score_away", None)
    first_half_final_score_home = request.json.get(
        "first_half_final_score_home", None)
    # --------------
    second_half_spread_away = request.json.get("second_half_spread_away", None)
    second_half_spread_home = request.json.get("second_half_spread_home", None)
    second_half_juice_spread_away = request.json.get(
        "second_half_juice_spread_away", None)
    second_half_juice_spread_home = request.json.get(
        "second_half_juice_spread_home", None)
    second_half_moneyLineAway = request.json.get(
        "second_half_moneyLineAway", None)
    second_half_moneyLineHome = request.json.get(
        "second_half_moneyLineHome", None)
    second_half_total = request.json.get("second_half_total", None)
    sh_juice_total_over = request.json.get("sh_juice_total_over", None)
    sh_juice_total_under = request.json.get("sh_juice_total_under", None)
    second_half_tt_away = request.json.get("second_half_tt_away", None)
    second_half_juice_over_away = request.json.get(
        "second_half_juice_over_away", None)
    second_half_juice_under_away = request.json.get(
        "second_half_juice_under_away", None)
    second_half_tt_home = request.json.get("second_half_tt_home", None)
    second_half_juice_over_home = request.json.get(
        "second_half_juice_over_home", None)
    second_half_juice_under_home = request.json.get(
        "second_half_juice_under_home", None)
    second_half_final_score_away = request.json.get(
        "second_half_final_score_away", None)
    second_half_final_score_home = request.json.get(
        "second_half_final_score_home", None)
    # ------
    q1_half_spread_away = request.json.get("q1_half_spread_away", None)
    q1_half_spread_home = request.json.get("q1_half_spread_home", None)
    q1_half_juice_spread_away = request.json.get(
        "q1_half_juice_spread_away", None)
    q1_half_juice_spread_home = request.json.get(
        "q1_half_juice_spread_home", None)
    q1_half_moneyLineAway = request.json.get("q1_half_moneyLineAway", None)
    q1_half_moneyLineHome = request.json.get("q1_half_moneyLineHome", None)
    q1_half_total = request.json.get("q1_half_total", None)
    q1_juice_over = request.json.get("q1_juice_over", None)
    q1_juice_under = request.json.get("q1_juice_under", None)
    q1_half_tt_away = request.json.get("q1_half_tt_away", None)
    q1_half_juice_over_away = request.json.get("q1_half_juice_over_away", None)
    q1_half_juice_under_away = request.json.get(
        "q1_half_juice_under_away", None)
    q1_half_tt_home = request.json.get("q1_half_tt_home", None)
    q1_half_juice_over_home = request.json.get("q1_half_juice_over_home", None)
    q1_half_juice_under_home = request.json.get(
        "q1_half_juice_under_home", None)
    q1_half_final_score_away = request.json.get(
        "q1_half_final_score_away", None)
    q1_half_final_score_home = request.json.get(
        "q1_half_final_score_home", None)

    # busca mlb en BBDD
    ncaa_football = Ncaa_Football.query.filter_by(
        home=home, away=away, date=date).first()
    # the mlb was not found on the database
    if ncaa_football:
        return jsonify({"msg": "Ncaa_Football game already exists", "status": ncaa_football.status}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        ncaa_football = Ncaa_Football(
            date=date,
            hour=hour,
            week=week,
            status=status,
            away=away,
            home=home,
            spread_away=spread_away,
            spread_home=spread_home,
            juice_spread_away=juice_spread_away,
            juice_spread_home=juice_spread_home,
            moneyLineAway=moneyLineAway,
            moneyLineHome=moneyLineHome,
            total=total,
            juice_total_over=juice_total_over,
            juice_total_under=juice_total_under,
            tt_away=tt_away,
            juice_over_away=juice_over_away,
            juice_under_away=juice_under_away,
            tt_home=tt_home,
            juice_over_home=juice_over_home,
            juice_under_home=juice_under_home,
            final_score_away=final_score_away,
            final_score_home=final_score_home,
            # --
            first_half_spread_away=first_half_spread_away,
            first_half_spread_home=first_half_spread_home,
            first_half_juice_spread_away=first_half_juice_spread_away,
            first_half_juice_spread_home=first_half_juice_spread_home,
            first_half_moneyLineAway=first_half_moneyLineAway,
            first_half_moneyLineHome=first_half_moneyLineHome,
            first_half_total=first_half_total,
            fh_juice_total_over=fh_juice_total_over,
            fh_juice_total_under=fh_juice_total_under,
            first_half_tt_away=first_half_tt_away,
            first_half_juice_over_away=first_half_juice_over_away,
            first_half_juice_under_away=first_half_juice_under_away,
            first_half_tt_home=first_half_tt_home,
            first_half_juice_over_home=first_half_juice_over_home,
            first_half_juice_under_home=first_half_juice_under_home,
            first_half_final_score_away=first_half_final_score_away,
            first_half_final_score_home=first_half_final_score_home,
            # --
            second_half_spread_away=second_half_spread_away,
            second_half_spread_home=second_half_spread_home,
            second_half_juice_spread_away=second_half_juice_spread_away,
            second_half_juice_spread_home=second_half_juice_spread_home,
            second_half_moneyLineAway=second_half_moneyLineAway,
            second_half_moneyLineHome=second_half_moneyLineHome,
            second_half_total=second_half_total,
            sh_juice_total_over=sh_juice_total_over,
            sh_juice_total_under=sh_juice_total_under,
            second_half_tt_away=second_half_tt_away,
            second_half_juice_over_away=second_half_juice_over_away,
            second_half_juice_under_away=second_half_juice_under_away,
            second_half_tt_home=second_half_tt_home,
            second_half_juice_over_home=second_half_juice_over_home,
            second_half_juice_under_home=second_half_juice_under_home,
            second_half_final_score_away=second_half_final_score_away,
            second_half_final_score_home=second_half_final_score_home,
            # --
            q1_half_spread_away=q1_half_spread_away,
            q1_half_spread_home=q1_half_spread_home,
            q1_half_juice_spread_away=q1_half_juice_spread_away,
            q1_half_juice_spread_home=q1_half_juice_spread_home,
            q1_half_moneyLineAway=q1_half_moneyLineAway,
            q1_half_moneyLineHome=q1_half_moneyLineHome,
            q1_half_total=q1_half_total,
            q1_juice_over=q1_juice_over,
            q1_juice_under=q1_juice_under,
            q1_half_tt_away=q1_half_tt_away,
            q1_half_juice_over_away=q1_half_juice_over_away,
            q1_half_juice_under_away=q1_half_juice_under_away,
            q1_half_tt_home=q1_half_tt_home,
            q1_half_juice_over_home=q1_half_juice_over_home,
            q1_half_juice_under_home=q1_half_juice_under_home,
            q1_half_final_score_away=q1_half_final_score_away,
            q1_half_final_score_home=q1_half_final_score_home
        )

        db.session.add(ncaa_football)
        db.session.commit()
        return jsonify({"msg": "Game created successfully"}), 200


@app.route('/confederations_cup', methods=['POST'])
def createConfederations_cup():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    status = request.json.get("status", None)
    away = request.json.get("away", None)
    home = request.json.get("home", None)
    goal_line_away = request.json.get("goal_line_away", None)
    goal_line_home = request.json.get("goal_line_home", None)
    juice_goal_away = request.json.get("juice_goal_away", None)
    juice_goal_home = request.json.get("juice_goal_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)

    # --------------------------------------------------------------
    goal_away_1H = request.json.get("goal_away_1H", None)
    goal_home_1H = request.json.get("goal_home_1H", None)
    juice_goal_away_1H = request.json.get("juice_goal_away_1H", None)
    juice_goal_home_1H = request.json.get("juice_goal_home_1H", None)
    moneyLineAway_1H = request.json.get("moneyLineAway_1H", None)
    moneyLineHome_1H = request.json.get("moneyLineHome_1H", None)
    total_1H = request.json.get("total_1H", None)
    H1_juice_over = request.json.get("H1_juice_over", None)
    H1_juice_under = request.json.get("H1_juice_under", None)
    tt_away_1H = request.json.get("tt_away_1H", None)
    juice_over_away_1H = request.json.get("juice_over_away_1H", None)
    juice_under_away_1H = request.json.get("juice_under_away_1H", None)
    tt_home_1H = request.json.get("tt_home_1H", None)
    juice_over_home_1H = request.json.get("juice_over_home_1H", None)
    juice_under_home_1H = request.json.get("juice_under_home_1H", None)

    # busca mlb en BBDD
    confederations_cup = Confederations_cup.query.filter_by(
        home=home, away=away, date=date).first()
    # the mlb was not found on the database
    if confederations_cup:
        return jsonify({"msg": "confederations_cup already exists", "team away": confederations_cup.away, "team home": confederations_cup.home}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        confederations_cup = Confederations_cup(
            date=date,
            hour=hour,
            status=status,
            away=away,
            home=home,
            goal_line_away=goal_line_away,
            goal_line_home=goal_line_home,
            juice_goal_away=juice_goal_away,
            juice_goal_home=juice_goal_home,
            moneyLineAway=moneyLineAway,
            moneyLineHome=moneyLineHome,
            total=total,
            juice_total_over=juice_total_over,
            juice_total_under=juice_total_under,
            tt_away=tt_away,
            juice_over_away=juice_over_away,
            juice_under_away=juice_under_away,
            tt_home=tt_home,
            juice_over_home=juice_over_home,
            juice_under_home=juice_under_home,
            final_score_away=final_score_away,
            final_score_home=final_score_home,

            goal_away_1H=goal_away_1H,
            goal_home_1H=goal_home_1H,
            juice_puck_away_1H=juice_puck_away_1H,
            juice_puck_home_1H=juice_puck_home_1H,
            moneyLineAway_1H=moneyLineAway_1H,
            moneyLineHome_1H=moneyLineHome_1H,
            total_1H=total_1H,
            H1_juice_over=H1_juice_over,
            H1_juice_under=H1_juice_under,
            tt_away_1H=tt_away_1H,
            juice_over_away_1H=juice_over_away_1H,
            juice_under_away_1H=juice_under_away_1H,
            tt_home_1H=tt_home_1H,
            juice_over_home_1H=juice_over_home_1H,
            juice_under_home_1H=juice_under_home_1H
        )
        db.session.add(confederations_cup)
        db.session.commit()
        return jsonify({"msg": "Game Confederations Cup created successfully"}), 200


@app.route('/champions_league', methods=['POST'])
def createChampions_league():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    status = request.json.get("status", None)
    away = request.json.get("away", None)
    home = request.json.get("home", None)
    goal_line_away = request.json.get("goal_line_away", None)
    goal_line_home = request.json.get("goal_line_home", None)
    juice_goal_away = request.json.get("juice_goal_away", None)
    juice_goal_home = request.json.get("juice_goal_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)

    # --------------------------------------------------------------
    goal_away_1H = request.json.get("goal_away_1H", None)
    goal_home_1H = request.json.get("goal_home_1H", None)
    juice_goal_away_1H = request.json.get("juice_goal_away_1H", None)
    juice_goal_home_1H = request.json.get("juice_goal_home_1H", None)
    moneyLineAway_1H = request.json.get("moneyLineAway_1H", None)
    moneyLineHome_1H = request.json.get("moneyLineHome_1H", None)
    total_1H = request.json.get("total_1H", None)
    H1_juice_over = request.json.get("H1_juice_over", None)
    H1_juice_under = request.json.get("H1_juice_under", None)
    tt_away_1H = request.json.get("tt_away_1H", None)
    juice_over_away_1H = request.json.get("juice_over_away_1H", None)
    juice_under_away_1H = request.json.get("juice_under_away_1H", None)
    tt_home_1H = request.json.get("tt_home_1H", None)
    juice_over_home_1H = request.json.get("juice_over_home_1H", None)
    juice_under_home_1H = request.json.get("juice_under_home_1H", None)

    # busca mlb en BBDD
    champions_league = Champions_league.query.filter_by(
        home=home, away=away, date=date).first()
    # the mlb was not found on the database
    if champions_league:
        return jsonify({"msg": "champions_league already exists", "team away": champions_league.away, "team home": champions_league.home}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        champions_league = Champions_league(
            date=date,
            hour=hour,
            status=status,
            away=away,
            home=home,
            goal_line_away=goal_line_away,
            goal_line_home=goal_line_home,
            juice_goal_away=juice_goal_away,
            juice_goal_home=juice_goal_home,
            moneyLineAway=moneyLineAway,
            moneyLineHome=moneyLineHome,
            total=total,
            juice_total_over=juice_total_over,
            juice_total_under=juice_total_under,
            tt_away=tt_away,
            juice_over_away=juice_over_away,
            juice_under_away=juice_under_away,
            tt_home=tt_home,
            juice_over_home=juice_over_home,
            juice_under_home=juice_under_home,
            final_score_away=final_score_away,
            final_score_home=final_score_home,

            goal_away_1H=goal_away_1H,
            goal_home_1H=goal_home_1H,
            moneyLineAway_1H=moneyLineAway_1H,
            moneyLineHome_1H=moneyLineHome_1H,
            total_1H=total_1H,
            H1_juice_over=H1_juice_over,
            H1_juice_under=H1_juice_under,
            tt_away_1H=tt_away_1H,
            juice_over_away_1H=juice_over_away_1H,
            juice_under_away_1H=juice_under_away_1H,
            tt_home_1H=tt_home_1H,
            juice_over_home_1H=juice_over_home_1H,
            juice_under_home_1H=juice_under_home_1H
        )
        db.session.add(champions_league)
        db.session.commit()
        return jsonify({"msg": "Game Confederations Cup created successfully"}), 200


@app.route('/w_c_qualifying', methods=['POST'])
def createW_C_qualifying():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    status = request.json.get("status", None)
    away = request.json.get("away", None)
    home = request.json.get("home", None)
    goal_line_away = request.json.get("goal_line_away", None)
    goal_line_home = request.json.get("goal_line_home", None)
    juice_goal_away = request.json.get("juice_goal_away", None)
    juice_goal_home = request.json.get("juice_goal_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)

    # --------------------------------------------------------------
    goal_away_1H = request.json.get("goal_away_1H", None)
    goal_home_1H = request.json.get("goal_home_1H", None)
    juice_goal_away_1H = request.json.get("juice_goal_away_1H", None)
    juice_goal_home_1H = request.json.get("juice_goal_home_1H", None)
    moneyLineAway_1H = request.json.get("moneyLineAway_1H", None)
    moneyLineHome_1H = request.json.get("moneyLineHome_1H", None)
    total_1H = request.json.get("total_1H", None)
    H1_juice_over = request.json.get("H1_juice_over", None)
    H1_juice_under = request.json.get("H1_juice_under", None)
    tt_away_1H = request.json.get("tt_away_1H", None)
    juice_over_away_1H = request.json.get("juice_over_away_1H", None)
    juice_under_away_1H = request.json.get("juice_under_away_1H", None)
    tt_home_1H = request.json.get("tt_home_1H", None)
    juice_over_home_1H = request.json.get("juice_over_home_1H", None)
    juice_under_home_1H = request.json.get("juice_under_home_1H", None)

    # busca team en BBDD
    w_c_qualifying = W_C_Qualifying.query.filter_by(
        home=home, away=away, date=date).first()
    # the team was not found on the database
    if w_c_qualifying:
        return jsonify({"msg": "w_c_qualifying already exists", "team away": w_c_qualifying.away, "team home": w_c_qualifying.home}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        w_c_qualifying = W_C_Qualifying(
            date=date,
            hour=hour,
            status=status,
            away=away,
            home=home,
            goal_line_away=goal_line_away,
            goal_line_home=goal_line_home,
            juice_goal_away=juice_goal_away,
            juice_goal_home=juice_goal_home,
            moneyLineAway=moneyLineAway,
            moneyLineHome=moneyLineHome,
            total=total,
            juice_total_over=juice_total_over,
            juice_total_under=juice_total_under,
            tt_away=tt_away,
            juice_over_away=juice_over_away,
            juice_under_away=juice_under_away,
            tt_home=tt_home,
            juice_over_home=juice_over_home,
            juice_under_home=juice_under_home,
            final_score_away=final_score_away,
            final_score_home=final_score_home,

            goal_away_1H=goal_away_1H,
            goal_home_1H=goal_home_1H,
            juice_puck_away_1H=juice_puck_away_1H,
            juice_puck_home_1H=juice_puck_home_1H,
            moneyLineAway_1H=moneyLineAway_1H,
            moneyLineHome_1H=moneyLineHome_1H,
            total_1H=total_1H,
            H1_juice_over=H1_juice_over,
            H1_juice_under=H1_juice_under,
            tt_away_1H=tt_away_1H,
            juice_over_away_1H=juice_over_away_1H,
            juice_under_away_1H=juice_under_away_1H,
            tt_home_1H=tt_home_1H,
            juice_over_home_1H=juice_over_home_1H,
            juice_under_home_1H=juice_under_home_1H
        )
        db.session.add(w_c_qualifying)
        db.session.commit()
        return jsonify({"msg": "Game W C Hualifying  created successfully"}), 200


@app.route('/CONCACAF', methods=['POST'])
def createCONCACAF():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    status = request.json.get("status", None)
    away = request.json.get("away", None)
    home = request.json.get("home", None)
    goal_line_away = request.json.get("goal_line_away", None)
    goal_line_home = request.json.get("goal_line_home", None)
    juice_goal_away = request.json.get("juice_goal_away", None)
    juice_goal_home = request.json.get("juice_goal_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)

    # --------------------------------------------------------------
    goal_away_1H = request.json.get("goal_away_1H", None)
    goal_home_1H = request.json.get("goal_home_1H", None)
    juice_goal_away_1H = request.json.get("juice_goal_away_1H", None)
    juice_goal_home_1H = request.json.get("juice_goal_home_1H", None)
    moneyLineAway_1H = request.json.get("moneyLineAway_1H", None)
    moneyLineHome_1H = request.json.get("moneyLineHome_1H", None)
    total_1H = request.json.get("total_1H", None)
    H1_juice_over = request.json.get("H1_juice_over", None)
    H1_juice_under = request.json.get("H1_juice_under", None)
    tt_away_1H = request.json.get("tt_away_1H", None)
    juice_over_away_1H = request.json.get("juice_over_away_1H", None)
    juice_under_away_1H = request.json.get("juice_under_away_1H", None)
    tt_home_1H = request.json.get("tt_home_1H", None)
    juice_over_home_1H = request.json.get("juice_over_home_1H", None)
    juice_under_home_1H = request.json.get("juice_under_home_1H", None)

    # busca team en BBDD
    CONCACAF = CONCACAF.query.filter_by(
        home=home, away=away, date=date).first()
    # the team was not found on the database
    if CONCACAF:
        return jsonify({"msg": "CONCACAF already exists", "team away": CONCACAF.away, "team home": CONCACAF.home}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        CONCACAF = CONCACAF(
            date=date,
            hour=hour,
            status=status,
            away=away,
            home=home,
            goal_line_away=goal_line_away,
            goal_line_home=goal_line_home,
            juice_goal_away=juice_goal_away,
            juice_goal_home=juice_goal_home,
            moneyLineAway=moneyLineAway,
            moneyLineHome=moneyLineHome,
            total=total,
            juice_total_over=juice_total_over,
            juice_total_under=juice_total_under,
            tt_away=tt_away,
            juice_over_away=juice_over_away,
            juice_under_away=juice_under_away,
            tt_home=tt_home,
            juice_over_home=juice_over_home,
            juice_under_home=juice_under_home,
            final_score_away=final_score_away,
            final_score_home=final_score_home,

            goal_away_1H=goal_away_1H,
            goal_home_1H=goal_home_1H,
            juice_puck_away_1H=juice_puck_away_1H,
            juice_puck_home_1H=juice_puck_home_1H,
            moneyLineAway_1H=moneyLineAway_1H,
            moneyLineHome_1H=moneyLineHome_1H,
            total_1H=total_1H,
            H1_juice_over=H1_juice_over,
            H1_juice_under=H1_juice_under,
            tt_away_1H=tt_away_1H,
            juice_over_away_1H=juice_over_away_1H,
            juice_under_away_1H=juice_under_away_1H,
            tt_home_1H=tt_home_1H,
            juice_over_home_1H=juice_over_home_1H,
            juice_under_home_1H=juice_under_home_1H
        )
        db.session.add(CONCACAF)
        db.session.commit()
        return jsonify({"msg": "Game CONCACAF created successfully"}), 200


@app.route('/england_premier_league', methods=['POST'])
def createEngland_premier_league():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    status = request.json.get("status", None)
    away = request.json.get("away", None)
    home = request.json.get("home", None)
    goal_line_away = request.json.get("goal_line_away", None)
    goal_line_home = request.json.get("goal_line_home", None)
    juice_goal_away = request.json.get("juice_goal_away", None)
    juice_goal_home = request.json.get("juice_goal_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)

    # --------------------------------------------------------------
    goal_away_1H = request.json.get("goal_away_1H", None)
    goal_home_1H = request.json.get("goal_home_1H", None)
    juice_goal_away_1H = request.json.get("juice_goal_away_1H", None)
    juice_goal_home_1H = request.json.get("juice_goal_home_1H", None)
    moneyLineAway_1H = request.json.get("moneyLineAway_1H", None)
    moneyLineHome_1H = request.json.get("moneyLineHome_1H", None)
    total_1H = request.json.get("total_1H", None)
    H1_juice_over = request.json.get("H1_juice_over", None)
    H1_juice_under = request.json.get("H1_juice_under", None)
    tt_away_1H = request.json.get("tt_away_1H", None)
    juice_over_away_1H = request.json.get("juice_over_away_1H", None)
    juice_under_away_1H = request.json.get("juice_under_away_1H", None)
    tt_home_1H = request.json.get("tt_home_1H", None)
    juice_over_home_1H = request.json.get("juice_over_home_1H", None)
    juice_under_home_1H = request.json.get("juice_under_home_1H", None)

    # busca team en BBDD
    england_premier_league = England_premier_league.query.filter_by(
        home=home, away=away, date=date).first()
    # the team was not found on the database
    if england_premier_league:
        return jsonify({"msg": "england_premier_league already exists", "team away": england_premier_league.away, "team home": england_premier_league.home}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        england_premier_league = England_premier_league(
            date=date,
            hour=hour,
            status=status,
            away=away,
            home=home,
            goal_line_away=goal_line_away,
            goal_line_home=goal_line_home,
            juice_goal_away=juice_goal_away,
            juice_goal_home=juice_goal_home,
            moneyLineAway=moneyLineAway,
            moneyLineHome=moneyLineHome,
            total=total,
            juice_total_over=juice_total_over,
            juice_total_under=juice_total_under,
            tt_away=tt_away,
            juice_over_away=juice_over_away,
            juice_under_away=juice_under_away,
            tt_home=tt_home,
            juice_over_home=juice_over_home,
            juice_under_home=juice_under_home,
            final_score_away=final_score_away,
            final_score_home=final_score_home,

            goal_away_1H=goal_away_1H,
            goal_home_1H=goal_home_1H,
            juice_puck_away_1H=juice_puck_away_1H,
            juice_puck_home_1H=juice_puck_home_1H,
            moneyLineAway_1H=moneyLineAway_1H,
            moneyLineHome_1H=moneyLineHome_1H,
            total_1H=total_1H,
            H1_juice_over=H1_juice_over,
            H1_juice_under=H1_juice_under,
            tt_away_1H=tt_away_1H,
            juice_over_away_1H=juice_over_away_1H,
            juice_under_away_1H=juice_under_away_1H,
            tt_home_1H=tt_home_1H,
            juice_over_home_1H=juice_over_home_1H,
            juice_under_home_1H=juice_under_home_1H
        )
        db.session.add(england_premier_league)
        db.session.commit()
        return jsonify({"msg": "Game england_premier_league created successfully"}), 200


@app.route('/europa_league', methods=['POST'])
def createEuropa_league():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    status = request.json.get("status", None)
    away = request.json.get("away", None)
    home = request.json.get("home", None)
    goal_line_away = request.json.get("goal_line_away", None)
    goal_line_home = request.json.get("goal_line_home", None)
    juice_goal_away = request.json.get("juice_goal_away", None)
    juice_goal_home = request.json.get("juice_goal_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)

    # --------------------------------------------------------------
    goal_away_1H = request.json.get("goal_away_1H", None)
    goal_home_1H = request.json.get("goal_home_1H", None)
    juice_goal_away_1H = request.json.get("juice_goal_away_1H", None)
    juice_goal_home_1H = request.json.get("juice_goal_home_1H", None)
    moneyLineAway_1H = request.json.get("moneyLineAway_1H", None)
    moneyLineHome_1H = request.json.get("moneyLineHome_1H", None)
    total_1H = request.json.get("total_1H", None)
    H1_juice_over = request.json.get("H1_juice_over", None)
    H1_juice_under = request.json.get("H1_juice_under", None)
    tt_away_1H = request.json.get("tt_away_1H", None)
    juice_over_away_1H = request.json.get("juice_over_away_1H", None)
    juice_under_away_1H = request.json.get("juice_under_away_1H", None)
    tt_home_1H = request.json.get("tt_home_1H", None)
    juice_over_home_1H = request.json.get("juice_over_home_1H", None)
    juice_under_home_1H = request.json.get("juice_under_home_1H", None)

    # busca team en BBDD
    europa_league = Europa_League.query.filter_by(
        home=home, away=away, date=date).first()
    # the team was not found on the database
    if europa_league:
        return jsonify({"msg": "europa_league already exists", "team away": europa_league.away, "team home": europa_league.home}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        europa_league = Europa_League(
            date=date,
            hour=hour,
            status=status,
            away=away,
            home=home,
            goal_line_away=goal_line_away,
            goal_line_home=goal_line_home,
            juice_goal_away=juice_goal_away,
            juice_goal_home=juice_goal_home,
            moneyLineAway=moneyLineAway,
            moneyLineHome=moneyLineHome,
            total=total,
            juice_total_over=juice_total_over,
            juice_total_under=juice_total_under,
            tt_away=tt_away,
            juice_over_away=juice_over_away,
            juice_under_away=juice_under_away,
            tt_home=tt_home,
            juice_over_home=juice_over_home,
            juice_under_home=juice_under_home,
            final_score_away=final_score_away,
            final_score_home=final_score_home,

            goal_away_1H=goal_away_1H,
            goal_home_1H=goal_home_1H,
            juice_puck_away_1H=juice_puck_away_1H,
            juice_puck_home_1H=juice_puck_home_1H,
            moneyLineAway_1H=moneyLineAway_1H,
            moneyLineHome_1H=moneyLineHome_1H,
            total_1H=total_1H,
            H1_juice_over=H1_juice_over,
            H1_juice_under=H1_juice_under,
            tt_away_1H=tt_away_1H,
            juice_over_away_1H=juice_over_away_1H,
            juice_under_away_1H=juice_under_away_1H,
            tt_home_1H=tt_home_1H,
            juice_over_home_1H=juice_over_home_1H,
            juice_under_home_1H=juice_under_home_1H
        )
        db.session.add(europa_league)
        db.session.commit()
        return jsonify({"msg": "Game europa_league created successfully"}), 200


@app.route('/international_friendlies', methods=['POST'])
def createInternational_friendlies():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    status = request.json.get("status", None)
    away = request.json.get("away", None)
    home = request.json.get("home", None)
    goal_line_away = request.json.get("goal_line_away", None)
    goal_line_home = request.json.get("goal_line_home", None)
    juice_goal_away = request.json.get("juice_goal_away", None)
    juice_goal_home = request.json.get("juice_goal_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)

    # --------------------------------------------------------------
    goal_away_1H = request.json.get("goal_away_1H", None)
    goal_home_1H = request.json.get("goal_home_1H", None)
    juice_goal_away_1H = request.json.get("juice_goal_away_1H", None)
    juice_goal_home_1H = request.json.get("juice_goal_home_1H", None)
    moneyLineAway_1H = request.json.get("moneyLineAway_1H", None)
    moneyLineHome_1H = request.json.get("moneyLineHome_1H", None)
    total_1H = request.json.get("total_1H", None)
    H1_juice_over = request.json.get("H1_juice_over", None)
    H1_juice_under = request.json.get("H1_juice_under", None)
    tt_away_1H = request.json.get("tt_away_1H", None)
    juice_over_away_1H = request.json.get("juice_over_away_1H", None)
    juice_under_away_1H = request.json.get("juice_under_away_1H", None)
    tt_home_1H = request.json.get("tt_home_1H", None)
    juice_over_home_1H = request.json.get("juice_over_home_1H", None)
    juice_under_home_1H = request.json.get("juice_under_home_1H", None)
    # busca team en BBDD
    international_friendlies = International_Friendlies.query.filter_by(
        home=home, away=away, date=date).first()
    # the team was not found on the database
    if international_friendlies:
        return jsonify({"msg": "international_friendlies already exists", "team away": international_friendlies.away, "team home": international_friendlies.home}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        international_friendlies = International_Friendlies(
            date=date,
            hour=hour,
            status=status,
            away=away,
            home=home,
            goal_line_away=goal_line_away,
            goal_line_home=goal_line_home,
            juice_goal_away=juice_goal_away,
            juice_goal_home=juice_goal_home,
            moneyLineAway=moneyLineAway,
            moneyLineHome=moneyLineHome,
            total=total,
            juice_total_over=juice_total_over,
            juice_total_under=juice_total_under,
            tt_away=tt_away,
            juice_over_away=juice_over_away,
            juice_under_away=juice_under_away,
            tt_home=tt_home,
            juice_over_home=juice_over_home,
            juice_under_home=juice_under_home,
            final_score_away=final_score_away,
            final_score_home=final_score_home,

            goal_away_1H=goal_away_1H,
            goal_home_1H=goal_home_1H,
            juice_puck_away_1H=juice_puck_away_1H,
            juice_puck_home_1H=juice_puck_home_1H,
            moneyLineAway_1H=moneyLineAway_1H,
            moneyLineHome_1H=moneyLineHome_1H,
            total_1H=total_1H,
            H1_juice_over=H1_juice_over,
            H1_juice_under=H1_juice_under,
            tt_away_1H=tt_away_1H,
            juice_over_away_1H=juice_over_away_1H,
            juice_under_away_1H=juice_under_away_1H,
            tt_home_1H=tt_home_1H,
            juice_over_home_1H=juice_over_home_1H,
            juice_under_home_1H=juice_under_home_1H
        )
        db.session.add(international_friendlies)
        db.session.commit()
        return jsonify({"msg": "Game international_friendlies created successfully"}), 200


@app.route('/france_league', methods=['POST'])
def createFrance_league():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    status = request.json.get("status", None)
    away = request.json.get("away", None)
    home = request.json.get("home", None)
    goal_line_away = request.json.get("goal_line_away", None)
    goal_line_home = request.json.get("goal_line_home", None)
    juice_goal_away = request.json.get("juice_goal_away", None)
    juice_goal_home = request.json.get("juice_goal_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)

    # --------------------------------------------------------------
    goal_away_1H = request.json.get("goal_away_1H", None)
    goal_home_1H = request.json.get("goal_home_1H", None)
    juice_goal_away_1H = request.json.get("juice_goal_away_1H", None)
    juice_goal_home_1H = request.json.get("juice_goal_home_1H", None)
    moneyLineAway_1H = request.json.get("moneyLineAway_1H", None)
    moneyLineHome_1H = request.json.get("moneyLineHome_1H", None)
    total_1H = request.json.get("total_1H", None)
    H1_juice_over = request.json.get("H1_juice_over", None)
    H1_juice_under = request.json.get("H1_juice_under", None)
    tt_away_1H = request.json.get("tt_away_1H", None)
    juice_over_away_1H = request.json.get("juice_over_away_1H", None)
    juice_under_away_1H = request.json.get("juice_under_away_1H", None)
    tt_home_1H = request.json.get("tt_home_1H", None)
    juice_over_home_1H = request.json.get("juice_over_home_1H", None)
    juice_under_home_1H = request.json.get("juice_under_home_1H", None)

    # busca team en BBDD
    france_league = France_League.query.filter_by(
        home=home, away=away, date=date).first()
    # the team was not found on the database
    if france_league:
        return jsonify({"msg": "france_league already exists", "team away": france_league.away, "team home": france_league.home}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        france_league = France_League(
            date=date,
            hour=hour,
            status=status,
            away=away,
            home=home,
            goal_line_away=goal_line_away,
            goal_line_home=goal_line_home,
            juice_goal_away=juice_goal_away,
            juice_goal_home=juice_goal_home,
            moneyLineAway=moneyLineAway,
            moneyLineHome=moneyLineHome,
            total=total,
            juice_total_over=juice_total_over,
            juice_total_under=juice_total_under,
            tt_away=tt_away,
            juice_over_away=juice_over_away,
            juice_under_away=juice_under_away,
            tt_home=tt_home,
            juice_over_home=juice_over_home,
            juice_under_home=juice_under_home,
            final_score_away=final_score_away,
            final_score_home=final_score_home,

            goal_away_1H=goal_away_1H,
            goal_home_1H=goal_home_1H,
            juice_puck_away_1H=juice_puck_away_1H,
            juice_puck_home_1H=juice_puck_home_1H,
            moneyLineAway_1H=moneyLineAway_1H,
            moneyLineHome_1H=moneyLineHome_1H,
            total_1H=total_1H,
            H1_juice_over=H1_juice_over,
            H1_juice_under=H1_juice_under,
            tt_away_1H=tt_away_1H,
            juice_over_away_1H=juice_over_away_1H,
            juice_under_away_1H=juice_under_away_1H,
            tt_home_1H=tt_home_1H,
            juice_over_home_1H=juice_over_home_1H,
            juice_under_home_1H=juice_under_home_1H
        )
        db.session.add(france_league)
        db.session.commit()
        return jsonify({"msg": "Game france_league created successfully"}), 200


@app.route('/bundesliga', methods=['POST'])
def createBundesliga():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    status = request.json.get("status", None)
    away = request.json.get("away", None)
    home = request.json.get("home", None)
    goal_line_away = request.json.get("goal_line_away", None)
    goal_line_home = request.json.get("goal_line_home", None)
    juice_goal_away = request.json.get("juice_goal_away", None)
    juice_goal_home = request.json.get("juice_goal_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)

    # --------------------------------------------------------------
    goal_away_1H = request.json.get("goal_away_1H", None)
    goal_home_1H = request.json.get("goal_home_1H", None)
    juice_goal_away_1H = request.json.get("juice_goal_away_1H", None)
    juice_goal_home_1H = request.json.get("juice_goal_home_1H", None)
    moneyLineAway_1H = request.json.get("moneyLineAway_1H", None)
    moneyLineHome_1H = request.json.get("moneyLineHome_1H", None)
    total_1H = request.json.get("total_1H", None)
    H1_juice_over = request.json.get("H1_juice_over", None)
    H1_juice_under = request.json.get("H1_juice_under", None)
    tt_away_1H = request.json.get("tt_away_1H", None)
    juice_over_away_1H = request.json.get("juice_over_away_1H", None)
    juice_under_away_1H = request.json.get("juice_under_away_1H", None)
    tt_home_1H = request.json.get("tt_home_1H", None)
    juice_over_home_1H = request.json.get("juice_over_home_1H", None)
    juice_under_home_1H = request.json.get("juice_under_home_1H", None)

    # busca team en BBDD
    bundesliga = Bundesliga.query.filter_by(
        home=home, away=away, date=date).first()
    # the team was not found on the database
    if bundesliga:
        return jsonify({"msg": "bundesliga already exists", "team away": bundesliga.away, "team home": bundesliga.home}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        bundesliga = Bundesliga(
            date=date,
            hour=hour,
            status=status,
            away=away,
            home=home,
            goal_line_away=goal_line_away,
            goal_line_home=goal_line_home,
            juice_goal_away=juice_goal_away,
            juice_goal_home=juice_goal_home,
            moneyLineAway=moneyLineAway,
            moneyLineHome=moneyLineHome,
            total=total,
            juice_total_over=juice_total_over,
            juice_total_under=juice_total_under,
            tt_away=tt_away,
            juice_over_away=juice_over_away,
            juice_under_away=juice_under_away,
            tt_home=tt_home,
            juice_over_home=juice_over_home,
            juice_under_home=juice_under_home,
            final_score_away=final_score_away,
            final_score_home=final_score_home,

            goal_away_1H=goal_away_1H,
            goal_home_1H=goal_home_1H,
            juice_puck_away_1H=juice_puck_away_1H,
            juice_puck_home_1H=juice_puck_home_1H,
            moneyLineAway_1H=moneyLineAway_1H,
            moneyLineHome_1H=moneyLineHome_1H,
            total_1H=total_1H,
            H1_juice_over=H1_juice_over,
            H1_juice_under=H1_juice_under,
            tt_away_1H=tt_away_1H,
            juice_over_away_1H=juice_over_away_1H,
            juice_under_away_1H=juice_under_away_1H,
            tt_home_1H=tt_home_1H,
            juice_over_home_1H=juice_over_home_1H,
            juice_under_home_1H=juice_under_home_1H
        )
        db.session.add(bundesliga)
        db.session.commit()
        return jsonify({"msg": "Game bundesliga created successfully"}), 200


@app.route('/international_matches', methods=['POST'])
def createInternational_Matches():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    status = request.json.get("status", None)
    away = request.json.get("away", None)
    home = request.json.get("home", None)
    goal_line_away = request.json.get("goal_line_away", None)
    goal_line_home = request.json.get("goal_line_home", None)
    juice_goal_away = request.json.get("juice_goal_away", None)
    juice_goal_home = request.json.get("juice_goal_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)

    # --------------------------------------------------------------
    goal_away_1H = request.json.get("goal_away_1H", None)
    goal_home_1H = request.json.get("goal_home_1H", None)
    juice_goal_away_1H = request.json.get("juice_goal_away_1H", None)
    juice_goal_home_1H = request.json.get("juice_goal_home_1H", None)
    moneyLineAway_1H = request.json.get("moneyLineAway_1H", None)
    moneyLineHome_1H = request.json.get("moneyLineHome_1H", None)
    total_1H = request.json.get("total_1H", None)
    H1_juice_over = request.json.get("H1_juice_over", None)
    H1_juice_under = request.json.get("H1_juice_under", None)
    tt_away_1H = request.json.get("tt_away_1H", None)
    juice_over_away_1H = request.json.get("juice_over_away_1H", None)
    juice_under_away_1H = request.json.get("juice_under_away_1H", None)
    tt_home_1H = request.json.get("tt_home_1H", None)
    juice_over_home_1H = request.json.get("juice_over_home_1H", None)
    juice_under_home_1H = request.json.get("juice_under_home_1H", None)

    # busca team en BBDD
    international_matches = International_Matches.query.filter_by(
        home=home, away=away, date=date).first()
    # the team was not found on the database
    if international_matches:
        return jsonify({"msg": "international_matches already exists", "team away": international_matches.away, "team home": international_matches.home}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        international_matches = International_Matches(
            date=date,
            hour=hour,
            status=status,
            away=away,
            home=home,
            goal_line_away=goal_line_away,
            goal_line_home=goal_line_home,
            juice_goal_away=juice_goal_away,
            juice_goal_home=juice_goal_home,
            moneyLineAway=moneyLineAway,
            moneyLineHome=moneyLineHome,
            total=total,
            juice_total_over=juice_total_over,
            juice_total_under=juice_total_under,
            tt_away=tt_away,
            juice_over_away=juice_over_away,
            juice_under_away=juice_under_away,
            tt_home=tt_home,
            juice_over_home=juice_over_home,
            juice_under_home=juice_under_home,
            final_score_away=final_score_away,
            final_score_home=final_score_home,

            goal_away_1H=goal_away_1H,
            goal_home_1H=goal_home_1H,
            juice_puck_away_1H=juice_puck_away_1H,
            juice_puck_home_1H=juice_puck_home_1H,
            moneyLineAway_1H=moneyLineAway_1H,
            moneyLineHome_1H=moneyLineHome_1H,
            total_1H=total_1H,
            H1_juice_over=H1_juice_over,
            H1_juice_under=H1_juice_under,
            tt_away_1H=tt_away_1H,
            juice_over_away_1H=juice_over_away_1H,
            juice_under_away_1H=juice_under_away_1H,
            tt_home_1H=tt_home_1H,
            juice_over_home_1H=juice_over_home_1H,
            juice_under_home_1H=juice_under_home_1H
        )
        db.session.add(international_matches)
        db.session.commit()
        return jsonify({"msg": "Game international_matches created successfully"}), 200


@app.route('/italia_serie_A', methods=['POST'])
def createItalia_Serie_A():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    status = request.json.get("status", None)
    away = request.json.get("away", None)
    home = request.json.get("home", None)
    goal_line_away = request.json.get("goal_line_away", None)
    goal_line_home = request.json.get("goal_line_home", None)
    juice_goal_away = request.json.get("juice_goal_away", None)
    juice_goal_home = request.json.get("juice_goal_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)

    # --------------------------------------------------------------
    goal_away_1H = request.json.get("goal_away_1H", None)
    goal_home_1H = request.json.get("goal_home_1H", None)
    juice_goal_away_1H = request.json.get("juice_goal_away_1H", None)
    juice_goal_home_1H = request.json.get("juice_goal_home_1H", None)
    moneyLineAway_1H = request.json.get("moneyLineAway_1H", None)
    moneyLineHome_1H = request.json.get("moneyLineHome_1H", None)
    total_1H = request.json.get("total_1H", None)
    H1_juice_over = request.json.get("H1_juice_over", None)
    H1_juice_under = request.json.get("H1_juice_under", None)
    tt_away_1H = request.json.get("tt_away_1H", None)
    juice_over_away_1H = request.json.get("juice_over_away_1H", None)
    juice_under_away_1H = request.json.get("juice_under_away_1H", None)
    tt_home_1H = request.json.get("tt_home_1H", None)
    juice_over_home_1H = request.json.get("juice_over_home_1H", None)
    juice_under_home_1H = request.json.get("juice_under_home_1H", None)

    # busca team en BBDD
    italia_serie_A = Italia_Serie_A.query.filter_by(
        home=home, away=away, date=date).first()
    # the team was not found on the database
    if italia_serie_A:
        return jsonify({"msg": "italia_serie_A already exists", "team away": italia_serie_A.away, "team home": italia_serie_A.home}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        italia_serie_A = Italia_Serie_A(
            date=date,
            hour=hour,
            status=status,
            away=away,
            home=home,
            goal_line_away=goal_line_away,
            goal_line_home=goal_line_home,
            juice_goal_away=juice_goal_away,
            juice_goal_home=juice_goal_home,
            moneyLineAway=moneyLineAway,
            moneyLineHome=moneyLineHome,
            total=total,
            juice_total_over=juice_total_over,
            juice_total_under=juice_total_under,
            tt_away=tt_away,
            juice_over_away=juice_over_away,
            juice_under_away=juice_under_away,
            tt_home=tt_home,
            juice_over_home=juice_over_home,
            juice_under_home=juice_under_home,
            final_score_away=final_score_away,
            final_score_home=final_score_home,

            goal_away_1H=goal_away_1H,
            goal_home_1H=goal_home_1H,
            juice_puck_away_1H=juice_puck_away_1H,
            juice_puck_home_1H=juice_puck_home_1H,
            moneyLineAway_1H=moneyLineAway_1H,
            moneyLineHome_1H=moneyLineHome_1H,
            total_1H=total_1H,
            H1_juice_over=H1_juice_over,
            H1_juice_under=H1_juice_under,
            tt_away_1H=tt_away_1H,
            juice_over_away_1H=juice_over_away_1H,
            juice_under_away_1H=juice_under_away_1H,
            tt_home_1H=tt_home_1H,
            juice_over_home_1H=juice_over_home_1H,
            juice_under_home_1H=juice_under_home_1H
        )
        db.session.add(italia_serie_A)
        db.session.commit()
        return jsonify({"msg": "Game italia_serie_A created successfully"}), 200


@app.route('/mx_expansion', methods=['POST'])
def createMx_expansion():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    status = request.json.get("status", None)
    away = request.json.get("away", None)
    home = request.json.get("home", None)
    goal_line_away = request.json.get("goal_line_away", None)
    goal_line_home = request.json.get("goal_line_home", None)
    juice_goal_away = request.json.get("juice_goal_away", None)
    juice_goal_home = request.json.get("juice_goal_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)

    # --------------------------------------------------------------
    goal_away_1H = request.json.get("goal_away_1H", None)
    goal_home_1H = request.json.get("goal_home_1H", None)
    juice_goal_away_1H = request.json.get("juice_goal_away_1H", None)
    juice_goal_home_1H = request.json.get("juice_goal_home_1H", None)
    moneyLineAway_1H = request.json.get("moneyLineAway_1H", None)
    moneyLineHome_1H = request.json.get("moneyLineHome_1H", None)
    total_1H = request.json.get("total_1H", None)
    H1_juice_over = request.json.get("H1_juice_over", None)
    H1_juice_under = request.json.get("H1_juice_under", None)
    tt_away_1H = request.json.get("tt_away_1H", None)
    juice_over_away_1H = request.json.get("juice_over_away_1H", None)
    juice_under_away_1H = request.json.get("juice_under_away_1H", None)
    tt_home_1H = request.json.get("tt_home_1H", None)
    juice_over_home_1H = request.json.get("juice_over_home_1H", None)
    juice_under_home_1H = request.json.get("juice_under_home_1H", None)

    # busca team en BBDD
    mx_expansion = Mx_Expansion.query.filter_by(
        home=home, away=away, date=date).first()
    # the team was not found on the database
    if mx_expansion:
        return jsonify({"msg": "mx_expansion already exists", "team away": mx_expansion.away, "team home": mx_expansion.home}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        mx_expansion = Mx_Expansion(
            date=date,
            hour=hour,
            status=status,
            away=away,
            home=home,
            goal_line_away=goal_line_away,
            goal_line_home=goal_line_home,
            juice_goal_away=juice_goal_away,
            juice_goal_home=juice_goal_home,
            moneyLineAway=moneyLineAway,
            moneyLineHome=moneyLineHome,
            total=total,
            juice_total_over=juice_total_over,
            juice_total_under=juice_total_under,
            tt_away=tt_away,
            juice_over_away=juice_over_away,
            juice_under_away=juice_under_away,
            tt_home=tt_home,
            juice_over_home=juice_over_home,
            juice_under_home=juice_under_home,
            final_score_away=final_score_away,
            final_score_home=final_score_home,

            goal_away_1H=goal_away_1H,
            goal_home_1H=goal_home_1H,
            juice_puck_away_1H=juice_puck_away_1H,
            juice_puck_home_1H=juice_puck_home_1H,
            moneyLineAway_1H=moneyLineAway_1H,
            moneyLineHome_1H=moneyLineHome_1H,
            total_1H=total_1H,
            H1_juice_over=H1_juice_over,
            H1_juice_under=H1_juice_under,
            tt_away_1H=tt_away_1H,
            juice_over_away_1H=juice_over_away_1H,
            juice_under_away_1H=juice_under_away_1H,
            tt_home_1H=tt_home_1H,
            juice_over_home_1H=juice_over_home_1H,
            juice_under_home_1H=juice_under_home_1H
        )
        db.session.add(mx_expansion)
        db.session.commit()
        return jsonify({"msg": "Game mx_expansion created successfully"}), 200


@app.route('/mx_apertura', methods=['POST'])
def createMx_Apertura():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    status = request.json.get("status", None)
    away = request.json.get("away", None)
    home = request.json.get("home", None)
    goal_line_away = request.json.get("goal_line_away", None)
    goal_line_home = request.json.get("goal_line_home", None)
    juice_goal_away = request.json.get("juice_goal_away", None)
    juice_goal_home = request.json.get("juice_goal_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)

    # --------------------------------------------------------------
    goal_away_1H = request.json.get("goal_away_1H", None)
    goal_home_1H = request.json.get("goal_home_1H", None)
    juice_goal_away_1H = request.json.get("juice_goal_away_1H", None)
    juice_goal_home_1H = request.json.get("juice_goal_home_1H", None)
    moneyLineAway_1H = request.json.get("moneyLineAway_1H", None)
    moneyLineHome_1H = request.json.get("moneyLineHome_1H", None)
    total_1H = request.json.get("total_1H", None)
    H1_juice_over = request.json.get("H1_juice_over", None)
    H1_juice_under = request.json.get("H1_juice_under", None)
    tt_away_1H = request.json.get("tt_away_1H", None)
    juice_over_away_1H = request.json.get("juice_over_away_1H", None)
    juice_under_away_1H = request.json.get("juice_under_away_1H", None)
    tt_home_1H = request.json.get("tt_home_1H", None)
    juice_over_home_1H = request.json.get("juice_over_home_1H", None)
    juice_under_home_1H = request.json.get("juice_under_home_1H", None)
    # busca team en BBDD
    mx_apertura = Mx_Apertura.query.filter_by(
        home=home, away=away, date=date).first()
    # the team was not found on the database
    if mx_apertura:
        return jsonify({"msg": "mx_apertura already exists", "team away": mx_apertura.away, "team home": mx_apertura.home}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        mx_apertura = Mx_Apertura(
            date=date,
            hour=hour,
            status=status,
            away=away,
            home=home,
            goal_line_away=goal_line_away,
            goal_line_home=goal_line_home,
            juice_goal_away=juice_goal_away,
            juice_goal_home=juice_goal_home,
            moneyLineAway=moneyLineAway,
            moneyLineHome=moneyLineHome,
            total=total,
            juice_total_over=juice_total_over,
            juice_total_under=juice_total_under,
            tt_away=tt_away,
            juice_over_away=juice_over_away,
            juice_under_away=juice_under_away,
            tt_home=tt_home,
            juice_over_home=juice_over_home,
            juice_under_home=juice_under_home,
            final_score_away=final_score_away,
            final_score_home=final_score_home,

            goal_away_1H=goal_away_1H,
            goal_home_1H=goal_home_1H,
            juice_puck_away_1H=juice_puck_away_1H,
            juice_puck_home_1H=juice_puck_home_1H,
            moneyLineAway_1H=moneyLineAway_1H,
            moneyLineHome_1H=moneyLineHome_1H,
            total_1H=total_1H,
            H1_juice_over=H1_juice_over,
            H1_juice_under=H1_juice_under,
            tt_away_1H=tt_away_1H,
            juice_over_away_1H=juice_over_away_1H,
            juice_under_away_1H=juice_under_away_1H,
            tt_home_1H=tt_home_1H,
            juice_over_home_1H=juice_over_home_1H,
            juice_under_home_1H=juice_under_home_1H
        )
        db.session.add(mx_apertura)
        db.session.commit()
        return jsonify({"msg": "Game mx_apertura created successfully"}), 200


@app.route('/spain_primera_liga', methods=['POST'])
def createSpain_Primera_Liga():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    status = request.json.get("status", None)
    away = request.json.get("away", None)
    home = request.json.get("home", None)
    goal_line_away = request.json.get("goal_line_away", None)
    goal_line_home = request.json.get("goal_line_home", None)
    juice_goal_away = request.json.get("juice_goal_away", None)
    juice_goal_home = request.json.get("juice_goal_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)

    # --------------------------------------------------------------
    goal_away_1H = request.json.get("goal_away_1H", None)
    goal_home_1H = request.json.get("goal_home_1H", None)
    juice_goal_away_1H = request.json.get("juice_goal_away_1H", None)
    juice_goal_home_1H = request.json.get("juice_goal_home_1H", None)
    moneyLineAway_1H = request.json.get("moneyLineAway_1H", None)
    moneyLineHome_1H = request.json.get("moneyLineHome_1H", None)
    total_1H = request.json.get("total_1H", None)
    H1_juice_over = request.json.get("H1_juice_over", None)
    H1_juice_under = request.json.get("H1_juice_under", None)
    tt_away_1H = request.json.get("tt_away_1H", None)
    juice_over_away_1H = request.json.get("juice_over_away_1H", None)
    juice_under_away_1H = request.json.get("juice_under_away_1H", None)
    tt_home_1H = request.json.get("tt_home_1H", None)
    juice_over_home_1H = request.json.get("juice_over_home_1H", None)
    juice_under_home_1H = request.json.get("juice_under_home_1H", None)

    # busca team en BBDD
    spain_primera_liga = Spain_Primera_Liga.query.filter_by(
        home=home, away=away, date=date).first()
    # the team was not found on the database
    if spain_primera_liga:
        return jsonify({"msg": "spain_primera_liga already exists", "team away": spain_primera_liga.away, "team home": spain_primera_liga.home}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        spain_primera_liga = Spain_Primera_Liga(
            date=date,
            hour=hour,
            status=status,
            away=away,
            home=home,
            goal_line_away=goal_line_away,
            goal_line_home=goal_line_home,
            juice_goal_away=juice_goal_away,
            juice_goal_home=juice_goal_home,
            moneyLineAway=moneyLineAway,
            moneyLineHome=moneyLineHome,
            total=total,
            juice_total_over=juice_total_over,
            juice_total_under=juice_total_under,
            tt_away=tt_away,
            juice_over_away=juice_over_away,
            juice_under_away=juice_under_away,
            tt_home=tt_home,
            juice_over_home=juice_over_home,
            juice_under_home=juice_under_home,
            final_score_away=final_score_away,
            final_score_home=final_score_home,

            goal_away_1H=goal_away_1H,
            goal_home_1H=goal_home_1H,
            juice_puck_away_1H=juice_puck_away_1H,
            juice_puck_home_1H=juice_puck_home_1H,
            moneyLineAway_1H=moneyLineAway_1H,
            moneyLineHome_1H=moneyLineHome_1H,
            total_1H=total_1H,
            H1_juice_over=H1_juice_over,
            H1_juice_under=H1_juice_under,
            tt_away_1H=tt_away_1H,
            juice_over_away_1H=juice_over_away_1H,
            juice_under_away_1H=juice_under_away_1H,
            tt_home_1H=tt_home_1H,
            juice_over_home_1H=juice_over_home_1H,
            juice_under_home_1H=juice_under_home_1H
        )
        db.session.add(spain_primera_liga)
        db.session.commit()
        return jsonify({"msg": "Game spain_primera_liga created successfully"}), 200


@app.route('/USA_MLS', methods=['POST'])
def createUSA_MLS():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    status = request.json.get("status", None)
    away = request.json.get("away", None)
    home = request.json.get("home", None)
    goal_line_away = request.json.get("goal_line_away", None)
    goal_line_home = request.json.get("goal_line_home", None)
    juice_goal_away = request.json.get("juice_goal_away", None)
    juice_goal_home = request.json.get("juice_goal_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)

    # --------------------------------------------------------------
    goal_away_1H = request.json.get("goal_away_1H", None)
    goal_home_1H = request.json.get("goal_home_1H", None)
    juice_goal_away_1H = request.json.get("juice_goal_away_1H", None)
    juice_goal_home_1H = request.json.get("juice_goal_home_1H", None)
    moneyLineAway_1H = request.json.get("moneyLineAway_1H", None)
    moneyLineHome_1H = request.json.get("moneyLineHome_1H", None)
    total_1H = request.json.get("total_1H", None)
    H1_juice_over = request.json.get("H1_juice_over", None)
    H1_juice_under = request.json.get("H1_juice_under", None)
    tt_away_1H = request.json.get("tt_away_1H", None)
    juice_over_away_1H = request.json.get("juice_over_away_1H", None)
    juice_under_away_1H = request.json.get("juice_under_away_1H", None)
    tt_home_1H = request.json.get("tt_home_1H", None)
    juice_over_home_1H = request.json.get("juice_over_home_1H", None)
    juice_under_home_1H = request.json.get("juice_under_home_1H", None)
    # busca team en BBDD
    USA_MLS = USA_MLS.query.filter_by(home=home, away=away, date=date).first()
    # the team was not found on the database
    if USA_MLS:
        return jsonify({"msg": "USA_MLS already exists", "team away": USA_MLS.away, "team home": USA_MLS.home}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        USA_MLS = USA_MLS(date=date,
                          hour=hour,
                          status=status,
                          away=away,
                          home=home,
                          goal_line_away=goal_line_away,
                          goal_line_home=goal_line_home,
                          juice_goal_away=juice_goal_away,
                          juice_goal_home=juice_goal_home,
                          moneyLineAway=moneyLineAway,
                          moneyLineHome=moneyLineHome,
                          total=total,
                          juice_total_over=juice_total_over,
                          juice_total_under=juice_total_under,
                          tt_away=tt_away,
                          juice_over_away=juice_over_away,
                          juice_under_away=juice_under_away,
                          tt_home=tt_home,
                          juice_over_home=juice_over_home,
                          juice_under_home=juice_under_home,
                          final_score_away=final_score_away,
                          final_score_home=final_score_home,

                          goal_away_1H=goal_away_1H,
                          goal_home_1H=goal_home_1H,
                          juice_puck_away_1H=juice_puck_away_1H,
                          juice_puck_home_1H=juice_puck_home_1H,
                          moneyLineAway_1H=moneyLineAway_1H,
                          moneyLineHome_1H=moneyLineHome_1H,
                          total_1H=total_1H,
                          H1_juice_over=H1_juice_over,
                          H1_juice_under=H1_juice_under,
                          tt_away_1H=tt_away_1H,
                          juice_over_away_1H=juice_over_away_1H,
                          juice_under_away_1H=juice_under_away_1H,
                          tt_home_1H=tt_home_1H,
                          juice_over_home_1H=juice_over_home_1H,
                          juice_under_home_1H=juice_under_home_1H
                          )
        db.session.add(USA_MLS)
        db.session.commit()
        return jsonify({"msg": "Game USA_MLS created successfully"}), 200


@app.route('/brazil_serie_A', methods=['POST'])
def createBrazil_Serie_A():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    status = request.json.get("status", None)
    away = request.json.get("away", None)
    home = request.json.get("home", None)
    goal_line_away = request.json.get("goal_line_away", None)
    goal_line_home = request.json.get("goal_line_home", None)
    juice_goal_away = request.json.get("juice_goal_away", None)
    juice_goal_home = request.json.get("juice_goal_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)

    # --------------------------------------------------------------
    goal_away_1H = request.json.get("goal_away_1H", None)
    goal_home_1H = request.json.get("goal_home_1H", None)
    juice_goal_away_1H = request.json.get("juice_goal_away_1H", None)
    juice_goal_home_1H = request.json.get("juice_goal_home_1H", None)
    moneyLineAway_1H = request.json.get("moneyLineAway_1H", None)
    moneyLineHome_1H = request.json.get("moneyLineHome_1H", None)
    total_1H = request.json.get("total_1H", None)
    H1_juice_over = request.json.get("H1_juice_over", None)
    H1_juice_under = request.json.get("H1_juice_under", None)
    tt_away_1H = request.json.get("tt_away_1H", None)
    juice_over_away_1H = request.json.get("juice_over_away_1H", None)
    juice_under_away_1H = request.json.get("juice_under_away_1H", None)
    tt_home_1H = request.json.get("tt_home_1H", None)
    juice_over_home_1H = request.json.get("juice_over_home_1H", None)
    juice_under_home_1H = request.json.get("juice_under_home_1H", None)

    # busca team en BBDD
    brazil_serie_A = Brazil_Serie_A.query.filter_by(
        home=home, away=away, date=date).first()
    # the team was not found on the database
    if brazil_serie_A:
        return jsonify({"msg": "brazil_serie_A already exists", "team away": brazil_serie_A.away, "team home": brazil_serie_A.home}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        brazil_serie_A = Brazil_Serie_A(
            date=date,
            hour=hour,
            status=status,
            away=away,
            home=home,
            goal_line_away=goal_line_away,
            goal_line_home=goal_line_home,
            juice_goal_away=juice_goal_away,
            juice_goal_home=juice_goal_home,
            moneyLineAway=moneyLineAway,
            moneyLineHome=moneyLineHome,
            total=total,
            juice_total_over=juice_total_over,
            juice_total_under=juice_total_under,
            tt_away=tt_away,
            juice_over_away=juice_over_away,
            juice_under_away=juice_under_away,
            tt_home=tt_home,
            juice_over_home=juice_over_home,
            juice_under_home=juice_under_home,
            final_score_away=final_score_away,
            final_score_home=final_score_home,
            goal_away_1H=goal_away_1H,
            goal_home_1H=goal_home_1H,
            juice_puck_away_1H=juice_puck_away_1H,
            juice_puck_home_1H=juice_puck_home_1H,
            moneyLineAway_1H=moneyLineAway_1H,
            moneyLineHome_1H=moneyLineHome_1H,
            total_1H=total_1H,
            H1_juice_over=H1_juice_over,
            H1_juice_under=H1_juice_under,
            tt_away_1H=tt_away_1H,
            juice_over_away_1H=juice_over_away_1H,
            juice_under_away_1H=juice_under_away_1H,
            tt_home_1H=tt_home_1H,
            juice_over_home_1H=juice_over_home_1H,
            juice_under_home_1H=juice_under_home_1H
        )
        db.session.add(brazil_serie_A)
        db.session.commit()
        return jsonify({"msg": "Game brazil_serie_A created successfully"}), 200


@app.route('/colombia_primera_A', methods=['POST'])
def createColombia_Primera_A():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    status = request.json.get("status", None)
    away = request.json.get("away", None)
    home = request.json.get("home", None)
    goal_line_away = request.json.get("goal_line_away", None)
    goal_line_home = request.json.get("goal_line_home", None)
    juice_goal_away = request.json.get("juice_goal_away", None)
    juice_goal_home = request.json.get("juice_goal_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)

    # --------------------------------------------------------------
    goal_away_1H = request.json.get("goal_away_1H", None)
    goal_home_1H = request.json.get("goal_home_1H", None)
    juice_goal_away_1H = request.json.get("juice_goal_away_1H", None)
    juice_goal_home_1H = request.json.get("juice_goal_home_1H", None)
    moneyLineAway_1H = request.json.get("moneyLineAway_1H", None)
    moneyLineHome_1H = request.json.get("moneyLineHome_1H", None)
    total_1H = request.json.get("total_1H", None)
    H1_juice_over = request.json.get("H1_juice_over", None)
    H1_juice_under = request.json.get("H1_juice_under", None)
    tt_away_1H = request.json.get("tt_away_1H", None)
    juice_over_away_1H = request.json.get("juice_over_away_1H", None)
    juice_under_away_1H = request.json.get("juice_under_away_1H", None)
    tt_home_1H = request.json.get("tt_home_1H", None)
    juice_over_home_1H = request.json.get("juice_over_home_1H", None)
    juice_under_home_1H = request.json.get("juice_under_home_1H", None)

    # busca team en BBDD
    colombia_primera_A = Colombia_Primera_A.query.filter_by(
        home=home, away=away, date=date).first()
    # the team was not found on the database
    if colombia_primera_A:
        return jsonify({"msg": "colombia_primera_A already exists", "team away": colombia_primera_A.away, "team home": colombia_primera_A.home}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        colombia_primera_A = Colombia_Primera_A(
            date=date,
            hour=hour,
            status=status,
            away=away,
            home=home,
            goal_line_away=goal_line_away,
            goal_line_home=goal_line_home,
            juice_goal_away=juice_goal_away,
            juice_goal_home=juice_goal_home,
            moneyLineAway=moneyLineAway,
            moneyLineHome=moneyLineHome,
            total=total,
            juice_total_over=juice_total_over,
            juice_total_under=juice_total_under,
            tt_away=tt_away,
            juice_over_away=juice_over_away,
            juice_under_away=juice_under_away,
            tt_home=tt_home,
            juice_over_home=juice_over_home,
            juice_under_home=juice_under_home,
            final_score_away=final_score_away,
            final_score_home=final_score_home,

            goal_away_1H=goal_away_1H,
            goal_home_1H=goal_home_1H,
            juice_puck_away_1H=juice_puck_away_1H,
            juice_puck_home_1H=juice_puck_home_1H,
            moneyLineAway_1H=moneyLineAway_1H,
            moneyLineHome_1H=moneyLineHome_1H,
            total_1H=total_1H,
            H1_juice_over=H1_juice_over,
            H1_juice_under=H1_juice_under,
            tt_away_1H=tt_away_1H,
            juice_over_away_1H=juice_over_away_1H,
            juice_under_away_1H=juice_under_away_1H,
            tt_home_1H=tt_home_1H,
            juice_over_home_1H=juice_over_home_1H,
            juice_under_home_1H=juice_under_home_1H
        )
        db.session.add(colombia_primera_A)
        db.session.commit()
        return jsonify({"msg": "Game colombia_primera_A created successfully"}), 200


@app.route('/stats_nba_team', methods=['POST'])
def createStats_nba_team():
    season = request.json.get("season", None)
    team = request.json.get("team", None)
    conference = request.json.get("conference", None)
    division = request.json.get("division", None)
    pts = request.json.get("pts", None)
    fmg = request.json.get("fmg", None)
    fga = request.json.get("fga", None)
    fg = request.json.get("fg", None)
    fg_AVG = request.json.get("fg_AVG", None)
    three_pm = request.json.get("three_pm", None)
    three_pa = request.json.get("three_pa", None)
    three_p_AVG = request.json.get("three_p_AVG", None)
    ftm = request.json.get("ftm", None)
    fta = request.json.get("fta", None)
    ft_AVG = request.json.get("ft_AVG", None)
    tt_away = request.json.get("tt_away", None)
    Or = request.json.get("Or", None)
    dr = request.json.get("dr", None)
    reb = request.json.get("reb", None)
    ast = request.json.get("ast", None)
    stl = request.json.get("stl", None)
    blk = request.json.get("blk", None)
    pf = request.json.get("final_score_home", None)
    # busca team en BBDD
    stats_nba_team = Stats_nba_team.query.filter_by(team=team).first()
    # the team was not found on the database
    if stats_nba_team:
        return jsonify({"msg": "stats_nba_team already exists", "team": stats_nba_team.team}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_nba_team = Stats_nba_team(
            season=season,
            team=team,
            conference=conference,
            division=division,
            pts=pts,
            fmg=fmg,
            fga=fga,
            fg=fg,
            fg_AVG=fg_AVG,
            three_pm=three_pm,
            three_pa=three_pa,
            moneyLineAway=moneyLineAway,
            three_p_AVG=three_p_AVG,
            ftm=ftm,
            fta=fta,
            ft_AVG=ft_AVG,
            Or=Or,
            dr=dr,
            reb=reb,
            ast=ast,
            stl=stl,
            blk=blk,
            to=to,
            pf=pf
        )
        db.session.add(stats_nba_team)
        db.session.commit()
        return jsonify({"msg": "Game stats_nba_team created successfully"}), 200


@app.route('/stats_nba_player', methods=['POST'])
def createStats_nba_player():
    name = request.json.get("name", None)
    height = request.json.get("height", None)
    weight = request.json.get("weight", None)
    birth = request.json.get("birth", None)
    college = request.json.get("college", None)
    season = request.json.get("season", None)
    team = request.json.get("team", None)

    dorsal = request.json.get("dorsal", None)
    minutes = request.json.get("minutes", None)
    position = request.json.get("position", None)
    gp = request.json.get("gp", None)
    gs = request.json.get("gs", None)
    fg = request.json.get("fg", None)
    fg_AVG = request.json.get("fg_AVG", None)
    three_pt = request.json.get("three_pt", None)
    three_pt_AVG = request.json.get("three_pt_AVG", None)
    ft = request.json.get("ft", None)
    ft_AVG = request.json.get("ft_AVG", None)
    Or = request.json.get("Or", None)
    dr = request.json.get("dr", None)
    reb = request.json.get("reb", None)
    ast = request.json.get("ast", None)
    stl = request.json.get("stl", None)
    blk = request.json.get("blk", None)
    to = request.json.get("to", None)
    pf = request.json.get("pf", None)
    pts = request.json.get("pts", None)
    # busca team en BBDD
    stats_nba_player = Stats_nba_player.query.filter_by(
        name=name, dorsal=dorsal, team=team).first()
    # the team was not found on the database
    if stats_nba_player:
        return jsonify({"msg": "stats_nba_player already exists", "name": stats_nba_player.name}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_nba_player = Stats_nba_player(
            name=name,
            height=height,
            weight=weight,
            birth=birth,
            college=college,
            season=season,
            team=team,
            dorsal=dorsal,
            minutes=minutes,
            position=position,
            gp=gp,
            gs=gs,
            fg=fg,
            fg_AVG=fg_AVG,
            three_pt=three_pt,
            three_pt_AVG=three_pt_AVG,
            ft=ft,
            fta=fta,
            ft_AVG=ft_AVG,
            Or=Or,
            dr=dr,
            reb=reb,
            ast=ast,
            stl=stl,
            blk=blk,
            to=to,
            pf=pf,
            pts=pts
        )
        db.session.add(stats_nba_player)
        db.session.commit()
        return jsonify({"msg": "Game stats_nba_player created successfully"}), 200


@app.route('/stats_nhl_team', methods=['POST'])
def createStats_nhl_team():
    season = request.json.get("season", None)
    team = request.json.get("team", None)
    conference = request.json.get("conference", None)
    division = request.json.get("division", None)
    w = request.json.get("w", None)
    l = request.json.get("l", None)
    Ga_a = request.json.get("Ga_a", None)
    otl = request.json.get("otl", None)
    sa = request.json.get("sa", None)
    ga = request.json.get("ga", None)
    s = request.json.get("s", None)
    sv_AVG = request.json.get("sv_AVG", None)
    so = request.json.get("so", None)
    so_sa = request.json.get("so_sa", None)
    sos = request.json.get("sos", None)
    sos_AVG = request.json.get("sos_AVG", None)

    # busca team en BBDD
    stats_nhl_team = Stats_nhl_team.query.filter_by(
        team=team, conference=conference, division=division).first()
    # the team was not found on the database
    if stats_nhl_team:
        return jsonify({"msg": "stats_nhl_team already exists", "team": stats_nhl_team.team}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_nhl_team = Stats_nhl_team(
            season=season,
            team=team,
            conference=conference,
            division=division,
            w=w,
            l=l,
            Ga_a=Ga_a,
            otl=otl,
            sa=sa,
            ga=ga,
            s=s,
            sv_AVG=sv_AVG,
            so=so,
            so_sa=so_sa,
            sos=sos,
            sos_AVG=sos_AVG
        )
        db.session.add(stats_nhl_team)
        db.session.commit()
        return jsonify({"msg": "Game stats_nhl_team created successfully"}), 200


@app.route('/stats_nhl_player', methods=['POST'])
def createStats_nhl_player():
    name = request.json.get("name", None)
    height = request.json.get("height", None)
    weight = request.json.get("weight", None)
    birth = request.json.get("birth", None)
    season = request.json.get("season", None)
    team = request.json.get("team", None)
    dorsal = request.json.get("dorsal", None)
    position = request.json.get("position", None)
    gp = request.json.get("gp", None)
    g = request.json.get("g", None)
    a = request.json.get("a", None)
    pts = request.json.get("pts", None)
    p_m_rating = request.json.get("p_m_rating", None)
    pim = request.json.get("pim", None)
    sog = request.json.get("sog", None)
    spct = request.json.get("spct", None)
    ppg = request.json.get("ppg", None)
    ppa = request.json.get("ppa", None)
    shg = request.json.get("shg", None)
    sha = request.json.get("sha", None)
    gwg = request.json.get("gwg", None)
    gtg = request.json.get("gtg", None)
    toi_g = request.json.get("toi_g", None)
    prod = request.json.get("prod", None)
    # busca team en BBDD
    stats_nhl_player = Stats_nhl_player.query.filter_by(
        name=name, dorsal=dorsal, team=team).first()
    # the team was not found on the database
    if stats_nhl_player:
        return jsonify({"msg": "stats_nhl_player already exists", "name": stats_nhl_player.name}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_nhl_player = Stats_nhl_player(
            name=name,
            height=height,
            weight=weight,
            birth=birth,
            season=season,
            team=team,
            dorsal=dorsal,
            position=position,
            gp=gp,
            g=g,
            a=a,
            pts=pts,
            p_m_rating=p_m_rating,
            pim=pim,
            sog=sog,
            spct=spct,
            ppg=ppg,
            ppa=ppa,
            shg=shg,
            sha=sha,
            gwg=gwg,
            gtg=gtg,
            toi_g=toi_g,
            prod=prod
        )
        db.session.add(stats_nhl_player)
        db.session.commit()
        return jsonify({"msg": "Game stats_nhl_player created successfully"}), 200


@app.route('/stats_mlb_team', methods=['POST'])
def createStats_mlb_team():
    season = request.json.get("season", None)
    team = request.json.get("team", None)
    league = request.json.get("league", None)
    division = request.json.get("division", None)
    w = request.json.get("w", None)
    l = request.json.get("l", None)
    pct = request.json.get("pct", None)
    gb = request.json.get("gb", None)
    home = request.json.get("home", None)
    away = request.json.get("away", None)
    rs = request.json.get("rs", None)
    ra = request.json.get("ra", None)
    diff = request.json.get("diff", None)
    strk = request.json.get("strk", None)
    L10 = request.json.get("L10", None)
    poff = request.json.get("poff", None)

    # busca team en BBDD
    stats_mlb_team = Stats_mlb_team.query.filter_by(
        team=team, league=league, division=division).first()
    # the team was not found on the database
    if stats_mlb_team:
        return jsonify({"msg": "stats_mlb_team already exists", "team": stats_mlb_team.team}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_mlb_team = Stats_mlb_team(
            season=season,
            team=team,
            league=league,
            division=division,
            w=w,
            l=l,
            pct=pct,
            gb=gb,
            home=home,
            away=away,
            rs=rs,
            ra=ra,
            diff=diff,
            strk=strk,
            L10=L10,
            poff=poff
        )
        db.session.add(stats_mlb_team)
        db.session.commit()
        return jsonify({"msg": "Game stats_mlb_team created successfully"}), 200


@app.route('/stats_mlb_player', methods=['POST'])
def createStats_mlb_player():
    name = request.json.get("name", None)
    height = request.json.get("height", None)
    weight = request.json.get("weight", None)
    birth = request.json.get("birth", None)
    season = request.json.get("season", None)
    team = request.json.get("team", None)
    dorsal = request.json.get("dorsal", None)
    position = request.json.get("position", None)
    gp = request.json.get("gp", None)
    ab = request.json.get("ab", None)
    r = request.json.get("r", None)
    h = request.json.get("h", None)
    two_b = request.json.get("two_b", None)
    three_b = request.json.get("three_b", None)
    hb = request.json.get("hb", None)
    rbi = request.json.get("rbi", None)
    tb = request.json.get("tb", None)
    bb = request.json.get("bb", None)
    so = request.json.get("so", None)
    sb = request.json.get("sb", None)
    avg = request.json.get("avg", None)
    obp = request.json.get("obp", None)
    slg = request.json.get("slg", None)
    ops = request.json.get("ops", None)
    war = request.json.get("war", None)

    # busca team en BBDD
    stats_mlb_player = Stats_mlb_player.query.filter_by(
        name=name, dorsal=dorsal, birth=birth).first()
    # the team was not found on the database
    if stats_mlb_player:
        return jsonify({"msg": "stats_mlb_player already exists", "name": stats_mlb_player.name}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_mlb_player = Stats_mlb_player(
            name=name,
            height=height,
            weight=weight,
            birth=birth,
            season=season,
            team=team,
            dorsal=dorsal,
            position=position,
            gp=gp,
            adb=adb,
            r=r,
            h=h,
            two_b=two_b,
            three_b=three_b,
            hb=hb,
            rbi=rbi,
            tb=tb,
            bb=bb,
            so=so,
            sb=sb,
            avg=avg,
            obp=obp,
            slg=slg,
            ops=ops,
            war=war
        )
        db.session.add(stats_mlb_player)
        db.session.commit()
        return jsonify({"msg": "Game stats_mlb_player created successfully"}), 200


@app.route('/stats_box_fighter', methods=['POST'])
def createStats_box_fighter():
    name = request.json.get("name", None)
    nickname = request.json.get("nickname", None)
    height = request.json.get("height", None)
    weight = request.json.get("weight", None)
    birth = request.json.get("birth", None)
    country = request.json.get("country", None)
    association = request.json.get("association", None)
    category = request.json.get("category", None)
    w = request.json.get("w", None)
    w_by = request.json.get("w_by", None)
    L = request.json.get("L", None)
    L_by = request.json.get("L_by", None)

    # busca team en BBDD
    stats_box_fighter = Stats_box_fighter.query.filter_by(
        name=name, nickname=nickname, birth=birthn).first()
    # the team was not found on the database
    if stats_box_fighter:
        return jsonify({"msg": "stats_box_fighter already exists", "name": stats_box_fighter.name}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_box_fighter = Stats_box_fighter(
            name=name,
            nickname=nickname,
            league=league,
            height=height,
            weight=weight,
            birth=birth,
            country=country,
            association=association,
            category=category,
            w=w,
            w_by=w_by,
            L=L,
            L_by=L_by
        )
        db.session.add(stats_box_fighter)
        db.session.commit()
        return jsonify({"msg": "Game stats_box_fighter created successfully"}), 200


@app.route('/stats_mma_fighter', methods=['POST'])
def createStats_mma_fighter():
    name = request.json.get("name", None)
    nickname = request.json.get("nickname", None)
    height = request.json.get("height", None)
    weight = request.json.get("weight", None)
    birth = request.json.get("birth", None)
    country = request.json.get("country", None)
    association = request.json.get("association", None)
    category = request.json.get("category", None)
    w = request.json.get("w", None)
    w_by = request.json.get("w_by", None)
    L = request.json.get("L", None)
    L_by = request.json.get("L_by", None)

    # busca team en BBDD
    stats_mma_fighter = Stats_mma_fighter.query.filter_by(
        name=name, nickname=nickname, birth=birth).first()
    # the team was not found on the database
    if stats_mma_fighter:
        return jsonify({"msg": "stats_mma_fighter already exists", "team": stats_mma_fighter.name}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_mma_fighter = Stats_mma_fighter(
            name=name,
            nickname=nickname,
            league=league,
            height=height,
            weight=weight,
            birth=birth,
            country=country,
            association=association,
            category=category,
            w=w,
            w_by=w_by,
            L=L,
            L_by=L_by
        )
        db.session.add(stats_mma_fighter)
        db.session.commit()
        return jsonify({"msg": "Game stats_mma_fighter created successfully"}), 200


@app.route('/stats_nfl_team', methods=['POST'])
def createStats_nfl_team():
    season = request.json.get("season", None)
    team = request.json.get("team", None)
    conference = request.json.get("conference", None)
    division = request.json.get("division", None)
    TP = request.json.get("TP", None)
    ttpg = request.json.get("ttpg", None)
    t_td = request.json.get("t_td", None)
    t_1_down = request.json.get("t_1_down", None)
    Russ_1_d = request.json.get("Russ_1_d", None)
    pass_1_d = request.json.get("pass_1_d", None)
    down_1_penal = request.json.get("down_1_penal", None)
    down_3_eff = request.json.get("down_3_eff", None)
    down_3_AVG = request.json.get("down_3_AVG", None)
    down_4_eff = request.json.get("down_4_eff", None)
    down_4_AVG = request.json.get("down_4_AVG", None)
    comp_att = request.json.get("comp_att", None)
    net_pass_y = request.json.get("net_pass_y", None)
    y_p_pas_attps = request.json.get("y_p_pas_attps", None)
    net_pass_y_pg = request.json.get("net_pass_y_pg", None)
    pass_td = request.json.get("pass_td", None)
    interceptions = request.json.get("interceptions", None)
    sacks_y_lost = request.json.get("sacks_y_lost", None)
    russ_attps = request.json.get("russ_attps", None)
    russ_y = request.json.get("russ_y", None)
    y_p_russ_attp = request.json.get("y_p_russ_attp", None)
    russ_y_pg = request.json.get("russ_y_pg", None)
    russ_td = request.json.get("russ_td", None)
    total_of_plays = request.json.get("total_of_plays", None)
    total_y = request.json.get("total_y", None)
    y_pg = request.json.get("y_pg", None)
    kickoffs_t = request.json.get("kickoffs_t", None)
    AVG_kickoff_return_y = request.json.get("AVG_kickoff_return_y", None)
    punt_t = request.json.get("punt_t", None)
    AVG_punt_ruturn_y = request.json.get("AVG_punt_ruturn_y", None)
    int_t = request.json.get("int_t", None)
    AVG_intercept_y = request.json.get("AVG_intercept_y", None)
    net_AVG_punt_y = request.json.get("net_AVG_punt_y", None)
    punt_ty = request.json.get("punt_ty", None)
    fg_goog_attps = request.json.get("fg_goog_attps", None)
    touchback_percent = request.json.get("touchback_percent", None)
    penal_ty = request.json.get("penal_ty", None)
    penal_y_AVG_pg = request.json.get("penal_y_AVG_pg", None)
    possesion_time = request.json.get("possesion_time", None)
    fumbles_lost = request.json.get("fumbles_lost", None)
    turnover_ratio = request.json.get("turnover_ratio", None)

    # valida si estan vacios los ingresos
    # busca team en BBDD
    stats_nfl_team = Stats_nfl_team.query.filter_by(
        team=team, season=season, conference=conference, division=division).first()
    # the team was not found on the database
    if stats_nfl_team:
        return jsonify({"msg": "stats_nfl_team already exists", "team": stats_nfl_team.team}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_nfl_team = Stats_nfl_team(
            season=season,
            team=team,
            conference=conference,
            division=division,
            TP=TP,
            ttpg=ttpg,
            t_td=t_td,
            t_1_down=t_1_down,
            Russ_1_d=Russ_1_d,
            pass_1_d=pass_1_d,
            down_1_penal=down_1_penal,
            down_3_eff=down_3_eff,
            down_3_AVG=down_3_AVG,
            down_4_eff=down_4_eff,
            down_4_AVG=down_4_AVG,
            comp_att=comp_att,
            net_pass_y=net_pass_y,
            y_p_pas_attps=y_p_pas_attps,
            net_pass_y_pg=net_pass_y_pg,
            pass_td=pass_td,
            interceptions=interceptions,
            sacks_y_lost=sacks_y_lost,
            russ_attps=russ_attps,
            russ_y=russ_y,
            y_p_russ_attp=y_p_russ_attp,
            russ_y_pg=russ_y_pg,
            russ_td=russ_td,
            total_of_plays=total_of_plays,
            total_y=total_y,
            y_pg=y_pg,
            kickoffs_t=kickoffs_t,
            AVG_kickoff_return_y=AVG_kickoff_return_y,
            punt_t=punt_t,
            AVG_punt_ruturn_y=AVG_punt_ruturn_y,
            int_t=int_t,
            AVG_intercept_y=AVG_intercept_y,
            net_AVG_punt_y=net_AVG_punt_y,
            punt_ty=punt_ty,
            fg_goog_attps=fg_goog_attps,
            touchback_percent=touchback_percent,
            penal_ty=penal_ty,
            penal_y_AVG_pg=penal_y_AVG_pg,
            possesion_time=possesion_time,
            fumbles_lost=fumbles_lost,
            turnover_ratio=turnover_ratio
        )
        db.session.add(stats_nfl_team)
        db.session.commit()
        return jsonify({"msg": "Game stats_nfl_team created successfully"}), 200


@app.route('/stats_defensive_player_nfl', methods=['POST'])
def createStats_defensive_player_nfl():
    name = request.json.get("name", None)
    height = request.json.get("height", None)
    weight = request.json.get("weight", None)
    birth = request.json.get("birth", None)
    position = request.json.get("position", None)
    dorsal = request.json.get("dorsal", None)
    season = request.json.get("season", None)
    team = request.json.get("team", None)
    games = request.json.get("games", None)
    tack_solo = request.json.get("tack_solo", None)
    tack_ast = request.json.get("tack_ast", None)
    tack_total = request.json.get("tack_total", None)
    sacks = request.json.get("sacks", None)
    sacks_yards = request.json.get("sacks_yards", None)
    tfl = request.json.get("tfl", None)
    pd = request.json.get("pd", None)
    Int = request.json.get("Int", None)
    yds = request.json.get("yds", None)
    ing = request.json.get("ing", None)
    td = request.json.get("td", None)
    ff = request.json.get("ff", None)
    fr = request.json.get("fr", None)
    ftd = request.json.get("ftd", None)
    kb = request.json.get("kb", None)

    # busca team en BBDD
    stats_defensive_player_nfl = Stats_defensive_player_nfl.query.filter_by(name=name, height=height, birth=birth, season=season).first()
    # the team was not found on the database
    if stats_defensive_player_nfl:
        return jsonify({"msg": "stats_defensive_player_nfl already exists", "name": stats_defensive_player_nfl.name}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_defensive_player_nfl = Stats_defensive_player_nfl(
            name=name,
            height=height,
            weight=weight,
            birth=birth,
            position=position,
            dorsal=dorsal,
            season=season,
            team=team,
            games=games,
            tack_solo=tack_solo,
            tack_ast=tack_ast,
            tack_total=tack_total,
            sacks=sacks,
            sacks_yards=sacks_yards,
            tfl=tfl,
            pd=pd,
            Int=Int,
            yds=yds,
            ing=ing,
            td=td,
            ff=ff,
            fr=fr,
            ftd=ftd,
            kb=kb
        )
        db.session.add(stats_defensive_player_nfl)
        db.session.commit()
        return jsonify({"msg": "Game stats_defensive_player_nfl created successfully"}), 200


@app.route('/stats_offensive_player_nfl', methods=['POST'])
def createStats_offensive_player_nfl():
    name = request.json.get("name", None)
    height = request.json.get("height", None)
    weight = request.json.get("weight", None)
    birth = request.json.get("birth", None)
    position = request.json.get("position", None)
    dorsal = request.json.get("dorsal", None)
    season = request.json.get("season", None)
    team = request.json.get("team", None)
    games = request.json.get("games", None)
    Cmp = request.json.get("Cmp", None)
    pass_att = request.json.get("pass_att", None)
    cmp_AVG = request.json.get("cmp_AVG", None)
    yards = request.json.get("yards", None)
    yards_AVG = request.json.get("yards_AVG", None)
    yards_pg = request.json.get("yards_pg", None)
    pass_td = request.json.get("pass_td", None)
    Int = request.json.get("Int", None)
    asck = request.json.get("asck", None)
    syl = request.json.get("syl", None)
    rtg = request.json.get("rtg", None)
    russ_att = request.json.get("russ_att", None)
    russ_yards = request.json.get("russ_yards", None)
    yards_p_russ = request.json.get("yards_p_russ", None)
    big = request.json.get("big", None)
    rush_tt = request.json.get("rush_tt", None)
    rush_yard_pg = request.json.get("rush_yard_pg", None)
    fum = request.json.get("fum", None)
    lst = request.json.get("lst", None)
    fd = request.json.get("fd", None)
    rec = request.json.get("rec", None)
    r_tgts = request.json.get("r_tgts", None)
    r_yards = request.json.get("r_yards", None)
    yards_p_r = request.json.get("yards_p_r", None)
    r_td = request.json.get("r_td", None)
    lr = request.json.get("lr", None)
    r_big = request.json.get("r_big", None)
    r_ypg = request.json.get("r_ypg", None)
    r_fl = request.json.get("r_fl", None)
    r_yac = request.json.get("r_yac", None)
    r_fd = request.json.get("r_fd", None)
    pts = request.json.get("pts", None)

    # valida si estan vacios los ingresos

    # busca team en BBDD
    stats_offensive_player_nfl = Stats_offensive_player_nfl.query.filter_by(
        name=name, dorsal=dorsal, birth=birth).first()
    # the team was not found on the database
    if stats_offensive_player_nfl:
        return jsonify({"msg": "stats_offensive_player_nfl already exists", "name": stats_offensive_player_nfl.name}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_offensive_player_nfl = Stats_offensive_player_nfl(
            name=name,
            height=height,
            weight=weight,
            birth=birth,
            position=position,
            dorsal=dorsal,
            season=season,
            team=team,
            games=games,
            Cmp=Cmp,
            pass_att=pass_att,
            cmp_AVG=cmp_AVG,
            yards=yards,
            yards_AVG=yards_AVG,
            yards_pg=yards_pg,
            pass_td=pass_td,
            Int=Int,
            asck=asck,
            syl=syl,
            rtg=rtg,
            russ_att=russ_att,
            russ_yards=russ_yards,
            yards_p_russ=yards_p_russ,
            big=big,
            rush_tt=rush_tt,
            rush_yard_pg=rush_yard_pg,
            fum=fum,
            lst=lst,
            fd=fd,
            rec=rec,
            r_tgts=r_tgts,
            r_yards=r_yards,
            yards_p_r=yards_p_r,
            r_td=r_td,
            lr=lr,
            r_big=r_big,
            r_ypg=r_ypg,
            r_fl=r_fl,
            r_yac=r_yac,
            r_fd=r_fd,
            pts=pts
        )
        db.session.add(stats_offensive_player_nfl)
        db.session.commit()
        return jsonify({"msg": "Game stats_offensive_player_nfl created successfully"}), 200


@app.route('/stats_returning_player_nfl', methods=['POST'])
def createStats_returning_player_nfl():
    name = request.json.get("name", None)
    height = request.json.get("height", None)
    weight = request.json.get("weight", None)
    birth = request.json.get("birth", None)
    position = request.json.get("position", None)
    dorsal = request.json.get("dorsal", None)
    season = request.json.get("season", None)
    team = request.json.get("team", None)
    games = request.json.get("games", None)
    kick_returns = request.json.get("kick_returns", None)
    kick_returns_yards = request.json.get("kick_returns_yards", None)
    yards_p_k_p = request.json.get("yards_p_k_p", None)
    l_k_r = request.json.get("l_k_r", None)
    k_r_td = request.json.get("k_r_td", None)
    punt_r = request.json.get("punt_r", None)
    punt_r_y = request.json.get("punt_r_y", None)
    y_ppr = request.json.get("y_ppr", None)
    lpr = request.json.get("lpr", None)
    pr_td = request.json.get("pr_td", None)
    punt_r_fair_carches = request.json.get("punt_r_fair_carches", None)

    # busca team en BBDD
    stats_returning_player_nfl = Stats_returning_player_nfl.query.filter_by(
        name=name, dorsal=dorsal, birth=birth).first()
    # the team was not found on the database
    if stats_returning_player_nfl:
        return jsonify({"msg": "stats_returning_player_nfl already exists", "name": stats_returning_player_nfl.name}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_returning_player_nfl = Stats_returning_player_nfl(
            name=name,
            height=height,
            weight=weight,
            birth=birth,
            position=position,
            dorsal=dorsal,
            season=season,
            team=team,
            games=games,
            kick_returns=kick_returns,
            kick_returns_yards=kick_returns_yards,
            yards_p_k_p=yards_p_k_p,
            l_k_r=l_k_r,
            k_r_td=k_r_td,
            punt_r=punt_r,
            punt_r_y=punt_r_y,
            y_ppr=y_ppr,
            lpr=lpr,
            pr_td=pr_td,
            punt_r_fair_carches=punt_r_fair_carches,
        )
        db.session.add(stats_returning_player_nfl)
        db.session.commit()
        return jsonify({"msg": "Game stats_returning_player_nfl created successfully"}), 200


@app.route('/stats_kiking_player_nfl', methods=['POST'])
def createStats_kiking_player_nfl():
    name = request.json.get("name", None)
    height = request.json.get("height", None)
    weight = request.json.get("weight", None)
    birth = request.json.get("birth", None)
    position = request.json.get("position", None)
    dorsal = request.json.get("dorsal", None)
    season = request.json.get("season", None)
    team = request.json.get("team", None)
    games = request.json.get("games", None)
    fgm = request.json.get("fgm", None)
    fga = request.json.get("fga", None)
    fg_AVG = request.json.get("fg_AVG", None)
    lng = request.json.get("lng", None)
    yars_f_goals_1_19 = request.json.get("yars_f_goals_1_19", None)
    yars_f_goals_20_29 = request.json.get("yars_f_goals_20_29", None)
    yars_f_goals_30_49 = request.json.get("yars_f_goals_30_49", None)
    yars_f_goals_40_49 = request.json.get("yars_f_goals_40_49", None)
    more_50 = request.json.get("more_50", None)
    xpm = request.json.get("xpm", None)
    xpa = request.json.get("xpa", None)
    xp_AVG = request.json.get("xp_AVG", None)

    # busca team en BBDD
    stats_kiking_player_nfl = Stats_kiking_player_nfl.query.filter_by(
        name=name, dorsal=dorsal, birth=birth).first()
    # the team was not found on the database
    if stats_kiking_player_nfl:
        return jsonify({"msg": "stats_kiking_player_nfl already exists", "name": stats_kiking_player_nfl.name}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_kiking_player_nfl = Stats_kiking_player_nfl(
            name=name,
            height=height,
            weight=weight,
            birth=birth,
            position=position,
            dorsal=dorsal,
            season=season,
            team=team,
            games=games,
            fgm=fgm,
            fga=fga,
            fg_AVG=fg_AVG,
            lng=lng,
            yars_f_goals_1_19=yars_f_goals_1_19,
            yars_f_goals_20_29=yars_f_goals_20_29,
            yars_f_goals_30_49=yars_f_goals_30_49,
            yars_f_goals_40_49=yars_f_goals_40_49,
            more_50=more_50,
            xpm=xpm,
            xpa=xpa,
            xp_AVG=xp_AVG
        )
        db.session.add(stats_kiking_player_nfl)
        db.session.commit()
        return jsonify({"msg": "Game stats_kiking_player_nfl created successfully"}), 200


@app.route('/stats_punting_player_nfl', methods=['POST'])
def createStats_punting_player_nfl():
    name = request.json.get("name", None)
    height = request.json.get("height", None)
    weight = request.json.get("weight", None)
    birth = request.json.get("birth", None)
    position = request.json.get("position", None)
    dorsal = request.json.get("dorsal", None)
    season = request.json.get("season", None)
    team = request.json.get("team", None)
    games = request.json.get("games", None)

    punts = request.json.get("punts", None)
    yards = request.json.get("yards", None)
    lng = request.json.get("lng", None)
    AVG = request.json.get("AVG", None)
    net = request.json.get("net", None)
    p_blk = request.json.get("p_blk", None)
    IN_20 = request.json.get("IN_20", None)
    tb = request.json.get("tb", None)
    fc = request.json.get("fc", None)
    att = request.json.get("att", None)
    punt_return_yds = request.json.get("punt_return_yds", None)
    AVG_punt_retun_yards = request.json.get("AVG_punt_retun_yards", None)

    # busca team en BBDD
    stats_punting_player_nfl = Stats_punting_player_nfl.query.filter_by(
        name=name, dorsal=dorsal, birth=birth).first()
    # the team was not found on the database
    if stats_punting_player_nfl:
        return jsonify({"msg": "stats_punting_player_nfl already exists", "name": stats_punting_player_nfl.name}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_punting_player_nfl = Stats_punting_player_nfl(
            name=name,
            height=height,
            weight=weight,
            birth=birth,
            position=position,
            dorsal=dorsal,
            season=season,
            team=team,
            games=games,
            punts=punts,
            yards=yards,
            lng=lng,
            AVG=AVG,
            net=net,
            p_blk=p_blk,
            IN_20=IN_20,
            tb=tb,
            fc=fc,
            att=att,
            punt_return_yds=punt_return_yds,
            AVG_punt_retun_yards=AVG_punt_retun_yards
        )
        db.session.add(stats_punting_player_nfl)
        db.session.commit()
        return jsonify({"msg": "Game stats_punting_player_nfl created successfully"}), 200


@app.route('/news', methods=['POST'])
def createnews():
    date = request.json.get("date", None)
    title = request.json.get("title", None)
    url_image = request.json.get("url_image", None)
    short_description = request.json.get("short_description", None)
    news_post = request.json.get("news_post", None)
    written = request.json.get("written", None)

    # busca team en BBDD
    news = News.query.filter_by(date=date, title=title).first()
    # the team was not found on the database
    if news:
        return jsonify({"msg": "news already exists", "title": news.title}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        news = News(
            date=date,
            title=title,
            url_image=url_image,
            short_description=short_description,
            news_post=news_post,
            written=written
        )
        db.session.add(news)
        db.session.commit()
        return jsonify({"msg": "News created successfully"}), 200
# Endpoint for edith records

# ------------put


@app.route('/news/<id>', methods=['PUT'])
def newsEdit(id):
    news = News.query.get(id)
    date = request.json['date']
    title = request.json['title']
    url_image = request.json['url_image']
    short_description = request.json['short_description']
    news_post = request.json['news_post']
    written = request.json['written']
    news.date = date
    news.title = title
    news.url_image = url_image
    news.short_description = short_description
    news.news_post = news_post
    news.written = written
    db.session.commit()
    return jsonify({"msg": "News edith successfully"}), 200


@app.route('/casinos/<id>', methods=['PUT'])
def newsCasinos(id):
    casinos = Casinos.query.get(id)
    name = request.json['name']
    casinos.name = name

    db.session.commit()
    return jsonify({"msg": "casino edith successfully"}), 200


@app.route('/mlb/<id>', methods=['PUT'])
def mlbEdit(id):
    mlb = Mlb.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    preview = request.json['preview']
    img_preview = request.json['img_preview']
    status = request.json['status']
    away = request.json['away']
    pitcher_a = request.json['pitcher_a']
    home = request.json['home']
    pitcher_h = request.json['pitcher_h']
    rl_away = request.json['rl_away']
    rl_home = request.json['rl_home']
    juice_rl_away = request.json['juice_rl_away']
    juice_rl_home = request.json['juice_rl_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']

    rl_away_f5 = request.json['rl_away_f5']
    rl_home_f5 = request.json['rl_home_f5']
    juice_rl_away_f5 = request.json['juice_rl_away_f5']
    juice_rl_home_f5 = request.json['juice_rl_home_f5']
    moneyLineAway_f5 = request.json['moneyLineAway_f5']
    moneyLineHome_f5 = request.json['moneyLineHome_f5']
    total_f5 = request.json['total_f5']
    juice_total_over_f5 = request.json['juice_total_over_f5']
    juice_total_under_f5 = request.json['juice_total_under_f5']
    tt_away_f5 = request.json['tt_away_f5']
    juice_over_away_f5 = request.json['juice_over_away_f5']
    juice_under_away_f5 = request.json['juice_under_away_f5']
    tt_home_f5 = request.json['tt_home_f5']
    juice_over_home_f5 = request.json['juice_over_home_f5']
    juice_under_home_f5 = request.json['juice_under_home_f5']
    fs_away_f5 = request.json['fs_away_f5']
    fs_home_f5 = request.json['fs_home_f5']
    sa_1inning = request.json['sa_1inning']
    sh_1inning = request.json['sh_1inning']
    sa_2inning = request.json['sa_2inning']
    sh_2inning = request.json['sh_2inning']
    sa_3inning = request.json['sa_3inning']
    sh_3inning = request.json['sh_3inning']
    sa_4inning = request.json['sa_4inning']
    sh_4inning = request.json['sh_4inning']
    sa_5inning = request.json['sa_5inning']
    sh_5inning = request.json['sh_5inning']
    sa_6inning = request.json['sa_6inning']
    sh_6inning = request.json['sh_6inning']
    sa_7inning = request.json['sa_7inning']
    sh_7inning = request.json['sh_7inning']
    sa_8inning = request.json['sa_8inning']
    sh_8inning = request.json['sh_8inning']
    sa_9inning = request.json['sa_9inning']
    sh_9inning = request.json['sh_9inning']
    sa_10inning = request.json['sa_10inning']
    sh_10inning = request.json['sh_10inning']
    sa_11inning = request.json['sa_11inning']
    sh_11inning = request.json['sh_11inning']
    sa_12inning = request.json['sa_12inning']
    sh_12inning = request.json['sh_12inning']
    sa_13inning = request.json['sa_13inning']
    sh_13inning = request.json['sh_13inning']
    sa_14inning = request.json['sa_14inning']
    sh_14inning = request.json['sh_14inning']
    sa_15inning = request.json['sa_15inning']
    sh_15inning = request.json['sh_15inning']
    sa_16inning = request.json['sa_16inning']
    sh_16inning = request.json['sh_16inning']
    sa_17inning = request.json['sa_17inning']
    sh_17inning = request.json['sh_17inning']
    sa_18inning = request.json['sa_18inning']
    sh_18inning = request.json['sh_18inning']
    sa_19inning = request.json['sa_19inning']
    sh_19inning = request.json['sh_19inning']
    sa_20inning = request.json['sa_20inning']
    sh_20inning = request.json['sh_20inning']
    sa_21inning = request.json['sa_21inning']
    sh_21inning = request.json['sh_21inning']
    sa_22inning = request.json['sa_22inning']
    sh_22inning = request.json['sh_22inning']
    sa_23inning = request.json['sa_23inning']
    sh_23inning = request.json['sh_23inning']
    sa_24inning = request.json['sa_24inning']
    sh_24inning = request.json['sh_24inning']
    sa_25inning = request.json['sa_25inning']
    sh_25inning = request.json['sh_25inning']
    mlb.date = date
    mlb.hour = hour
    mlb.preview = preview
    mlb.img_preview = img_preview
    mlb.status = status
    mlb.away = away
    mlb.pitcher_a = pitcher_a
    mlb.home = home
    mlb.pitcher_h = pitcher_h
    mlb.rl_away = rl_away
    mlb.rl_home = rl_home
    mlb.juice_rl_away = juice_rl_away
    mlb.juice_rl_home = juice_rl_home
    mlb.moneyLineAway = moneyLineAway
    mlb.moneyLineHome = moneyLineHome
    mlb.total = total
    mlb.juice_total_over = juice_total_over
    mlb.juice_total_under = juice_total_under
    mlb.tt_away = tt_away
    mlb.juice_over_away = juice_over_away
    mlb.juice_under_away = juice_under_away
    mlb.tt_home = tt_home
    mlb.juice_over_home = juice_over_home
    mlb.juice_under_home = juice_under_home
    mlb.final_score_away = final_score_away
    mlb.final_score_home = final_score_home
    mlb.final_score_home = final_score_home
    mlb.rl_home_f5 = rl_home_f5
    mlb.juice_rl_away_f5 = juice_rl_away_f5
    mlb.juice_rl_home_f5 = juice_rl_home_f5
    mlb.moneyLineAway_f5 = moneyLineAway_f5
    mlb.moneyLineHome_f5 = moneyLineHome_f5
    mlb.total_f5 = total_f5
    mlb.juice_total_over_f5 = juice_total_over_f5
    mlb.juice_total_under_f5 = juice_total_under_f5
    mlb.tt_away_f5 = tt_away_f5
    mlb.juice_over_away_f5 = juice_over_away_f5
    mlb.juice_under_away_f5 = juice_under_away_f5
    mlb.tt_home_f5 = tt_home_f5
    mlb.juice_over_home_f5 = juice_over_home_f5
    mlb.juice_under_home_f5 = juice_under_home_f5
    mlb.fs_away_f5 = fs_away_f5
    mlb.fs_home_f5 = fs_home_f5
    mlb.sa_1inning = sa_1inning
    mlb.sh_1inning = sh_1inning
    mlb.sa_2inning = sa_2inning
    mlb.sh_2inning = sh_2inning
    mlb.sa_3inning = sa_3inning
    mlb.sh_3inning = sh_3inning
    mlb.sa_4inning = sa_4inning
    mlb.sh_4inning = sh_4inning
    mlb.sa_5inning = sa_5inning
    mlb.sh_5inning = sh_5inning
    mlb.sa_6inning = sa_6inning
    mlb.sh_6inning = sh_6inning
    mlb.sa_7inning = sa_7inning
    mlb.sh_7inning = sh_7inning
    mlb.sa_8inning = sa_8inning
    mlb.sh_8inning = sh_8inning
    mlb.sa_9inning = sa_9inning
    mlb.sh_9inning = sh_9inning
    mlb.sa_10inning = sa_10inning
    mlb.sh_10inning = sh_10inning
    mlb.sa_11inning = sa_11inning
    mlb.sh_11inning = sh_11inning
    mlb.sa_12inning = sa_12inning
    mlb.sh_12inning = sh_12inning
    mlb.sa_13inning = sa_13inning
    mlb.sh_13inning = sh_13inning
    mlb.sa_14inning = sa_14inning
    mlb.sh_14inning = sh_14inning
    mlb.sa_15inning = sa_15inning
    mlb.sh_15inning = sh_15inning
    mlb.sa_16inning = sa_16inning
    mlb.sh_16inning = sh_16inning
    mlb.sa_17inning = sa_17inning
    mlb.sh_17inning = sh_17inning
    mlb.sa_18inning = sa_18inning
    mlb.sh_18inning = sh_18inning
    mlb.sa_19inning = sa_19inning
    mlb.sh_19inning = sh_19inning
    mlb.sa_20inning = sa_20inning
    mlb.sh_20inning = sh_20inning
    mlb.sa_21inning = sa_21inning
    mlb.sh_21inning = sh_21inning
    mlb.sa_22inning = sa_22inning
    mlb.sh_22inning = sh_22inning
    mlb.sa_23inning = sa_23inning
    mlb.sh_23inning = sh_23inning
    mlb.sa_24inning = sa_24inning
    mlb.sh_24inning = sh_24inning
    mlb.sa_25inning = sa_25inning
    mlb.sh_25inning = sh_25inning
    db.session.commit()
    return jsonify({"msg": "Mlb match edith successfully"}), 200


@app.route('/ncaa_baseball/<id>', methods=['PUT'])
def ncaa_baseballEdit(id):
    ncaa_baseball = Ncaa_Baseball.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    preview = request.json['preview']
    img_preview = request.json['img_preview']
    status = request.json['status']
    away = request.json['away']
    pitcher_a = request.json['pitcher_a']
    home = request.json['home']
    pitcher_h = request.json['pitcher_h']
    rl_away = request.json['rl_away']
    rl_home = request.json['rl_home']
    juice_rl_away = request.json['juice_rl_away']
    juice_rl_home = request.json['juice_rl_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']

    rl_away_f5 = request.json['rl_away_f5']
    rl_home_f5 = request.json['rl_home_f5']
    juice_rl_away_f5 = request.json['juice_rl_away_f5']
    juice_rl_home_f5 = request.json['juice_rl_home_f5']
    moneyLineAway_f5 = request.json['moneyLineAway_f5']
    moneyLineHome_f5 = request.json['moneyLineHome_f5']
    total_f5 = request.json['total_f5']
    juice_total_over_f5 = request.json['juice_total_over_f5']
    juice_total_under_f5 = request.json['juice_total_under_f5']
    tt_away_f5 = request.json['tt_away_f5']
    juice_over_away_f5 = request.json['juice_over_away_f5']
    juice_under_away_f5 = request.json['juice_under_away_f5']
    tt_home_f5 = request.json['tt_home_f5']
    juice_over_home_f5 = request.json['juice_over_home_f5']
    juice_under_home_f5 = request.json['juice_under_home_f5']
    fs_away_f5 = request.json['fs_away_f5']
    fs_home_f5 = request.json['fs_home_f5']
    sa_1inning = request.json['sa_1inning']
    sh_1inning = request.json['sh_1inning']
    sa_2inning = request.json['sa_2inning']
    sh_2inning = request.json['sh_2inning']
    sa_3inning = request.json['sa_3inning']
    sh_3inning = request.json['sh_3inning']
    sa_4inning = request.json['sa_4inning']
    sh_4inning = request.json['sh_4inning']
    sa_5inning = request.json['sa_5inning']
    sh_5inning = request.json['sh_5inning']
    sa_6inning = request.json['sa_6inning']
    sh_6inning = request.json['sh_6inning']
    sa_7inning = request.json['sa_7inning']
    sh_7inning = request.json['sh_7inning']
    sa_8inning = request.json['sa_8inning']
    sh_8inning = request.json['sh_8inning']
    sa_9inning = request.json['sa_9inning']
    sh_9inning = request.json['sh_9inning']
    sa_10inning = request.json['sa_10inning']
    sh_10inning = request.json['sh_10inning']
    sa_11inning = request.json['sa_11inning']
    sh_11inning = request.json['sh_11inning']
    sa_12inning = request.json['sa_12inning']
    sh_12inning = request.json['sh_12inning']
    sa_13inning = request.json['sa_13inning']
    sh_13inning = request.json['sh_13inning']
    sa_14inning = request.json['sa_14inning']
    sh_14inning = request.json['sh_14inning']
    sa_15inning = request.json['sa_15inning']
    sh_15inning = request.json['sh_15inning']
    sa_16inning = request.json['sa_16inning']
    sh_16inning = request.json['sh_16inning']
    sa_17inning = request.json['sa_17inning']
    sh_17inning = request.json['sh_17inning']
    sa_18inning = request.json['sa_18inning']
    sh_18inning = request.json['sh_18inning']
    sa_19inning = request.json['sa_19inning']
    sh_19inning = request.json['sh_19inning']
    sa_20inning = request.json['sa_20inning']
    sh_20inning = request.json['sh_20inning']
    sa_21inning = request.json['sa_21inning']
    sh_21inning = request.json['sh_21inning']
    sa_22inning = request.json['sa_22inning']
    sh_22inning = request.json['sh_22inning']
    sa_23inning = request.json['sa_23inning']
    sh_23inning = request.json['sh_23inning']
    sa_24inning = request.json['sa_24inning']
    sh_24inning = request.json['sh_24inning']
    sa_25inning = request.json['sa_25inning']
    sh_25inning = request.json['sh_25inning']
    ncaa_baseball.date = date
    ncaa_baseball.hour = hour
    ncaa_baseball.preview = preview
    ncaa_baseball.img_preview = img_preview
    ncaa_baseball.status = status
    ncaa_baseball.away = away
    ncaa_baseball.pitcher_a = pitcher_a
    ncaa_baseball.home = home
    ncaa_baseball.pitcher_h = pitcher_h
    ncaa_baseball.rl_away = rl_away
    ncaa_baseball.rl_home = rl_home
    ncaa_baseball.juice_rl_away = juice_rl_away
    ncaa_baseball.juice_rl_home = juice_rl_home
    ncaa_baseball.moneyLineAway = moneyLineAway
    ncaa_baseball.moneyLineHome = moneyLineHome
    ncaa_baseball.total = total
    ncaa_baseball.juice_total_over = juice_total_over
    ncaa_baseball.juice_total_under = juice_total_under
    ncaa_baseball.tt_away = tt_away
    ncaa_baseball.juice_over_away = juice_over_away
    ncaa_baseball.juice_under_away = juice_under_away
    ncaa_baseball.tt_home = tt_home
    ncaa_baseball.juice_over_home = juice_over_home
    ncaa_baseball.juice_under_home = juice_under_home
    ncaa_baseball.final_score_away = final_score_away
    ncaa_baseball.final_score_home = final_score_home
    ncaa_baseball.final_score_home = final_score_home
    ncaa_baseball.rl_home_f5 = rl_home_f5
    ncaa_baseball.juice_rl_away_f5 = juice_rl_away_f5
    ncaa_baseball.juice_rl_home_f5 = juice_rl_home_f5
    ncaa_baseball.moneyLineAway_f5 = moneyLineAway_f5
    ncaa_baseball.moneyLineHome_f5 = moneyLineHome_f5
    ncaa_baseball.total_f5 = total_f5
    ncaa_baseball.juice_total_over_f5 = juice_total_over_f5
    ncaa_baseball.juice_total_under_f5 = juice_total_under_f5
    ncaa_baseball.tt_away_f5 = tt_away_f5
    ncaa_baseball.juice_over_away_f5 = juice_over_away_f5
    ncaa_baseball.juice_under_away_f5 = juice_under_away_f5
    ncaa_baseball.tt_home_f5 = tt_home_f5
    ncaa_baseball.juice_over_home_f5 = juice_over_home_f5
    ncaa_baseball.juice_under_home_f5 = juice_under_home_f5
    ncaa_baseball.fs_away_f5 = fs_away_f5
    ncaa_baseball.fs_home_f5 = fs_home_f5
    ncaa_baseball.sa_1inning = sa_1inning
    ncaa_baseball.sh_1inning = sh_1inning
    ncaa_baseball.sa_2inning = sa_2inning
    ncaa_baseball.sh_2inning = sh_2inning
    ncaa_baseball.sa_3inning = sa_3inning
    ncaa_baseball.sh_3inning = sh_3inning
    ncaa_baseball.sa_4inning = sa_4inning
    ncaa_baseball.sh_4inning = sh_4inning
    ncaa_baseball.sa_5inning = sa_5inning
    ncaa_baseball.sh_5inning = sh_5inning
    ncaa_baseball.sa_6inning = sa_6inning
    ncaa_baseball.sh_6inning = sh_6inning
    ncaa_baseball.sa_7inning = sa_7inning
    ncaa_baseball.sh_7inning = sh_7inning
    ncaa_baseball.sa_8inning = sa_8inning
    ncaa_baseball.sh_8inning = sh_8inning
    ncaa_baseball.sa_9inning = sa_9inning
    ncaa_baseball.sh_9inning = sh_9inning
    ncaa_baseball.sa_10inning = sa_10inning
    ncaa_baseball.sh_10inning = sh_10inning
    ncaa_baseball.sa_11inning = sa_11inning
    ncaa_baseball.sh_11inning = sh_11inning
    ncaa_baseball.sa_12inning = sa_12inning
    ncaa_baseball.sh_12inning = sh_12inning
    ncaa_baseball.sa_13inning = sa_13inning
    ncaa_baseball.sh_13inning = sh_13inning
    ncaa_baseball.sa_14inning = sa_14inning
    ncaa_baseball.sh_14inning = sh_14inning
    ncaa_baseball.sa_15inning = sa_15inning
    ncaa_baseball.sh_15inning = sh_15inning
    ncaa_baseball.sa_16inning = sa_16inning
    ncaa_baseball.sh_16inning = sh_16inning
    ncaa_baseball.sa_17inning = sa_17inning
    ncaa_baseball.sh_17inning = sh_17inning
    ncaa_baseball.sa_18inning = sa_18inning
    ncaa_baseball.sh_18inning = sh_18inning
    ncaa_baseball.sa_19inning = sa_19inning
    ncaa_baseball.sh_19inning = sh_19inning
    ncaa_baseball.sa_20inning = sa_20inning
    ncaa_baseball.sh_20inning = sh_20inning
    ncaa_baseball.sa_21inning = sa_21inning
    ncaa_baseball.sh_21inning = sh_21inning
    ncaa_baseball.sa_22inning = sa_22inning
    ncaa_baseball.sh_22inning = sh_22inning
    ncaa_baseball.sa_23inning = sa_23inning
    ncaa_baseball.sh_23inning = sh_23inning
    ncaa_baseball.sa_24inning = sa_24inning
    ncaa_baseball.sh_24inning = sh_24inning
    ncaa_baseball.sa_25inning = sa_25inning
    ncaa_baseball.sh_25inning = sh_25inning
    db.session.commit()
    return jsonify({"msg": "ncaa_baseball edith successfully"}), 200


@app.route('/nfl/<id>', methods=['PUT'])
def nflEdit(id):
    nfl = Nfl.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    week = request.json['week']
    status = request.json['status']
    casino = request.json['casino']
    rotation_away = request.json['rotation_away']
    rotation_home = request.json['rotation_home']
    away = request.json['away']
    home = request.json['home']
    spread_away = request.json['spread_away']
    spread_home = request.json['spread_home']
    juice_spread_away = request.json['juice_spread_away']
    juice_spread_home = request.json['juice_spread_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']
    # --
    first_half_spread_away = request.json['first_half_spread_away']
    first_half_spread_home = request.json['first_half_spread_home']
    first_half_juice_spread_away = request.json['first_half_juice_spread_away']
    first_half_juice_spread_home = request.json['first_half_juice_spread_home']
    first_half_moneyLineAway = request.json['first_half_moneyLineAway']
    first_half_moneyLineHome = request.json['first_half_moneyLineHome']
    first_half_total = request.json['first_half_total']
    fh_juice_total_over = request.json['fh_juice_total_over']
    fh_juice_total_under = request.json['fh_juice_total_under']
    first_half_tt_away = request.json['first_half_tt_away']
    first_half_juice_over_away = request.json['first_half_juice_over_away']
    first_half_juice_under_away = request.json['first_half_juice_under_away']
    first_half_tt_home = request.json['first_half_tt_home']
    first_half_juice_over_home = request.json['first_half_juice_over_home']
    first_half_juice_under_home = request.json['first_half_juice_under_home']
    first_half_final_score_away = request.json['first_half_final_score_away']
    first_half_final_score_home = request.json['first_half_final_score_home']
    # --
    second_half_spread_away = request.json['second_half_spread_away']
    second_half_spread_home = request.json['second_half_spread_home']
    second_half_juice_spread_away = request.json['second_half_juice_spread_away']
    second_half_juice_spread_home = request.json['second_half_juice_spread_home']
    second_half_moneyLineAway = request.json['second_half_moneyLineAway']
    second_half_moneyLineHome = request.json['second_half_moneyLineHome']
    second_half_total = request.json['second_half_total']
    sh_juice_total_over = request.json['sh_juice_total_over']
    sh_juice_total_under = request.json['sh_juice_total_under']
    second_half_tt_away = request.json['second_half_tt_away']
    second_half_juice_over_away = request.json['second_half_juice_over_away']
    second_half_juice_under_away = request.json['second_half_juice_under_away']
    second_half_tt_home = request.json['second_half_tt_home']
    second_half_juice_over_home = request.json['second_half_juice_over_home']
    second_half_juice_under_home = request.json['second_half_juice_under_home']
    second_half_final_score_away = request.json['second_half_final_score_away']
    second_half_final_score_home = request.json['second_half_final_score_home']
    # --
    q1_half_spread_away = request.json['q1_half_spread_away']
    q1_half_spread_home = request.json['q1_half_spread_home']
    q1_half_juice_spread_away = request.json['q1_half_juice_spread_away']
    q1_half_juice_spread_home = request.json['q1_half_juice_spread_home']
    q1_half_moneyLineAway = request.json['q1_half_moneyLineAway']
    q1_half_moneyLineHome = request.json['q1_half_moneyLineHome']
    q1_half_total = request.json['q1_half_total']
    q1_juice_over = request.json['q1_juice_over']
    q1_juice_under = request.json['q1_juice_under']
    q1_half_tt_away = request.json['q1_half_tt_away']
    q1_half_juice_over_away = request.json['q1_half_juice_over_away']
    q1_half_juice_under_away = request.json['q1_half_juice_under_away']
    q1_half_tt_home = request.json['q1_half_tt_home']
    q1_half_juice_over_home = request.json['q1_half_juice_over_home']
    q1_half_juice_under_home = request.json['q1_half_juice_under_home']
    q1_half_final_score_away = request.json['q1_half_final_score_away']
    q1_half_final_score_home = request.json['q1_half_final_score_home']
    # --
    q2_half_spread_away = request.json['q2_half_spread_away']
    q2_half_spread_home = request.json['q2_half_spread_home']
    q2_half_juice_spread_away = request.json['q2_half_juice_spread_away']
    q2_half_juice_spread_home = request.json['q2_half_juice_spread_home']
    q2_half_moneyLineAway = request.json['q2_half_moneyLineAway']
    q2_half_moneyLineHome = request.json['q2_half_moneyLineHome']
    q2_half_total = request.json['q2_half_total']
    q2_juice_over = request.json['q2_juice_over']
    q2_juice_under = request.json['q2_juice_under']
    q2_half_tt_away = request.json['q2_half_tt_away']
    q2_half_juice_over_away = request.json['q2_half_juice_over_away']
    q2_half_juice_under_away = request.json['q2_half_juice_under_away']
    q2_half_tt_home = request.json['q2_half_tt_home']
    q2_half_juice_over_home = request.json['q2_half_juice_over_home']
    q2_half_juice_under_home = request.json['q2_half_juice_under_home']
    q2_half_final_score_away = request.json['q2_half_final_score_away']
    q2_half_final_score_home = request.json['q2_half_final_score_home']
    # --
    q3_half_spread_away = request.json['q3_half_spread_away']
    q3_half_spread_home = request.json['q3_half_spread_home']
    q3_half_juice_spread_away = request.json['q3_half_juice_spread_away']
    q3_half_juice_spread_home = request.json['q3_half_juice_spread_home']
    q3_half_moneyLineAway = request.json['q3_half_moneyLineAway']
    q3_half_moneyLineHome = request.json['q3_half_moneyLineHome']
    q3_half_total = request.json['q3_half_total']
    q3_juice_over = request.json['q3_juice_over']
    q3_juice_under = request.json['q3_juice_under']
    q3_half_tt_away = request.json['q3_half_tt_away']
    q3_half_juice_over_away = request.json['q3_half_juice_over_away']
    q3_half_juice_under_away = request.json['q3_half_juice_under_away']
    q3_half_tt_home = request.json['q3_half_tt_home']
    q3_half_juice_over_home = request.json['q3_half_juice_over_home']
    q3_half_juice_under_home = request.json['q3_half_juice_under_home']
    q3_half_final_score_away = request.json['q3_half_final_score_away']
    q3_half_final_score_home = request.json['q3_half_final_score_home']
    # --
    q4_half_spread_away = request.json['q4_half_spread_away']
    q4_half_spread_home = request.json['q4_half_spread_home']
    q4_half_juice_spread_away = request.json['q4_half_juice_spread_away']
    q4_half_juice_spread_home = request.json['q4_half_juice_spread_home']
    q4_half_moneyLineAway = request.json['q4_half_moneyLineAway']
    q4_half_moneyLineHome = request.json['q4_half_moneyLineHome']
    q4_half_total = request.json['q4_half_total']
    q4_juice_over = request.json['q4_juice_over']
    q4_juice_under = request.json['q4_juice_under']
    q4_half_tt_away = request.json['q4_half_tt_away']
    q4_half_juice_over_away = request.json['q4_half_juice_over_away']
    q4_half_juice_under_away = request.json['q4_half_juice_under_away']
    q4_half_tt_home = request.json['q4_half_tt_home']
    q4_half_juice_over_home = request.json['q4_half_juice_over_home']
    q4_half_juice_under_home = request.json['q4_half_juice_under_home']
    q4_half_final_score_away = request.json['q4_half_final_score_away']
    q4_half_final_score_home = request.json['q4_half_final_score_home']

    nfl.date = date
    nfl.hour = hour
    nfl.week = week
    nfl.status = status
    nfl.casino = casino
    nfl.rotation_away = rotation_away
    nfl.rotation_home = rotation_home
    nfl.away = away
    nfl.home = home
    nfl.spread_away = spread_away
    nfl.spread_home = spread_home
    nfl.juice_spread_away = juice_spread_away
    nfl.juice_spread_home = juice_spread_home
    nfl.moneyLineAway = moneyLineAway
    nfl.moneyLineHome = moneyLineHome
    nfl.total = total
    nfl.juice_total_over = juice_total_over
    nfl.juice_total_under = juice_total_under
    nfl.tt_away = tt_away
    nfl.juice_over_away = juice_over_away
    nfl.juice_under_away = juice_under_away
    nfl.tt_home = tt_home
    nfl.juice_over_home = juice_over_home
    nfl.juice_under_home = juice_under_home
    nfl.final_score_away = final_score_away
    nfl.final_score_home = final_score_home

    nfl.first_half_spread_away = first_half_spread_away
    nfl.first_half_spread_home = first_half_spread_home
    nfl.first_half_juice_spread_away = first_half_juice_spread_away
    nfl.first_half_juice_spread_home = first_half_juice_spread_home
    nfl.first_half_moneyLineAway = first_half_moneyLineAway
    nfl.first_half_moneyLineHome = first_half_moneyLineHome
    nfl.first_half_total = first_half_total
    nfl.fh_juice_total_over = fh_juice_total_over
    nfl.fh_juice_total_under = fh_juice_total_under
    nfl.first_half_tt_away = first_half_tt_away
    nfl.first_half_juice_over_away = first_half_juice_over_away
    nfl.first_half_juice_under_away = first_half_juice_under_away
    nfl.first_half_tt_home = first_half_tt_home
    nfl.first_half_juice_over_home = first_half_juice_over_home
    nfl.first_half_juice_under_home = first_half_juice_under_home
    nfl.first_half_final_score_away = first_half_final_score_away
    nfl.first_half_final_score_home = first_half_final_score_home
    # --
    nfl.second_half_spread_away = second_half_spread_away
    nfl.second_half_spread_home = second_half_spread_home
    nfl.second_half_juice_spread_away = second_half_juice_spread_away
    nfl.second_half_juice_spread_home = second_half_juice_spread_home
    nfl.second_half_moneyLineAway = second_half_moneyLineAway
    nfl.second_half_moneyLineHome = second_half_moneyLineHome
    nfl.second_half_total = second_half_total
    nfl.sh_juice_total_over = sh_juice_total_over
    nfl.sh_juice_total_under = sh_juice_total_under
    nfl.second_half_tt_away = second_half_tt_away
    nfl.second_half_juice_over_away = second_half_juice_over_away
    nfl.second_half_juice_under_away = second_half_juice_under_away
    nfl.second_half_tt_home = second_half_tt_home
    nfl.second_half_juice_over_home = second_half_juice_over_home
    nfl.second_half_juice_under_home = second_half_juice_under_home
    nfl.second_half_final_score_away = second_half_final_score_away
    nfl.second_half_final_score_home = second_half_final_score_home
    # --
    nfl.q1_half_spread_away = q1_half_spread_away
    nfl.q1_half_spread_home = q1_half_spread_home
    nfl.q1_half_juice_spread_away = q1_half_juice_spread_away
    nfl.q1_half_juice_spread_home = q1_half_juice_spread_home
    nfl.q1_half_moneyLineAway = q1_half_moneyLineAway
    nfl.q1_half_moneyLineHome = q1_half_moneyLineHome
    nfl.q1_half_total = q1_half_total
    nfl.q1_juice_over = q1_juice_over
    nfl.q1_juice_under = q1_juice_under
    nfl.q1_half_tt_away = q1_half_tt_away
    nfl.q1_half_juice_over_away = q1_half_juice_over_away
    nfl.q1_half_juice_under_away = q1_half_juice_under_away
    nfl.q1_half_tt_home = q1_half_tt_home
    nfl.q1_half_juice_over_home = q1_half_juice_over_home
    nfl.q1_half_juice_under_home = q1_half_juice_under_home
    nfl.q1_half_final_score_away = q1_half_final_score_away
    nfl.q1_half_final_score_home = q1_half_final_score_home
    # --
    nfl.q2_half_spread_away = q2_half_spread_away
    nfl.q2_half_spread_home = q2_half_spread_home
    nfl.q2_half_juice_spread_away = q2_half_juice_spread_away
    nfl.q2_half_juice_spread_home = q2_half_juice_spread_home
    nfl.q2_half_moneyLineAway = q2_half_moneyLineAway
    nfl.q2_half_moneyLineHome = q2_half_moneyLineHome
    nfl.q2_half_total = q2_half_total
    nfl.q2_juice_over = q2_juice_over
    nfl.q2_juice_under = q2_juice_under
    nfl.q2_half_tt_away = q2_half_tt_away
    nfl.q2_half_juice_over_away = q2_half_juice_over_away
    nfl.q2_half_juice_under_away = q2_half_juice_under_away
    nfl.q2_half_tt_home = q2_half_tt_home
    nfl.q2_half_juice_over_home = q2_half_juice_over_home
    nfl.q2_half_juice_under_home = q2_half_juice_under_home
    nfl.q2_half_final_score_away = q2_half_final_score_away
    nfl.q2_half_final_score_home = q2_half_final_score_home
    # --
    nfl.q3_half_spread_away = q3_half_spread_away
    nfl.q3_half_spread_home = q3_half_spread_home
    nfl.q3_half_juice_spread_away = q3_half_juice_spread_away
    nfl.q3_half_juice_spread_home = q3_half_juice_spread_home
    nfl.q3_half_moneyLineAway = q3_half_moneyLineAway
    nfl.q3_half_moneyLineHome = q3_half_moneyLineHome
    nfl.q3_half_total = q3_half_total
    nfl.q3_juice_over = q3_juice_over
    nfl.q3_juice_under = q3_juice_under
    nfl.q3_half_tt_away = q3_half_tt_away
    nfl.q3_half_juice_over_away = q3_half_juice_over_away
    nfl.q3_half_juice_under_away = q3_half_juice_under_away
    nfl.q3_half_tt_home = q3_half_tt_home
    nfl.q3_half_juice_over_home = q3_half_juice_over_home
    nfl.q3_half_juice_under_home = q3_half_juice_under_home
    nfl.q3_half_final_score_away = q3_half_final_score_away
    nfl.q3_half_final_score_home = q3_half_final_score_home
    # --
    nfl.q4_half_spread_away = q4_half_spread_away
    nfl.q4_half_spread_home = q4_half_spread_home
    nfl.q4_half_juice_spread_away = q4_half_juice_spread_away
    nfl.q4_half_juice_spread_home = q4_half_juice_spread_home
    nfl.q4_half_moneyLineAway = q4_half_moneyLineAway
    nfl.q4_half_moneyLineHome = q4_half_moneyLineHome
    nfl.q4_half_total = q4_half_total
    nfl.q4_juice_over = q4_juice_over
    nfl.q4_juice_under = q4_juice_under
    nfl.q4_half_tt_away = q4_half_tt_away
    nfl.q4_half_juice_over_away = q4_half_juice_over_away
    nfl.q4_half_juice_under_away = q4_half_juice_under_away
    nfl.q4_half_tt_home = q4_half_tt_home
    nfl.q4_half_juice_over_home = q4_half_juice_over_home
    nfl.q4_half_juice_under_home = q4_half_juice_under_home
    nfl.q4_half_final_score_away = q4_half_final_score_away
    nfl.q4_half_final_score_home = q4_half_final_score_home
    db.session.commit()
    return jsonify({"msg": "nfl edith successfully"}), 200


@app.route('/ncaa_football/<id>', methods=['PUT'])
def ncaa_footballEdit(id):
    ncaa_football = Ncaa_Football.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    week = request.json['week']
    status = request.json['status']
    away = request.json['away']
    home = request.json['home']
    spread_away = request.json['spread_away']
    spread_home = request.json['spread_home']
    juice_spread_away = request.json['juice_spread_away']
    juice_spread_home = request.json['juice_spread_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']
    # --
    first_half_spread_away = request.json['first_half_spread_away']
    first_half_spread_home = request.json['first_half_spread_home']
    first_half_juice_spread_away = request.json['first_half_juice_spread_away']
    first_half_juice_spread_home = request.json['first_half_juice_spread_home']
    first_half_moneyLineAway = request.json['first_half_moneyLineAway']
    first_half_moneyLineHome = request.json['first_half_moneyLineHome']
    first_half_total = request.json['first_half_total']
    fh_juice_total_over = request.json['fh_juice_total_over']
    fh_juice_total_under = request.json['fh_juice_total_under']
    first_half_tt_away = request.json['first_half_tt_away']
    first_half_juice_over_away = request.json['first_half_juice_over_away']
    first_half_juice_under_away = request.json['first_half_juice_under_away']
    first_half_tt_home = request.json['first_half_tt_home']
    first_half_juice_over_home = request.json['first_half_juice_over_home']
    first_half_juice_under_home = request.json['first_half_juice_under_home']
    first_half_final_score_away = request.json['first_half_final_score_away']
    first_half_final_score_home = request.json['first_half_final_score_home']
    # --
    second_half_spread_away = request.json['second_half_spread_away']
    second_half_spread_home = request.json['second_half_spread_home']
    second_half_juice_spread_away = request.json['second_half_juice_spread_away']
    second_half_juice_spread_home = request.json['second_half_juice_spread_home']
    second_half_moneyLineAway = request.json['second_half_moneyLineAway']
    second_half_moneyLineHome = request.json['second_half_moneyLineHome']
    second_half_total = request.json['second_half_total']
    sh_juice_total_over = request.json['sh_juice_total_over']
    sh_juice_total_under = request.json['sh_juice_total_under']
    second_half_tt_away = request.json['second_half_tt_away']
    second_half_juice_over_away = request.json['second_half_juice_over_away']
    second_half_juice_under_away = request.json['second_half_juice_under_away']
    second_half_tt_home = request.json['second_half_tt_home']
    second_half_juice_over_home = request.json['second_half_juice_over_home']
    second_half_juice_under_home = request.json['second_half_juice_under_home']
    second_half_final_score_away = request.json['second_half_final_score_away']
    second_half_final_score_home = request.json['second_half_final_score_home']
    # --
    q1_half_spread_away = request.json['q1_half_spread_away']
    q1_half_spread_home = request.json['q1_half_spread_home']
    q1_half_juice_spread_away = request.json['q1_half_juice_spread_away']
    q1_half_juice_spread_home = request.json['q1_half_juice_spread_home']
    q1_half_moneyLineAway = request.json['q1_half_moneyLineAway']
    q1_half_moneyLineHome = request.json['q1_half_moneyLineHome']
    q1_half_total = request.json['q1_half_total']
    q1_juice_over = request.json['q1_juice_over']
    q1_juice_under = request.json['q1_juice_under']
    q1_half_tt_away = request.json['q1_half_tt_away']
    q1_half_juice_over_away = request.json['q1_half_juice_over_away']
    q1_half_juice_under_away = request.json['q1_half_juice_under_away']
    q1_half_tt_home = request.json['q1_half_tt_home']
    q1_half_juice_over_home = request.json['q1_half_juice_over_home']
    q1_half_juice_under_home = request.json['q1_half_juice_under_home']
    q1_half_final_score_away = request.json['q1_half_final_score_away']
    q1_half_final_score_home = request.json['q1_half_final_score_home']

    ncaa_football.date = date
    ncaa_football.hour = hour
    ncaa_football.week = week
    ncaa_football.status = status
    ncaa_football.away = away
    ncaa_football.home = home
    ncaa_football.spread_away = spread_away
    ncaa_football.spread_home = spread_home
    ncaa_football.juice_spread_away = juice_spread_away
    ncaa_football.juice_spread_home = juice_spread_home
    ncaa_football.moneyLineAway = moneyLineAway
    ncaa_football.moneyLineHome = moneyLineHome
    ncaa_football.total = total
    ncaa_football.juice_total_over = juice_total_over
    ncaa_football.juice_total_under = juice_total_under
    ncaa_football.tt_away = tt_away
    ncaa_football.juice_over_away = juice_over_away
    ncaa_football.juice_under_away = juice_under_away
    ncaa_football.tt_home = tt_home
    ncaa_football.juice_over_home = juice_over_home
    ncaa_football.juice_under_home = juice_under_home
    ncaa_football.final_score_away = final_score_away
    ncaa_football.final_score_home = final_score_home

    ncaa_football.first_half_spread_away = first_half_spread_away
    ncaa_football.first_half_spread_home = first_half_spread_home
    ncaa_football.first_half_juice_spread_away = first_half_juice_spread_away
    ncaa_football.first_half_juice_spread_home = first_half_juice_spread_home
    ncaa_football.first_half_moneyLineAway = first_half_moneyLineAway
    ncaa_football.first_half_moneyLineHome = first_half_moneyLineHome
    ncaa_football.first_half_total = first_half_total
    ncaa_football.fh_juice_total_over = fh_juice_total_over
    ncaa_football.fh_juice_total_under = fh_juice_total_under
    ncaa_football.first_half_tt_away = first_half_tt_away
    ncaa_football.first_half_juice_over_away = first_half_juice_over_away
    ncaa_football.first_half_juice_under_away = first_half_juice_under_away
    ncaa_football.first_half_tt_home = first_half_tt_home
    ncaa_football.first_half_juice_over_home = first_half_juice_over_home
    ncaa_football.first_half_juice_under_home = first_half_juice_under_home
    ncaa_football.first_half_final_score_away = first_half_final_score_away
    ncaa_football.first_half_final_score_home = first_half_final_score_home
    # --
    ncaa_football.second_half_spread_away = second_half_spread_away
    ncaa_football.second_half_spread_home = second_half_spread_home
    ncaa_football.second_half_juice_spread_away = second_half_juice_spread_away
    ncaa_football.second_half_juice_spread_home = second_half_juice_spread_home
    ncaa_football.second_half_moneyLineAway = second_half_moneyLineAway
    ncaa_football.second_half_moneyLineHome = second_half_moneyLineHome
    ncaa_football.second_half_total = second_half_total
    ncaa_football.sh_juice_total_over = sh_juice_total_over
    ncaa_football.sh_juice_total_under = sh_juice_total_under
    ncaa_football.second_half_tt_away = second_half_tt_away
    ncaa_football.second_half_juice_over_away = second_half_juice_over_away
    ncaa_football.second_half_juice_under_away = second_half_juice_under_away
    ncaa_football.second_half_tt_home = second_half_tt_home
    ncaa_football.second_half_juice_over_home = second_half_juice_over_home
    ncaa_football.second_half_juice_under_home = second_half_juice_under_home
    ncaa_football.second_half_final_score_away = second_half_final_score_away
    ncaa_football.second_half_final_score_home = second_half_final_score_home
    # --
    ncaa_football.q1_half_spread_away = q1_half_spread_away
    ncaa_football.q1_half_spread_home = q1_half_spread_home
    ncaa_football.q1_half_juice_spread_away = q1_half_juice_spread_away
    ncaa_football.q1_half_juice_spread_home = q1_half_juice_spread_home
    ncaa_football.q1_half_moneyLineAway = q1_half_moneyLineAway
    ncaa_football.q1_half_moneyLineHome = q1_half_moneyLineHome
    ncaa_football.q1_half_total = q1_half_total
    ncaa_football.q1_juice_over = q1_juice_over
    ncaa_football.q1_juice_under = q1_juice_under
    ncaa_football.q1_half_tt_away = q1_half_tt_away
    ncaa_football.q1_half_juice_over_away = q1_half_juice_over_away
    ncaa_football.q1_half_juice_under_away = q1_half_juice_under_away
    ncaa_football.q1_half_tt_home = q1_half_tt_home
    ncaa_football.q1_half_juice_over_home = q1_half_juice_over_home
    ncaa_football.q1_half_juice_under_home = q1_half_juice_under_home
    ncaa_football.q1_half_final_score_away = q1_half_final_score_away
    ncaa_football.q1_half_final_score_home = q1_half_final_score_home
    db.session.commit()
    return jsonify({"msg": "nfl edith successfully"}), 200


@app.route('/nba/<id>', methods=['PUT'])
def nbaEdit(id):
    nba = Nba.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    status = request.json['status']
    preview = request.json['preview']
    img_preview = request.json['img_preview']
    away = request.json['away']
    home = request.json['home']
    spread_away = request.json['spread_away']
    spread_home = request.json['spread_home']
    juice_spread_away = request.json['juice_spread_away']
    juice_spread_home = request.json['juice_spread_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']

    first_half_spread_away = request.json['first_half_spread_away']
    first_half_spread_home = request.json['first_half_spread_home']
    first_half_juice_spread_away = request.json['first_half_juice_spread_away']
    first_half_juice_spread_home = request.json['first_half_juice_spread_home']
    first_half_moneyLineHome = request.json['first_half_moneyLineHome']
    first_half_moneyLineAway = request.json['first_half_moneyLineAway']
    first_half_total = request.json['first_half_total']
    first_half_juice_total = request.json['first_half_juice_total']
    first_half_tt_away = request.json['first_half_tt_away']
    first_half_tt_home = request.json['first_half_tt_home']
    first_half_juice_over_away = request.json['first_half_juice_over_away']
    first_half_juice_over_home = request.json['first_half_juice_over_home']
    first_half_juice_under_away = request.json['first_half_juice_under_away']
    first_half_juice_under_home = request.json['first_half_juice_under_home']
    first_half_juice_over_away = request.json['first_half_juice_over_away']
    first_half_juice_over_home = request.json['first_half_juice_over_home']
    first_half_juice_under_away = request.json['first_half_juice_under_away']
    first_half_juice_under_home = request.json['first_half_juice_under_home']
    first_half_final_score_away = request.json['first_half_final_score_away']
    first_half_final_score_home = request.json['first_half_final_score_home']
    second_half_spread_away = request.json['second_half_spread_away']
    second_half_spread_home = request.json['second_half_spread_home']
    second_half_juice_spread_away = request.json['second_half_juice_spread_away']
    second_half_juice_spread_home = request.json['second_half_juice_spread_home']
    second_half_moneyLineHome = request.json['second_half_moneyLineHome']
    second_half_moneyLineAway = request.json['second_half_moneyLineAway']
    second_half_total = request.json['second_half_total']
    second_half_juice_total = request.json['second_half_juice_total']
    second_half_tt_away = request.json['second_half_tt_away']
    second_half_tt_home = request.json['second_half_tt_home']
    second_half_juice_over_away = request.json['second_half_juice_over_away']
    second_half_juice_over_home = request.json['second_half_juice_over_home']
    second_half_juice_under_away = request.json['second_half_juice_under_away']
    second_half_juice_under_home = request.json['second_half_juice_under_home']
    second_half_final_score_away = request.json['second_half_final_score_away']
    second_half_final_score_home = request.json['second_half_final_score_home']
    q1_half_spread_away = request.json['q1_half_spread_away']
    q1_half_spread_home = request.json['q1_half_spread_home']
    q1_half_juice_spread_away = request.json['q1_half_juice_spread_away']
    q1_half_juice_spread_home = request.json['q1_half_juice_spread_home']
    q1_half_moneyLineHome = request.json['q1_half_moneyLineHome']
    q1_half_moneyLineAway = request.json['q1_half_moneyLineAway']
    q1_half_total = request.json['q1_half_total']
    q1_juice_over = request.json['q1_juice_over']
    q1_juice_under = request.json['q1_juice_under']
    q1_half_tt_away = request.json['q1_half_tt_away']
    q1_half_tt_home = request.json['q1_half_tt_home']
    q1_half_juice_over_away = request.json['q1_half_juice_over_away']
    q1_half_juice_over_home = request.json['q1_half_juice_over_home']
    q1_half_final_score_away = request.json['q1_half_final_score_away']
    q1_half_final_score_home = request.json['q1_half_final_score_home']

    nba.date = date
    nba.hour = hour
    nba.preview = preview
    nba.img_preview = img_preview
    nba.status = status
    nba.away = away
    nba.home = home
    nba.spread_away = spread_away
    nba.spread_home = spread_home
    nba.juice_spread_away = juice_spread_away
    nba.juice_spread_home = juice_spread_home
    nba.moneyLineAway = moneyLineAway
    nba.moneyLineHome = moneyLineHome
    nba.total = total
    nba.juice_total_over = juice_total_over
    nba.juice_total_under = juice_total_under
    nba.tt_away = tt_away
    nba.juice_over_away = juice_over_away
    nba.juice_under_away = juice_under_away
    nba.tt_home = tt_home
    nba.juice_over_home = juice_over_home
    nba.juice_under_home = juice_under_home
    nba.final_score_away = final_score_away
    nba.final_score_home = final_score_home
    nba.final_score_home = final_score_home

    nba.first_half_spread_away = first_half_spread_away
    nba.first_half_spread_home = first_half_spread_home
    nba.first_half_juice_spread_away = first_half_juice_spread_away
    nba.first_half_juice_spread_home = first_half_juice_spread_home
    nba.first_half_moneyLineAway = first_half_moneyLineAway
    nba.first_half_moneyLineHome = first_half_moneyLineHome
    nba.first_half_total = first_half_total
    nba.fh_juice_total_over = fh_juice_total_over
    nba.fh_juice_total_under = fh_juice_total_under
    nba.first_half_tt_away = first_half_tt_away
    nba.first_half_juice_over_away = first_half_juice_over_away
    nba.first_half_juice_under_away = first_half_juice_under_away
    nba.first_half_tt_home = first_half_tt_home
    nba.first_half_juice_over_home = first_half_juice_over_home
    nba.first_half_juice_under_home = first_half_juice_under_home
    nba.first_half_final_score_away = first_half_final_score_away
    nba.first_half_final_score_home = first_half_final_score_home
    nba.second_half_spread_away = second_half_spread_away
    nba.second_half_spread_home = second_half_spread_home
    nba.second_half_juice_spread_away = second_half_juice_spread_away
    nba.second_half_juice_spread_home = second_half_juice_spread_home
    nba.second_half_moneyLineAway = second_half_moneyLineAway
    nba.second_half_moneyLineHome = second_half_moneyLineHome
    nba.second_half_total = second_half_total
    nba.sh_juice_total_over = sh_juice_total_over
    nba.sh_juice_total_under = sh_juice_total_under
    nba.second_half_tt_away = second_half_tt_away
    nba.second_half_juice_over_away = second_half_juice_over_away
    nba.second_half_juice_under_away = second_half_juice_under_away
    nba.second_half_tt_home = second_half_tt_home
    nba.second_half_juice_over_home = second_half_juice_over_home
    nba.second_half_juice_under_home = second_half_juice_under_home
    nba.second_half_final_score_away = second_half_final_score_away
    nba.second_half_final_score_home = second_half_final_score_home
    nba.q1_half_spread_away = q1_half_spread_away
    nba.q1_half_spread_home = q1_half_spread_home
    nba.q1_half_juice_spread_away = q1_half_juice_spread_away
    nba.q1_half_juice_spread_home = q1_half_juice_spread_home
    nba.q1_half_moneyLineAway = q1_half_moneyLineAway
    nba.q1_half_moneyLineHome = q1_half_moneyLineHome
    nba.q1_half_total = q1_half_total
    nba.q1_juice_over = q1_juice_over
    nba.q1_juice_under = q1_juice_under
    nba.q1_half_tt_away = q1_half_tt_away
    nba.q1_half_juice_over_away = q1_half_juice_over_away
    nba.q1_half_juice_under_away = q1_half_juice_under_away
    nba.q1_half_tt_home = q1_half_tt_home
    nba.q1_half_juice_over_home = q1_half_juice_over_home
    nba.q1_half_juice_under_home = q1_half_juice_under_home
    nba.q1_half_final_score_away = q1_half_final_score_away
    nba.q1_half_final_score_home = q1_half_final_score_home
    db.session.commit()
    return jsonify({"msg": "nba edith successfully"}), 200


@app.route('/ncaa_basketball/<id>', methods=['PUT'])
def ncaa_basketballEdit(id):
    ncaa_basketball = Ncaa_Basketball.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    status = request.json['status']
    preview = request.json['preview']
    img_preview = request.json['img_preview']
    away = request.json['away']
    home = request.json['home']
    spread_away = request.json['spread_away']
    spread_home = request.json['spread_home']
    juice_spread_away = request.json['juice_spread_away']
    juice_spread_home = request.json['juice_spread_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']

    first_half_spread_away = request.json['first_half_spread_away']
    first_half_spread_home = request.json['first_half_spread_home']
    first_half_juice_spread_away = request.json['first_half_juice_spread_away']
    first_half_juice_spread_home = request.json['first_half_juice_spread_home']
    first_half_moneyLineHome = request.json['first_half_moneyLineHome']
    first_half_moneyLineAway = request.json['first_half_moneyLineAway']
    first_half_total = request.json['first_half_total']
    first_half_juice_total = request.json['first_half_juice_total']
    first_half_tt_away = request.json['first_half_tt_away']
    first_half_tt_home = request.json['first_half_tt_home']
    first_half_juice_over_away = request.json['first_half_juice_over_away']
    first_half_juice_over_home = request.json['first_half_juice_over_home']
    first_half_juice_under_away = request.json['first_half_juice_under_away']
    first_half_juice_under_home = request.json['first_half_juice_under_home']
    first_half_juice_over_away = request.json['first_half_juice_over_away']
    first_half_juice_over_home = request.json['first_half_juice_over_home']
    first_half_juice_under_away = request.json['first_half_juice_under_away']
    first_half_juice_under_home = request.json['first_half_juice_under_home']
    first_half_final_score_away = request.json['first_half_final_score_away']
    first_half_final_score_home = request.json['first_half_final_score_home']
    second_half_spread_away = request.json['second_half_spread_away']
    second_half_spread_home = request.json['second_half_spread_home']
    second_half_juice_spread_away = request.json['second_half_juice_spread_away']
    second_half_juice_spread_home = request.json['second_half_juice_spread_home']
    second_half_moneyLineHome = request.json['second_half_moneyLineHome']
    second_half_moneyLineAway = request.json['second_half_moneyLineAway']
    second_half_total = request.json['second_half_total']
    second_half_juice_total = request.json['second_half_juice_total']
    second_half_tt_away = request.json['second_half_tt_away']
    second_half_tt_home = request.json['second_half_tt_home']
    second_half_juice_over_away = request.json['second_half_juice_over_away']
    second_half_juice_over_home = request.json['second_half_juice_over_home']
    second_half_juice_under_away = request.json['second_half_juice_under_away']
    second_half_juice_under_home = request.json['second_half_juice_under_home']
    second_half_final_score_away = request.json['second_half_final_score_away']
    second_half_final_score_home = request.json['second_half_final_score_home']
    q1_half_spread_away = request.json['q1_half_spread_away']
    q1_half_spread_home = request.json['q1_half_spread_home']
    q1_half_juice_spread_away = request.json['q1_half_juice_spread_away']
    q1_half_juice_spread_home = request.json['q1_half_juice_spread_home']
    q1_half_moneyLineHome = request.json['q1_half_moneyLineHome']
    q1_half_moneyLineAway = request.json['q1_half_moneyLineAway']
    q1_half_total = request.json['q1_half_total']
    q1_juice_over = request.json['q1_juice_over']
    q1_juice_under = request.json['q1_juice_under']
    q1_half_tt_away = request.json['q1_half_tt_away']
    q1_half_tt_home = request.json['q1_half_tt_home']
    q1_half_juice_over_away = request.json['q1_half_juice_over_away']
    q1_half_juice_over_home = request.json['q1_half_juice_over_home']
    q1_half_final_score_away = request.json['q1_half_final_score_away']
    q1_half_final_score_home = request.json['q1_half_final_score_home']

    ncaa_basketball.date = date
    ncaa_basketball.hour = hour
    ncaa_basketball.preview = preview
    ncaa_basketball.img_preview = img_preview
    ncaa_basketball.status = status
    ncaa_basketball.away = away
    ncaa_basketball.home = home
    ncaa_basketball.spread_away = spread_away
    ncaa_basketball.spread_home = spread_home
    ncaa_basketball.juice_spread_away = juice_spread_away
    ncaa_basketball.juice_spread_home = juice_spread_home
    ncaa_basketball.moneyLineAway = moneyLineAway
    ncaa_basketball.moneyLineHome = moneyLineHome
    ncaa_basketball.total = total
    ncaa_basketball.juice_total_over = juice_total_over
    ncaa_basketball.juice_total_under = juice_total_under
    ncaa_basketball.tt_away = tt_away
    ncaa_basketball.juice_over_away = juice_over_away
    ncaa_basketball.juice_under_away = juice_under_away
    ncaa_basketball.tt_home = tt_home
    ncaa_basketball.juice_over_home = juice_over_home
    ncaa_basketball.juice_under_home = juice_under_home
    ncaa_basketball.final_score_away = final_score_away
    ncaa_basketball.final_score_home = final_score_home
    ncaa_basketball.final_score_home = final_score_home

    ncaa_basketball.first_half_spread_away = first_half_spread_away
    ncaa_basketball.first_half_spread_home = first_half_spread_home
    ncaa_basketball.first_half_juice_spread_away = first_half_juice_spread_away
    ncaa_basketball.first_half_juice_spread_home = first_half_juice_spread_home
    ncaa_basketball.first_half_moneyLineAway = first_half_moneyLineAway
    ncaa_basketball.first_half_moneyLineHome = first_half_moneyLineHome
    ncaa_basketball.first_half_total = first_half_total
    ncaa_basketball.fh_juice_total_over = fh_juice_total_over
    ncaa_basketball.fh_juice_total_under = fh_juice_total_under
    ncaa_basketball.first_half_tt_away = first_half_tt_away
    ncaa_basketball.first_half_juice_over_away = first_half_juice_over_away
    ncaa_basketball.first_half_juice_under_away = first_half_juice_under_away
    ncaa_basketball.first_half_tt_home = first_half_tt_home
    ncaa_basketball.first_half_juice_over_home = first_half_juice_over_home
    ncaa_basketball.first_half_juice_under_home = first_half_juice_under_home
    ncaa_basketball.first_half_final_score_away = first_half_final_score_away
    ncaa_basketball.first_half_final_score_home = first_half_final_score_home
    ncaa_basketball.second_half_spread_away = second_half_spread_away
    ncaa_basketball.second_half_spread_home = second_half_spread_home
    ncaa_basketball.second_half_juice_spread_away = second_half_juice_spread_away
    ncaa_basketball.second_half_juice_spread_home = second_half_juice_spread_home
    ncaa_basketball.second_half_moneyLineAway = second_half_moneyLineAway
    ncaa_basketball.second_half_moneyLineHome = second_half_moneyLineHome
    ncaa_basketball.second_half_total = second_half_total
    ncaa_basketball.sh_juice_total_over = sh_juice_total_over
    ncaa_basketball.sh_juice_total_under = sh_juice_total_under
    ncaa_basketball.second_half_tt_away = second_half_tt_away
    ncaa_basketball.second_half_juice_over_away = second_half_juice_over_away
    ncaa_basketball.second_half_juice_under_away = second_half_juice_under_away
    ncaa_basketball.second_half_tt_home = second_half_tt_home
    ncaa_basketball.second_half_juice_over_home = second_half_juice_over_home
    ncaa_basketball.second_half_juice_under_home = second_half_juice_under_home
    ncaa_basketball.second_half_final_score_away = second_half_final_score_away
    ncaa_basketball.second_half_final_score_home = second_half_final_score_home
    ncaa_basketball.q1_half_spread_away = q1_half_spread_away
    ncaa_basketball.q1_half_spread_home = q1_half_spread_home
    ncaa_basketball.q1_half_juice_spread_away = q1_half_juice_spread_away
    ncaa_basketball.q1_half_juice_spread_home = q1_half_juice_spread_home
    ncaa_basketball.q1_half_moneyLineAway = q1_half_moneyLineAway
    ncaa_basketball.q1_half_moneyLineHome = q1_half_moneyLineHome
    ncaa_basketball.q1_half_total = q1_half_total
    ncaa_basketball.q1_juice_over = q1_juice_over
    ncaa_basketball.q1_juice_under = q1_juice_under
    ncaa_basketball.q1_half_tt_away = q1_half_tt_away
    ncaa_basketball.q1_half_juice_over_away = q1_half_juice_over_away
    ncaa_basketball.q1_half_juice_under_away = q1_half_juice_under_away
    ncaa_basketball.q1_half_tt_home = q1_half_tt_home
    ncaa_basketball.q1_half_juice_over_home = q1_half_juice_over_home
    ncaa_basketball.q1_half_juice_under_home = q1_half_juice_under_home
    ncaa_basketball.q1_half_final_score_away = q1_half_final_score_away
    ncaa_basketball.q1_half_final_score_home = q1_half_final_score_home
    db.session.commit()
    return jsonify({"msg": "ncaa_basketball edith successfully"}), 200


@app.route('/nhl/<id>', methods=['PUT'])
def nhlEdit(id):
    nhl = Nhl.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    status = request.json['status']
    preview = request.json['preview']
    img_preview = request.json['img_preview']
    away = request.json['away']
    home = request.json['home']
    puck_line_away = request.json['puck_line_away']
    puck_line_home = request.json['puck_line_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']
    puck_away_1Q = request.json['puck_away_1Q']
    puck_home_1Q = request.json['puck_home_1Q']
    juice_puck_away_1Q = request.json['juice_puck_away_1Q']
    juice_puck_home_1Q = request.json['juice_puck_home_1Q']
    moneyLineAway_1Q = request.json['moneyLineAway_1Q']
    moneyLineHome_1Q = request.json['moneyLineHome_1Q']
    total_1Q = request.json['total_1Q']
    Q1_juice_over = request.json['Q1_juice_over']
    Q1_juice_under = request.json['Q1_juice_under']
    tt_away_1Q = request.json['tt_away_1Q']
    juice_over_away_1Q = request.json['juice_over_away_1Q']
    juice_under_away_1Q = request.json['juice_under_away_1Q']
    tt_home_1Q = request.json['tt_home_1Q']
    juice_over_home_1Q = request.json['juice_over_home_1Q']
    juice_under_home_1Q = request.json['juice_under_home_1Q']
    sa_1Q = request.json['sa_1Q']
    sh_1Q = request.json['sh_1Q']
    sa_2Q = request.json['sa_2Q']
    sh_2Q = request.json['sh_2Q']
    sa_3Q = request.json['sa_3Q']
    sh_3Q = request.json['sh_3Q']

    nhl.date = date
    nhl.hour = hour
    nhl.week = week
    nhl.preview = preview
    nhl.img_preview = img_preview
    nhl.status = status
    nhl.away = away
    nhl.home = home
    nhl.puck_line_away = puck_line_away
    nhl.puck_line_home = puck_line_home
    nhl.juice_puck_away = juice_puck_away
    nhl.juice_puck_home = juice_puck_home
    nhl.moneyLineAway = moneyLineAway
    nhl.moneyLineHome = moneyLineHome
    nhl.total = total
    nhl.juice_total_over = juice_total_over
    nhl.juice_total_under = juice_total_under
    nhl.tt_away = tt_away
    nhl.juice_over_away = juice_over_away
    nhl.juice_under_away = juice_under_away
    nhl.tt_home = tt_home
    nhl.juice_over_home = juice_over_home
    nhl.juice_under_home = juice_under_home
    nhl.final_score_away = final_score_away
    nhl.final_score_home = final_score_home
    nhl.final_score_home = final_score_home
    nhl.puck_away_1Q = puck_away_1Q
    nhl.puck_home_1Q = puck_home_1Q
    nhl.moneyLineAway_1Q = moneyLineAway_1Q
    nhl.moneyLineHome_1Q = first_half_juice_spread_home
    nhl.total_1Q = total_1Q
    nhl.Q1_juice_over = Q1_juice_over
    nhl.Q1_juice_under = Q1_juice_under
    nhl.tt_away_1Q = tt_away_1Q
    nhl.juice_over_away_1Q = juice_over_away_1Q
    nhl.juice_under_away_1Q = juice_under_away_1Q
    nhl.tt_home_1Q = tt_home_1Q
    nhl.juice_over_home_1Q = juice_over_home_1Q
    nhl.juice_under_home_1Q = juice_under_home_1Q
    nhl.sa_1Q = sa_1Q
    nhl.sh_1Q = sh_1Q
    nhl.sa_2Q = sa_2Q
    nhl.sh_2Q = sh_2Q
    nhl.sa_3Q = sa_3Q
    nhl.sh_3Q = sh_3Q
    db.session.commit()
    return jsonify({"msg": "nhl edith successfully"}), 200


@app.route('/boxeo/<id>', methods=['PUT'])
def boxeoEdit(id):
    boxeo = Boxeo.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    week = request.json['week']
    status = request.json['status']
    preview = request.json['preview']
    img_preview = request.json['img_preview']

    event = request.json['event']
    rounds = request.json['rounds']
    location_Fight = request.json['location_Fight']
    fighter_One = request.json['fighter_One']
    money_Line_One = request.json['money_Line_One']
    fighter_Two = request.json['fighter_Two']
    money_Line_Two = request.json['money_Line_Two']
    finish_by = request.json['finish_by']
    r1_result = request.json['r1_result']
    r2_result = request.json['r2_result']
    r3_result = request.json['r3_result']
    r4_result = request.json['r4_result']
    r5_result = request.json['r5_result']
    r6_result = request.json['r6_result']
    r7_result = request.json['r7_result']
    r8_result = request.json['r8_result']
    r9_result = request.json['r9_result']
    r10_result = request.json['r10_result']
    r11_result = request.json['r11_result']
    r12_result = request.json['r12_result']
    r13_result = request.json['r13_result']
    r14_result = request.json['r14_result']
    r15_result = request.json['r15_result']

    boxeo.date = date
    boxeo.hour = hour
    boxeo.week = week
    boxeo.status = status
    boxeo.preview = preview
    boxeo.img_preview = img_preview
    boxeo.event = event
    boxeo.rounds = rounds
    boxeo.location_Fight = location_Fight
    boxeo.fighter_One = fighter_One
    boxeo.money_Line_One = money_Line_One
    boxeo.fighter_Two = fighter_Two
    boxeo.money_Line_Two = money_Line_Two
    boxeo.winner = winner
    boxeo.finish_by = finish_by
    boxeo.r1_result = r1_result
    boxeo.r2_result = r2_result
    boxeo.r3_result = r3_result
    boxeo.r4_result = r4_result
    boxeo.r5_result = r5_result
    boxeo.r6_result = r6_result
    boxeo.r7_result = r7_result
    boxeo.r8_result = r8_result
    boxeo.r9_result = r9_result
    boxeo.r10_result = r10_result
    boxeo.r11_result = r11_result
    boxeo.r12_result = r12_result
    boxeo.r13_result = r13_result
    boxeo.r14_result = r14_result
    boxeo.r15_result = r15_result

    db.session.commit()
    return jsonify({"msg": "boxeo edith successfully"}), 200


@app.route('/mma/<id>', methods=['PUT'])
def mmaEdit(id):
    mma = Mma.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    week = request.json['week']
    status = request.json['status']
    preview = request.json['preview']
    img_preview = request.json['img_preview']

    event = request.json['event']
    rounds = request.json['rounds']
    location_Fight = request.json['location_Fight']
    fighter_One = request.json['fighter_One']
    money_Line_One = request.json['money_Line_One']
    fighter_Two = request.json['fighter_Two']
    money_Line_Two = request.json['money_Line_Two']
    finish_by = request.json['finish_by']
    r1_result = request.json['r1_result']
    r2_result = request.json['r2_result']
    r3_result = request.json['r3_result']
    r4_result = request.json['r4_result']
    r5_result = request.json['r5_result']
    r6_result = request.json['r6_result']
    r7_result = request.json['r7_result']
    r8_result = request.json['r8_result']
    r9_result = request.json['r9_result']
    r10_result = request.json['r10_result']
    r11_result = request.json['r11_result']
    r12_result = request.json['r12_result']
    r13_result = request.json['r13_result']
    r14_result = request.json['r14_result']
    r15_result = request.json['r15_result']

    mma.date = date
    mma.hour = hour
    mma.week = week
    mma.status = status
    mma.preview = preview
    mma.img_preview = img_preview
    mma.event = event
    mma.rounds = rounds
    mma.location_Fight = location_Fight
    mma.fighter_One = fighter_One
    mma.money_Line_One = money_Line_One
    mma.fighter_Two = fighter_Two
    mma.money_Line_Two = money_Line_Two
    mma.winner = winner
    mma.finish_by = finish_by
    mma.r1_result = r1_result
    mma.r2_result = r2_result
    mma.r3_result = r3_result
    mma.r4_result = r4_result
    mma.r5_result = r5_result
    mma.r6_result = r6_result
    mma.r7_result = r7_result
    mma.r8_result = r8_result
    mma.r9_result = r9_result
    mma.r10_result = r10_result
    mma.r11_result = r11_result
    mma.r12_result = r12_result
    mma.r13_result = r13_result
    mma.r14_result = r14_result
    mma.r15_result = r15_result

    db.session.commit()
    return jsonify({"msg": "mma edith successfully"}), 200


@app.route('/nascar/<id>', methods=['PUT'])
def nascarEdit(id):
    nascar = Nascar.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    week = request.json['week']
    status = request.json['status']
    preview = request.json['preview']
    img_preview = request.json['img_preview']
    race = request.json['race']
    track = request.json['track']
    location = request.json['location']
    place1 = request.json['place1']
    place2 = request.json['place2']
    place3 = request.json['place3']

    nascar.date = date
    nascar.hour = hour
    nascar.week = week
    nascar.status = status
    nascar.preview = preview
    nascar.img_preview = img_preview
    nascar.race = race
    nascar.track = track
    nascar.location = location
    nascar.place1 = place1
    nascar.place2 = place2
    nascar.place3 = place3

    db.session.commit()
    return jsonify({"msg": "nascar edith successfully"}), 200


@app.route('/nascar_drivers/<id>', methods=['PUT'])
def nascar_driversEdit(id):
    nascar_drivers = Nascar_drivers.query.get(id)
    name = request.json['name']
    country = request.json['country']
    birth = request.json['birth']
    sponsor = request.json['sponsor']
    engine = request.json['engine']
    number_car = request.json['number_car']
    rank = request.json['rank']
    starts = request.json['starts']
    poles = request.json['poles']
    top5 = request.json['top5']
    top10 = request.json['top10']
    laps_lead = request.json['laps_lead']
    pts = request.json['pts']
    AVG_laps = request.json['AVG_laps']
    AVG_finish = request.json['AVG_finish']

    nascar_drivers.name = name
    nascar_drivers.country = country
    nascar_drivers.birth = birth
    nascar_drivers.sponsor = sponsor
    nascar_drivers.engine = engine
    nascar_drivers.number_car = number_car
    nascar_drivers.rank = rank
    nascar_drivers.starts = starts
    nascar_drivers.poles = poles
    nascar_drivers.top5 = top5
    nascar_drivers.top10 = top10
    nascar_drivers.laps_lead = laps_lead
    nascar_drivers.pts = pts
    nascar_drivers.AVG_laps = AVG_laps
    nascar_drivers.AVG_finish = AVG_finish

    db.session.commit()
    return jsonify({"msg": "nascar_drivers edith successfully"}), 200


@app.route('/match_ups_nascar/<id>', methods=['PUT'])
def match_ups_nascarEdit(id):
    match_ups_nascar = Match_Ups_Nacar.query.get(id)
    name1 = request.json['name1']
    mu1 = request.json['mu1']
    name2 = request.json['name2']
    mu2 = request.json['mu2']
    match_ups_nascar.name1 = name1
    match_ups_nascar.mu1 = mu1
    match_ups_nascar.name2 = name2
    match_ups_nascar.mu2 = mu2

    db.session.commit()
    return jsonify({"msg": "match_ups_nascar edith successfully"}), 200


@app.route('/golf/<id>', methods=['PUT'])
def golfEdit(id):
    golf = Golf.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    week = request.json['week']
    preview = request.json['preview']
    img_preview = request.json['img_preview']
    status = request.json['status']
    event = request.json['event']
    location = request.json['location']
    place1 = request.json['place1']
    place2 = request.json['place2']
    place3 = request.json['place3']

    golf.date = date
    golf.hour = hour
    golf.week = week
    golf.preview = preview
    golf.img_preview = img_preview
    golf.status = status
    golf.event = event
    golf.location = location
    golf.place1 = place1
    golf.place2 = place2
    golf.place3 = place3

    db.session.commit()
    return jsonify({"msg": "golf edith successfully"}), 200


@app.route('/golfer/<id>', methods=['PUT'])
def golferEdit(id):
    golfer = Golfer.query.get(id)
    country = request.json['country']
    swing = request.json['swing']
    birth = request.json['birth']
    cuts = request.json['cuts']
    top10 = request.json['top10']
    w = request.json['w']
    rnds = request.json['rnds']
    holes = request.json['holes']
    avg = request.json['avg']

    golfer.country = country
    golfer.swing = swing
    golfer.birth = birth
    golfer.cuts = cuts
    golfer.top10 = top10
    golfer.w = w
    golfer.rnds = rnds
    golfer.holes = holes
    golfer.avg = avg

    db.session.commit()
    return jsonify({"msg": "golfer edith successfully"}), 200


@app.route('/confederations_cup/<id>', methods=['PUT'])
def confederations_cupEdit(id):
    confederations_cup = Confederations_Cup.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    status = request.json['status']
    preview = request.json['preview']
    img_preview = request.json['img_preview']
    away = request.json['away']
    home = request.json['home']
    goal_line_away = request.json['goal_line_away']
    goal_line_home = request.json['goal_line_home']
    juice_goal_away = request.json['juice_goal_away']
    juice_goal_home = request.json['juice_goal_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']
    goal_away_1H = request.json['goal_away_1H']
    goal_home_1H = request.json['goal_home_1H']
    juice_goal_away_1H = request.json['juice_goal_away_1H']
    juice_goal_home_1H = request.json['juice_goal_home_1H']
    moneyLineAway_1H = request.json['moneyLineAway_1H']
    moneyLineHome_1H = request.json['moneyLineHome_1H']
    total_1H = request.json['total_1H']
    H1_juice_over = request.json['H1_juice_over']
    H1_juice_under = request.json['H1_juice_under']
    tt_away_1H = request.json['tt_away_1H']
    juice_over_away_1H = request.json['juice_over_away_1H']
    juice_under_away_1H = request.json['juice_under_away_1H']
    tt_home_1H = request.json['tt_home_1H']
    juice_over_home_1H = request.json['juice_over_home_1H']
    juice_under_home_1H = request.json['juice_under_home_1H']

    confederations_cup.date = date
    confederations_cup.hour = hour
    confederations_cup.preview = preview
    confederations_cup.img_preview = img_preview
    confederations_cup.status = status
    confederations_cup.away = away
    confederations_cup.home = home
    confederations_cup.goal_line_away = goal_line_away
    confederations_cup.goal_line_home = goal_line_home
    confederations_cup.juice_goal_away = juice_goal_away
    confederations_cup.juice_goal_home = juice_goal_home
    confederations_cup.moneyLineAway = moneyLineAway
    confederations_cup.moneyLineHome = moneyLineHome
    confederations_cup.total = total
    confederations_cup.juice_total_over = juice_total_over
    confederations_cup.juice_total_under = juice_total_under
    confederations_cup.tt_away = tt_away
    confederations_cup.juice_over_away = juice_over_away
    confederations_cup.juice_under_away = juice_under_away
    confederations_cup.tt_home = tt_home
    confederations_cup.juice_over_home = juice_over_home
    confederations_cup.juice_under_home = juice_under_home
    confederations_cup.final_score_away = final_score_away
    confederations_cup.final_score_home = final_score_home
    confederations_cup.final_score_home = final_score_home
    confederations_cup.goal_away_1H = goal_away_1H
    confederations_cup.goal_home_1H = goal_home_1H
    confederations_cup.juice_goal_away_1H = juice_goal_away_1H
    confederations_cup.juice_goal_home_1H = juice_goal_home_1H
    confederations_cup.moneyLineAway_1H = moneyLineAway_1H
    confederations_cup.moneyLineHome_1H = moneyLineHome_1H
    confederations_cup.total_1H = total_1H
    confederations_cup.H1_juice_over = H1_juice_over
    confederations_cup.H1_juice_under = H1_juice_under
    confederations_cup.tt_away_1H = tt_away_1H
    confederations_cup.juice_over_away_1H = juice_over_away_1H
    confederations_cup.juice_under_away_1H = juice_under_away_1H
    confederations_cup.tt_home_1H = tt_home_1H
    confederations_cup.juice_over_home_1H = juice_over_home_1H
    confederations_cup.juice_under_home_1H = juice_under_home_1H

    db.session.commit()
    return jsonify({"msg": "confederations_cup edith successfully"}), 200


@app.route('/champions_league/<id>', methods=['PUT'])
def champions_leagueEdit(id):
    champions_league = Champions_League.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    status = request.json['status']
    preview = request.json['preview']
    img_preview = request.json['img_preview']
    away = request.json['away']
    home = request.json['home']
    goal_line_away = request.json['goal_line_away']
    goal_line_home = request.json['goal_line_home']
    juice_goal_away = request.json['juice_goal_away']
    juice_goal_home = request.json['juice_goal_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']
    goal_away_1H = request.json['goal_away_1H']
    goal_home_1H = request.json['goal_home_1H']
    juice_goal_away_1H = request.json['juice_goal_away_1H']
    juice_goal_home_1H = request.json['juice_goal_home_1H']
    moneyLineAway_1H = request.json['moneyLineAway_1H']
    moneyLineHome_1H = request.json['moneyLineHome_1H']
    total_1H = request.json['total_1H']
    H1_juice_over = request.json['H1_juice_over']
    H1_juice_under = request.json['H1_juice_under']
    tt_away_1H = request.json['tt_away_1H']
    juice_over_away_1H = request.json['juice_over_away_1H']
    juice_under_away_1H = request.json['juice_under_away_1H']
    tt_home_1H = request.json['tt_home_1H']
    juice_over_home_1H = request.json['juice_over_home_1H']
    juice_under_home_1H = request.json['juice_under_home_1H']

    champions_league.date = date
    champions_league.hour = hour
    champions_league.preview = preview
    champions_league.img_preview = img_preview
    champions_league.status = status
    champions_league.away = away
    champions_league.home = home
    champions_league.goal_line_away = goal_line_away
    champions_league.goal_line_home = goal_line_home
    champions_league.juice_goal_away = juice_goal_away
    champions_league.juice_goal_home = juice_goal_home
    champions_league.moneyLineAway = moneyLineAway
    champions_league.moneyLineHome = moneyLineHome
    champions_league.total = total
    champions_league.juice_total_over = juice_total_over
    champions_league.juice_total_under = juice_total_under
    champions_league.tt_away = tt_away
    champions_league.juice_over_away = juice_over_away
    champions_league.juice_under_away = juice_under_away
    champions_league.tt_home = tt_home
    champions_league.juice_over_home = juice_over_home
    champions_league.juice_under_home = juice_under_home
    champions_league.final_score_away = final_score_away
    champions_league.final_score_home = final_score_home
    champions_league.final_score_home = final_score_home
    champions_league.goal_away_1H = goal_away_1H
    champions_league.goal_home_1H = goal_home_1H
    champions_league.juice_goal_away_1H = juice_goal_away_1H
    champions_league.juice_goal_home_1H = juice_goal_home_1H
    champions_league.moneyLineAway_1H = moneyLineAway_1H
    champions_league.moneyLineHome_1H = moneyLineHome_1H
    champions_league.total_1H = total_1H
    champions_league.H1_juice_over = H1_juice_over
    champions_league.H1_juice_under = H1_juice_under
    champions_league.tt_away_1H = tt_away_1H
    champions_league.juice_over_away_1H = juice_over_away_1H
    champions_league.juice_under_away_1H = juice_under_away_1H
    champions_league.tt_home_1H = tt_home_1H
    champions_league.juice_over_home_1H = juice_over_home_1H
    champions_league.juice_under_home_1H = juice_under_home_1H

    db.session.commit()
    return jsonify({"msg": "champions_league edith successfully"}), 200


@app.route('/w_c_qualifying/<id>', methods=['PUT'])
def w_c_qualifyingEdit(id):
    w_c_qualifying = W_C_Qualifying.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    status = request.json['status']
    preview = request.json['preview']
    img_preview = request.json['img_preview']
    away = request.json['away']
    home = request.json['home']
    goal_line_away = request.json['goal_line_away']
    goal_line_home = request.json['goal_line_home']
    juice_goal_away = request.json['juice_goal_away']
    juice_goal_home = request.json['juice_goal_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']
    goal_away_1H = request.json['goal_away_1H']
    goal_home_1H = request.json['goal_home_1H']
    juice_goal_away_1H = request.json['juice_goal_away_1H']
    juice_goal_home_1H = request.json['juice_goal_home_1H']
    moneyLineAway_1H = request.json['moneyLineAway_1H']
    moneyLineHome_1H = request.json['moneyLineHome_1H']
    total_1H = request.json['total_1H']
    H1_juice_over = request.json['H1_juice_over']
    H1_juice_under = request.json['H1_juice_under']
    tt_away_1H = request.json['tt_away_1H']
    juice_over_away_1H = request.json['juice_over_away_1H']
    juice_under_away_1H = request.json['juice_under_away_1H']
    tt_home_1H = request.json['tt_home_1H']
    juice_over_home_1H = request.json['juice_over_home_1H']
    juice_under_home_1H = request.json['juice_under_home_1H']

    w_c_qualifying.date = date
    w_c_qualifying.hour = hour
    w_c_qualifying.preview = preview
    w_c_qualifying.img_preview = img_preview
    w_c_qualifying.status = status
    w_c_qualifying.away = away
    w_c_qualifying.home = home
    w_c_qualifying.goal_line_away = goal_line_away
    w_c_qualifying.goal_line_home = goal_line_home
    w_c_qualifying.juice_goal_away = juice_goal_away
    w_c_qualifying.juice_goal_home = juice_goal_home
    w_c_qualifying.moneyLineAway = moneyLineAway
    w_c_qualifying.moneyLineHome = moneyLineHome
    w_c_qualifying.total = total
    w_c_qualifying.juice_total_over = juice_total_over
    w_c_qualifying.juice_total_under = juice_total_under
    w_c_qualifying.tt_away = tt_away
    w_c_qualifying.juice_over_away = juice_over_away
    w_c_qualifying.juice_under_away = juice_under_away
    w_c_qualifying.tt_home = tt_home
    w_c_qualifying.juice_over_home = juice_over_home
    w_c_qualifying.juice_under_home = juice_under_home
    w_c_qualifying.final_score_away = final_score_away
    w_c_qualifying.final_score_home = final_score_home
    w_c_qualifying.final_score_home = final_score_home
    w_c_qualifying.goal_away_1H = goal_away_1H
    w_c_qualifying.goal_home_1H = goal_home_1H
    w_c_qualifying.juice_goal_away_1H = juice_goal_away_1H
    w_c_qualifying.juice_goal_home_1H = juice_goal_home_1H
    w_c_qualifying.moneyLineAway_1H = moneyLineAway_1H
    w_c_qualifying.moneyLineHome_1H = moneyLineHome_1H
    w_c_qualifying.total_1H = total_1H
    w_c_qualifying.H1_juice_over = H1_juice_over
    w_c_qualifying.H1_juice_under = H1_juice_under
    w_c_qualifying.tt_away_1H = tt_away_1H
    w_c_qualifying.juice_over_away_1H = juice_over_away_1H
    w_c_qualifying.juice_under_away_1H = juice_under_away_1H
    w_c_qualifying.tt_home_1H = tt_home_1H
    w_c_qualifying.juice_over_home_1H = juice_over_home_1H
    w_c_qualifying.juice_under_home_1H = juice_under_home_1H

    db.session.commit()
    return jsonify({"msg": "w_c_qualifying edith successfully"}), 200


@app.route('/CONCACAF/<id>', methods=['PUT'])
def CONCACAFEdit(id):
    CONCACAF = CONCACAF.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    status = request.json['status']
    preview = request.json['preview']
    img_preview = request.json['img_preview']
    away = request.json['away']
    home = request.json['home']
    goal_line_away = request.json['goal_line_away']
    goal_line_home = request.json['goal_line_home']
    juice_goal_away = request.json['juice_goal_away']
    juice_goal_home = request.json['juice_goal_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']
    goal_away_1H = request.json['goal_away_1H']
    goal_home_1H = request.json['goal_home_1H']
    juice_goal_away_1H = request.json['juice_goal_away_1H']
    juice_goal_home_1H = request.json['juice_goal_home_1H']
    moneyLineAway_1H = request.json['moneyLineAway_1H']
    moneyLineHome_1H = request.json['moneyLineHome_1H']
    total_1H = request.json['total_1H']
    H1_juice_over = request.json['H1_juice_over']
    H1_juice_under = request.json['H1_juice_under']
    tt_away_1H = request.json['tt_away_1H']
    juice_over_away_1H = request.json['juice_over_away_1H']
    juice_under_away_1H = request.json['juice_under_away_1H']
    tt_home_1H = request.json['tt_home_1H']
    juice_over_home_1H = request.json['juice_over_home_1H']
    juice_under_home_1H = request.json['juice_under_home_1H']

    CONCACAF.date = date
    CONCACAF.hour = hour
    CONCACAF.preview = preview
    CONCACAF.img_preview = img_preview
    CONCACAF.status = status
    CONCACAF.away = away
    CONCACAF.home = home
    CONCACAF.goal_line_away = goal_line_away
    CONCACAF.goal_line_home = goal_line_home
    CONCACAF.juice_goal_away = juice_goal_away
    CONCACAF.juice_goal_home = juice_goal_home
    CONCACAF.moneyLineAway = moneyLineAway
    CONCACAF.moneyLineHome = moneyLineHome
    CONCACAF.total = total
    CONCACAF.juice_total_over = juice_total_over
    CONCACAF.juice_total_under = juice_total_under
    CONCACAF.tt_away = tt_away
    CONCACAF.juice_over_away = juice_over_away
    CONCACAF.juice_under_away = juice_under_away
    CONCACAF.tt_home = tt_home
    CONCACAF.juice_over_home = juice_over_home
    CONCACAF.juice_under_home = juice_under_home
    CONCACAF.final_score_away = final_score_away
    CONCACAF.final_score_home = final_score_home
    CONCACAF.final_score_home = final_score_home
    CONCACAF.goal_away_1H = goal_away_1H
    CONCACAF.goal_home_1H = goal_home_1H
    CONCACAF.juice_goal_away_1H = juice_goal_away_1H
    CONCACAF.juice_goal_home_1H = juice_goal_home_1H
    CONCACAF.moneyLineAway_1H = moneyLineAway_1H
    CONCACAF.moneyLineHome_1H = moneyLineHome_1H
    CONCACAF.total_1H = total_1H
    CONCACAF.H1_juice_over = H1_juice_over
    CONCACAF.H1_juice_under = H1_juice_under
    CONCACAF.tt_away_1H = tt_away_1H
    CONCACAF.juice_over_away_1H = juice_over_away_1H
    CONCACAF.juice_under_away_1H = juice_under_away_1H
    CONCACAF.tt_home_1H = tt_home_1H
    CONCACAF.juice_over_home_1H = juice_over_home_1H
    CONCACAF.juice_under_home_1H = juice_under_home_1H

    db.session.commit()
    return jsonify({"msg": "CONCACAF edith successfully"}), 200


@app.route('/england_premier_league/<id>', methods=['PUT'])
def england_premier_leagueEdit(id):
    england_premier_league = England_Premier_League.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    status = request.json['status']
    preview = request.json['preview']
    img_preview = request.json['img_preview']
    away = request.json['away']
    home = request.json['home']
    goal_line_away = request.json['goal_line_away']
    goal_line_home = request.json['goal_line_home']
    juice_goal_away = request.json['juice_goal_away']
    juice_goal_home = request.json['juice_goal_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']
    goal_away_1H = request.json['goal_away_1H']
    goal_home_1H = request.json['goal_home_1H']
    juice_goal_away_1H = request.json['juice_goal_away_1H']
    juice_goal_home_1H = request.json['juice_goal_home_1H']
    moneyLineAway_1H = request.json['moneyLineAway_1H']
    moneyLineHome_1H = request.json['moneyLineHome_1H']
    total_1H = request.json['total_1H']
    H1_juice_over = request.json['H1_juice_over']
    H1_juice_under = request.json['H1_juice_under']
    tt_away_1H = request.json['tt_away_1H']
    juice_over_away_1H = request.json['juice_over_away_1H']
    juice_under_away_1H = request.json['juice_under_away_1H']
    tt_home_1H = request.json['tt_home_1H']
    juice_over_home_1H = request.json['juice_over_home_1H']
    juice_under_home_1H = request.json['juice_under_home_1H']

    england_premier_league.date = date
    england_premier_league.hour = hour
    england_premier_league.preview = preview
    england_premier_league.img_preview = img_preview
    england_premier_league.status = status
    england_premier_league.away = away
    england_premier_league.home = home
    england_premier_league.goal_line_away = goal_line_away
    england_premier_league.goal_line_home = goal_line_home
    england_premier_league.juice_goal_away = juice_goal_away
    england_premier_league.juice_goal_home = juice_goal_home
    england_premier_league.moneyLineAway = moneyLineAway
    england_premier_league.moneyLineHome = moneyLineHome
    england_premier_league.total = total
    england_premier_league.juice_total_over = juice_total_over
    england_premier_league.juice_total_under = juice_total_under
    england_premier_league.tt_away = tt_away
    england_premier_league.juice_over_away = juice_over_away
    england_premier_league.juice_under_away = juice_under_away
    england_premier_league.tt_home = tt_home
    england_premier_league.juice_over_home = juice_over_home
    england_premier_league.juice_under_home = juice_under_home
    england_premier_league.final_score_away = final_score_away
    england_premier_league.final_score_home = final_score_home
    england_premier_league.final_score_home = final_score_home
    england_premier_league.goal_away_1H = goal_away_1H
    england_premier_league.goal_home_1H = goal_home_1H
    england_premier_league.juice_goal_away_1H = juice_goal_away_1H
    england_premier_league.juice_goal_home_1H = juice_goal_home_1H
    england_premier_league.moneyLineAway_1H = moneyLineAway_1H
    england_premier_league.moneyLineHome_1H = moneyLineHome_1H
    england_premier_league.total_1H = total_1H
    england_premier_league.H1_juice_over = H1_juice_over
    england_premier_league.H1_juice_under = H1_juice_under
    england_premier_league.tt_away_1H = tt_away_1H
    england_premier_league.juice_over_away_1H = juice_over_away_1H
    england_premier_league.juice_under_away_1H = juice_under_away_1H
    england_premier_league.tt_home_1H = tt_home_1H
    england_premier_league.juice_over_home_1H = juice_over_home_1H
    england_premier_league.juice_under_home_1H = juice_under_home_1H

    db.session.commit()
    return jsonify({"msg": "england_premier_league edith successfully"}), 200


@app.route('/europa_league/<id>', methods=['PUT'])
def europa_leagueEdit(id):
    europa_league = Europa_League.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    status = request.json['status']
    preview = request.json['preview']
    img_preview = request.json['img_preview']
    away = request.json['away']
    home = request.json['home']
    goal_line_away = request.json['goal_line_away']
    goal_line_home = request.json['goal_line_home']
    juice_goal_away = request.json['juice_goal_away']
    juice_goal_home = request.json['juice_goal_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']
    goal_away_1H = request.json['goal_away_1H']
    goal_home_1H = request.json['goal_home_1H']
    juice_goal_away_1H = request.json['juice_goal_away_1H']
    juice_goal_home_1H = request.json['juice_goal_home_1H']
    moneyLineAway_1H = request.json['moneyLineAway_1H']
    moneyLineHome_1H = request.json['moneyLineHome_1H']
    total_1H = request.json['total_1H']
    H1_juice_over = request.json['H1_juice_over']
    H1_juice_under = request.json['H1_juice_under']
    tt_away_1H = request.json['tt_away_1H']
    juice_over_away_1H = request.json['juice_over_away_1H']
    juice_under_away_1H = request.json['juice_under_away_1H']
    tt_home_1H = request.json['tt_home_1H']
    juice_over_home_1H = request.json['juice_over_home_1H']
    juice_under_home_1H = request.json['juice_under_home_1H']

    europa_league.date = date
    europa_league.hour = hour
    europa_league.preview = preview
    europa_league.img_preview = img_preview
    europa_league.status = status
    europa_league.away = away
    europa_league.home = home
    europa_league.goal_line_away = goal_line_away
    europa_league.goal_line_home = goal_line_home
    europa_league.juice_goal_away = juice_goal_away
    europa_league.juice_goal_home = juice_goal_home
    europa_league.moneyLineAway = moneyLineAway
    europa_league.moneyLineHome = moneyLineHome
    europa_league.total = total
    europa_league.juice_total_over = juice_total_over
    europa_league.juice_total_under = juice_total_under
    europa_league.tt_away = tt_away
    europa_league.juice_over_away = juice_over_away
    europa_league.juice_under_away = juice_under_away
    europa_league.tt_home = tt_home
    europa_league.juice_over_home = juice_over_home
    europa_league.juice_under_home = juice_under_home
    europa_league.final_score_away = final_score_away
    europa_league.final_score_home = final_score_home
    europa_league.final_score_home = final_score_home
    europa_league.goal_away_1H = goal_away_1H
    europa_league.goal_home_1H = goal_home_1H
    europa_league.juice_goal_away_1H = juice_goal_away_1H
    europa_league.juice_goal_home_1H = juice_goal_home_1H
    europa_league.moneyLineAway_1H = moneyLineAway_1H
    europa_league.moneyLineHome_1H = moneyLineHome_1H
    europa_league.total_1H = total_1H
    europa_league.H1_juice_over = H1_juice_over
    europa_league.H1_juice_under = H1_juice_under
    europa_league.tt_away_1H = tt_away_1H
    europa_league.juice_over_away_1H = juice_over_away_1H
    europa_league.juice_under_away_1H = juice_under_away_1H
    europa_league.tt_home_1H = tt_home_1H
    europa_league.juice_over_home_1H = juice_over_home_1H
    europa_league.juice_under_home_1H = juice_under_home_1H

    db.session.commit()
    return jsonify({"msg": "europa_league edith successfully"}), 200


@app.route('/international_friendlies/<id>', methods=['PUT'])
def international_friendliesEdit(id):
    international_friendlies = International_Friendlies.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    status = request.json['status']
    preview = request.json['preview']
    img_preview = request.json['img_preview']
    away = request.json['away']
    home = request.json['home']
    goal_line_away = request.json['goal_line_away']
    goal_line_home = request.json['goal_line_home']
    juice_goal_away = request.json['juice_goal_away']
    juice_goal_home = request.json['juice_goal_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']
    goal_away_1H = request.json['goal_away_1H']
    goal_home_1H = request.json['goal_home_1H']
    juice_goal_away_1H = request.json['juice_goal_away_1H']
    juice_goal_home_1H = request.json['juice_goal_home_1H']
    moneyLineAway_1H = request.json['moneyLineAway_1H']
    moneyLineHome_1H = request.json['moneyLineHome_1H']
    total_1H = request.json['total_1H']
    H1_juice_over = request.json['H1_juice_over']
    H1_juice_under = request.json['H1_juice_under']
    tt_away_1H = request.json['tt_away_1H']
    juice_over_away_1H = request.json['juice_over_away_1H']
    juice_under_away_1H = request.json['juice_under_away_1H']
    tt_home_1H = request.json['tt_home_1H']
    juice_over_home_1H = request.json['juice_over_home_1H']
    juice_under_home_1H = request.json['juice_under_home_1H']

    international_friendlies.date = date
    international_friendlies.hour = hour
    international_friendlies.preview = preview
    international_friendlies.img_preview = img_preview
    international_friendlies.status = status
    international_friendlies.away = away
    international_friendlies.home = home
    international_friendlies.goal_line_away = goal_line_away
    international_friendlies.goal_line_home = goal_line_home
    international_friendlies.juice_goal_away = juice_goal_away
    international_friendlies.juice_goal_home = juice_goal_home
    international_friendlies.moneyLineAway = moneyLineAway
    international_friendlies.moneyLineHome = moneyLineHome
    international_friendlies.total = total
    international_friendlies.juice_total_over = juice_total_over
    international_friendlies.juice_total_under = juice_total_under
    international_friendlies.tt_away = tt_away
    international_friendlies.juice_over_away = juice_over_away
    international_friendlies.juice_under_away = juice_under_away
    international_friendlies.tt_home = tt_home
    international_friendlies.juice_over_home = juice_over_home
    international_friendlies.juice_under_home = juice_under_home
    international_friendlies.final_score_away = final_score_away
    international_friendlies.final_score_home = final_score_home
    international_friendlies.final_score_home = final_score_home
    international_friendlies.goal_away_1H = goal_away_1H
    international_friendlies.goal_home_1H = goal_home_1H
    international_friendlies.juice_goal_away_1H = juice_goal_away_1H
    international_friendlies.juice_goal_home_1H = juice_goal_home_1H
    international_friendlies.moneyLineAway_1H = moneyLineAway_1H
    international_friendlies.moneyLineHome_1H = moneyLineHome_1H
    international_friendlies.total_1H = total_1H
    international_friendlies.H1_juice_over = H1_juice_over
    international_friendlies.H1_juice_under = H1_juice_under
    international_friendlies.tt_away_1H = tt_away_1H
    international_friendlies.juice_over_away_1H = juice_over_away_1H
    international_friendlies.juice_under_away_1H = juice_under_away_1H
    international_friendlies.tt_home_1H = tt_home_1H
    international_friendlies.juice_over_home_1H = juice_over_home_1H
    international_friendlies.juice_under_home_1H = juice_under_home_1H

    db.session.commit()
    return jsonify({"msg": "international_friendlies edith successfully"}), 200


@app.route('/france_league/<id>', methods=['PUT'])
def france_leagueEdit(id):
    france_league = France_League.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    status = request.json['status']
    preview = request.json['preview']
    img_preview = request.json['img_preview']
    away = request.json['away']
    home = request.json['home']
    goal_line_away = request.json['goal_line_away']
    goal_line_home = request.json['goal_line_home']
    juice_goal_away = request.json['juice_goal_away']
    juice_goal_home = request.json['juice_goal_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']
    goal_away_1H = request.json['goal_away_1H']
    goal_home_1H = request.json['goal_home_1H']
    juice_goal_away_1H = request.json['juice_goal_away_1H']
    juice_goal_home_1H = request.json['juice_goal_home_1H']
    moneyLineAway_1H = request.json['moneyLineAway_1H']
    moneyLineHome_1H = request.json['moneyLineHome_1H']
    total_1H = request.json['total_1H']
    H1_juice_over = request.json['H1_juice_over']
    H1_juice_under = request.json['H1_juice_under']
    tt_away_1H = request.json['tt_away_1H']
    juice_over_away_1H = request.json['juice_over_away_1H']
    juice_under_away_1H = request.json['juice_under_away_1H']
    tt_home_1H = request.json['tt_home_1H']
    juice_over_home_1H = request.json['juice_over_home_1H']
    juice_under_home_1H = request.json['juice_under_home_1H']

    france_league.date = date
    france_league.hour = hour
    france_league.preview = preview
    france_league.img_preview = img_preview
    france_league.status = status
    france_league.away = away
    france_league.home = home
    france_league.goal_line_away = goal_line_away
    france_league.goal_line_home = goal_line_home
    france_league.juice_goal_away = juice_goal_away
    france_league.juice_goal_home = juice_goal_home
    france_league.moneyLineAway = moneyLineAway
    france_league.moneyLineHome = moneyLineHome
    france_league.total = total
    france_league.juice_total_over = juice_total_over
    france_league.juice_total_under = juice_total_under
    france_league.tt_away = tt_away
    france_league.juice_over_away = juice_over_away
    france_league.juice_under_away = juice_under_away
    france_league.tt_home = tt_home
    france_league.juice_over_home = juice_over_home
    france_league.juice_under_home = juice_under_home
    france_league.final_score_away = final_score_away
    france_league.final_score_home = final_score_home
    france_league.final_score_home = final_score_home
    france_league.goal_away_1H = goal_away_1H
    france_league.goal_home_1H = goal_home_1H
    france_league.juice_goal_away_1H = juice_goal_away_1H
    france_league.juice_goal_home_1H = juice_goal_home_1H
    france_league.moneyLineAway_1H = moneyLineAway_1H
    france_league.moneyLineHome_1H = moneyLineHome_1H
    france_league.total_1H = total_1H
    france_league.H1_juice_over = H1_juice_over
    france_league.H1_juice_under = H1_juice_under
    france_league.tt_away_1H = tt_away_1H
    france_league.juice_over_away_1H = juice_over_away_1H
    france_league.juice_under_away_1H = juice_under_away_1H
    france_league.tt_home_1H = tt_home_1H
    france_league.juice_over_home_1H = juice_over_home_1H
    france_league.juice_under_home_1H = juice_under_home_1H

    db.session.commit()
    return jsonify({"msg": "france_league edith successfully"}), 200


@app.route('/bundesliga/<id>', methods=['PUT'])
def bundesligaEdit(id):
    bundesliga = Bundesliga.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    status = request.json['status']
    preview = request.json['preview']
    img_preview = request.json['img_preview']
    away = request.json['away']
    home = request.json['home']
    goal_line_away = request.json['goal_line_away']
    goal_line_home = request.json['goal_line_home']
    juice_goal_away = request.json['juice_goal_away']
    juice_goal_home = request.json['juice_goal_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']
    goal_away_1H = request.json['goal_away_1H']
    goal_home_1H = request.json['goal_home_1H']
    juice_goal_away_1H = request.json['juice_goal_away_1H']
    juice_goal_home_1H = request.json['juice_goal_home_1H']
    moneyLineAway_1H = request.json['moneyLineAway_1H']
    moneyLineHome_1H = request.json['moneyLineHome_1H']
    total_1H = request.json['total_1H']
    H1_juice_over = request.json['H1_juice_over']
    H1_juice_under = request.json['H1_juice_under']
    tt_away_1H = request.json['tt_away_1H']
    juice_over_away_1H = request.json['juice_over_away_1H']
    juice_under_away_1H = request.json['juice_under_away_1H']
    tt_home_1H = request.json['tt_home_1H']
    juice_over_home_1H = request.json['juice_over_home_1H']
    juice_under_home_1H = request.json['juice_under_home_1H']

    bundesliga.date = date
    bundesliga.hour = hour
    bundesliga.preview = preview
    bundesliga.img_preview = img_preview
    bundesliga.status = status
    bundesliga.away = away
    bundesliga.home = home
    bundesliga.goal_line_away = goal_line_away
    bundesliga.goal_line_home = goal_line_home
    bundesliga.juice_goal_away = juice_goal_away
    bundesliga.juice_goal_home = juice_goal_home
    bundesliga.moneyLineAway = moneyLineAway
    bundesliga.moneyLineHome = moneyLineHome
    bundesliga.total = total
    bundesliga.juice_total_over = juice_total_over
    bundesliga.juice_total_under = juice_total_under
    bundesliga.tt_away = tt_away
    bundesliga.juice_over_away = juice_over_away
    bundesliga.juice_under_away = juice_under_away
    bundesliga.tt_home = tt_home
    bundesliga.juice_over_home = juice_over_home
    bundesliga.juice_under_home = juice_under_home
    bundesliga.final_score_away = final_score_away
    bundesliga.final_score_home = final_score_home
    bundesliga.final_score_home = final_score_home
    bundesliga.goal_away_1H = goal_away_1H
    bundesliga.goal_home_1H = goal_home_1H
    bundesliga.juice_goal_away_1H = juice_goal_away_1H
    bundesliga.juice_goal_home_1H = juice_goal_home_1H
    bundesliga.moneyLineAway_1H = moneyLineAway_1H
    bundesliga.moneyLineHome_1H = moneyLineHome_1H
    bundesliga.total_1H = total_1H
    bundesliga.H1_juice_over = H1_juice_over
    bundesliga.H1_juice_under = H1_juice_under
    bundesliga.tt_away_1H = tt_away_1H
    bundesliga.juice_over_away_1H = juice_over_away_1H
    bundesliga.juice_under_away_1H = juice_under_away_1H
    bundesliga.tt_home_1H = tt_home_1H
    bundesliga.juice_over_home_1H = juice_over_home_1H
    bundesliga.juice_under_home_1H = juice_under_home_1H

    db.session.commit()
    return jsonify({"msg": "bundesliga edith successfully"}), 200


@app.route('/international_matches/<id>', methods=['PUT'])
def international_matchesEdit(id):
    international_matches = International_Matches.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    status = request.json['status']
    preview = request.json['preview']
    img_preview = request.json['img_preview']
    away = request.json['away']
    home = request.json['home']
    goal_line_away = request.json['goal_line_away']
    goal_line_home = request.json['goal_line_home']
    juice_goal_away = request.json['juice_goal_away']
    juice_goal_home = request.json['juice_goal_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']
    goal_away_1H = request.json['goal_away_1H']
    goal_home_1H = request.json['goal_home_1H']
    juice_goal_away_1H = request.json['juice_goal_away_1H']
    juice_goal_home_1H = request.json['juice_goal_home_1H']
    moneyLineAway_1H = request.json['moneyLineAway_1H']
    moneyLineHome_1H = request.json['moneyLineHome_1H']
    total_1H = request.json['total_1H']
    H1_juice_over = request.json['H1_juice_over']
    H1_juice_under = request.json['H1_juice_under']
    tt_away_1H = request.json['tt_away_1H']
    juice_over_away_1H = request.json['juice_over_away_1H']
    juice_under_away_1H = request.json['juice_under_away_1H']
    tt_home_1H = request.json['tt_home_1H']
    juice_over_home_1H = request.json['juice_over_home_1H']
    juice_under_home_1H = request.json['juice_under_home_1H']

    international_matches.date = date
    international_matches.hour = hour
    international_matches.preview = preview
    international_matches.img_preview = img_preview
    international_matches.status = status
    international_matches.away = away
    international_matches.home = home
    international_matches.goal_line_away = goal_line_away
    international_matches.goal_line_home = goal_line_home
    international_matches.juice_goal_away = juice_goal_away
    international_matches.juice_goal_home = juice_goal_home
    international_matches.moneyLineAway = moneyLineAway
    international_matches.moneyLineHome = moneyLineHome
    international_matches.total = total
    international_matches.juice_total_over = juice_total_over
    international_matches.juice_total_under = juice_total_under
    international_matches.tt_away = tt_away
    international_matches.juice_over_away = juice_over_away
    international_matches.juice_under_away = juice_under_away
    international_matches.tt_home = tt_home
    international_matches.juice_over_home = juice_over_home
    international_matches.juice_under_home = juice_under_home
    international_matches.final_score_away = final_score_away
    international_matches.final_score_home = final_score_home
    international_matches.final_score_home = final_score_home
    international_matches.goal_away_1H = goal_away_1H
    international_matches.goal_home_1H = goal_home_1H
    international_matches.juice_goal_away_1H = juice_goal_away_1H
    international_matches.juice_goal_home_1H = juice_goal_home_1H
    international_matches.moneyLineAway_1H = moneyLineAway_1H
    international_matches.moneyLineHome_1H = moneyLineHome_1H
    international_matches.total_1H = total_1H
    international_matches.H1_juice_over = H1_juice_over
    international_matches.H1_juice_under = H1_juice_under
    international_matches.tt_away_1H = tt_away_1H
    international_matches.juice_over_away_1H = juice_over_away_1H
    international_matches.juice_under_away_1H = juice_under_away_1H
    international_matches.tt_home_1H = tt_home_1H
    international_matches.juice_over_home_1H = juice_over_home_1H
    international_matches.juice_under_home_1H = juice_under_home_1H

    db.session.commit()
    return jsonify({"msg": "international_matches edith successfully"}), 200


@app.route('/italia_serie_A/<id>', methods=['PUT'])
def italia_serie_AEdit(id):
    italia_serie_A = Italia_Serie_A.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    status = request.json['status']
    preview = request.json['preview']
    img_preview = request.json['img_preview']
    away = request.json['away']
    home = request.json['home']
    goal_line_away = request.json['goal_line_away']
    goal_line_home = request.json['goal_line_home']
    juice_goal_away = request.json['juice_goal_away']
    juice_goal_home = request.json['juice_goal_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']
    goal_away_1H = request.json['goal_away_1H']
    goal_home_1H = request.json['goal_home_1H']
    juice_goal_away_1H = request.json['juice_goal_away_1H']
    juice_goal_home_1H = request.json['juice_goal_home_1H']
    moneyLineAway_1H = request.json['moneyLineAway_1H']
    moneyLineHome_1H = request.json['moneyLineHome_1H']
    total_1H = request.json['total_1H']
    H1_juice_over = request.json['H1_juice_over']
    H1_juice_under = request.json['H1_juice_under']
    tt_away_1H = request.json['tt_away_1H']
    juice_over_away_1H = request.json['juice_over_away_1H']
    juice_under_away_1H = request.json['juice_under_away_1H']
    tt_home_1H = request.json['tt_home_1H']
    juice_over_home_1H = request.json['juice_over_home_1H']
    juice_under_home_1H = request.json['juice_under_home_1H']

    italia_serie_A.date = date
    italia_serie_A.hour = hour
    italia_serie_A.preview = preview
    italia_serie_A.img_preview = img_preview
    italia_serie_A.status = status
    italia_serie_A.away = away
    italia_serie_A.home = home
    italia_serie_A.goal_line_away = goal_line_away
    italia_serie_A.goal_line_home = goal_line_home
    italia_serie_A.juice_goal_away = juice_goal_away
    italia_serie_A.juice_goal_home = juice_goal_home
    italia_serie_A.moneyLineAway = moneyLineAway
    italia_serie_A.moneyLineHome = moneyLineHome
    italia_serie_A.total = total
    italia_serie_A.juice_total_over = juice_total_over
    italia_serie_A.juice_total_under = juice_total_under
    italia_serie_A.tt_away = tt_away
    italia_serie_A.juice_over_away = juice_over_away
    italia_serie_A.juice_under_away = juice_under_away
    italia_serie_A.tt_home = tt_home
    italia_serie_A.juice_over_home = juice_over_home
    italia_serie_A.juice_under_home = juice_under_home
    italia_serie_A.final_score_away = final_score_away
    italia_serie_A.final_score_home = final_score_home
    italia_serie_A.final_score_home = final_score_home
    italia_serie_A.goal_away_1H = goal_away_1H
    italia_serie_A.goal_home_1H = goal_home_1H
    italia_serie_A.juice_goal_away_1H = juice_goal_away_1H
    italia_serie_A.juice_goal_home_1H = juice_goal_home_1H
    italia_serie_A.moneyLineAway_1H = moneyLineAway_1H
    italia_serie_A.moneyLineHome_1H = moneyLineHome_1H
    italia_serie_A.total_1H = total_1H
    italia_serie_A.H1_juice_over = H1_juice_over
    italia_serie_A.H1_juice_under = H1_juice_under
    italia_serie_A.tt_away_1H = tt_away_1H
    italia_serie_A.juice_over_away_1H = juice_over_away_1H
    italia_serie_A.juice_under_away_1H = juice_under_away_1H
    italia_serie_A.tt_home_1H = tt_home_1H
    italia_serie_A.juice_over_home_1H = juice_over_home_1H
    italia_serie_A.juice_under_home_1H = juice_under_home_1H

    db.session.commit()
    return jsonify({"msg": "italia_serie_A edith successfully"}), 200


@app.route('/mx_expansion/<id>', methods=['PUT'])
def mx_expansionEdit(id):
    mx_expansion = Mx_Expansion.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    status = request.json['status']
    preview = request.json['preview']
    img_preview = request.json['img_preview']
    away = request.json['away']
    home = request.json['home']
    goal_line_away = request.json['goal_line_away']
    goal_line_home = request.json['goal_line_home']
    juice_goal_away = request.json['juice_goal_away']
    juice_goal_home = request.json['juice_goal_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']
    goal_away_1H = request.json['goal_away_1H']
    goal_home_1H = request.json['goal_home_1H']
    juice_goal_away_1H = request.json['juice_goal_away_1H']
    juice_goal_home_1H = request.json['juice_goal_home_1H']
    moneyLineAway_1H = request.json['moneyLineAway_1H']
    moneyLineHome_1H = request.json['moneyLineHome_1H']
    total_1H = request.json['total_1H']
    H1_juice_over = request.json['H1_juice_over']
    H1_juice_under = request.json['H1_juice_under']
    tt_away_1H = request.json['tt_away_1H']
    juice_over_away_1H = request.json['juice_over_away_1H']
    juice_under_away_1H = request.json['juice_under_away_1H']
    tt_home_1H = request.json['tt_home_1H']
    juice_over_home_1H = request.json['juice_over_home_1H']
    juice_under_home_1H = request.json['juice_under_home_1H']

    mx_expansion.date = date
    mx_expansion.hour = hour
    mx_expansion.preview = preview
    mx_expansion.img_preview = img_preview
    mx_expansion.status = status
    mx_expansion.away = away
    mx_expansion.home = home
    mx_expansion.goal_line_away = goal_line_away
    mx_expansion.goal_line_home = goal_line_home
    mx_expansion.juice_goal_away = juice_goal_away
    mx_expansion.juice_goal_home = juice_goal_home
    mx_expansion.moneyLineAway = moneyLineAway
    mx_expansion.moneyLineHome = moneyLineHome
    mx_expansion.total = total
    mx_expansion.juice_total_over = juice_total_over
    mx_expansion.juice_total_under = juice_total_under
    mx_expansion.tt_away = tt_away
    mx_expansion.juice_over_away = juice_over_away
    mx_expansion.juice_under_away = juice_under_away
    mx_expansion.tt_home = tt_home
    mx_expansion.juice_over_home = juice_over_home
    mx_expansion.juice_under_home = juice_under_home
    mx_expansion.final_score_away = final_score_away
    mx_expansion.final_score_home = final_score_home
    mx_expansion.final_score_home = final_score_home
    mx_expansion.goal_away_1H = goal_away_1H
    mx_expansion.goal_home_1H = goal_home_1H
    mx_expansion.juice_goal_away_1H = juice_goal_away_1H
    mx_expansion.juice_goal_home_1H = juice_goal_home_1H
    mx_expansion.moneyLineAway_1H = moneyLineAway_1H
    mx_expansion.moneyLineHome_1H = moneyLineHome_1H
    mx_expansion.total_1H = total_1H
    mx_expansion.H1_juice_over = H1_juice_over
    mx_expansion.H1_juice_under = H1_juice_under
    mx_expansion.tt_away_1H = tt_away_1H
    mx_expansion.juice_over_away_1H = juice_over_away_1H
    mx_expansion.juice_under_away_1H = juice_under_away_1H
    mx_expansion.tt_home_1H = tt_home_1H
    mx_expansion.juice_over_home_1H = juice_over_home_1H
    mx_expansion.juice_under_home_1H = juice_under_home_1H

    db.session.commit()
    return jsonify({"msg": "mx_expansion edith successfully"}), 200


@app.route('/mx_apertura/<id>', methods=['PUT'])
def mx_aperturaEdit(id):
    mx_apertura = Mx_Apertura.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    status = request.json['status']
    preview = request.json['preview']
    img_preview = request.json['img_preview']
    away = request.json['away']
    home = request.json['home']
    goal_line_away = request.json['goal_line_away']
    goal_line_home = request.json['goal_line_home']
    juice_goal_away = request.json['juice_goal_away']
    juice_goal_home = request.json['juice_goal_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']
    goal_away_1H = request.json['goal_away_1H']
    goal_home_1H = request.json['goal_home_1H']
    juice_goal_away_1H = request.json['juice_goal_away_1H']
    juice_goal_home_1H = request.json['juice_goal_home_1H']
    moneyLineAway_1H = request.json['moneyLineAway_1H']
    moneyLineHome_1H = request.json['moneyLineHome_1H']
    total_1H = request.json['total_1H']
    H1_juice_over = request.json['H1_juice_over']
    H1_juice_under = request.json['H1_juice_under']
    tt_away_1H = request.json['tt_away_1H']
    juice_over_away_1H = request.json['juice_over_away_1H']
    juice_under_away_1H = request.json['juice_under_away_1H']
    tt_home_1H = request.json['tt_home_1H']
    juice_over_home_1H = request.json['juice_over_home_1H']
    juice_under_home_1H = request.json['juice_under_home_1H']

    mx_apertura.date = date
    mx_apertura.hour = hour
    mx_apertura.preview = preview
    mx_apertura.img_preview = img_preview
    mx_apertura.status = status
    mx_apertura.away = away
    mx_apertura.home = home
    mx_apertura.goal_line_away = goal_line_away
    mx_apertura.goal_line_home = goal_line_home
    mx_apertura.juice_goal_away = juice_goal_away
    mx_apertura.juice_goal_home = juice_goal_home
    mx_apertura.moneyLineAway = moneyLineAway
    mx_apertura.moneyLineHome = moneyLineHome
    mx_apertura.total = total
    mx_apertura.juice_total_over = juice_total_over
    mx_apertura.juice_total_under = juice_total_under
    mx_apertura.tt_away = tt_away
    mx_apertura.juice_over_away = juice_over_away
    mx_apertura.juice_under_away = juice_under_away
    mx_apertura.tt_home = tt_home
    mx_apertura.juice_over_home = juice_over_home
    mx_apertura.juice_under_home = juice_under_home
    mx_apertura.final_score_away = final_score_away
    mx_apertura.final_score_home = final_score_home
    mx_apertura.final_score_home = final_score_home
    mx_apertura.goal_away_1H = goal_away_1H
    mx_apertura.goal_home_1H = goal_home_1H
    mx_apertura.juice_goal_away_1H = juice_goal_away_1H
    mx_apertura.juice_goal_home_1H = juice_goal_home_1H
    mx_apertura.moneyLineAway_1H = moneyLineAway_1H
    mx_apertura.moneyLineHome_1H = moneyLineHome_1H
    mx_apertura.total_1H = total_1H
    mx_apertura.H1_juice_over = H1_juice_over
    mx_apertura.H1_juice_under = H1_juice_under
    mx_apertura.tt_away_1H = tt_away_1H
    mx_apertura.juice_over_away_1H = juice_over_away_1H
    mx_apertura.juice_under_away_1H = juice_under_away_1H
    mx_apertura.tt_home_1H = tt_home_1H
    mx_apertura.juice_over_home_1H = juice_over_home_1H
    mx_apertura.juice_under_home_1H = juice_under_home_1H

    db.session.commit()
    return jsonify({"msg": "mx_apertura edith successfully"}), 200


@app.route('/spain_primera_liga/<id>', methods=['PUT'])
def spain_primera_ligaEdit(id):
    spain_primera_liga = Spain_Primera_Liga.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    status = request.json['status']
    preview = request.json['preview']
    img_preview = request.json['img_preview']
    away = request.json['away']
    home = request.json['home']
    goal_line_away = request.json['goal_line_away']
    goal_line_home = request.json['goal_line_home']
    juice_goal_away = request.json['juice_goal_away']
    juice_goal_home = request.json['juice_goal_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']
    goal_away_1H = request.json['goal_away_1H']
    goal_home_1H = request.json['goal_home_1H']
    juice_goal_away_1H = request.json['juice_goal_away_1H']
    juice_goal_home_1H = request.json['juice_goal_home_1H']
    moneyLineAway_1H = request.json['moneyLineAway_1H']
    moneyLineHome_1H = request.json['moneyLineHome_1H']
    total_1H = request.json['total_1H']
    H1_juice_over = request.json['H1_juice_over']
    H1_juice_under = request.json['H1_juice_under']
    tt_away_1H = request.json['tt_away_1H']
    juice_over_away_1H = request.json['juice_over_away_1H']
    juice_under_away_1H = request.json['juice_under_away_1H']
    tt_home_1H = request.json['tt_home_1H']
    juice_over_home_1H = request.json['juice_over_home_1H']
    juice_under_home_1H = request.json['juice_under_home_1H']

    spain_primera_liga.date = date
    spain_primera_liga.hour = hour
    spain_primera_liga.preview = preview
    spain_primera_liga.img_preview = img_preview
    spain_primera_liga.status = status
    spain_primera_liga.away = away
    spain_primera_liga.home = home
    spain_primera_liga.goal_line_away = goal_line_away
    spain_primera_liga.goal_line_home = goal_line_home
    spain_primera_liga.juice_goal_away = juice_goal_away
    spain_primera_liga.juice_goal_home = juice_goal_home
    spain_primera_liga.moneyLineAway = moneyLineAway
    spain_primera_liga.moneyLineHome = moneyLineHome
    spain_primera_liga.total = total
    spain_primera_liga.juice_total_over = juice_total_over
    spain_primera_liga.juice_total_under = juice_total_under
    spain_primera_liga.tt_away = tt_away
    spain_primera_liga.juice_over_away = juice_over_away
    spain_primera_liga.juice_under_away = juice_under_away
    spain_primera_liga.tt_home = tt_home
    spain_primera_liga.juice_over_home = juice_over_home
    spain_primera_liga.juice_under_home = juice_under_home
    spain_primera_liga.final_score_away = final_score_away
    spain_primera_liga.final_score_home = final_score_home
    spain_primera_liga.final_score_home = final_score_home
    spain_primera_liga.goal_away_1H = goal_away_1H
    spain_primera_liga.goal_home_1H = goal_home_1H
    spain_primera_liga.juice_goal_away_1H = juice_goal_away_1H
    spain_primera_liga.juice_goal_home_1H = juice_goal_home_1H
    spain_primera_liga.moneyLineAway_1H = moneyLineAway_1H
    spain_primera_liga.moneyLineHome_1H = moneyLineHome_1H
    spain_primera_liga.total_1H = total_1H
    spain_primera_liga.H1_juice_over = H1_juice_over
    spain_primera_liga.H1_juice_under = H1_juice_under
    spain_primera_liga.tt_away_1H = tt_away_1H
    spain_primera_liga.juice_over_away_1H = juice_over_away_1H
    spain_primera_liga.juice_under_away_1H = juice_under_away_1H
    spain_primera_liga.tt_home_1H = tt_home_1H
    spain_primera_liga.juice_over_home_1H = juice_over_home_1H
    spain_primera_liga.juice_under_home_1H = juice_under_home_1H

    db.session.commit()
    return jsonify({"msg": "spain_primera_liga edith successfully"}), 200


@app.route('/USA_MLS/<id>', methods=['PUT'])
def USA_MLSEdit(id):
    USA_MLS = USA_MLS.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    status = request.json['status']
    preview = request.json['preview']
    img_preview = request.json['img_preview']
    away = request.json['away']
    home = request.json['home']
    goal_line_away = request.json['goal_line_away']
    goal_line_home = request.json['goal_line_home']
    juice_goal_away = request.json['juice_goal_away']
    juice_goal_home = request.json['juice_goal_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']
    goal_away_1H = request.json['goal_away_1H']
    goal_home_1H = request.json['goal_home_1H']
    juice_goal_away_1H = request.json['juice_goal_away_1H']
    juice_goal_home_1H = request.json['juice_goal_home_1H']
    moneyLineAway_1H = request.json['moneyLineAway_1H']
    moneyLineHome_1H = request.json['moneyLineHome_1H']
    total_1H = request.json['total_1H']
    H1_juice_over = request.json['H1_juice_over']
    H1_juice_under = request.json['H1_juice_under']
    tt_away_1H = request.json['tt_away_1H']
    juice_over_away_1H = request.json['juice_over_away_1H']
    juice_under_away_1H = request.json['juice_under_away_1H']
    tt_home_1H = request.json['tt_home_1H']
    juice_over_home_1H = request.json['juice_over_home_1H']
    juice_under_home_1H = request.json['juice_under_home_1H']

    USA_MLS.date = date
    USA_MLS.hour = hour
    USA_MLS.preview = preview
    USA_MLS.img_preview = img_preview
    USA_MLS.status = status
    USA_MLS.away = away
    USA_MLS.home = home
    USA_MLS.goal_line_away = goal_line_away
    USA_MLS.goal_line_home = goal_line_home
    USA_MLS.juice_goal_away = juice_goal_away
    USA_MLS.juice_goal_home = juice_goal_home
    USA_MLS.moneyLineAway = moneyLineAway
    USA_MLS.moneyLineHome = moneyLineHome
    USA_MLS.total = total
    USA_MLS.juice_total_over = juice_total_over
    USA_MLS.juice_total_under = juice_total_under
    USA_MLS.tt_away = tt_away
    USA_MLS.juice_over_away = juice_over_away
    USA_MLS.juice_under_away = juice_under_away
    USA_MLS.tt_home = tt_home
    USA_MLS.juice_over_home = juice_over_home
    USA_MLS.juice_under_home = juice_under_home
    USA_MLS.final_score_away = final_score_away
    USA_MLS.final_score_home = final_score_home
    USA_MLS.final_score_home = final_score_home
    USA_MLS.goal_away_1H = goal_away_1H
    USA_MLS.goal_home_1H = goal_home_1H
    USA_MLS.juice_goal_away_1H = juice_goal_away_1H
    USA_MLS.juice_goal_home_1H = juice_goal_home_1H
    USA_MLS.moneyLineAway_1H = moneyLineAway_1H
    USA_MLS.moneyLineHome_1H = moneyLineHome_1H
    USA_MLS.total_1H = total_1H
    USA_MLS.H1_juice_over = H1_juice_over
    USA_MLS.H1_juice_under = H1_juice_under
    USA_MLS.tt_away_1H = tt_away_1H
    USA_MLS.juice_over_away_1H = juice_over_away_1H
    USA_MLS.juice_under_away_1H = juice_under_away_1H
    USA_MLS.tt_home_1H = tt_home_1H
    USA_MLS.juice_over_home_1H = juice_over_home_1H
    USA_MLS.juice_under_home_1H = juice_under_home_1H

    db.session.commit()
    return jsonify({"msg": "USA_MLS edith successfully"}), 200


@app.route('/brazil_serie_A/<id>', methods=['PUT'])
def brazil_serie_AEdit(id):
    brazil_serie_A = Brazil_Serie_A.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    status = request.json['status']
    preview = request.json['preview']
    img_preview = request.json['img_preview']
    away = request.json['away']
    home = request.json['home']
    goal_line_away = request.json['goal_line_away']
    goal_line_home = request.json['goal_line_home']
    juice_goal_away = request.json['juice_goal_away']
    juice_goal_home = request.json['juice_goal_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']
    goal_away_1H = request.json['goal_away_1H']
    goal_home_1H = request.json['goal_home_1H']
    juice_goal_away_1H = request.json['juice_goal_away_1H']
    juice_goal_home_1H = request.json['juice_goal_home_1H']
    moneyLineAway_1H = request.json['moneyLineAway_1H']
    moneyLineHome_1H = request.json['moneyLineHome_1H']
    total_1H = request.json['total_1H']
    H1_juice_over = request.json['H1_juice_over']
    H1_juice_under = request.json['H1_juice_under']
    tt_away_1H = request.json['tt_away_1H']
    juice_over_away_1H = request.json['juice_over_away_1H']
    juice_under_away_1H = request.json['juice_under_away_1H']
    tt_home_1H = request.json['tt_home_1H']
    juice_over_home_1H = request.json['juice_over_home_1H']
    juice_under_home_1H = request.json['juice_under_home_1H']

    brazil_serie_A.date = date
    brazil_serie_A.hour = hour
    brazil_serie_A.preview = preview
    brazil_serie_A.img_preview = img_preview
    brazil_serie_A.status = status
    brazil_serie_A.away = away
    brazil_serie_A.home = home
    brazil_serie_A.goal_line_away = goal_line_away
    brazil_serie_A.goal_line_home = goal_line_home
    brazil_serie_A.juice_goal_away = juice_goal_away
    brazil_serie_A.juice_goal_home = juice_goal_home
    brazil_serie_A.moneyLineAway = moneyLineAway
    brazil_serie_A.moneyLineHome = moneyLineHome
    brazil_serie_A.total = total
    brazil_serie_A.juice_total_over = juice_total_over
    brazil_serie_A.juice_total_under = juice_total_under
    brazil_serie_A.tt_away = tt_away
    brazil_serie_A.juice_over_away = juice_over_away
    brazil_serie_A.juice_under_away = juice_under_away
    brazil_serie_A.tt_home = tt_home
    brazil_serie_A.juice_over_home = juice_over_home
    brazil_serie_A.juice_under_home = juice_under_home
    brazil_serie_A.final_score_away = final_score_away
    brazil_serie_A.final_score_home = final_score_home
    brazil_serie_A.final_score_home = final_score_home
    brazil_serie_A.goal_away_1H = goal_away_1H
    brazil_serie_A.goal_home_1H = goal_home_1H
    brazil_serie_A.juice_goal_away_1H = juice_goal_away_1H
    brazil_serie_A.juice_goal_home_1H = juice_goal_home_1H
    brazil_serie_A.moneyLineAway_1H = moneyLineAway_1H
    brazil_serie_A.moneyLineHome_1H = moneyLineHome_1H
    brazil_serie_A.total_1H = total_1H
    brazil_serie_A.H1_juice_over = H1_juice_over
    brazil_serie_A.H1_juice_under = H1_juice_under
    brazil_serie_A.tt_away_1H = tt_away_1H
    brazil_serie_A.juice_over_away_1H = juice_over_away_1H
    brazil_serie_A.juice_under_away_1H = juice_under_away_1H
    brazil_serie_A.tt_home_1H = tt_home_1H
    brazil_serie_A.juice_over_home_1H = juice_over_home_1H
    brazil_serie_A.juice_under_home_1H = juice_under_home_1H

    db.session.commit()
    return jsonify({"msg": "brazil_serie_A edith successfully"}), 200


@app.route('/colombia_primera_A/<id>', methods=['PUT'])
def colombia_primera_AEdit(id):
    colombia_primera_A = Colombia_Primera_A.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    status = request.json['status']
    preview = request.json['preview']
    img_preview = request.json['img_preview']
    away = request.json['away']
    home = request.json['home']
    goal_line_away = request.json['goal_line_away']
    goal_line_home = request.json['goal_line_home']
    juice_goal_away = request.json['juice_goal_away']
    juice_goal_home = request.json['juice_goal_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']
    goal_away_1H = request.json['goal_away_1H']
    goal_home_1H = request.json['goal_home_1H']
    juice_goal_away_1H = request.json['juice_goal_away_1H']
    juice_goal_home_1H = request.json['juice_goal_home_1H']
    moneyLineAway_1H = request.json['moneyLineAway_1H']
    moneyLineHome_1H = request.json['moneyLineHome_1H']
    total_1H = request.json['total_1H']
    H1_juice_over = request.json['H1_juice_over']
    H1_juice_under = request.json['H1_juice_under']
    tt_away_1H = request.json['tt_away_1H']
    juice_over_away_1H = request.json['juice_over_away_1H']
    juice_under_away_1H = request.json['juice_under_away_1H']
    tt_home_1H = request.json['tt_home_1H']
    juice_over_home_1H = request.json['juice_over_home_1H']
    juice_under_home_1H = request.json['juice_under_home_1H']

    colombia_primera_A.date = date
    colombia_primera_A.hour = hour
    colombia_primera_A.preview = preview
    colombia_primera_A.img_preview = img_preview
    colombia_primera_A.status = status
    colombia_primera_A.away = away
    colombia_primera_A.home = home
    colombia_primera_A.goal_line_away = goal_line_away
    colombia_primera_A.goal_line_home = goal_line_home
    colombia_primera_A.juice_goal_away = juice_goal_away
    colombia_primera_A.juice_goal_home = juice_goal_home
    colombia_primera_A.moneyLineAway = moneyLineAway
    colombia_primera_A.moneyLineHome = moneyLineHome
    colombia_primera_A.total = total
    colombia_primera_A.juice_total_over = juice_total_over
    colombia_primera_A.juice_total_under = juice_total_under
    colombia_primera_A.tt_away = tt_away
    colombia_primera_A.juice_over_away = juice_over_away
    colombia_primera_A.juice_under_away = juice_under_away
    colombia_primera_A.tt_home = tt_home
    colombia_primera_A.juice_over_home = juice_over_home
    colombia_primera_A.juice_under_home = juice_under_home
    colombia_primera_A.final_score_away = final_score_away
    colombia_primera_A.final_score_home = final_score_home
    colombia_primera_A.final_score_home = final_score_home
    colombia_primera_A.goal_away_1H = goal_away_1H
    colombia_primera_A.goal_home_1H = goal_home_1H
    colombia_primera_A.juice_goal_away_1H = juice_goal_away_1H
    colombia_primera_A.juice_goal_home_1H = juice_goal_home_1H
    colombia_primera_A.moneyLineAway_1H = moneyLineAway_1H
    colombia_primera_A.moneyLineHome_1H = moneyLineHome_1H
    colombia_primera_A.total_1H = total_1H
    colombia_primera_A.H1_juice_over = H1_juice_over
    colombia_primera_A.H1_juice_under = H1_juice_under
    colombia_primera_A.tt_away_1H = tt_away_1H
    colombia_primera_A.juice_over_away_1H = juice_over_away_1H
    colombia_primera_A.juice_under_away_1H = juice_under_away_1H
    colombia_primera_A.tt_home_1H = tt_home_1H
    colombia_primera_A.juice_over_home_1H = juice_over_home_1H
    colombia_primera_A.juice_under_home_1H = juice_under_home_1H

    db.session.commit()
    return jsonify({"msg": "colombia_primera_A edith successfully"}), 200


@app.route('/costa_rica_PD/<id>', methods=['PUT'])
def costa_rica_PDEdit(id):
    costa_rica_PD = Costa_Rica_PD.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    status = request.json['status']
    preview = request.json['preview']
    img_preview = request.json['img_preview']
    away = request.json['away']
    home = request.json['home']
    goal_line_away = request.json['goal_line_away']
    goal_line_home = request.json['goal_line_home']
    juice_goal_away = request.json['juice_goal_away']
    juice_goal_home = request.json['juice_goal_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']
    goal_away_1H = request.json['goal_away_1H']
    goal_home_1H = request.json['goal_home_1H']
    juice_goal_away_1H = request.json['juice_goal_away_1H']
    juice_goal_home_1H = request.json['juice_goal_home_1H']
    moneyLineAway_1H = request.json['moneyLineAway_1H']
    moneyLineHome_1H = request.json['moneyLineHome_1H']
    total_1H = request.json['total_1H']
    H1_juice_over = request.json['H1_juice_over']
    H1_juice_under = request.json['H1_juice_under']
    tt_away_1H = request.json['tt_away_1H']
    juice_over_away_1H = request.json['juice_over_away_1H']
    juice_under_away_1H = request.json['juice_under_away_1H']
    tt_home_1H = request.json['tt_home_1H']
    juice_over_home_1H = request.json['juice_over_home_1H']
    juice_under_home_1H = request.json['juice_under_home_1H']

    costa_rica_PD.date = date
    costa_rica_PD.hour = hour
    costa_rica_PD.preview = preview
    costa_rica_PD.img_preview = img_preview
    costa_rica_PD.status = status
    costa_rica_PD.away = away
    costa_rica_PD.home = home
    costa_rica_PD.goal_line_away = goal_line_away
    costa_rica_PD.goal_line_home = goal_line_home
    costa_rica_PD.juice_goal_away = juice_goal_away
    costa_rica_PD.juice_goal_home = juice_goal_home
    costa_rica_PD.moneyLineAway = moneyLineAway
    costa_rica_PD.moneyLineHome = moneyLineHome
    costa_rica_PD.total = total
    costa_rica_PD.juice_total_over = juice_total_over
    costa_rica_PD.juice_total_under = juice_total_under
    costa_rica_PD.tt_away = tt_away
    costa_rica_PD.juice_over_away = juice_over_away
    costa_rica_PD.juice_under_away = juice_under_away
    costa_rica_PD.tt_home = tt_home
    costa_rica_PD.juice_over_home = juice_over_home
    costa_rica_PD.juice_under_home = juice_under_home
    costa_rica_PD.final_score_away = final_score_away
    costa_rica_PD.final_score_home = final_score_home
    costa_rica_PD.final_score_home = final_score_home
    costa_rica_PD.goal_away_1H = goal_away_1H
    costa_rica_PD.goal_home_1H = goal_home_1H
    costa_rica_PD.juice_goal_away_1H = juice_goal_away_1H
    costa_rica_PD.juice_goal_home_1H = juice_goal_home_1H
    costa_rica_PD.moneyLineAway_1H = moneyLineAway_1H
    costa_rica_PD.moneyLineHome_1H = moneyLineHome_1H
    costa_rica_PD.total_1H = total_1H
    costa_rica_PD.H1_juice_over = H1_juice_over
    costa_rica_PD.H1_juice_under = H1_juice_under
    costa_rica_PD.tt_away_1H = tt_away_1H
    costa_rica_PD.juice_over_away_1H = juice_over_away_1H
    costa_rica_PD.juice_under_away_1H = juice_under_away_1H
    costa_rica_PD.tt_home_1H = tt_home_1H
    costa_rica_PD.juice_over_home_1H = juice_over_home_1H
    costa_rica_PD.juice_under_home_1H = juice_under_home_1H

    db.session.commit()
    return jsonify({"msg": "costa_rica_PD edith successfully"}), 200


@app.route('/stats_nba_team/<id>', methods=['PUT'])
def stats_nba_teamEdit(id):
    stats_nba_team = Stats_nba_team.query.get(id)
    season = request.json['season']
    team = request.json['team']
    conference = request.json['conference']
    division = request.json['division']
    pts = request.json['pts']
    fmg = request.json['fmg']
    fga = request.json['fga']
    fg = request.json['fg']
    fg_AVG = request.json['fg_AVG']
    three_pm = request.json['three_pm']
    three_pa = request.json['three_pa']
    three_p_AVG = request.json['three_p_AVG']
    ftm = request.json['ftm']
    fta = request.json['fta']
    ft_AVG = request.json['ft_AVG']
    Or = request.json['Or']
    dr = request.json['dr']
    reb = request.json['reb']
    ast = request.json['ast']
    stl = request.json['stl']
    blk = request.json['blk']
    to = request.json['to']
    pf = request.json['pf']

    stats_nba_team.season = season
    stats_nba_team.team = team
    stats_nba_team.conference = conference
    stats_nba_team.division = division
    stats_nba_team.pts = pts
    stats_nba_team.fmg = fmg
    stats_nba_team.fga = fga
    stats_nba_team.fg = fg
    stats_nba_team.fg_AVG = fg_AVG
    stats_nba_team.three_pm = three_pm
    stats_nba_team.three_pa = three_pa
    stats_nba_team.three_p_AVG = three_p_AVG
    stats_nba_team.ftm = ftm
    stats_nba_team.fta = fta
    stats_nba_team.ft_AVG = ft_AVG
    stats_nba_team.Or = Or
    stats_nba_team.dr = dr
    stats_nba_team.reb = reb
    stats_nba_team.ast = ast
    stats_nba_team.stl = stl
    stats_nba_team.blk = blk
    stats_nba_team.to = to
    stats_nba_team.pf = pf

    db.session.commit()
    return jsonify({"msg": "stats_nba_team edith successfully"}), 200


@app.route('/stats_nba_player/<id>', methods=['PUT'])
def stats_nba_playerEdit(id):
    stats_nba_player = Stats_nba_player.query.get(id)
    name = request.json['name']
    height = request.json['height']
    weight = request.json['weight']
    birth = request.json['birth']
    college = request.json['college']
    season = request.json['season']
    team = request.json['team']
    dorsal = request.json['dorsal']
    minutes = request.json['minutes']
    position = request.json['position']
    gp = request.json['gp']
    gs = request.json['gs']
    fg = request.json['fg']
    fg_AVG = request.json['fg_AVG']
    three_pt = request.json['three_pt']
    three_pt_AVG = request.json['three_pt_AVG']
    ft = request.json['ft']
    ft_AVG = request.json['ft_AVG']
    Or = request.json['Or']
    dr = request.json['dr']
    reb = request.json['reb']
    ast = request.json['ast']
    stl = request.json['stl']
    blk = request.json['blk']
    to = request.json['to']
    pf = request.json['pf']
    pts = request.json['pts']

    stats_nba_player.name = name
    stats_nba_player.height = height
    stats_nba_player.weight = weight
    stats_nba_player.birth = birth
    stats_nba_player.college = college
    stats_nba_player.season = season
    stats_nba_player.team = team
    stats_nba_player.dorsal = dorsal
    stats_nba_player.minutes = minutes
    stats_nba_player.position = position
    stats_nba_player.gp = gp
    stats_nba_player.gs = gs
    stats_nba_player.fg = fg
    stats_nba_player.fg_AVG = fg_AVG
    stats_nba_player.three_pt = three_pt
    stats_nba_player.three_pt_AVG = three_pt_AVG
    stats_nba_player.ft = ft
    stats_nba_player.ft_AVG = ft_AVG
    stats_nba_player.Or = Or
    stats_nba_player.dr = dr
    stats_nba_player.reb = reb
    stats_nba_player.ast = ast
    stats_nba_player.stl = stl
    stats_nba_player.blk = blk
    stats_nba_player.to = to
    stats_nba_player.pf = pf
    stats_nba_player.pts = pts

    db.session.commit()
    return jsonify({"msg": "stats_nba_player edith successfully"}), 200


@app.route('/stats_mlb_team/<id>', methods=['PUT'])
def stats_mlb_teamEdit(id):
    stats_mlb_team = Stats_mlb_team.query.get(id)
    season = request.json['season']
    team = request.json['team']
    league = request.json['league']
    division = request.json['division']
    w = request.json['w']
    L = request.json['L']
    pct = request.json['pct']
    gb = request.json['gb']
    home = request.json['home']
    away = request.json['away']
    rs = request.json['rs']
    ra = request.json['ra']
    diff = request.json['diff']
    strk = request.json['strk']
    L10 = request.json['L10']
    poff = request.json['poff']

    stats_mlb_team.season = season
    stats_mlb_team.team = team
    stats_mlb_team.league = league
    stats_mlb_team.division = division
    stats_mlb_team.w = w
    stats_mlb_team.L = L
    stats_mlb_team.pct = pct
    stats_mlb_team.gb = gb
    stats_mlb_team.home = home
    stats_mlb_team.away = away
    stats_mlb_team.rs = rs
    stats_mlb_team.ra = ra
    stats_mlb_team.diff = diff
    stats_mlb_team.strk = strk
    stats_mlb_team.L10 = L10
    stats_mlb_team.poff = poff

    db.session.commit()
    return jsonify({"msg": "stats_mlb_team edith successfully"}), 200


@app.route('/stats_mlb_player/<id>', methods=['PUT'])
def stats_mlb_playerEdit(id):
    stats_mlb_player = Stats_mlb_player.query.get(id)
    name = request.json['name']
    height = request.json['height']
    weight = request.json['weight']
    birth = request.json['birth']
    season = request.json['season']
    team = request.json['team']
    dorsal = request.json['dorsal']
    position = request.json['position']
    gp = request.json['gp']
    ab = request.json['ab']
    r = request.json['r']
    h = request.json['h']
    two_b = request.json['two_b']
    three_b = request.json['three_b']
    hb = request.json['hb']
    rbi = request.json['rbi']
    tb = request.json['tb']
    bb = request.json['bb']
    so = request.json['so']
    sb = request.json['sb']
    avg = request.json['avg']
    obp = request.json['obp']
    slg = request.json['slg']
    ops = request.json['ops']
    war = request.json['war']

    stats_mlb_player.name = name
    stats_mlb_player.height = height
    stats_mlb_player.weight = weight
    stats_mlb_player.birth = birth
    stats_mlb_player.season = season
    stats_mlb_player.team = team
    stats_mlb_player.dorsal = dorsal
    stats_mlb_player.position = position
    stats_mlb_player.gp = gp
    stats_mlb_player.ab = ab
    stats_mlb_player.r = r
    stats_mlb_player.h = h
    stats_mlb_player.two_b = two_b
    stats_mlb_player.three_b = three_b
    stats_mlb_player.hb = hb
    stats_mlb_player.rbi = rbi
    stats_mlb_player.tb = tb
    stats_mlb_player.bb = bb
    stats_mlb_player.so = so
    stats_mlb_player.sb = sb
    stats_mlb_player.avg = avg
    stats_mlb_player.obp = obp
    stats_mlb_player.slg = slg
    stats_mlb_player.ops = ops
    stats_mlb_player.war = war

    db.session.commit()
    return jsonify({"msg": "stats_mlb_player edith successfully"}), 200


@app.route('/stats_nhl_team/<id>', methods=['PUT'])
def stats_nhl_teamEdit(id):
    stats_nhl_team = Stats_nhl_team.query.get(id)
    season = request.json['season']
    team = request.json['team']
    conference = request.json['conference']
    division = request.json['division']
    w = request.json['w']
    L = request.json['L']

    Ga_a = request.json['Ga_a']
    otl = request.json['otl']
    sa = request.json['sa']
    ga = request.json['ga']
    s = request.json['s']
    sv_AVG = request.json['sv_AVG']
    so = request.json['so']
    so_sa = request.json['so_sa']
    sos = request.json['sos']
    sos_AVG = request.json['sos_AVG']

    stats_nhl_team.season = season
    stats_nhl_team.team = team
    stats_nhl_team.conference = conference
    stats_nhl_team.division = division
    stats_nhl_team.w = w
    stats_nhl_team.L = L
    stats_nhl_team.Ga_a = Ga_a
    stats_nhl_team.otl = otl
    stats_nhl_team.sa = sa
    stats_nhl_team.ga = ga
    stats_nhl_team.s = s
    stats_nhl_team.sv_AVG = sv_AVG
    stats_nhl_team.so = so
    stats_nhl_team.so_sa = so_sa
    stats_nhl_team.sos = sos
    stats_nhl_team.sos_AVG = sos_AVG

    db.session.commit()
    return jsonify({"msg": "stats_nhl_team edith successfully"}), 200


@app.route('/stats_nhl_player/<id>', methods=['PUT'])
def stats_nhl_playerEdit(id):
    stats_nhl_player = Stats_nhl_player.query.get(id)
    name = request.json['name']
    height = request.json['height']
    weight = request.json['weight']
    birth = request.json['birth']
    season = request.json['season']
    team = request.json['team']
    dorsal = request.json['dorsal']
    position = request.json['position']
    gp = request.json['gp']

    g = request.json['g']
    a = request.json['a']
    pts = request.json['pts']
    p_m_rating = request.json['p_m_rating']
    pim = request.json['pim']
    sog = request.json['sog']
    spct = request.json['spct']
    ppg = request.json['ppg']
    ppa = request.json['ppa']
    shg = request.json['shg']
    sha = request.json['sha']
    gwg = request.json['gwg']
    gtg = request.json['gtg']
    toi_g = request.json['toi_g']
    prod = request.json['prod']

    stats_nhl_player.name = name
    stats_nhl_player.height = height
    stats_nhl_player.weight = weight
    stats_nhl_player.birth = birth
    stats_nhl_player.season = season
    stats_nhl_player.team = team
    stats_nhl_player.dorsal = dorsal
    stats_nhl_player.position = position
    stats_nhl_player.gp = gp
    stats_nhl_player.g = g
    stats_nhl_player.a = a
    stats_nhl_player.pts = pts
    stats_nhl_player.p_m_rating = p_m_rating
    stats_nhl_player.pim = pim
    stats_nhl_player.sog = sog
    stats_nhl_player.spct = spct
    stats_nhl_player.ppg = ppg
    stats_nhl_player.ppa = ppa
    stats_nhl_player.shg = shg
    stats_nhl_player.sha = sha
    stats_nhl_player.gwg = gwg
    stats_nhl_player.gtg = gtg
    stats_nhl_player.toi_g = toi_g
    stats_nhl_player.prod = prod
    db.session.commit()
    return jsonify({"msg": "stats_nhl_player edith successfully"}), 200


@app.route('/stats_box_fighter/<id>', methods=['PUT'])
def stats_box_fighterEdit(id):
    stats_box_fighter = Stats_box_fighter.query.get(id)
    name = request.json['name']
    nickname = request.json['nickname']
    height = request.json['height']
    weight = request.json['weight']
    birth = request.json['birth']
    country = request.json['country']
    association = request.json['association']
    category = request.json['category']
    w = request.json['w']
    w_by = request.json['w_by']
    L = request.json['L']
    L_by = request.json['L_by']

    stats_box_fighter.name = name
    stats_box_fighter.nickname = nickname
    stats_box_fighter.height = height
    stats_box_fighter.weight = weight
    stats_box_fighter.birth = birth
    stats_box_fighter.country = country
    stats_box_fighter.association = association
    stats_box_fighter.category = category
    stats_box_fighter.w = w
    stats_box_fighter.w_by = w_by
    stats_box_fighter.L = L
    stats_box_fighter.L_by = L_by
    db.session.commit()
    return jsonify({"msg": "stats_box_fighter edith successfully"}), 200


@app.route('/stats_mma_fighter/<id>', methods=['PUT'])
def stats_mma_fighterEdit(id):
    stats_mma_fighter = Stats_mma_fighter.query.get(id)
    name = request.json['name']
    nickname = request.json['nickname']
    height = request.json['height']
    weight = request.json['weight']
    birth = request.json['birth']
    country = request.json['country']
    association = request.json['association']
    category = request.json['category']
    w = request.json['w']
    w_by = request.json['w_by']
    L = request.json['L']
    L_by = request.json['L_by']

    stats_mma_fighter.name = name
    stats_mma_fighter.nickname = nickname
    stats_mma_fighter.height = height
    stats_mma_fighter.weight = weight
    stats_mma_fighter.birth = birth
    stats_mma_fighter.country = country
    stats_mma_fighter.association = association
    stats_mma_fighter.category = category
    stats_mma_fighter.w = w
    stats_mma_fighter.w_by = w_by
    stats_mma_fighter.L = L
    stats_mma_fighter.L_by = L_by
    db.session.commit()
    return jsonify({"msg": "stats_mma_fighter edith successfully"}), 200


@app.route('/stats_nfl_team/<id>', methods=['PUT'])
def stats_nfl_teamEdit(id):
    stats_nfl_team = Stats_nfl_team.query.get(id)
    season = request.json['season']
    team = request.json['team']
    conference = request.json['conference']
    division = request.json['division']
    TP = request.json['TP']
    ttpg = request.json['ttpg']
    t_td = request.json['t_td']
    t_1_down = request.json['t_1_down']
    Russ_1_d = request.json['Russ_1_d']
    pass_1_d = request.json['pass_1_d']
    down_1_penal = request.json['down_1_penal']
    down_3_eff = request.json['down_3_eff']
    down_3_AVG = request.json['down_3_AVG']
    down_4_eff = request.json['down_4_eff']
    down_4_AVG = request.json['down_4_AVG']
    comp_att = request.json['comp_att']
    net_pass_y = request.json['net_pass_y']
    y_p_pas_attps = request.json['y_p_pas_attps']
    net_pass_y_pg = request.json['net_pass_y_pg']
    pass_td = request.json['pass_td']
    interceptions = request.json['interceptions']
    sacks_y_lost = request.json['sacks_y_lost']
    russ_attps = request.json['russ_attps']
    russ_y = request.json['russ_y']
    y_p_russ_attp = request.json['y_p_russ_attp']
    russ_y_pg = request.json['russ_y_pg']
    russ_td = request.json['russ_td']
    total_of_plays = request.json['total_of_plays']
    total_y = request.json['total_y']
    y_pg = request.json['y_pg']
    kickoffs_t = request.json['kickoffs_t']
    AVG_kickoff_return_y = request.json['AVG_kickoff_return_y']
    punt_t = request.json['punt_t']
    AVG_punt_ruturn_y = request.json['AVG_punt_ruturn_y']
    int_t = request.json['int_t']
    AVG_intercept_y = request.json['AVG_intercept_y']
    net_AVG_punt_y = request.json['net_AVG_punt_y']
    punt_ty = request.json['punt_ty']
    fg_goog_attps = request.json['fg_goog_attps']
    touchback_percent = request.json['touchback_percent']
    penal_ty = request.json['penal_ty']
    penal_y_AVG_pg = request.json['penal_y_AVG_pg']
    possesion_time = request.json['possesion_time']
    fumbles_lost = request.json['fumbles_lost']
    turnover_ratio = request.json['turnover_ratio']

    stats_nfl_team.season = season
    stats_nfl_team.team = team
    stats_nfl_team.conference = conference
    stats_nfl_team.division = division
    stats_nfl_team.TP = TP
    stats_nfl_team.ttpg = ttpg
    stats_nfl_team.t_td = t_td
    stats_nfl_team.t_1_down = t_1_down
    stats_nfl_team.Russ_1_d = Russ_1_d
    stats_nfl_team.pass_1_d = pass_1_d
    stats_nfl_team.down_1_penal = down_1_penal
    stats_nfl_team.down_3_eff = down_3_eff
    stats_nfl_team.down_3_AVG = down_3_AVG
    stats_nfl_team.down_4_eff = down_4_eff
    stats_nfl_team.down_4_AVG = down_4_AVG
    stats_nfl_team.comp_att = comp_att
    stats_nfl_team.net_pass_y = net_pass_y
    stats_nfl_team.y_p_pas_attps = y_p_pas_attps
    stats_nfl_team.net_pass_y_pg = net_pass_y_pg
    stats_nfl_team.pass_td = pass_td
    stats_nfl_team.interceptions = interceptions
    stats_nfl_team.sacks_y_lost = sacks_y_lost
    stats_nfl_team.russ_attps = russ_attps
    stats_nfl_team.russ_y = russ_y
    stats_nfl_team.y_p_russ_attp = y_p_russ_attp
    stats_nfl_team.russ_y_pg = russ_y_pg
    stats_nfl_team.russ_td = russ_td
    stats_nfl_team.total_of_plays = total_of_plays
    stats_nfl_team.total_y = total_y
    stats_nfl_team.y_pg = y_pg
    stats_nfl_team.kickoffs_t = kickoffs_t
    stats_nfl_team.AVG_kickoff_return_y = AVG_kickoff_return_y
    stats_nfl_team.punt_t = punt_t
    stats_nfl_team.AVG_punt_ruturn_y = AVG_punt_ruturn_y
    stats_nfl_team.int_t = int_t
    stats_nfl_team.AVG_intercept_y = AVG_intercept_y
    stats_nfl_team.net_AVG_punt_y = net_AVG_punt_y
    stats_nfl_team.punt_ty = punt_ty
    stats_nfl_team.fg_goog_attps = fg_goog_attps
    stats_nfl_team.touchback_percent = touchback_percent
    stats_nfl_team.penal_ty = penal_ty
    stats_nfl_team.penal_y_AVG_pg = penal_y_AVG_pg
    stats_nfl_team.possesion_time = possesion_time
    stats_nfl_team.fumbles_lost = fumbles_lost
    stats_nfl_team.turnover_ratio = turnover_ratio

    db.session.commit()
    return jsonify({"msg": "stats_nfl_team edith successfully"}), 200


@app.route('/stats_defensive_player_nfl/<id>', methods=['PUT'])
def stats_defensive_player_nflEdit(id):
    stats_defensive_player_nfl = Stats_defensive_player_nfl.query.get(id)
    name = request.json['name']
    height = request.json['height']
    weight = request.json['weight']
    birth = request.json['birth']
    position = request.json['position']
    dorsal = request.json['dorsal']
    season = request.json['season']
    team = request.json['team']
    games = request.json['games']
    tack_solo = request.json['tack_solo']
    tack_ast = request.json['tack_ast']
    tack_total = request.json['tack_total']
    sacks = request.json['sacks']
    sacks_yards = request.json['sacks_yards']
    tfl = request.json['tfl']
    pd = request.json['pd']
    Int = request.json['Int']
    yds = request.json['yds']
    ing = request.json['ing']
    td = request.json['td']
    ff = request.json['ff']
    fr = request.json['fr']
    ftd = request.json['ftd']
    kb = request.json['kb']

    stats_defensive_player_nfl.name = name
    stats_defensive_player_nfl.height = height
    stats_defensive_player_nfl.weight = weight
    stats_defensive_player_nfl.birth = birth
    stats_defensive_player_nfl.position = position
    stats_defensive_player_nfl.dorsal = dorsal
    stats_defensive_player_nfl.season = season
    stats_defensive_player_nfl.team = team
    stats_defensive_player_nfl.games = games
    stats_defensive_player_nfl.tack_solo = tack_solo
    stats_defensive_player_nfl.tack_ast = tack_ast
    stats_defensive_player_nfl.tack_total = tack_total
    stats_defensive_player_nfl.sacks = sacks
    stats_defensive_player_nfl.sacks_yards = sacks_yards
    stats_defensive_player_nfl.tfl = tfl
    stats_defensive_player_nfl.pd = pd
    stats_defensive_player_nfl.Int = Int
    stats_defensive_player_nfl.yds = yds
    stats_defensive_player_nfl.ing = ing
    stats_defensive_player_nfl.td = td
    stats_defensive_player_nfl.ff = ff
    stats_defensive_player_nfl.fr = fr
    stats_defensive_player_nfl.ftd = ftd
    stats_defensive_player_nfl.kb = kb
    db.session.commit()
    return jsonify({"msg": "stats_defensive_player_nfl edith successfully"}), 200


@app.route('/stats_offensive_player_nfl/<id>', methods=['PUT'])
def stats_offensive_player_nflEdit(id):
    stats_offensive_player_nfl = Stats_offensive_player_nfl.query.get(id)
    name = request.json['name']
    height = request.json['height']
    weight = request.json['weight']
    birth = request.json['birth']
    position = request.json['position']
    dorsal = request.json['dorsal']
    season = request.json['season']
    team = request.json['team']
    games = request.json['games']

    Cmp = request.json['Cmp']
    pass_att = request.json['pass_att']
    cmp_AVG = request.json['cmp_AVG']
    yards = request.json['yards']
    yards_AVG = request.json['yards_AVG']
    yards_pg = request.json['yards_pg']
    pass_td = request.json['pass_td']
    Int = request.json['Int']
    asck = request.json['asck']
    syl = request.json['syl']
    rtg = request.json['rtg']
    russ_att = request.json['russ_att']
    russ_yards = request.json['russ_yards']
    yards_p_russ = request.json['yards_p_russ']
    big = request.json['big']
    rush_tt = request.json['rush_tt']
    rush_yard_pg = request.json['rush_yard_pg']
    fum = request.json['fum']
    lst = request.json['lst']
    fd = request.json['fd']
    rec = request.json['rec']
    r_tgts = request.json['r_tgts']
    r_yards = request.json['r_yards']
    yards_p_r = request.json['yards_p_r']
    r_td = request.json['r_td']
    lr = request.json['lr']
    r_big = request.json['r_big']
    r_ypg = request.json['r_ypg']
    r_fl = request.json['r_fl']
    r_yac = request.json['r_yac']
    r_fd = request.json['r_fd']
    pts = request.json['pts']

    stats_offensive_player_nfl.name = name
    stats_offensive_player_nfl.height = height
    stats_offensive_player_nfl.weight = weight
    stats_offensive_player_nfl.birth = birth
    stats_offensive_player_nfl.position = position
    stats_offensive_player_nfl.dorsal = dorsal
    stats_offensive_player_nfl.season = season
    stats_offensive_player_nfl.team = team
    stats_offensive_player_nfl.games = games
    stats_offensive_player_nfl.Cmp = Cmp
    stats_offensive_player_nfl.pass_att = pass_att
    stats_offensive_player_nfl.cmp_AVG = cmp_AVG
    stats_offensive_player_nfl.yards = yards
    stats_offensive_player_nfl.yards_AVG = yards_AVG
    stats_offensive_player_nfl.yards_pg = yards_pg
    stats_offensive_player_nfl.pass_td = pass_td
    stats_offensive_player_nfl.Int = Int
    stats_offensive_player_nfl.asck = asck
    stats_offensive_player_nfl.syl = syl
    stats_offensive_player_nfl.rtg = rtg
    stats_offensive_player_nfl.russ_att = russ_att
    stats_offensive_player_nfl.russ_yards = russ_yards
    stats_offensive_player_nfl.yards_p_russ = yards_p_russ
    stats_offensive_player_nfl.big = big
    stats_offensive_player_nfl.rush_tt = rush_tt
    stats_offensive_player_nfl.rush_yard_pg = rush_yard_pg
    stats_offensive_player_nfl.fum = fum
    stats_offensive_player_nfl.lst = lst
    stats_offensive_player_nfl.fd = fd
    stats_offensive_player_nfl.rec = rec
    stats_offensive_player_nfl.r_tgts = r_tgts
    stats_offensive_player_nfl.r_yards = r_yards
    stats_offensive_player_nfl.yards_p_r = yards_p_r
    stats_offensive_player_nfl.r_td = r_td
    stats_offensive_player_nfl.lr = lr
    stats_offensive_player_nfl.r_big = r_big
    stats_offensive_player_nfl.r_ypg = r_ypg
    stats_offensive_player_nfl.r_fl = r_fl
    stats_offensive_player_nfl.r_yac = r_yac
    stats_offensive_player_nfl.r_fd = r_fd
    stats_offensive_player_nfl.pts = pts
    db.session.commit()
    return jsonify({"msg": "stats_offensive_player_nfl edith successfully"}), 200


@app.route('/stats_returning_player_nfl/<id>', methods=['PUT'])
def stats_returning_player_nflEdit(id):
    stats_returning_player_nfl = Stats_returning_player_nfl.query.get(id)
    name = request.json['name']
    height = request.json['height']
    weight = request.json['weight']
    birth = request.json['birth']
    position = request.json['position']
    dorsal = request.json['dorsal']
    season = request.json['season']
    team = request.json['team']
    games = request.json['games']
    kick_returns = request.json['kick_returns']
    kick_returns_yards = request.json['kick_returns_yards']
    yards_p_k_p = request.json['yards_p_k_p']
    l_k_r = request.json['l_k_r']
    k_r_td = request.json['k_r_td']
    punt_r = request.json['punt_r']
    punt_r_y = request.json['punt_r_y']
    y_ppr = request.json['y_ppr']
    lpr = request.json['lpr']
    pr_td = request.json['pr_td']
    punt_r_fair_carches = request.json['punt_r_fair_carches']

    stats_returning_player_nfl.name = name
    stats_returning_player_nfl.height = height
    stats_returning_player_nfl.weight = weight
    stats_returning_player_nfl.birth = birth
    stats_returning_player_nfl.position = position
    stats_returning_player_nfl.dorsal = dorsal
    stats_returning_player_nfl.season = season
    stats_returning_player_nfl.team = team
    stats_returning_player_nfl.games = games
    stats_returning_player_nfl.kick_returns = kick_returns
    stats_returning_player_nfl.kick_returns_yards = kick_returns_yards
    stats_returning_player_nfl.yards_p_k_p = yards_p_k_p
    stats_returning_player_nfl.l_k_r = l_k_r
    stats_returning_player_nfl.k_r_td = k_r_td
    stats_returning_player_nfl.punt_r = punt_r
    stats_returning_player_nfl.punt_r_y = punt_r_y
    stats_returning_player_nfl.y_ppr = y_ppr
    stats_returning_player_nfl.lpr = lpr
    stats_returning_player_nfl.pr_td = pr_td
    stats_returning_player_nfl.punt_r_fair_carches = punt_r_fair_carches
    db.session.commit()
    return jsonify({"msg": "stats_returning_player_nfl edith successfully"}), 200


@app.route('/stats_kiking_player_nfl/<id>', methods=['PUT'])
def stats_kiking_player_nflEdit(id):
    stats_kiking_player_nfl = Stats_kiking_player_nfl.query.get(id)
    name = request.json['name']
    height = request.json['height']
    weight = request.json['weight']
    birth = request.json['birth']
    position = request.json['position']
    dorsal = request.json['dorsal']
    season = request.json['season']
    team = request.json['team']
    games = request.json['games']
    fgm = request.json['fgm']
    fga = request.json['fga']
    fg_AVG = request.json['fg_AVG']
    lng = request.json['lng']
    yars_f_goals_1_19 = request.json['yars_f_goals_1_19']
    yars_f_goals_20_29 = request.json['yars_f_goals_20_29']
    yars_f_goals_30_49 = request.json['yars_f_goals_30_49']
    yars_f_goals_40_49 = request.json['yars_f_goals_40_49']
    more_50 = request.json['more_50']
    xpm = request.json['xpm']
    xpa = request.json['xpa']
    xp_AVG = request.json['xp_AVG']

    stats_kiking_player_nfl.name = name
    stats_kiking_player_nfl.height = height
    stats_kiking_player_nfl.weight = weight
    stats_kiking_player_nfl.birth = birth
    stats_kiking_player_nfl.position = position
    stats_kiking_player_nfl.dorsal = dorsal
    stats_kiking_player_nfl.season = season
    stats_kiking_player_nfl.team = team
    stats_kiking_player_nfl.games = games
    stats_kiking_player_nfl.fgm = fgm
    stats_kiking_player_nfl.fga = fga
    stats_kiking_player_nfl.fg_AVG = fg_AVG
    stats_kiking_player_nfl.lng = lng
    stats_kiking_player_nfl.yars_f_goals_1_19 = yars_f_goals_1_19
    stats_kiking_player_nfl.yars_f_goals_20_29 = yars_f_goals_20_29
    stats_kiking_player_nfl.yars_f_goals_30_49 = yars_f_goals_30_49
    stats_kiking_player_nfl.yars_f_goals_40_49 = yars_f_goals_40_49
    stats_kiking_player_nfl.more_50 = more_50
    stats_kiking_player_nfl.xpm = xpm
    stats_kiking_player_nfl.xpa = xpa
    stats_kiking_player_nfl.xp_AVG = xp_AVG
    db.session.commit()
    return jsonify({"msg": "stats_kiking_player_nfl edith successfully"}), 200


@app.route('/stats_punting_player_nfl/<id>', methods=['PUT'])
def stats_punting_player_nflEdit(id):
    stats_punting_player_nfl = Stats_punting_player_nfl.query.get(id)
    name = request.json['name']
    height = request.json['height']
    weight = request.json['weight']
    birth = request.json['birth']
    position = request.json['position']
    dorsal = request.json['dorsal']
    season = request.json['season']
    team = request.json['team']
    games = request.json['games']
    punts = request.json['punts']
    yards = request.json['yards']
    lng = request.json['lng']
    lng = request.json['lng']
    AVG = request.json['AVG']
    net = request.json['net']
    p_blk = request.json['p_blk']
    IN_20 = request.json['IN_20']
    tb = request.json['tb']
    fc = request.json['fc']
    att = request.json['att']
    punt_return_yds = request.json['punt_return_yds']
    AVG_punt_retun_yards = request.json['AVG_punt_retun_yards']

    stats_punting_player_nfl.name = name
    stats_punting_player_nfl.height = height
    stats_punting_player_nfl.weight = weight
    stats_punting_player_nfl.birth = birth
    stats_punting_player_nfl.position = position
    stats_punting_player_nfl.dorsal = dorsal
    stats_punting_player_nfl.season = season
    stats_punting_player_nfl.team = team
    stats_punting_player_nfl.games = games
    stats_punting_player_nfl.punts = punts
    stats_punting_player_nfl.yards = yards
    stats_punting_player_nfl.lng = lng
    stats_punting_player_nfl.lng = lng
    stats_punting_player_nfl.AVG = AVG
    stats_punting_player_nfl.net = net
    stats_punting_player_nfl.p_blk = p_blk
    stats_punting_player_nfl.IN_20 = IN_20
    stats_punting_player_nfl.tb = tb
    stats_punting_player_nfl.fc = fc
    stats_punting_player_nfl.att = att
    stats_punting_player_nfl.punt_return_yds = punt_return_yds
    stats_punting_player_nfl.AVG_punt_retun_yards = AVG_punt_retun_yards
    db.session.commit()
    return jsonify({"msg": "stats_punting_player_nfl edith successfully"}), 200

# Endpoint for deleting a record


@app.route("/news/<id>", methods=["DELETE"])
def news_delete(id):
    news = News.query.get(id)
    db.session.delete(news)
    db.session.commit()
    return "News was successfully deleted"


@app.route("/casinos/<id>", methods=["DELETE"])
def casinos_delete(id):
    casinos = Casinos.query.get(id)
    db.session.delete(casinos)
    db.session.commit()
    return "casinos was successfully deleted"


@app.route("/mlb/<id>", methods=["DELETE"])
def mlb_delete(id):
    mlb = Nlb.query.get(id)
    db.session.delete(mlb)
    db.session.commit()
    return "mlb was successfully deleted"


@app.route("/ncaa_baseball/<id>", methods=["DELETE"])
def ncaa_baseball_delete(id):
    ncaa_baseball = Ncaa_Baseball.query.get(id)
    db.session.delete(ncaa_baseball)
    db.session.commit()
    return "ncaa_baseball was successfully deleted"


@app.route("/nfl/<id>", methods=["DELETE"])
def nfl_delete(id):
    nfl = Nfl.query.get(id)
    db.session.delete(nfl)
    db.session.commit()
    return "nfl was successfully deleted"


@app.route("/ncaa_football/<id>", methods=["DELETE"])
def ncaa_football_delete(id):
    ncaa_football = Ncaa_Football.query.get(id)
    db.session.delete(ncaa_football)
    db.session.commit()
    return "ncaa_football was successfully deleted"


@app.route("/nba/<id>", methods=["DELETE"])
def nba_delete(id):
    nba = Nba.query.get(id)
    db.session.delete(nba)
    db.session.commit()
    return "nba was successfully deleted"


@app.route("/ncaa_basketball/<id>", methods=["DELETE"])
def ncaa_basketball_delete(id):
    ncaa_basketball = Ncaa_Basketball.query.get(id)
    db.session.delete(ncaa_basketball)
    db.session.commit()
    return "ncaa_basketball was successfully deleted"


@app.route("/nhl/<id>", methods=["DELETE"])
def nhl_delete(id):
    nhl = Nhl.query.get(id)
    db.session.delete(nhl)
    db.session.commit()
    return "nhl was successfully deleted"


@app.route("/boxeo/<id>", methods=["DELETE"])
def boxeo_delete(id):
    boxeo = Boxeo.query.get(id)
    db.session.delete(boxeo)
    db.session.commit()
    return "boxeo was successfully deleted"


@app.route("/mma/<id>", methods=["DELETE"])
def mma_delete(id):
    mma = Mma.query.get(id)
    db.session.delete(mma)
    db.session.commit()
    return "mma was successfully deleted"


@app.route("/nascar/<id>", methods=["DELETE"])
def nascar_delete(id):
    nascar = Nascar.query.get(id)
    db.session.delete(nascar)
    db.session.commit()
    return "nascar was successfully deleted"


@app.route("/match_ups_nascar/<id>", methods=["DELETE"])
def match_ups_nascar_delete(id):
    match_ups_nascar = Match_Ups_Nacar.query.get(id)
    db.session.delete(match_ups_nascar)
    db.session.commit()
    return "match_ups_nascar was successfully deleted"


@app.route("/golf/<id>", methods=["DELETE"])
def golf_delete(id):
    golf = Golf.query.get(id)
    db.session.delete(golf)
    db.session.commit()
    return "golf was successfully deleted"


@app.route("/champions_league/<id>", methods=["DELETE"])
def champions_league_delete(id):
    champions_league = Champions_League.query.get(id)
    db.session.delete(champions_league)
    db.session.commit()
    return "champions_league was successfully deleted"


@app.route("/confederations_cup/<id>", methods=["DELETE"])
def confederations_cup_delete(id):
    confederations_cup = Confederations_Cup.query.get(id)
    db.session.delete(confederations_cup)
    db.session.commit()
    return "confederations_cup was successfully deleted"


@app.route("/w_c_qualifying/<id>", methods=["DELETE"])
def w_c_qualifying_delete(id):
    w_c_qualifying = W_C_Qualifying.query.get(id)
    db.session.delete(w_c_qualifying)
    db.session.commit()
    return "w_c_qualifying was successfully deleted"


@app.route("/CONCACAF/<id>", methods=["DELETE"])
def CONCACAF_delete(id):
    CONCACAF = CONCACAF.query.get(id)
    db.session.delete(CONCACAF)
    db.session.commit()
    return "CONCACAF was successfully deleted"


@app.route("/england_premier_league/<id>", methods=["DELETE"])
def england_premier_league_delete(id):
    england_premier_league = England_Premier_League.query.get(id)
    db.session.delete(england_premier_league)
    db.session.commit()
    return "england_premier_league was successfully deleted"


@app.route("/europa_league/<id>", methods=["DELETE"])
def europa_league_delete(id):
    europa_league = Europa_League.query.get(id)
    db.session.delete(europa_league)
    db.session.commit()
    return "europa_league was successfully deleted"


@app.route("/international_friendlies/<id>", methods=["DELETE"])
def international_friendlies_delete(id):
    international_friendlies = International_Friendlies.query.get(id)
    db.session.delete(international_friendlies)
    db.session.commit()
    return "international_friendlies was successfully deleted"


@app.route("/france_league/<id>", methods=["DELETE"])
def france_league_delete(id):
    france_league = France_League.query.get(id)
    db.session.delete(france_league)
    db.session.commit()
    return "france_league was successfully deleted"


@app.route("/bundesliga/<id>", methods=["DELETE"])
def bundesliga_delete(id):
    bundesliga = Bundesliga.query.get(id)
    db.session.delete(bundesliga)
    db.session.commit()
    return "bundesliga was successfully deleted"


@app.route("/international_matches/<id>", methods=["DELETE"])
def international_matches_delete(id):
    international_matches = International_Matches.query.get(id)
    db.session.delete(international_matches)
    db.session.commit()
    return "international_matches was successfully deleted"


@app.route("/italia_serie_A/<id>", methods=["DELETE"])
def italia_serie_A_delete(id):
    italia_serie_A = Italia_Serie_A.query.get(id)
    db.session.delete(italia_serie_A)
    db.session.commit()
    return "italia_serie_A was successfully deleted"


@app.route("/mx_expansion/<id>", methods=["DELETE"])
def mx_expansion_delete(id):
    mx_expansion = Mx_Expansion.query.get(id)
    db.session.delete(mx_expansion)
    db.session.commit()
    return "mx_expansion was successfully deleted"


@app.route("/mx_apertura/<id>", methods=["DELETE"])
def mx_apertura_delete(id):
    mx_apertura = Mx_Apertura.query.get(id)
    db.session.delete(mx_apertura)
    db.session.commit()
    return "mx_apertura was successfully deleted"


@app.route("/spain_primera_liga/<id>", methods=["DELETE"])
def spain_primera_liga_delete(id):
    spain_primera_liga = Spain_Primera_Liga.query.get(id)
    db.session.delete(spain_primera_liga)
    db.session.commit()
    return "spain_primera_liga was successfully deleted"


@app.route("/USA_MLS/<id>", methods=["DELETE"])
def USA_MLS_delete(id):
    USA_MLS = USA_MLS.query.get(id)
    db.session.delete(USA_MLS)
    db.session.commit()
    return "USA_MLS was successfully deleted"


@app.route("/brazil_serie_A/<id>", methods=["DELETE"])
def brazil_serie_A_delete(id):
    brazil_serie_A = Brazil_Serie_A.query.get(id)
    db.session.delete(brazil_serie_A)
    db.session.commit()
    return "brazil_serie_A was successfully deleted"


@app.route("/colombia_primera_A/<id>", methods=["DELETE"])
def colombia_primera_A_delete(id):
    colombia_primera_A = Colombia_Primera_A.query.get(id)
    db.session.delete(colombia_primera_A)
    db.session.commit()
    return "colombia_primera_A was successfully deleted"


@app.route("/costa_rica_PD/<id>", methods=["DELETE"])
def costa_rica_PD_delete(id):
    costa_rica_PD = Costa_Rica_PD.query.get(id)
    db.session.delete(costa_rica_PD)
    db.session.commit()
    return "costa_rica_PD was successfully deleted"


@app.route("/stats_nba_player/<id>", methods=["DELETE"])
def stats_nba_player_delete(id):
    stats_nba_player = Stats_nba_player.query.get(id)
    db.session.delete(stats_nba_player)
    db.session.commit()
    return "stats_nba_player was successfully deleted"


@app.route("/stats_nba_team/<id>", methods=["DELETE"])
def stats_nba_team_delete(id):
    stats_nba_team = Stats_nba_team.query.get(id)
    db.session.delete(stats_nba_team)
    db.session.commit()
    return "stats_nba_team was successfully deleted"


@app.route("/stats_mlb_team/<id>", methods=["DELETE"])
def stats_mlb_team_delete(id):
    stats_mlb_team = Stats_mlb_team.query.get(id)
    db.session.delete(stats_mlb_team)
    db.session.commit()
    return "stats_mlb_team was successfully deleted"


@app.route("/stats_mlb_player/<id>", methods=["DELETE"])
def stats_mlb_player_delete(id):
    stats_mlb_player = Stats_mlb_player.query.get(id)
    db.session.delete(stats_mlb_player)
    db.session.commit()
    return "stats_mlb_player was successfully deleted"


@app.route("/stats_nhl_team/<id>", methods=["DELETE"])
def stats_nhl_team_delete(id):
    stats_nhl_team = Stats_nhl_team.query.get(id)
    db.session.delete(stats_nhl_team)
    db.session.commit()
    return "stats_nhl_team was successfully deleted"


@app.route("/stats_nhl_player/<id>", methods=["DELETE"])
def stats_nhl_player_delete(id):
    stats_nhl_player = Stats_nhl_player.query.get(id)
    db.session.delete(stats_nhl_player)
    db.session.commit()
    return "stats_nhl_player was successfully deleted"


@app.route("/stats_box_fighter/<id>", methods=["DELETE"])
def stats_box_fighter_delete(id):
    stats_box_fighter = Stats_box_fighter.query.get(id)
    db.session.delete(stats_box_fighter)
    db.session.commit()
    return "stats_box_fighter was successfully deleted"


@app.route("/stats_mma_fighter/<id>", methods=["DELETE"])
def stats_mma_fighter_delete(id):
    stats_mma_fighter = Stats_mma_fighter.query.get(id)
    db.session.delete(stats_mma_fighter)
    db.session.commit()
    return "stats_mma_fighter was successfully deleted"


@app.route("/nascar_drivers/<id>", methods=["DELETE"])
def nascar_drivers_delete(id):
    nascar_drivers = Nascar_drivers.query.get(id)
    db.session.delete(nascar_drivers)
    db.session.commit()
    return "nascar_drivers was successfully deleted"


@app.route("/golfer/<id>", methods=["DELETE"])
def golfer_delete(id):
    golfer = Golfer.query.get(id)
    db.session.delete(golfer)
    db.session.commit()
    return "golfer was successfully deleted"


@app.route("/stats_nfl_team/<id>", methods=["DELETE"])
def stats_nfl_team_delete(id):
    stats_nfl_team = Stats_nfl_team.query.get(id)
    db.session.delete(stats_nfl_team)
    db.session.commit()
    return "stats_nfl_team was successfully deleted"


@app.route("/stats_defensive_player_nfl/<id>", methods=["DELETE"])
def stats_defensive_player_nfl_delete(id):
    stats_defensive_player_nfl = Stats_defensive_player_nfl.query.get(id)
    db.session.delete(stats_defensive_player_nfl)
    db.session.commit()
    return "stats_defensive_player_nfl was successfully deleted"


@app.route("/stats_offensive_player_nfl/<id>", methods=["DELETE"])
def stats_offensive_player_nfl_delete(id):
    stats_offensive_player_nfl = Stats_offensive_player_nfl.query.get(id)
    db.session.delete(stats_offensive_player_nfl)
    db.session.commit()
    return "stats_offensive_player_nfl was successfully deleted"


@app.route("/stats_returning_player_nfl/<id>", methods=["DELETE"])
def stats_returning_player_nfl_delete(id):
    stats_returning_player_nfl = Stats_returning_player_nfl.query.get(id)
    db.session.delete(stats_returning_player_nfl)
    db.session.commit()
    return "stats_returning_player_nfl was successfully deleted"


@app.route("/stats_kiking_player_nfl/<id>", methods=["DELETE"])
def stats_kiking_player_nfl_delete(id):
    stats_kiking_player_nfl = Stats_kiking_player_nfl.query.get(id)
    db.session.delete(stats_kiking_player_nfl)
    db.session.commit()
    return "stats_kiking_player_nfl was successfully deleted"


@app.route("/stats_punting_player_nfl/<id>", methods=["DELETE"])
def stats_punting_player_nfl_delete(id):
    stats_punting_player_nfl = Stats_punting_player_nfl.query.get(id)
    db.session.delete(stats_punting_player_nfl)
    db.session.commit()
    return "stats_punting_player_nfl was successfully deleted"
