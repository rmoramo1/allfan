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
from models import db, User, Nfl, Mlb, Nba, Nhl, Boxeo, Mma, Nascar, Nascar_drivers, Match_Ups_Nacar, Golf, Golfer, News, Ncaa_Baseball, Ncaa_Football, Ncaa_Basketball, Champions_League, Confederations_Cup, W_C_Qualifying, CONCACAF, Europa_League, International_Friendlies, France_League, Bundesliga, International_Matches, Italia_Serie_A, Mx_Expansion, Mx_Apertura, Spain_Primera_Liga, USA_MLS, Brazil_Serie_A, Colombia_Primera_A, Stats_nba_player, Stats_nba_team, Stats_mlb_team, Stats_nhl_team, Stats_nhl_player, Stats_box_fighter, Stats_mma_fighter, Stats_nfl_team, Stats_defensive_player_nfl, Stats_offensive_player_nfl, Stats_returning_player_nfl, Stats_kiking_player_nfl, Stats_punting_player_nfl

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
    if date is None:
        return jsonify({"msg": "No Date was provided"}), 400
    if hour is None:
        return jsonify({"msg": "No hour was provided"}), 400
    if status is None:
        return jsonify({"msg": "No status was provided"}), 400
    if away is None:
        return jsonify({"msg": "No away was provided"}), 400
    if pitcher_a is None:
        return jsonify({"msg": "No pitcher_a was provided"}), 400
    if home is None:
        return jsonify({"msg": "No home was provided"}), 400
    if pitcher_h is None:
        return jsonify({"msg": "No pitcher_h was provided"}), 400
    if rl_away is None:
        return jsonify({"msg": "No añosEXP was provided"}), 400
    if rl_home is None:
        return jsonify({"msg": "No rl_home was provided"}), 400
    if moneyLineAway is None:
        return jsonify({"msg": "No moneyLineAway was provided"}), 400
    if moneyLineHome is None:
        return jsonify({"msg": "No moneyLineHome was provided"}), 400
    if total is None:
        return jsonify({"msg": "No total was provided"}), 400
    if juice_total_over is None:
        return jsonify({"msg": "No juice_total_over was provided"}), 400
    if juice_total_under is None:
        return jsonify({"msg": "No juice_total_under was provided"}), 400
    if tt_away is None:
        return jsonify({"msg": "No tt_away was provided"}), 400
    if juice_over_away is None:
        return jsonify({"msg": "No juice_over_away was provided"}), 400
    if juice_under_away is None:
        return jsonify({"msg": "No juice_under_away was provided"}), 400
    if tt_home is None:
        return jsonify({"msg": "No tt_home was provided"}), 400
    if juice_over_home is None:
        return jsonify({"msg": "No juice_over_home was provided"}), 400
    if juice_under_home is None:
        return jsonify({"msg": "No juice_under_home was provided"}), 400
    if final_score_away is None:
        return jsonify({"msg": "No final_score_away was provided"}), 400
    if final_score_home is None:
        return jsonify({"msg": "No final_score_home was provided"}), 400
    if rl_away_f5 is None:
        return jsonify({"msg": "No rl_away_f5 was provided"}), 400
    if rl_home_f5 is None:
        return jsonify({"msg": "No rl_home_f5 was provided"}), 400
    if juice_rl_away_f5 is None:
        return jsonify({"msg": "No juice_rl_away_f5 was provided"}), 400
    if juice_rl_home_f5 is None:
        return jsonify({"msg": "No juice_rl_home_f5 was provided"}), 400
    if moneyLineAway_f5 is None:
        return jsonify({"msg": "No moneyLineAway_f5 was provided"}), 400
    if moneyLineHome_f5 is None:
        return jsonify({"msg": "No moneyLineHome_f5 was provided"}), 400
    if total_f5 is None:
        return jsonify({"msg": "No total_f5 was provided"}), 400
    if juice_total_over_f5 is None:
        return jsonify({"msg": "No juice_total_over_f5 was provided"}), 400
    if juice_total_under_f5 is None:
        return jsonify({"msg": "No juice_total_under_f5 was provided"}), 400
    if tt_away_f5 is None:
        return jsonify({"msg": "No tt_away_f5 was provided"}), 400
    if juice_over_away_f5 is None:
        return jsonify({"msg": "No juice_over_away_f5 was provided"}), 400
    if juice_under_away_f5 is None:
        return jsonify({"msg": "No juice_under_away_f5 was provided"}), 400
    if juice_over_home_f5 is None:
        return jsonify({"msg": "No juice_over_home_f5 was provided"}), 400
    if juice_under_home_f5 is None:
        return jsonify({"msg": "No juice_under_home_f5 was provided"}), 400
    if fs_away_f5 is None:
        return jsonify({"msg": "No fs_away_f5 was provided"}), 400
    if fs_home_f5 is None:
        return jsonify({"msg": "No fs_home_f5 was provided"}), 400
    if sa_1inning is None:
        return jsonify({"msg": "No sh_1inning was provided"}), 400
    if sh_1inning is None:
        return jsonify({"msg": "No sh_1inning was provided"}), 400
    if sa_2inning is None:
        return jsonify({"msg": "No sa_2inning was provided"}), 400
    if sh_2inning is None:
        return jsonify({"msg": "No sh_2inning was provided"}), 400
    if sa_3inning is None:
        return jsonify({"msg": "No sa_3inning was provided"}), 400
    if sh_3inning is None:
        return jsonify({"msg": "No sh_3inning was provided"}), 400
    if sa_4inning is None:
        return jsonify({"msg": "No sa_4inning was provided"}), 400
    if sh_4inning is None:
        return jsonify({"msg": "No sh_4inning was provided"}), 400
    if sa_5inning is None:
        return jsonify({"msg": "No sa_5inning was provided"}), 400
    if sh_5inning is None:
        return jsonify({"msg": "No sh_5inning was provided"}), 400
    if sa_6inning is None:
        return jsonify({"msg": "No sa_6inning was provided"}), 400
    if sh_6inning is None:
        return jsonify({"msg": "No sh_6inning was provided"}), 400
    if sa_7inning is None:
        return jsonify({"msg": "No sa_7inning was provided"}), 400
    if sh_7inning is None:
        return jsonify({"msg": "No sh_7inning was provided"}), 400
    if sa_8inning is None:
        return jsonify({"msg": "No sa_8inning was provided"}), 400
    if sh_8inning is None:
        return jsonify({"msg": "No sh_8inning was provided"}), 400
    if sa_9inning is None:
        return jsonify({"msg": "No sa_9inning was provided"}), 400
    if sh_9inning is None:
        return jsonify({"msg": "No sh_9inning was provided"}), 400
    if sa_10inning is None:
        return jsonify({"msg": "No sa_10inning was provided"}), 400
    if sh_10inning is None:
        return jsonify({"msg": "No sh_10inning was provided"}), 400
    if sa_11inning is None:
        return jsonify({"msg": "No sa_11inning was provided"}), 400
    if sh_11inning is None:
        return jsonify({"msg": "No sh_11inning was provided"}), 400
    if sa_12inning is None:
        return jsonify({"msg": "No sa_12inning was provided"}), 400
    if sh_12inning is None:
        return jsonify({"msg": "No sh_12inning was provided"}), 400
    if sa_13inning is None:
        return jsonify({"msg": "No sa_13inning was provided"}), 400
    if sh_13inning is None:
        return jsonify({"msg": "No sh_13inning was provided"}), 400
    if sa_14inning is None:
        return jsonify({"msg": "No sa_14inning was provided"}), 400
    if sh_14inning is None:
        return jsonify({"msg": "No sh_14inning was provided"}), 400
    if sa_15inning is None:
        return jsonify({"msg": "No sa_15inning was provided"}), 400
    if sh_15inning is None:
        return jsonify({"msg": "No sh_15inning was provided"}), 400
    if sa_16inning is None:
        return jsonify({"msg": "No sa_16inning was provided"}), 400
    if sh_16inning is None:
        return jsonify({"msg": "No sh_16inning was provided"}), 400
    if sa_17inning is None:
        return jsonify({"msg": "No sa_17inning was provided"}), 400
    if sh_17inning is None:
        return jsonify({"msg": "No sh_17inning was provided"}), 400
    if sa_18inning is None:
        return jsonify({"msg": "No sa_1inning was provided"}), 400
    if sh_18inning is None:
        return jsonify({"msg": "No sa_18inning was provided"}), 400
    if sa_19inning is None:
        return jsonify({"msg": "No sa_19inning was provided"}), 400
    if sh_19inning is None:
        return jsonify({"msg": "No sh_19inning was provided"}), 400
    if sa_20inning is None:
        return jsonify({"msg": "No sa_20inning was provided"}), 400
    if sh_20inning is None:
        return jsonify({"msg": "No sh_20inning was provided"}), 400
    if sa_21inning is None:
        return jsonify({"msg": "No sa_21inning was provided"}), 400
    if sh_21inning is None:
        return jsonify({"msg": "No sh_21inning was provided"}), 400
    if sa_22inning is None:
        return jsonify({"msg": "No sa_22inning was provided"}), 400
    if sh_22inning is None:
        return jsonify({"msg": "No sh_22inning was provided"}), 400
    if sa_23inning is None:
        return jsonify({"msg": "No sa_23inning was provided"}), 400
    if sh_23inning is None:
        return jsonify({"msg": "No sh_23inning was provided"}), 400
    if sa_24inning is None:
        return jsonify({"msg": "No sa_24inning was provided"}), 400
    if sh_24inning is None:
        return jsonify({"msg": "No sh_24inning was provided"}), 400
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
            rl_away=rl_away, rl_home=rl_home, juice_rl_away=juice_rl_away, juice_rl_home=juice_rl_home, moneyLineAway=moneyLineAway, moneyLineHome=moneyLineHome, total=total, juice_total_over=juice_total_over, juice_total_under=juice_total_under, tt_away=tt_away, juice_over_away=juice_over_away, juice_under_away=juice_under_away, tt_home=tt_home, juice_over_home=juice_over_home, juice_under_home=juice_under_home, final_score_away=final_score_away, final_score_home=final_score_home, rl_away_f5=rl_away_f5, rl_home_f5=rl_home_f5, juice_rl_away_f5=juice_rl_away_f5, juice_rl_home_f5=juice_rl_home_f5, moneyLineAway_f5=moneyLineAway_f5, moneyLineHome_f5=moneyLineHome_f5, total_f5=total_f5, juice_total_over_f5=juice_total_over_f5, juice_total_under_f5=juice_total_under_f5, tt_away_f5=tt_away_f5, juice_over_away_f5=juice_over_away_f5, juice_under_away_f5=juice_under_away_f5, juice_over_home_f5=juice_over_home_f5, juice_under_home_f5=juice_under_home_f5, fs_away_f5=fs_away_f5, fs_home_f5=fs_home_f5, sa_1inning=sa_1inning, sh_1inning=sh_1inning, sa_2inning=sa_2inning, sh_2inning=sh_2inning, sa_3inning=sa_3inning, sh_3inning=sh_3inning, sa_4inning=sa_4inning, sh_4inning=sh_4inning, sa_5inning=sa_5inning, sh_5inning=sh_5inning, sa_6inning=sa_6inning, sh_6inning=sh_6inning, sa_7inning=sa_7inning, sh_7inning=sh_7inning, sa_8inning=sa_8inning, sh_8inning=sh_8inning, sa_9inning=sa_9inning, sh_9inning=sh_9inning, sa_10inning=sa_10inning, sh_10inning=sh_10inning, sa_11inning=sa_11inning, sh_11inning=sh_11inning, sa_12inning=sa_12inning, sh_12inning=sh_12inning, sa_13inning=sa_13inning, sh_13inning=sh_13inning, sa_14inning=sa_14inning, sh_14inning=sh_14inning, sa_15inning=sa_15inning, sh_15inning=sh_15inning, sa_16inning=sa_16inning, sh_16inning=sh_16inning, sa_17inning=sa_17inning, sa_18inning=sa_18inning, sa_19inning=sa_19inning, sa_20inning=sa_20inning, sa_21inning=sa_21inning, sa_22inning=sa_22inning, sa_23inning=sa_23inning, sa_24inning=sa_24inning, sa_25inning=sa_25inning)
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

    # valida si estan vacios los ingresos
    if date is None:
        return jsonify({"msg": "No Date was provided"}), 400
    if hour is None:
        return jsonify({"msg": "No hour was provided"}), 400
    if status is None:
        return jsonify({"msg": "No status was provided"}), 400
    if away is None:
        return jsonify({"msg": "No away was provided"}), 400
    if home is None:
        return jsonify({"msg": "No home was provided"}), 400
    if spread_away is None:
        return jsonify({"msg": "No spread_away was provided"}), 400
    if spread_home is None:
        return jsonify({"msg": "No spread_home was provided"}), 400
    if juice_spread_away is None:
        return jsonify({"msg": "No juice_spread_away was provided"}), 400
    if juice_spread_home is None:
        return jsonify({"msg": "No juice_spread_home was provided"}), 400
    if moneyLineAway is None:
        return jsonify({"msg": "No moneyLineAway was provided"}), 400
    if moneyLineHome is None:
        return jsonify({"msg": "No moneyLineHome was provided"}), 400
    if total is None:
        return jsonify({"msg": "No total was provided"}), 400
    if juice_total_over is None:
        return jsonify({"msg": "No juice_total_over was provided"}), 400
    if juice_total_under is None:
        return jsonify({"msg": "No juice_total_under was provided"}), 400
    if tt_away is None:
        return jsonify({"msg": "No tt_away was provided"}), 400
    if juice_over_away is None:
        return jsonify({"msg": "No juice_over_away was provided"}), 400
    if juice_under_away is None:
        return jsonify({"msg": "No juice_under_away was provided"}), 400
    if tt_home is None:
        return jsonify({"msg": "No tt_home was provided"}), 400
    if juice_over_home is None:
        return jsonify({"msg": "No juice_over_home was provided"}), 400
    if juice_under_home is None:
        return jsonify({"msg": "No juice_under_home was provided"}), 400
    if final_score_away is None:
        return jsonify({"msg": "No final_score_away was provided"}), 400
    if final_score_home is None:
        return jsonify({"msg": "No final_score_home was provided"}), 400
    if first_half_spread_away is None:
        return jsonify({"msg": "No first_half_spread_away was provided"}), 400
    if first_half_spread_home is None:
        return jsonify({"msg": "No first_half_spread_home was provided"}), 400
    if first_half_juice_spread_away is None:
        return jsonify({"msg": "No first_half_juice_spread_away was provided"}), 400
    if first_half_juice_spread_home is None:
        return jsonify({"msg": "No first_half_juice_spread_home was provided"}), 400
    if first_half_moneyLineAway is None:
        return jsonify({"msg": "No first_half_moneyLineAway was provided"}), 400
    if first_half_moneyLineHome is None:
        return jsonify({"msg": "No first_half_moneyLineHome was provided"}), 400
    if first_half_total is None:
        return jsonify({"msg": "No first_half_total was provided"}), 400
    if fh_juice_over is None:
        return jsonify({"msg": "No fh_juice_over was provided"}), 400
    if fh_juice_under is None:
        return jsonify({"msg": "No fh_juice_under was provided"}), 400
    if first_half_tt_away is None:
        return jsonify({"msg": "No first_half_tt_away was provided"}), 400
    if first_half_juice_over_away is None:
        return jsonify({"msg": "No first_half_juice_over_away was provided"}), 400
    if first_half_juice_under_away is None:
        return jsonify({"msg": "No first_half_juice_under_away was provided"}), 400
    if first_half_tt_home is None:
        return jsonify({"msg": "No first_half_tt_home was provided"}), 400
    if first_half_juice_over_home is None:
        return jsonify({"msg": "No first_half_juice_over_home was provided"}), 400
    if first_half_juice_under_home is None:
        return jsonify({"msg": "No first_half_juice_under_home was provided"}), 400
    if first_half_final_score_away is None:
        return jsonify({"msg": "No first_half_final_score_away was provided"}), 400
    if first_half_final_score_home is None:
        return jsonify({"msg": "No first_half_final_score_home was provided"}), 400
    if second_half_spread_away is None:
        return jsonify({"msg": "No second_half_spread_away was provided"}), 400
    if second_half_spread_home is None:
        return jsonify({"msg": "No second_half_spread_home was provided"}), 400
    if second_half_juice_spread_away is None:
        return jsonify({"msg": "No second_half_juice_spread_away was provided"}), 400
    if second_half_juice_spread_home is None:
        return jsonify({"msg": "No second_half_juice_spread_home was provided"}), 400
    if second_half_moneyLineAway is None:
        return jsonify({"msg": "No second_half_moneyLineAway was provided"}), 400
    if second_half_moneyLineHome is None:
        return jsonify({"msg": "No second_half_moneyLineHome was provided"}), 400
    if second_half_total is None:
        return jsonify({"msg": "No second_half_total was provided"}), 400
    if sh_juice_over is None:
        return jsonify({"msg": "No sh_juice_over was provided"}), 400
    if sh_juice_under is None:
        return jsonify({"msg": "No sh_juice_under was provided"}), 400
    if second_half_tt_away is None:
        return jsonify({"msg": "No second_half_tt_away was provided"}), 400
    if second_half_juice_over_away is None:
        return jsonify({"msg": "No second_half_juice_over_away was provided"}), 400
    if second_half_juice_under_away is None:
        return jsonify({"msg": "No second_half_juice_under_away was provided"}), 400
    if second_half_tt_home is None:
        return jsonify({"msg": "No second_half_tt_home was provided"}), 400
    if second_half_juice_over_home is None:
        return jsonify({"msg": "No second_half_juice_over_home was provided"}), 400
    if second_half_juice_under_home is None:
        return jsonify({"msg": "No second_half_juice_under_home was provided"}), 400
    if second_half_final_score_away is None:
        return jsonify({"msg": "No second_half_final_score_away was provided"}), 400
    if second_half_final_score_home is None:
        return jsonify({"msg": "No second_half_final_score_home was provided"}), 400
    if q1_half_spread_away is None:
        return jsonify({"msg": "No q1_half_spread_away was provided"}), 400
    if q1_half_spread_home is None:
        return jsonify({"msg": "No q1_half_spread_home was provided"}), 400
    if q1_half_juice_spread_away is None:
        return jsonify({"msg": "No q1_half_juice_spread_away was provided"}), 400
    if q1_half_juice_spread_home is None:
        return jsonify({"msg": "No q1_half_juice_spread_home was provided"}), 400
    if q1_half_moneyLineAway is None:
        return jsonify({"msg": "No q1_half_moneyLineAway was provided"}), 400
    if q1_half_moneyLineHome is None:
        return jsonify({"msg": "No q1_half_moneyLineHome was provided"}), 400
    if q1_half_total is None:
        return jsonify({"msg": "No q1_half_total was provided"}), 400
    if q1_juice_over is None:
        return jsonify({"msg": "No q1_juice_over was provided"}), 400
    if q1_juice_under is None:
        return jsonify({"msg": "No q1_juice_under was provided"}), 400
    if q1_half_tt_away is None:
        return jsonify({"msg": "No q1_half_tt_away was provided"}), 400
    if q1_half_juice_over_away is None:
        return jsonify({"msg": "No q1_half_juice_over_away was provided"}), 400
    if q1_half_juice_under_away is None:
        return jsonify({"msg": "No q1_half_juice_under_away was provided"}), 400
    if q1_half_tt_home is None:
        return jsonify({"msg": "No q1_half_tt_home was provided"}), 400
    if q1_half_juice_over_home is None:
        return jsonify({"msg": "No q1_half_juice_over_home was provided"}), 400
    if q1_half_juice_under_home is None:
        return jsonify({"msg": "No q1_half_juice_under_home was provided"}), 400
    if q1_half_final_score_away is None:
        return jsonify({"msg": "No q1_half_final_score_away was provided"}), 400
    if q1_half_final_score_home is None:
        return jsonify({"msg": "No q1_half_final_score_home was provided"}), 400

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

    # valida si estan vacios los ingresos
    if date is None:
        return jsonify({"msg": "No Date was provided"}), 400
    if hour is None:
        return jsonify({"msg": "No hour was provided"}), 400
    if status is None:
        return jsonify({"msg": "No status was provided"}), 400
    if away is None:
        return jsonify({"msg": "No away was provided"}), 400
    if home is None:
        return jsonify({"msg": "No home was provided"}), 400
    if puck_line_away is None:
        return jsonify({"msg": "No puck_line_away was provided"}), 400
    if puck_line_home is None:
        return jsonify({"msg": "No puck_line_home was provided"}), 400
    if juice_puck_away is None:
        return jsonify({"msg": "No juice_puck_away was provided"}), 400
    if juice_puck_home is None:
        return jsonify({"msg": "No juice_puck_home was provided"}), 400
    if moneyLineAway is None:
        return jsonify({"msg": "No moneyLineAway was provided"}), 400
    if moneyLineHome is None:
        return jsonify({"msg": "No moneyLineHome was provided"}), 400
    if total is None:
        return jsonify({"msg": "No total was provided"}), 400
    if juice_total_over is None:
        return jsonify({"msg": "No juice_total_over was provided"}), 400
    if juice_total_under is None:
        return jsonify({"msg": "No juice_total_under was provided"}), 400
    if tt_away is None:
        return jsonify({"msg": "No tt_away was provided"}), 400
    if juice_over_away is None:
        return jsonify({"msg": "No juice_over_away was provided"}), 400
    if juice_under_away is None:
        return jsonify({"msg": "No juice_under_away was provided"}), 400
    if tt_home is None:
        return jsonify({"msg": "No tt_home was provided"}), 400
    if juice_over_home is None:
        return jsonify({"msg": "No juice_over_home was provided"}), 400
    if juice_under_home is None:
        return jsonify({"msg": "No juice_under_home was provided"}), 400
    if final_score_away is None:
        return jsonify({"msg": "No final_score_away was provided"}), 400
    if final_score_home is None:
        return jsonify({"msg": "No final_score_home was provided"}), 400
    if puck_away_1Q is None:
        return jsonify({"msg": "No puck_away_1Q was provided"}), 400
    if puck_home_1Q is None:
        return jsonify({"msg": "No puck_home_1Q was provided"}), 400
    if juice_puck_away_1Q is None:
        return jsonify({"msg": "No juice_puck_away_1Q was provided"}), 400
    if juice_puck_home_1Q is None:
        return jsonify({"msg": "No juice_puck_home_1Q was provided"}), 400
    if moneyLineAway_1Q is None:
        return jsonify({"msg": "No moneyLineAway_1Q was provided"}), 400
    if moneyLineHome_1Q is None:
        return jsonify({"msg": "No moneyLineHome_1Q was provided"}), 400
    if total_1Q is None:
        return jsonify({"msg": "No total_1Q was provided"}), 400
    if Q1_juice_over is None:
        return jsonify({"msg": "No Q1_juice_over was provided"}), 400
    if Q1_juice_under is None:
        return jsonify({"msg": "No Q1_juice_under was provided"}), 400
    if tt_away_1Q is None:
        return jsonify({"msg": "No tt_away_1Q was provided"}), 400
    if juice_over_away_1Q is None:
        return jsonify({"msg": "No juice_over_away_1Q was provided"}), 400
    if juice_under_away_1Q is None:
        return jsonify({"msg": "No juice_under_away_1Q was provided"}), 400
    if tt_home_1Q is None:
        return jsonify({"msg": "No tt_home_1Q was provided"}), 400
    if juice_over_home_1Q is None:
        return jsonify({"msg": "No juice_over_home_1Q was provided"}), 400
    if juice_under_home_1Q is None:
        return jsonify({"msg": "No juice_under_home_1Q was provided"}), 400
    if sa_1Q is None:
        return jsonify({"msg": "No sa_1Q was provided"}), 400
    if sh_1Q is None:
        return jsonify({"msg": "No sh_1Q was provided"}), 400
    if sa_2Q is None:
        return jsonify({"msg": "No sa_2Q was provided"}), 400
    if sh_2Q is None:
        return jsonify({"msg": "No sh_2Q was provided"}), 400
    if sa_3Q is None:
        return jsonify({"msg": "No sa_3Q was provided"}), 400
    if sh_3Q is None:
        return jsonify({"msg": "No sh_3Q was provided"}), 400

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

    # valida si estan vacios los ingresos
    if date is None:
        return jsonify({"msg": "No Date was provided"}), 400
    if hour is None:
        return jsonify({"msg": "No hour was provided"}), 400
    if week is None:
        return jsonify({"msg": "No week was provided"}), 400
    if status is None:
        return jsonify({"msg": "No status was provided"}), 400
    if away is None:
        return jsonify({"msg": "No away was provided"}), 400
    if home is None:
        return jsonify({"msg": "No home was provided"}), 400
    if spread_away is None:
        return jsonify({"msg": "No spread_away was provided"}), 400
    if spread_home is None:
        return jsonify({"msg": "No spread_home was provided"}), 400
    if juice_spread_away is None:
        return jsonify({"msg": "No juice_spread_away was provided"}), 400
    if juice_spread_home is None:
        return jsonify({"msg": "No juice_spread_home was provided"}), 400
    if moneyLineAway is None:
        return jsonify({"msg": "No moneyLineAway was provided"}), 400
    if moneyLineHome is None:
        return jsonify({"msg": "No moneyLineHome was provided"}), 400
    if total is None:
        return jsonify({"msg": "No total was provided"}), 400
    if juice_total_over is None:
        return jsonify({"msg": "No juice_total_over was provided"}), 400
    if juice_total_under is None:
        return jsonify({"msg": "No juice_total_under was provided"}), 400
    if tt_away is None:
        return jsonify({"msg": "No tt_away was provided"}), 400
    if juice_over_away is None:
        return jsonify({"msg": "No juice_over_away was provided"}), 400
    if juice_under_away is None:
        return jsonify({"msg": "No juice_under_away was provided"}), 400
    if tt_home is None:
        return jsonify({"msg": "No tt_home was provided"}), 400
    if juice_over_home is None:
        return jsonify({"msg": "No juice_over_home was provided"}), 400
    if juice_under_home is None:
        return jsonify({"msg": "No juice_under_home was provided"}), 400
    if final_score_away is None:
        return jsonify({"msg": "No final_score_away was provided"}), 400
    if final_score_home is None:
        return jsonify({"msg": "No final_score_home was provided"}), 400
    if first_half_spread_away is None:
        return jsonify({"msg": "No first_half_spread_away was provided"}), 400
    if first_half_spread_home is None:
        return jsonify({"msg": "No first_half_spread_home was provided"}), 400
    if first_half_juice_spread_away is None:
        return jsonify({"msg": "No first_half_juice_spread_away was provided"}), 400
    if first_half_juice_spread_home is None:
        return jsonify({"msg": "No first_half_juice_spread_home was provided"}), 400
    if first_half_moneyLineAway is None:
        return jsonify({"msg": "No first_half_moneyLineAway was provided"}), 400
    if first_half_moneyLineHome is None:
        return jsonify({"msg": "No first_half_moneyLineHome was provided"}), 400
    if first_half_total is None:
        return jsonify({"msg": "No first_half_total was provided"}), 400
    if fh_juice_over is None:
        return jsonify({"msg": "No fh_juice_over was provided"}), 400
    if fh_juice_under is None:
        return jsonify({"msg": "No fh_juice_under was provided"}), 400
    if first_half_tt_away is None:
        return jsonify({"msg": "No first_half_tt_away was provided"}), 400
    if first_half_juice_over_away is None:
        return jsonify({"msg": "No first_half_juice_over_away was provided"}), 400
    if first_half_juice_under_away is None:
        return jsonify({"msg": "No first_half_juice_under_away was provided"}), 400
    if first_half_tt_home is None:
        return jsonify({"msg": "No first_half_tt_home was provided"}), 400
    if first_half_juice_over_home is None:
        return jsonify({"msg": "No first_half_juice_over_home was provided"}), 400
    if first_half_juice_under_home is None:
        return jsonify({"msg": "No first_half_juice_under_home was provided"}), 400
    if first_half_final_score_away is None:
        return jsonify({"msg": "No first_half_final_score_away was provided"}), 400
    if first_half_final_score_home is None:
        return jsonify({"msg": "No first_half_final_score_home was provided"}), 400
    if second_half_spread_away is None:
        return jsonify({"msg": "No second_half_spread_away was provided"}), 400
    if second_half_spread_home is None:
        return jsonify({"msg": "No second_half_spread_home was provided"}), 400
    if second_half_juice_spread_away is None:
        return jsonify({"msg": "No second_half_juice_spread_away was provided"}), 400
    if second_half_juice_spread_home is None:
        return jsonify({"msg": "No second_half_juice_spread_home was provided"}), 400
    if second_half_moneyLineAway is None:
        return jsonify({"msg": "No second_half_moneyLineAway was provided"}), 400
    if second_half_moneyLineHome is None:
        return jsonify({"msg": "No second_half_moneyLineHome was provided"}), 400
    if second_half_total is None:
        return jsonify({"msg": "No second_half_total was provided"}), 400
    if sh_juice_over is None:
        return jsonify({"msg": "No sh_juice_over was provided"}), 400
    if sh_juice_under is None:
        return jsonify({"msg": "No sh_juice_under was provided"}), 400
    if second_half_tt_away is None:
        return jsonify({"msg": "No second_half_tt_away was provided"}), 400
    if second_half_juice_over_away is None:
        return jsonify({"msg": "No second_half_juice_over_away was provided"}), 400
    if second_half_juice_under_away is None:
        return jsonify({"msg": "No second_half_juice_under_away was provided"}), 400
    if second_half_tt_home is None:
        return jsonify({"msg": "No second_half_tt_home was provided"}), 400
    if second_half_juice_over_home is None:
        return jsonify({"msg": "No second_half_juice_over_home was provided"}), 400
    if second_half_juice_under_home is None:
        return jsonify({"msg": "No second_half_juice_under_home was provided"}), 400
    if second_half_final_score_away is None:
        return jsonify({"msg": "No second_half_final_score_away was provided"}), 400
    if second_half_final_score_home is None:
        return jsonify({"msg": "No second_half_final_score_home was provided"}), 400
    if q1_half_spread_away is None:
        return jsonify({"msg": "No q1_half_spread_away was provided"}), 400
    if q1_half_spread_home is None:
        return jsonify({"msg": "No q1_half_spread_home was provided"}), 400
    if q1_half_juice_spread_away is None:
        return jsonify({"msg": "No q1_half_juice_spread_away was provided"}), 400
    if q1_half_juice_spread_home is None:
        return jsonify({"msg": "No q1_half_juice_spread_home was provided"}), 400
    if q1_half_moneyLineAway is None:
        return jsonify({"msg": "No q1_half_moneyLineAway was provided"}), 400
    if q1_half_moneyLineHome is None:
        return jsonify({"msg": "No q1_half_moneyLineHome was provided"}), 400
    if q1_half_total is None:
        return jsonify({"msg": "No q1_half_total was provided"}), 400
    if q1_juice_over is None:
        return jsonify({"msg": "No q1_juice_over was provided"}), 400
    if q1_juice_under is None:
        return jsonify({"msg": "No q1_juice_under was provided"}), 400
    if q1_half_tt_away is None:
        return jsonify({"msg": "No q1_half_tt_away was provided"}), 400
    if q1_half_juice_over_away is None:
        return jsonify({"msg": "No q1_half_juice_over_away was provided"}), 400
    if q1_half_juice_under_away is None:
        return jsonify({"msg": "No q1_half_juice_under_away was provided"}), 400
    if q1_half_tt_home is None:
        return jsonify({"msg": "No q1_half_tt_home was provided"}), 400
    if q1_half_juice_over_home is None:
        return jsonify({"msg": "No q1_half_juice_over_home was provided"}), 400
    if q1_half_juice_under_home is None:
        return jsonify({"msg": "No q1_half_juice_under_home was provided"}), 400
    if q1_half_final_score_away is None:
        return jsonify({"msg": "No q1_half_final_score_away was provided"}), 400
    if q1_half_final_score_home is None:
        return jsonify({"msg": "No q1_half_final_score_home was provided"}), 400

    # busca mlb en BBDD
    nfl = Nfl.query.filter_by(home=home, away=away, date=date).first()
    # the mlb was not found on the database
    if nfl:
        return jsonify({"msg": "Mlb already exists", "status": nfl.status}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        nfl = Nfl(
            date=date,
            hour=hour,
            status=status,
            away=away,
            home=home,
            week=week,
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

    # valida si estan vacios los ingresos
    if date is None:
        return jsonify({"msg": "No Date was provided"}), 400
    if hour is None:
        return jsonify({"msg": "No hour was provided"}), 400
    if week is None:
        return jsonify({"msg": "No week was provided"}), 400
    if status is None:
        return jsonify({"msg": "No status was provided"}), 400
    if event is None:
        return jsonify({"msg": "No event was provided"}), 400
    if rounds is None:
        return jsonify({"msg": "No rounds was provided"}), 400
    if location_Fight is None:
        return jsonify({"msg": "No location_Fight was provided"}), 400
    if fighter_One is None:
        return jsonify({"msg": "No fighter_One was provided"}), 400
    if money_Line_One is None:
        return jsonify({"msg": "No money_Line_One was provided"}), 400
    if fighter_Two is None:
        return jsonify({"msg": "No fighter_Two was provided"}), 400
    if money_Line_Two is None:
        return jsonify({"msg": "No money_Line_Two was provided"}), 400
    if winner is None:
        return jsonify({"msg": "No winner was provided"}), 400
    if finish_by is None:
        return jsonify({"msg": "No finish_by was provided"}), 400
    if r1_result is None:
        return jsonify({"msg": "No r1_result was provided"}), 400
    if tt_away is None:
        return jsonify({"msg": "No tt_away was provided"}), 400
    if r2_result is None:
        return jsonify({"msg": "No r2_result was provided"}), 400
    if r3_result is None:
        return jsonify({"msg": "No r3_result was provided"}), 400
    if r4_result is None:
        return jsonify({"msg": "No r4_result was provided"}), 400
    if r5_result is None:
        return jsonify({"msg": "No r5_result was provided"}), 400
    if r6_result is None:
        return jsonify({"msg": "No r6_result was provided"}), 400
    if r7_result is None:
        return jsonify({"msg": "No r7_result was provided"}), 400
    if r8_result is None:
        return jsonify({"msg": "No r8_result was provided"}), 400
    if r9_result is None:
        return jsonify({"msg": "No r9_result was provided"}), 400
    if r10_result is None:
        return jsonify({"msg": "No r10_result was provided"}), 400
    if r11_result is None:
        return jsonify({"msg": "No r11_result was provided"}), 400
    if r12_result is None:
        return jsonify({"msg": "No r12_result was provided"}), 400
    if r13_result is None:
        return jsonify({"msg": "No r13_result was provided"}), 400
    if r14_result is None:
        return jsonify({"msg": "No r14_result was provided"}), 400
    if r15_result is None:
        return jsonify({"msg": "No r15_result was provided"}), 400

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

    # valida si estan vacios los ingresos
    if date is None:
        return jsonify({"msg": "No Date was provided"}), 400
    if hour is None:
        return jsonify({"msg": "No hour was provided"}), 400
    if week is None:
        return jsonify({"msg": "No week was provided"}), 400
    if status is None:
        return jsonify({"msg": "No status was provided"}), 400
    if event is None:
        return jsonify({"msg": "No event was provided"}), 400
    if rounds is None:
        return jsonify({"msg": "No rounds was provided"}), 400
    if location_Fight is None:
        return jsonify({"msg": "No location_Fight was provided"}), 400
    if fighter_One is None:
        return jsonify({"msg": "No fighter_One was provided"}), 400
    if money_Line_One is None:
        return jsonify({"msg": "No money_Line_One was provided"}), 400
    if fighter_Two is None:
        return jsonify({"msg": "No fighter_Two was provided"}), 400
    if money_Line_Two is None:
        return jsonify({"msg": "No money_Line_Two was provided"}), 400
    if winner is None:
        return jsonify({"msg": "No winner was provided"}), 400
    if finish_by is None:
        return jsonify({"msg": "No finish_by was provided"}), 400
    if r1_result is None:
        return jsonify({"msg": "No r1_result was provided"}), 400
    if tt_away is None:
        return jsonify({"msg": "No tt_away was provided"}), 400
    if r2_result is None:
        return jsonify({"msg": "No r2_result was provided"}), 400
    if r3_result is None:
        return jsonify({"msg": "No r3_result was provided"}), 400
    if r4_result is None:
        return jsonify({"msg": "No r4_result was provided"}), 400
    if r5_result is None:
        return jsonify({"msg": "No r5_result was provided"}), 400
    if r6_result is None:
        return jsonify({"msg": "No r6_result was provided"}), 400
    if r7_result is None:
        return jsonify({"msg": "No r7_result was provided"}), 400
    if r8_result is None:
        return jsonify({"msg": "No r8_result was provided"}), 400
    if r9_result is None:
        return jsonify({"msg": "No r9_result was provided"}), 400
    if r10_result is None:
        return jsonify({"msg": "No r10_result was provided"}), 400
    if r11_result is None:
        return jsonify({"msg": "No r11_result was provided"}), 400
    if r12_result is None:
        return jsonify({"msg": "No r12_result was provided"}), 400
    if r13_result is None:
        return jsonify({"msg": "No r13_result was provided"}), 400
    if r14_result is None:
        return jsonify({"msg": "No r14_result was provided"}), 400
    if r15_result is None:
        return jsonify({"msg": "No r15_result was provided"}), 400

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

    # valida si estan vacios los ingresos
    if date is None:
        return jsonify({"msg": "No Date was provided"}), 400
    if hour is None:
        return jsonify({"msg": "No hour was provided"}), 400
    if week is None:
        return jsonify({"msg": "No week was provided"}), 400
    if status is None:
        return jsonify({"msg": "No status was provided"}), 400
    if race is None:
        return jsonify({"msg": "No race was provided"}), 400
    if track is None:
        return jsonify({"msg": "No track was provided"}), 400
    if country is None:
        return jsonify({"msg": "No country was provided"}), 400
    if location is None:
        return jsonify({"msg": "No location was provided"}), 400
    if place1 is None:
        return jsonify({"msg": "No place1 was provided"}), 400
    if place2 is None:
        return jsonify({"msg": "No place2 was provided"}), 400
    if place3 is None:
        return jsonify({"msg": "No place3 was provided"}), 400

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

    # valida si estan vacios los ingresos
    if name is None:
        return jsonify({"msg": "No name was provided"}), 400
    if country is None:
        return jsonify({"msg": "No country was provided"}), 400
    if birth is None:
        return jsonify({"msg": "No birth was provided"}), 400
    if sponsor is None:
        return jsonify({"msg": "No sponsor was provided"}), 400
    if engine is None:
        return jsonify({"msg": "No engine was provided"}), 400
    if number_car is None:
        return jsonify({"msg": "No number_car was provided"}), 400
    if rank is None:
        return jsonify({"msg": "No rank was provided"}), 400
    if poles is None:
        return jsonify({"msg": "No poles was provided"}), 400
    if top5 is None:
        return jsonify({"msg": "No top5 was provided"}), 400
    if top10 is None:
        return jsonify({"msg": "No top10 was provided"}), 400
    if laps_lead is None:
        return jsonify({"msg": "No laps_lead was provided"}), 400
    if pts is None:
        return jsonify({"msg": "No pts was provided"}), 400
    if AVG_laps is None:
        return jsonify({"msg": "No AVG_laps was provided"}), 400
    if AVG_finish is None:
        return jsonify({"msg": "No AVG_finish was provided"}), 400

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
    # valida si estan vacios los ingresos
    if name1 is None:
        return jsonify({"msg": "No name1 was provided"}), 400
    if mu1 is None:
        return jsonify({"msg": "No mu1 was provided"}), 400
    if name2 is None:
        return jsonify({"msg": "No name2 was provided"}), 400
    if mu2 is None:
        return jsonify({"msg": "No mu2 was provided"}), 400
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
    # valida si estan vacios los ingresos
    if date is None:
        return jsonify({"msg": "No date was provided"}), 400
    if hour is None:
        return jsonify({"msg": "No hour was provided"}), 400
    if week is None:
        return jsonify({"msg": "No week was provided"}), 400
    if status is None:
        return jsonify({"msg": "No status was provided"}), 400
    if event is None:
        return jsonify({"msg": "No event was provided"}), 400
    if location is None:
        return jsonify({"msg": "No location was provided"}), 400
    if place1 is None:
        return jsonify({"msg": "No place1 was provided"}), 400
    if place2 is None:
        return jsonify({"msg": "No place2 was provided"}), 400
    if place3 is None:
        return jsonify({"msg": "No place3 was provided"}), 400
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
    # valida si estan vacios los ingresos
    if name is None:
        return jsonify({"msg": "No name was provided"}), 400
    if country is None:
        return jsonify({"msg": "No country was provided"}), 400
    if swing is None:
        return jsonify({"msg": "No swing was provided"}), 400
    if birth is None:
        return jsonify({"msg": "No birth was provided"}), 400
    if cuts is None:
        return jsonify({"msg": "No cuts was provided"}), 400
    if top10 is None:
        return jsonify({"msg": "No top10 was provided"}), 400
    if w is None:
        return jsonify({"msg": "No w was provided"}), 400
    if rnds is None:
        return jsonify({"msg": "No rnds was provided"}), 400
    if holes is None:
        return jsonify({"msg": "No holes was provided"}), 400
    if avg is None:
        return jsonify({"msg": "No avg was provided"}), 400
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

    # valida si estan vacios los ingresos
    if date is None:
        return jsonify({"msg": "No Date was provided"}), 400
    if hour is None:
        return jsonify({"msg": "No hour was provided"}), 400
    if status is None:
        return jsonify({"msg": "No status was provided"}), 400
    if away is None:
        return jsonify({"msg": "No away was provided"}), 400
    if home is None:
        return jsonify({"msg": "No home was provided"}), 400
    if spread_away is None:
        return jsonify({"msg": "No spread_away was provided"}), 400
    if spread_home is None:
        return jsonify({"msg": "No spread_home was provided"}), 400
    if juice_spread_away is None:
        return jsonify({"msg": "No juice_spread_away was provided"}), 400
    if juice_spread_home is None:
        return jsonify({"msg": "No juice_spread_home was provided"}), 400
    if moneyLineAway is None:
        return jsonify({"msg": "No moneyLineAway was provided"}), 400
    if moneyLineHome is None:
        return jsonify({"msg": "No moneyLineHome was provided"}), 400
    if total is None:
        return jsonify({"msg": "No total was provided"}), 400
    if juice_total_over is None:
        return jsonify({"msg": "No juice_total_over was provided"}), 400
    if juice_total_under is None:
        return jsonify({"msg": "No juice_total_under was provided"}), 400
    if tt_away is None:
        return jsonify({"msg": "No tt_away was provided"}), 400
    if juice_over_away is None:
        return jsonify({"msg": "No juice_over_away was provided"}), 400
    if juice_under_away is None:
        return jsonify({"msg": "No juice_under_away was provided"}), 400
    if tt_home is None:
        return jsonify({"msg": "No tt_home was provided"}), 400
    if juice_over_home is None:
        return jsonify({"msg": "No juice_over_home was provided"}), 400
    if juice_under_home is None:
        return jsonify({"msg": "No juice_under_home was provided"}), 400
    if final_score_away is None:
        return jsonify({"msg": "No final_score_away was provided"}), 400
    if final_score_home is None:
        return jsonify({"msg": "No final_score_home was provided"}), 400
    if first_half_spread_away is None:
        return jsonify({"msg": "No first_half_spread_away was provided"}), 400
    if first_half_spread_home is None:
        return jsonify({"msg": "No first_half_spread_home was provided"}), 400
    if first_half_juice_spread_away is None:
        return jsonify({"msg": "No first_half_juice_spread_away was provided"}), 400
    if first_half_juice_spread_home is None:
        return jsonify({"msg": "No first_half_juice_spread_home was provided"}), 400
    if first_half_moneyLineAway is None:
        return jsonify({"msg": "No first_half_moneyLineAway was provided"}), 400
    if first_half_moneyLineHome is None:
        return jsonify({"msg": "No first_half_moneyLineHome was provided"}), 400
    if first_half_total is None:
        return jsonify({"msg": "No first_half_total was provided"}), 400
    if fh_juice_over is None:
        return jsonify({"msg": "No fh_juice_over was provided"}), 400
    if fh_juice_under is None:
        return jsonify({"msg": "No fh_juice_under was provided"}), 400
    if first_half_tt_away is None:
        return jsonify({"msg": "No first_half_tt_away was provided"}), 400
    if first_half_juice_over_away is None:
        return jsonify({"msg": "No first_half_juice_over_away was provided"}), 400
    if first_half_juice_under_away is None:
        return jsonify({"msg": "No first_half_juice_under_away was provided"}), 400
    if first_half_tt_home is None:
        return jsonify({"msg": "No first_half_tt_home was provided"}), 400
    if first_half_juice_over_home is None:
        return jsonify({"msg": "No first_half_juice_over_home was provided"}), 400
    if first_half_juice_under_home is None:
        return jsonify({"msg": "No first_half_juice_under_home was provided"}), 400
    if first_half_final_score_away is None:
        return jsonify({"msg": "No first_half_final_score_away was provided"}), 400
    if first_half_final_score_home is None:
        return jsonify({"msg": "No first_half_final_score_home was provided"}), 400
    if second_half_spread_away is None:
        return jsonify({"msg": "No second_half_spread_away was provided"}), 400
    if second_half_spread_home is None:
        return jsonify({"msg": "No second_half_spread_home was provided"}), 400
    if second_half_juice_spread_away is None:
        return jsonify({"msg": "No second_half_juice_spread_away was provided"}), 400
    if second_half_juice_spread_home is None:
        return jsonify({"msg": "No second_half_juice_spread_home was provided"}), 400
    if second_half_moneyLineAway is None:
        return jsonify({"msg": "No second_half_moneyLineAway was provided"}), 400
    if second_half_moneyLineHome is None:
        return jsonify({"msg": "No second_half_moneyLineHome was provided"}), 400
    if second_half_total is None:
        return jsonify({"msg": "No second_half_total was provided"}), 400
    if sh_juice_over is None:
        return jsonify({"msg": "No sh_juice_over was provided"}), 400
    if sh_juice_under is None:
        return jsonify({"msg": "No sh_juice_under was provided"}), 400
    if second_half_tt_away is None:
        return jsonify({"msg": "No second_half_tt_away was provided"}), 400
    if second_half_juice_over_away is None:
        return jsonify({"msg": "No second_half_juice_over_away was provided"}), 400
    if second_half_juice_under_away is None:
        return jsonify({"msg": "No second_half_juice_under_away was provided"}), 400
    if second_half_tt_home is None:
        return jsonify({"msg": "No second_half_tt_home was provided"}), 400
    if second_half_juice_over_home is None:
        return jsonify({"msg": "No second_half_juice_over_home was provided"}), 400
    if second_half_juice_under_home is None:
        return jsonify({"msg": "No second_half_juice_under_home was provided"}), 400
    if second_half_final_score_away is None:
        return jsonify({"msg": "No second_half_final_score_away was provided"}), 400
    if second_half_final_score_home is None:
        return jsonify({"msg": "No second_half_final_score_home was provided"}), 400
    if q1_half_spread_away is None:
        return jsonify({"msg": "No q1_half_spread_away was provided"}), 400
    if q1_half_spread_home is None:
        return jsonify({"msg": "No q1_half_spread_home was provided"}), 400
    if q1_half_juice_spread_away is None:
        return jsonify({"msg": "No q1_half_juice_spread_away was provided"}), 400
    if q1_half_juice_spread_home is None:
        return jsonify({"msg": "No q1_half_juice_spread_home was provided"}), 400
    if q1_half_moneyLineAway is None:
        return jsonify({"msg": "No q1_half_moneyLineAway was provided"}), 400
    if q1_half_moneyLineHome is None:
        return jsonify({"msg": "No q1_half_moneyLineHome was provided"}), 400
    if q1_half_total is None:
        return jsonify({"msg": "No q1_half_total was provided"}), 400
    if q1_juice_over is None:
        return jsonify({"msg": "No q1_juice_over was provided"}), 400
    if q1_juice_under is None:
        return jsonify({"msg": "No q1_juice_under was provided"}), 400
    if q1_half_tt_away is None:
        return jsonify({"msg": "No q1_half_tt_away was provided"}), 400
    if q1_half_juice_over_away is None:
        return jsonify({"msg": "No q1_half_juice_over_away was provided"}), 400
    if q1_half_juice_under_away is None:
        return jsonify({"msg": "No q1_half_juice_under_away was provided"}), 400
    if q1_half_tt_home is None:
        return jsonify({"msg": "No q1_half_tt_home was provided"}), 400
    if q1_half_juice_over_home is None:
        return jsonify({"msg": "No q1_half_juice_over_home was provided"}), 400
    if q1_half_juice_under_home is None:
        return jsonify({"msg": "No q1_half_juice_under_home was provided"}), 400
    if q1_half_final_score_away is None:
        return jsonify({"msg": "No q1_half_final_score_away was provided"}), 400
    if q1_half_final_score_home is None:
        return jsonify({"msg": "No q1_half_final_score_home was provided"}), 400

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
    # valida si estan vacios los ingresos
    if date is None:
        return jsonify({"msg": "No Date was provided"}), 400
    if hour is None:
        return jsonify({"msg": "No hour was provided"}), 400
    if status is None:
        return jsonify({"msg": "No status was provided"}), 400
    if away is None:
        return jsonify({"msg": "No away was provided"}), 400
    if pitcher_a is None:
        return jsonify({"msg": "No pitcher_a was provided"}), 400
    if home is None:
        return jsonify({"msg": "No home was provided"}), 400
    if pitcher_h is None:
        return jsonify({"msg": "No pitcher_h was provided"}), 400
    if rl_away is None:
        return jsonify({"msg": "No añosEXP was provided"}), 400
    if rl_home is None:
        return jsonify({"msg": "No rl_home was provided"}), 400
    if moneyLineAway is None:
        return jsonify({"msg": "No moneyLineAway was provided"}), 400
    if moneyLineHome is None:
        return jsonify({"msg": "No moneyLineHome was provided"}), 400
    if total is None:
        return jsonify({"msg": "No total was provided"}), 400
    if juice_total_over is None:
        return jsonify({"msg": "No juice_total_over was provided"}), 400
    if juice_total_under is None:
        return jsonify({"msg": "No juice_total_under was provided"}), 400
    if tt_away is None:
        return jsonify({"msg": "No tt_away was provided"}), 400
    if juice_over_away is None:
        return jsonify({"msg": "No juice_over_away was provided"}), 400
    if juice_under_away is None:
        return jsonify({"msg": "No juice_under_away was provided"}), 400
    if tt_home is None:
        return jsonify({"msg": "No tt_home was provided"}), 400
    if juice_over_home is None:
        return jsonify({"msg": "No juice_over_home was provided"}), 400
    if juice_under_home is None:
        return jsonify({"msg": "No juice_under_home was provided"}), 400
    if final_score_away is None:
        return jsonify({"msg": "No final_score_away was provided"}), 400
    if final_score_home is None:
        return jsonify({"msg": "No final_score_home was provided"}), 400
    if rl_away_f5 is None:
        return jsonify({"msg": "No rl_away_f5 was provided"}), 400
    if rl_home_f5 is None:
        return jsonify({"msg": "No rl_home_f5 was provided"}), 400
    if juice_rl_away_f5 is None:
        return jsonify({"msg": "No juice_rl_away_f5 was provided"}), 400
    if juice_rl_home_f5 is None:
        return jsonify({"msg": "No juice_rl_home_f5 was provided"}), 400
    if moneyLineAway_f5 is None:
        return jsonify({"msg": "No moneyLineAway_f5 was provided"}), 400
    if moneyLineHome_f5 is None:
        return jsonify({"msg": "No moneyLineHome_f5 was provided"}), 400
    if total_f5 is None:
        return jsonify({"msg": "No total_f5 was provided"}), 400
    if juice_total_over_f5 is None:
        return jsonify({"msg": "No juice_total_over_f5 was provided"}), 400
    if juice_total_under_f5 is None:
        return jsonify({"msg": "No juice_total_under_f5 was provided"}), 400
    if tt_away_f5 is None:
        return jsonify({"msg": "No tt_away_f5 was provided"}), 400
    if juice_over_away_f5 is None:
        return jsonify({"msg": "No juice_over_away_f5 was provided"}), 400
    if juice_under_away_f5 is None:
        return jsonify({"msg": "No juice_under_away_f5 was provided"}), 400
    if juice_over_home_f5 is None:
        return jsonify({"msg": "No juice_over_home_f5 was provided"}), 400
    if juice_under_home_f5 is None:
        return jsonify({"msg": "No juice_under_home_f5 was provided"}), 400
    if fs_away_f5 is None:
        return jsonify({"msg": "No fs_away_f5 was provided"}), 400
    if fs_home_f5 is None:
        return jsonify({"msg": "No fs_home_f5 was provided"}), 400
    if sa_1inning is None:
        return jsonify({"msg": "No sh_1inning was provided"}), 400
    if sh_1inning is None:
        return jsonify({"msg": "No sh_1inning was provided"}), 400
    if sa_2inning is None:
        return jsonify({"msg": "No sa_2inning was provided"}), 400
    if sh_2inning is None:
        return jsonify({"msg": "No sh_2inning was provided"}), 400
    if sa_3inning is None:
        return jsonify({"msg": "No sa_3inning was provided"}), 400
    if sh_3inning is None:
        return jsonify({"msg": "No sh_3inning was provided"}), 400
    if sa_4inning is None:
        return jsonify({"msg": "No sa_4inning was provided"}), 400
    if sh_4inning is None:
        return jsonify({"msg": "No sh_4inning was provided"}), 400
    if sa_5inning is None:
        return jsonify({"msg": "No sa_5inning was provided"}), 400
    if sh_5inning is None:
        return jsonify({"msg": "No sh_5inning was provided"}), 400
    if sa_6inning is None:
        return jsonify({"msg": "No sa_6inning was provided"}), 400
    if sh_6inning is None:
        return jsonify({"msg": "No sh_6inning was provided"}), 400
    if sa_7inning is None:
        return jsonify({"msg": "No sa_7inning was provided"}), 400
    if sh_7inning is None:
        return jsonify({"msg": "No sh_7inning was provided"}), 400
    if sa_8inning is None:
        return jsonify({"msg": "No sa_8inning was provided"}), 400
    if sh_8inning is None:
        return jsonify({"msg": "No sh_8inning was provided"}), 400
    if sa_9inning is None:
        return jsonify({"msg": "No sa_9inning was provided"}), 400
    if sh_9inning is None:
        return jsonify({"msg": "No sh_9inning was provided"}), 400
    if sa_10inning is None:
        return jsonify({"msg": "No sa_10inning was provided"}), 400
    if sh_10inning is None:
        return jsonify({"msg": "No sh_10inning was provided"}), 400
    if sa_11inning is None:
        return jsonify({"msg": "No sa_11inning was provided"}), 400
    if sh_11inning is None:
        return jsonify({"msg": "No sh_11inning was provided"}), 400
    if sa_12inning is None:
        return jsonify({"msg": "No sa_12inning was provided"}), 400
    if sh_12inning is None:
        return jsonify({"msg": "No sh_12inning was provided"}), 400
    if sa_13inning is None:
        return jsonify({"msg": "No sa_13inning was provided"}), 400
    if sh_13inning is None:
        return jsonify({"msg": "No sh_13inning was provided"}), 400
    if sa_14inning is None:
        return jsonify({"msg": "No sa_14inning was provided"}), 400
    if sh_14inning is None:
        return jsonify({"msg": "No sh_14inning was provided"}), 400
    if sa_15inning is None:
        return jsonify({"msg": "No sa_15inning was provided"}), 400
    if sh_15inning is None:
        return jsonify({"msg": "No sh_15inning was provided"}), 400
    if sa_16inning is None:
        return jsonify({"msg": "No sa_16inning was provided"}), 400
    if sh_16inning is None:
        return jsonify({"msg": "No sh_16inning was provided"}), 400
    if sa_17inning is None:
        return jsonify({"msg": "No sa_17inning was provided"}), 400
    if sh_17inning is None:
        return jsonify({"msg": "No sh_17inning was provided"}), 400
    if sa_18inning is None:
        return jsonify({"msg": "No sa_1inning was provided"}), 400
    if sh_18inning is None:
        return jsonify({"msg": "No sa_18inning was provided"}), 400
    if sa_19inning is None:
        return jsonify({"msg": "No sa_19inning was provided"}), 400
    if sh_19inning is None:
        return jsonify({"msg": "No sh_19inning was provided"}), 400
    if sa_20inning is None:
        return jsonify({"msg": "No sa_20inning was provided"}), 400
    if sh_20inning is None:
        return jsonify({"msg": "No sh_20inning was provided"}), 400
    if sa_21inning is None:
        return jsonify({"msg": "No sa_21inning was provided"}), 400
    if sh_21inning is None:
        return jsonify({"msg": "No sh_21inning was provided"}), 400
    if sa_22inning is None:
        return jsonify({"msg": "No sa_22inning was provided"}), 400
    if sh_22inning is None:
        return jsonify({"msg": "No sh_22inning was provided"}), 400
    if sa_23inning is None:
        return jsonify({"msg": "No sa_23inning was provided"}), 400
    if sh_23inning is None:
        return jsonify({"msg": "No sh_23inning was provided"}), 400
    if sa_24inning is None:
        return jsonify({"msg": "No sa_24inning was provided"}), 400
    if sh_24inning is None:
        return jsonify({"msg": "No sh_24inning was provided"}), 400
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

    # valida si estan vacios los ingresos
    if date is None:
        return jsonify({"msg": "No Date was provided"}), 400
    if hour is None:
        return jsonify({"msg": "No hour was provided"}), 400
    if week is None:
        return jsonify({"msg": "No week was provided"}), 400
    if status is None:
        return jsonify({"msg": "No status was provided"}), 400
    if away is None:
        return jsonify({"msg": "No away was provided"}), 400
    if home is None:
        return jsonify({"msg": "No home was provided"}), 400
    if spread_away is None:
        return jsonify({"msg": "No spread_away was provided"}), 400
    if spread_home is None:
        return jsonify({"msg": "No spread_home was provided"}), 400
    if juice_spread_away is None:
        return jsonify({"msg": "No juice_spread_away was provided"}), 400
    if juice_spread_home is None:
        return jsonify({"msg": "No juice_spread_home was provided"}), 400
    if moneyLineAway is None:
        return jsonify({"msg": "No moneyLineAway was provided"}), 400
    if moneyLineHome is None:
        return jsonify({"msg": "No moneyLineHome was provided"}), 400
    if total is None:
        return jsonify({"msg": "No total was provided"}), 400
    if juice_total_over is None:
        return jsonify({"msg": "No juice_total_over was provided"}), 400
    if juice_total_under is None:
        return jsonify({"msg": "No juice_total_under was provided"}), 400
    if tt_away is None:
        return jsonify({"msg": "No tt_away was provided"}), 400
    if juice_over_away is None:
        return jsonify({"msg": "No juice_over_away was provided"}), 400
    if juice_under_away is None:
        return jsonify({"msg": "No juice_under_away was provided"}), 400
    if tt_home is None:
        return jsonify({"msg": "No tt_home was provided"}), 400
    if juice_over_home is None:
        return jsonify({"msg": "No juice_over_home was provided"}), 400
    if juice_under_home is None:
        return jsonify({"msg": "No juice_under_home was provided"}), 400
    if final_score_away is None:
        return jsonify({"msg": "No final_score_away was provided"}), 400
    if final_score_home is None:
        return jsonify({"msg": "No final_score_home was provided"}), 400
    if first_half_spread_away is None:
        return jsonify({"msg": "No first_half_spread_away was provided"}), 400
    if first_half_spread_home is None:
        return jsonify({"msg": "No first_half_spread_home was provided"}), 400
    if first_half_juice_spread_away is None:
        return jsonify({"msg": "No first_half_juice_spread_away was provided"}), 400
    if first_half_juice_spread_home is None:
        return jsonify({"msg": "No first_half_juice_spread_home was provided"}), 400
    if first_half_moneyLineAway is None:
        return jsonify({"msg": "No first_half_moneyLineAway was provided"}), 400
    if first_half_moneyLineHome is None:
        return jsonify({"msg": "No first_half_moneyLineHome was provided"}), 400
    if first_half_total is None:
        return jsonify({"msg": "No first_half_total was provided"}), 400
    if fh_juice_over is None:
        return jsonify({"msg": "No fh_juice_over was provided"}), 400
    if fh_juice_under is None:
        return jsonify({"msg": "No fh_juice_under was provided"}), 400
    if first_half_tt_away is None:
        return jsonify({"msg": "No first_half_tt_away was provided"}), 400
    if first_half_juice_over_away is None:
        return jsonify({"msg": "No first_half_juice_over_away was provided"}), 400
    if first_half_juice_under_away is None:
        return jsonify({"msg": "No first_half_juice_under_away was provided"}), 400
    if first_half_tt_home is None:
        return jsonify({"msg": "No first_half_tt_home was provided"}), 400
    if first_half_juice_over_home is None:
        return jsonify({"msg": "No first_half_juice_over_home was provided"}), 400
    if first_half_juice_under_home is None:
        return jsonify({"msg": "No first_half_juice_under_home was provided"}), 400
    if first_half_final_score_away is None:
        return jsonify({"msg": "No first_half_final_score_away was provided"}), 400
    if first_half_final_score_home is None:
        return jsonify({"msg": "No first_half_final_score_home was provided"}), 400
    if second_half_spread_away is None:
        return jsonify({"msg": "No second_half_spread_away was provided"}), 400
    if second_half_spread_home is None:
        return jsonify({"msg": "No second_half_spread_home was provided"}), 400
    if second_half_juice_spread_away is None:
        return jsonify({"msg": "No second_half_juice_spread_away was provided"}), 400
    if second_half_juice_spread_home is None:
        return jsonify({"msg": "No second_half_juice_spread_home was provided"}), 400
    if second_half_moneyLineAway is None:
        return jsonify({"msg": "No second_half_moneyLineAway was provided"}), 400
    if second_half_moneyLineHome is None:
        return jsonify({"msg": "No second_half_moneyLineHome was provided"}), 400
    if second_half_total is None:
        return jsonify({"msg": "No second_half_total was provided"}), 400
    if sh_juice_over is None:
        return jsonify({"msg": "No sh_juice_over was provided"}), 400
    if sh_juice_under is None:
        return jsonify({"msg": "No sh_juice_under was provided"}), 400
    if second_half_tt_away is None:
        return jsonify({"msg": "No second_half_tt_away was provided"}), 400
    if second_half_juice_over_away is None:
        return jsonify({"msg": "No second_half_juice_over_away was provided"}), 400
    if second_half_juice_under_away is None:
        return jsonify({"msg": "No second_half_juice_under_away was provided"}), 400
    if second_half_tt_home is None:
        return jsonify({"msg": "No second_half_tt_home was provided"}), 400
    if second_half_juice_over_home is None:
        return jsonify({"msg": "No second_half_juice_over_home was provided"}), 400
    if second_half_juice_under_home is None:
        return jsonify({"msg": "No second_half_juice_under_home was provided"}), 400
    if second_half_final_score_away is None:
        return jsonify({"msg": "No second_half_final_score_away was provided"}), 400
    if second_half_final_score_home is None:
        return jsonify({"msg": "No second_half_final_score_home was provided"}), 400
    if q1_half_spread_away is None:
        return jsonify({"msg": "No q1_half_spread_away was provided"}), 400
    if q1_half_spread_home is None:
        return jsonify({"msg": "No q1_half_spread_home was provided"}), 400
    if q1_half_juice_spread_away is None:
        return jsonify({"msg": "No q1_half_juice_spread_away was provided"}), 400
    if q1_half_juice_spread_home is None:
        return jsonify({"msg": "No q1_half_juice_spread_home was provided"}), 400
    if q1_half_moneyLineAway is None:
        return jsonify({"msg": "No q1_half_moneyLineAway was provided"}), 400
    if q1_half_moneyLineHome is None:
        return jsonify({"msg": "No q1_half_moneyLineHome was provided"}), 400
    if q1_half_total is None:
        return jsonify({"msg": "No q1_half_total was provided"}), 400
    if q1_juice_over is None:
        return jsonify({"msg": "No q1_juice_over was provided"}), 400
    if q1_juice_under is None:
        return jsonify({"msg": "No q1_juice_under was provided"}), 400
    if q1_half_tt_away is None:
        return jsonify({"msg": "No q1_half_tt_away was provided"}), 400
    if q1_half_juice_over_away is None:
        return jsonify({"msg": "No q1_half_juice_over_away was provided"}), 400
    if q1_half_juice_under_away is None:
        return jsonify({"msg": "No q1_half_juice_under_away was provided"}), 400
    if q1_half_tt_home is None:
        return jsonify({"msg": "No q1_half_tt_home was provided"}), 400
    if q1_half_juice_over_home is None:
        return jsonify({"msg": "No q1_half_juice_over_home was provided"}), 400
    if q1_half_juice_under_home is None:
        return jsonify({"msg": "No q1_half_juice_under_home was provided"}), 400
    if q1_half_final_score_away is None:
        return jsonify({"msg": "No q1_half_final_score_away was provided"}), 400
    if q1_half_final_score_home is None:
        return jsonify({"msg": "No q1_half_final_score_home was provided"}), 400

    # busca mlb en BBDD
    ncaa_football = Ncaa_football.query.filter_by(
        home=home, away=away, date=date).first()
    # the mlb was not found on the database
    if ncaa_football:
        return jsonify({"msg": "Mlb already exists", "status": ncaa_football.status}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        ncaa_football = Ncaa_football(
            date=date,
            hour=hour,
            status=status,
            away=away,
            home=home,
            week=week,
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

    # valida si estan vacios los ingresos
    if date is None:
        return jsonify({"msg": "No Date was provided"}), 400
    if hour is None:
        return jsonify({"msg": "No hour was provided"}), 400
    if status is None:
        return jsonify({"msg": "No status was provided"}), 400
    if away is None:
        return jsonify({"msg": "No away was provided"}), 400
    if home is None:
        return jsonify({"msg": "No home was provided"}), 400
    if goal_line_away is None:
        return jsonify({"msg": "No goal_line_away was provided"}), 400
    if goal_line_home is None:
        return jsonify({"msg": "No goal_line_home was provided"}), 400
    if juice_goal_away is None:
        return jsonify({"msg": "No juice_goal_away was provided"}), 400
    if juice_goal_home is None:
        return jsonify({"msg": "No juice_goal_home was provided"}), 400
    if moneyLineAway is None:
        return jsonify({"msg": "No moneyLineAway was provided"}), 400
    if moneyLineHome is None:
        return jsonify({"msg": "No moneyLineHome was provided"}), 400
    if total is None:
        return jsonify({"msg": "No total was provided"}), 400
    if juice_total_over is None:
        return jsonify({"msg": "No juice_total_over was provided"}), 400
    if juice_total_under is None:
        return jsonify({"msg": "No juice_total_under was provided"}), 400
    if tt_away is None:
        return jsonify({"msg": "No tt_away was provided"}), 400
    if juice_over_away is None:
        return jsonify({"msg": "No juice_over_away was provided"}), 400
    if juice_under_away is None:
        return jsonify({"msg": "No juice_under_away was provided"}), 400
    if tt_home is None:
        return jsonify({"msg": "No tt_home was provided"}), 400
    if juice_over_home is None:
        return jsonify({"msg": "No juice_over_home was provided"}), 400
    if juice_under_home is None:
        return jsonify({"msg": "No juice_under_home was provided"}), 400
    if final_score_away is None:
        return jsonify({"msg": "No final_score_away was provided"}), 400
    if final_score_home is None:
        return jsonify({"msg": "No final_score_home was provided"}), 400
    if goal_away_1H is None:
        return jsonify({"msg": "No goal_away_1H was provided"}), 400
    if goal_home_1H is None:
        return jsonify({"msg": "No goal_home_1H was provided"}), 400
    if juice_goal_away_1H is None:
        return jsonify({"msg": "No juice_goal_away_1H was provided"}), 400
    if juice_goal_home_1H is None:
        return jsonify({"msg": "No juice_goal_home_1H was provided"}), 400
    if moneyLineAway_1H is None:
        return jsonify({"msg": "No moneyLineAway_1H was provided"}), 400
    if moneyLineHome_1H is None:
        return jsonify({"msg": "No moneyLineHome_1H was provided"}), 400
    if total_1H is None:
        return jsonify({"msg": "No total_1H was provided"}), 400
    if H1_juice_over is None:
        return jsonify({"msg": "No H1_juice_over was provided"}), 400
    if H1_juice_under is None:
        return jsonify({"msg": "No H1_juice_under was provided"}), 400
    if tt_away_1H is None:
        return jsonify({"msg": "No tt_away_1H was provided"}), 400
    if juice_over_away_1H is None:
        return jsonify({"msg": "No juice_over_away_1H was provided"}), 400
    if juice_under_away_1H is None:
        return jsonify({"msg": "No juice_under_away_1H was provided"}), 400
    if tt_home_1H is None:
        return jsonify({"msg": "No tt_home_1H was provided"}), 400
    if juice_over_home_1H is None:
        return jsonify({"msg": "No juice_over_home_1H was provided"}), 400
    if juice_under_home_1H is None:
        return jsonify({"msg": "No juice_under_home_1H was provided"}), 400

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

    # valida si estan vacios los ingresos
    if date is None:
        return jsonify({"msg": "No Date was provided"}), 400
    if hour is None:
        return jsonify({"msg": "No hour was provided"}), 400
    if status is None:
        return jsonify({"msg": "No status was provided"}), 400
    if away is None:
        return jsonify({"msg": "No away was provided"}), 400
    if home is None:
        return jsonify({"msg": "No home was provided"}), 400
    if goal_line_away is None:
        return jsonify({"msg": "No goal_line_away was provided"}), 400
    if goal_line_home is None:
        return jsonify({"msg": "No goal_line_home was provided"}), 400
    if juice_goal_away is None:
        return jsonify({"msg": "No juice_goal_away was provided"}), 400
    if juice_goal_home is None:
        return jsonify({"msg": "No juice_goal_home was provided"}), 400
    if moneyLineAway is None:
        return jsonify({"msg": "No moneyLineAway was provided"}), 400
    if moneyLineHome is None:
        return jsonify({"msg": "No moneyLineHome was provided"}), 400
    if total is None:
        return jsonify({"msg": "No total was provided"}), 400
    if juice_total_over is None:
        return jsonify({"msg": "No juice_total_over was provided"}), 400
    if juice_total_under is None:
        return jsonify({"msg": "No juice_total_under was provided"}), 400
    if tt_away is None:
        return jsonify({"msg": "No tt_away was provided"}), 400
    if juice_over_away is None:
        return jsonify({"msg": "No juice_over_away was provided"}), 400
    if juice_under_away is None:
        return jsonify({"msg": "No juice_under_away was provided"}), 400
    if tt_home is None:
        return jsonify({"msg": "No tt_home was provided"}), 400
    if juice_over_home is None:
        return jsonify({"msg": "No juice_over_home was provided"}), 400
    if juice_under_home is None:
        return jsonify({"msg": "No juice_under_home was provided"}), 400
    if final_score_away is None:
        return jsonify({"msg": "No final_score_away was provided"}), 400
    if final_score_home is None:
        return jsonify({"msg": "No final_score_home was provided"}), 400
    if goal_away_1H is None:
        return jsonify({"msg": "No goal_away_1H was provided"}), 400
    if goal_home_1H is None:
        return jsonify({"msg": "No goal_home_1H was provided"}), 400
    if juice_goal_away_1H is None:
        return jsonify({"msg": "No juice_goal_away_1H was provided"}), 400
    if juice_goal_home_1H is None:
        return jsonify({"msg": "No juice_goal_home_1H was provided"}), 400
    if moneyLineAway_1H is None:
        return jsonify({"msg": "No moneyLineAway_1H was provided"}), 400
    if moneyLineHome_1H is None:
        return jsonify({"msg": "No moneyLineHome_1H was provided"}), 400
    if total_1H is None:
        return jsonify({"msg": "No total_1H was provided"}), 400
    if H1_juice_over is None:
        return jsonify({"msg": "No H1_juice_over was provided"}), 400
    if H1_juice_under is None:
        return jsonify({"msg": "No H1_juice_under was provided"}), 400
    if tt_away_1H is None:
        return jsonify({"msg": "No tt_away_1H was provided"}), 400
    if juice_over_away_1H is None:
        return jsonify({"msg": "No juice_over_away_1H was provided"}), 400
    if juice_under_away_1H is None:
        return jsonify({"msg": "No juice_under_away_1H was provided"}), 400
    if tt_home_1H is None:
        return jsonify({"msg": "No tt_home_1H was provided"}), 400
    if juice_over_home_1H is None:
        return jsonify({"msg": "No juice_over_home_1H was provided"}), 400
    if juice_under_home_1H is None:
        return jsonify({"msg": "No juice_under_home_1H was provided"}), 400

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

    # valida si estan vacios los ingresos
    if date is None:
        return jsonify({"msg": "No Date was provided"}), 400
    if hour is None:
        return jsonify({"msg": "No hour was provided"}), 400
    if status is None:
        return jsonify({"msg": "No status was provided"}), 400
    if away is None:
        return jsonify({"msg": "No away was provided"}), 400
    if home is None:
        return jsonify({"msg": "No home was provided"}), 400
    if goal_line_away is None:
        return jsonify({"msg": "No goal_line_away was provided"}), 400
    if goal_line_home is None:
        return jsonify({"msg": "No goal_line_home was provided"}), 400
    if juice_goal_away is None:
        return jsonify({"msg": "No juice_goal_away was provided"}), 400
    if juice_goal_home is None:
        return jsonify({"msg": "No juice_goal_home was provided"}), 400
    if moneyLineAway is None:
        return jsonify({"msg": "No moneyLineAway was provided"}), 400
    if moneyLineHome is None:
        return jsonify({"msg": "No moneyLineHome was provided"}), 400
    if total is None:
        return jsonify({"msg": "No total was provided"}), 400
    if juice_total_over is None:
        return jsonify({"msg": "No juice_total_over was provided"}), 400
    if juice_total_under is None:
        return jsonify({"msg": "No juice_total_under was provided"}), 400
    if tt_away is None:
        return jsonify({"msg": "No tt_away was provided"}), 400
    if juice_over_away is None:
        return jsonify({"msg": "No juice_over_away was provided"}), 400
    if juice_under_away is None:
        return jsonify({"msg": "No juice_under_away was provided"}), 400
    if tt_home is None:
        return jsonify({"msg": "No tt_home was provided"}), 400
    if juice_over_home is None:
        return jsonify({"msg": "No juice_over_home was provided"}), 400
    if juice_under_home is None:
        return jsonify({"msg": "No juice_under_home was provided"}), 400
    if final_score_away is None:
        return jsonify({"msg": "No final_score_away was provided"}), 400
    if final_score_home is None:
        return jsonify({"msg": "No final_score_home was provided"}), 400
    if goal_away_1H is None:
        return jsonify({"msg": "No goal_away_1H was provided"}), 400
    if goal_home_1H is None:
        return jsonify({"msg": "No goal_home_1H was provided"}), 400
    if juice_goal_away_1H is None:
        return jsonify({"msg": "No juice_goal_away_1H was provided"}), 400
    if juice_goal_home_1H is None:
        return jsonify({"msg": "No juice_goal_home_1H was provided"}), 400
    if moneyLineAway_1H is None:
        return jsonify({"msg": "No moneyLineAway_1H was provided"}), 400
    if moneyLineHome_1H is None:
        return jsonify({"msg": "No moneyLineHome_1H was provided"}), 400
    if total_1H is None:
        return jsonify({"msg": "No total_1H was provided"}), 400
    if H1_juice_over is None:
        return jsonify({"msg": "No H1_juice_over was provided"}), 400
    if H1_juice_under is None:
        return jsonify({"msg": "No H1_juice_under was provided"}), 400
    if tt_away_1H is None:
        return jsonify({"msg": "No tt_away_1H was provided"}), 400
    if juice_over_away_1H is None:
        return jsonify({"msg": "No juice_over_away_1H was provided"}), 400
    if juice_under_away_1H is None:
        return jsonify({"msg": "No juice_under_away_1H was provided"}), 400
    if tt_home_1H is None:
        return jsonify({"msg": "No tt_home_1H was provided"}), 400
    if juice_over_home_1H is None:
        return jsonify({"msg": "No juice_over_home_1H was provided"}), 400
    if juice_under_home_1H is None:
        return jsonify({"msg": "No juice_under_home_1H was provided"}), 400

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

    # valida si estan vacios los ingresos
    if date is None:
        return jsonify({"msg": "No Date was provided"}), 400
    if hour is None:
        return jsonify({"msg": "No hour was provided"}), 400
    if status is None:
        return jsonify({"msg": "No status was provided"}), 400
    if away is None:
        return jsonify({"msg": "No away was provided"}), 400
    if home is None:
        return jsonify({"msg": "No home was provided"}), 400
    if goal_line_away is None:
        return jsonify({"msg": "No goal_line_away was provided"}), 400
    if goal_line_home is None:
        return jsonify({"msg": "No goal_line_home was provided"}), 400
    if juice_goal_away is None:
        return jsonify({"msg": "No juice_goal_away was provided"}), 400
    if juice_goal_home is None:
        return jsonify({"msg": "No juice_goal_home was provided"}), 400
    if moneyLineAway is None:
        return jsonify({"msg": "No moneyLineAway was provided"}), 400
    if moneyLineHome is None:
        return jsonify({"msg": "No moneyLineHome was provided"}), 400
    if total is None:
        return jsonify({"msg": "No total was provided"}), 400
    if juice_total_over is None:
        return jsonify({"msg": "No juice_total_over was provided"}), 400
    if juice_total_under is None:
        return jsonify({"msg": "No juice_total_under was provided"}), 400
    if tt_away is None:
        return jsonify({"msg": "No tt_away was provided"}), 400
    if juice_over_away is None:
        return jsonify({"msg": "No juice_over_away was provided"}), 400
    if juice_under_away is None:
        return jsonify({"msg": "No juice_under_away was provided"}), 400
    if tt_home is None:
        return jsonify({"msg": "No tt_home was provided"}), 400
    if juice_over_home is None:
        return jsonify({"msg": "No juice_over_home was provided"}), 400
    if juice_under_home is None:
        return jsonify({"msg": "No juice_under_home was provided"}), 400
    if final_score_away is None:
        return jsonify({"msg": "No final_score_away was provided"}), 400
    if final_score_home is None:
        return jsonify({"msg": "No final_score_home was provided"}), 400
    if goal_away_1H is None:
        return jsonify({"msg": "No goal_away_1H was provided"}), 400
    if goal_home_1H is None:
        return jsonify({"msg": "No goal_home_1H was provided"}), 400
    if juice_goal_away_1H is None:
        return jsonify({"msg": "No juice_goal_away_1H was provided"}), 400
    if juice_goal_home_1H is None:
        return jsonify({"msg": "No juice_goal_home_1H was provided"}), 400
    if moneyLineAway_1H is None:
        return jsonify({"msg": "No moneyLineAway_1H was provided"}), 400
    if moneyLineHome_1H is None:
        return jsonify({"msg": "No moneyLineHome_1H was provided"}), 400
    if total_1H is None:
        return jsonify({"msg": "No total_1H was provided"}), 400
    if H1_juice_over is None:
        return jsonify({"msg": "No H1_juice_over was provided"}), 400
    if H1_juice_under is None:
        return jsonify({"msg": "No H1_juice_under was provided"}), 400
    if tt_away_1H is None:
        return jsonify({"msg": "No tt_away_1H was provided"}), 400
    if juice_over_away_1H is None:
        return jsonify({"msg": "No juice_over_away_1H was provided"}), 400
    if juice_under_away_1H is None:
        return jsonify({"msg": "No juice_under_away_1H was provided"}), 400
    if tt_home_1H is None:
        return jsonify({"msg": "No tt_home_1H was provided"}), 400
    if juice_over_home_1H is None:
        return jsonify({"msg": "No juice_over_home_1H was provided"}), 400
    if juice_under_home_1H is None:
        return jsonify({"msg": "No juice_under_home_1H was provided"}), 400

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

    # valida si estan vacios los ingresos
    if date is None:
        return jsonify({"msg": "No Date was provided"}), 400
    if hour is None:
        return jsonify({"msg": "No hour was provided"}), 400
    if status is None:
        return jsonify({"msg": "No status was provided"}), 400
    if away is None:
        return jsonify({"msg": "No away was provided"}), 400
    if home is None:
        return jsonify({"msg": "No home was provided"}), 400
    if goal_line_away is None:
        return jsonify({"msg": "No goal_line_away was provided"}), 400
    if goal_line_home is None:
        return jsonify({"msg": "No goal_line_home was provided"}), 400
    if juice_goal_away is None:
        return jsonify({"msg": "No juice_goal_away was provided"}), 400
    if juice_goal_home is None:
        return jsonify({"msg": "No juice_goal_home was provided"}), 400
    if moneyLineAway is None:
        return jsonify({"msg": "No moneyLineAway was provided"}), 400
    if moneyLineHome is None:
        return jsonify({"msg": "No moneyLineHome was provided"}), 400
    if total is None:
        return jsonify({"msg": "No total was provided"}), 400
    if juice_total_over is None:
        return jsonify({"msg": "No juice_total_over was provided"}), 400
    if juice_total_under is None:
        return jsonify({"msg": "No juice_total_under was provided"}), 400
    if tt_away is None:
        return jsonify({"msg": "No tt_away was provided"}), 400
    if juice_over_away is None:
        return jsonify({"msg": "No juice_over_away was provided"}), 400
    if juice_under_away is None:
        return jsonify({"msg": "No juice_under_away was provided"}), 400
    if tt_home is None:
        return jsonify({"msg": "No tt_home was provided"}), 400
    if juice_over_home is None:
        return jsonify({"msg": "No juice_over_home was provided"}), 400
    if juice_under_home is None:
        return jsonify({"msg": "No juice_under_home was provided"}), 400
    if final_score_away is None:
        return jsonify({"msg": "No final_score_away was provided"}), 400
    if final_score_home is None:
        return jsonify({"msg": "No final_score_home was provided"}), 400
    if goal_away_1H is None:
        return jsonify({"msg": "No goal_away_1H was provided"}), 400
    if goal_home_1H is None:
        return jsonify({"msg": "No goal_home_1H was provided"}), 400
    if juice_goal_away_1H is None:
        return jsonify({"msg": "No juice_goal_away_1H was provided"}), 400
    if juice_goal_home_1H is None:
        return jsonify({"msg": "No juice_goal_home_1H was provided"}), 400
    if moneyLineAway_1H is None:
        return jsonify({"msg": "No moneyLineAway_1H was provided"}), 400
    if moneyLineHome_1H is None:
        return jsonify({"msg": "No moneyLineHome_1H was provided"}), 400
    if total_1H is None:
        return jsonify({"msg": "No total_1H was provided"}), 400
    if H1_juice_over is None:
        return jsonify({"msg": "No H1_juice_over was provided"}), 400
    if H1_juice_under is None:
        return jsonify({"msg": "No H1_juice_under was provided"}), 400
    if tt_away_1H is None:
        return jsonify({"msg": "No tt_away_1H was provided"}), 400
    if juice_over_away_1H is None:
        return jsonify({"msg": "No juice_over_away_1H was provided"}), 400
    if juice_under_away_1H is None:
        return jsonify({"msg": "No juice_under_away_1H was provided"}), 400
    if tt_home_1H is None:
        return jsonify({"msg": "No tt_home_1H was provided"}), 400
    if juice_over_home_1H is None:
        return jsonify({"msg": "No juice_over_home_1H was provided"}), 400
    if juice_under_home_1H is None:
        return jsonify({"msg": "No juice_under_home_1H was provided"}), 400

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

    # valida si estan vacios los ingresos
    if date is None:
        return jsonify({"msg": "No Date was provided"}), 400
    if hour is None:
        return jsonify({"msg": "No hour was provided"}), 400
    if status is None:
        return jsonify({"msg": "No status was provided"}), 400
    if away is None:
        return jsonify({"msg": "No away was provided"}), 400
    if home is None:
        return jsonify({"msg": "No home was provided"}), 400
    if goal_line_away is None:
        return jsonify({"msg": "No goal_line_away was provided"}), 400
    if goal_line_home is None:
        return jsonify({"msg": "No goal_line_home was provided"}), 400
    if juice_goal_away is None:
        return jsonify({"msg": "No juice_goal_away was provided"}), 400
    if juice_goal_home is None:
        return jsonify({"msg": "No juice_goal_home was provided"}), 400
    if moneyLineAway is None:
        return jsonify({"msg": "No moneyLineAway was provided"}), 400
    if moneyLineHome is None:
        return jsonify({"msg": "No moneyLineHome was provided"}), 400
    if total is None:
        return jsonify({"msg": "No total was provided"}), 400
    if juice_total_over is None:
        return jsonify({"msg": "No juice_total_over was provided"}), 400
    if juice_total_under is None:
        return jsonify({"msg": "No juice_total_under was provided"}), 400
    if tt_away is None:
        return jsonify({"msg": "No tt_away was provided"}), 400
    if juice_over_away is None:
        return jsonify({"msg": "No juice_over_away was provided"}), 400
    if juice_under_away is None:
        return jsonify({"msg": "No juice_under_away was provided"}), 400
    if tt_home is None:
        return jsonify({"msg": "No tt_home was provided"}), 400
    if juice_over_home is None:
        return jsonify({"msg": "No juice_over_home was provided"}), 400
    if juice_under_home is None:
        return jsonify({"msg": "No juice_under_home was provided"}), 400
    if final_score_away is None:
        return jsonify({"msg": "No final_score_away was provided"}), 400
    if final_score_home is None:
        return jsonify({"msg": "No final_score_home was provided"}), 400
    if goal_away_1H is None:
        return jsonify({"msg": "No goal_away_1H was provided"}), 400
    if goal_home_1H is None:
        return jsonify({"msg": "No goal_home_1H was provided"}), 400
    if juice_goal_away_1H is None:
        return jsonify({"msg": "No juice_goal_away_1H was provided"}), 400
    if juice_goal_home_1H is None:
        return jsonify({"msg": "No juice_goal_home_1H was provided"}), 400
    if moneyLineAway_1H is None:
        return jsonify({"msg": "No moneyLineAway_1H was provided"}), 400
    if moneyLineHome_1H is None:
        return jsonify({"msg": "No moneyLineHome_1H was provided"}), 400
    if total_1H is None:
        return jsonify({"msg": "No total_1H was provided"}), 400
    if H1_juice_over is None:
        return jsonify({"msg": "No H1_juice_over was provided"}), 400
    if H1_juice_under is None:
        return jsonify({"msg": "No H1_juice_under was provided"}), 400
    if tt_away_1H is None:
        return jsonify({"msg": "No tt_away_1H was provided"}), 400
    if juice_over_away_1H is None:
        return jsonify({"msg": "No juice_over_away_1H was provided"}), 400
    if juice_under_away_1H is None:
        return jsonify({"msg": "No juice_under_away_1H was provided"}), 400
    if tt_home_1H is None:
        return jsonify({"msg": "No tt_home_1H was provided"}), 400
    if juice_over_home_1H is None:
        return jsonify({"msg": "No juice_over_home_1H was provided"}), 400
    if juice_under_home_1H is None:
        return jsonify({"msg": "No juice_under_home_1H was provided"}), 400

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

    # valida si estan vacios los ingresos
    if date is None:
        return jsonify({"msg": "No Date was provided"}), 400
    if hour is None:
        return jsonify({"msg": "No hour was provided"}), 400
    if status is None:
        return jsonify({"msg": "No status was provided"}), 400
    if away is None:
        return jsonify({"msg": "No away was provided"}), 400
    if home is None:
        return jsonify({"msg": "No home was provided"}), 400
    if goal_line_away is None:
        return jsonify({"msg": "No goal_line_away was provided"}), 400
    if goal_line_home is None:
        return jsonify({"msg": "No goal_line_home was provided"}), 400
    if juice_goal_away is None:
        return jsonify({"msg": "No juice_goal_away was provided"}), 400
    if juice_goal_home is None:
        return jsonify({"msg": "No juice_goal_home was provided"}), 400
    if moneyLineAway is None:
        return jsonify({"msg": "No moneyLineAway was provided"}), 400
    if moneyLineHome is None:
        return jsonify({"msg": "No moneyLineHome was provided"}), 400
    if total is None:
        return jsonify({"msg": "No total was provided"}), 400
    if juice_total_over is None:
        return jsonify({"msg": "No juice_total_over was provided"}), 400
    if juice_total_under is None:
        return jsonify({"msg": "No juice_total_under was provided"}), 400
    if tt_away is None:
        return jsonify({"msg": "No tt_away was provided"}), 400
    if juice_over_away is None:
        return jsonify({"msg": "No juice_over_away was provided"}), 400
    if juice_under_away is None:
        return jsonify({"msg": "No juice_under_away was provided"}), 400
    if tt_home is None:
        return jsonify({"msg": "No tt_home was provided"}), 400
    if juice_over_home is None:
        return jsonify({"msg": "No juice_over_home was provided"}), 400
    if juice_under_home is None:
        return jsonify({"msg": "No juice_under_home was provided"}), 400
    if final_score_away is None:
        return jsonify({"msg": "No final_score_away was provided"}), 400
    if final_score_home is None:
        return jsonify({"msg": "No final_score_home was provided"}), 400
    if goal_away_1H is None:
        return jsonify({"msg": "No goal_away_1H was provided"}), 400
    if goal_home_1H is None:
        return jsonify({"msg": "No goal_home_1H was provided"}), 400
    if juice_goal_away_1H is None:
        return jsonify({"msg": "No juice_goal_away_1H was provided"}), 400
    if juice_goal_home_1H is None:
        return jsonify({"msg": "No juice_goal_home_1H was provided"}), 400
    if moneyLineAway_1H is None:
        return jsonify({"msg": "No moneyLineAway_1H was provided"}), 400
    if moneyLineHome_1H is None:
        return jsonify({"msg": "No moneyLineHome_1H was provided"}), 400
    if total_1H is None:
        return jsonify({"msg": "No total_1H was provided"}), 400
    if H1_juice_over is None:
        return jsonify({"msg": "No H1_juice_over was provided"}), 400
    if H1_juice_under is None:
        return jsonify({"msg": "No H1_juice_under was provided"}), 400
    if tt_away_1H is None:
        return jsonify({"msg": "No tt_away_1H was provided"}), 400
    if juice_over_away_1H is None:
        return jsonify({"msg": "No juice_over_away_1H was provided"}), 400
    if juice_under_away_1H is None:
        return jsonify({"msg": "No juice_under_away_1H was provided"}), 400
    if tt_home_1H is None:
        return jsonify({"msg": "No tt_home_1H was provided"}), 400
    if juice_over_home_1H is None:
        return jsonify({"msg": "No juice_over_home_1H was provided"}), 400
    if juice_under_home_1H is None:
        return jsonify({"msg": "No juice_under_home_1H was provided"}), 400

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

    # valida si estan vacios los ingresos
    if date is None:
        return jsonify({"msg": "No Date was provided"}), 400
    if hour is None:
        return jsonify({"msg": "No hour was provided"}), 400
    if status is None:
        return jsonify({"msg": "No status was provided"}), 400
    if away is None:
        return jsonify({"msg": "No away was provided"}), 400
    if home is None:
        return jsonify({"msg": "No home was provided"}), 400
    if goal_line_away is None:
        return jsonify({"msg": "No goal_line_away was provided"}), 400
    if goal_line_home is None:
        return jsonify({"msg": "No goal_line_home was provided"}), 400
    if juice_goal_away is None:
        return jsonify({"msg": "No juice_goal_away was provided"}), 400
    if juice_goal_home is None:
        return jsonify({"msg": "No juice_goal_home was provided"}), 400
    if moneyLineAway is None:
        return jsonify({"msg": "No moneyLineAway was provided"}), 400
    if moneyLineHome is None:
        return jsonify({"msg": "No moneyLineHome was provided"}), 400
    if total is None:
        return jsonify({"msg": "No total was provided"}), 400
    if juice_total_over is None:
        return jsonify({"msg": "No juice_total_over was provided"}), 400
    if juice_total_under is None:
        return jsonify({"msg": "No juice_total_under was provided"}), 400
    if tt_away is None:
        return jsonify({"msg": "No tt_away was provided"}), 400
    if juice_over_away is None:
        return jsonify({"msg": "No juice_over_away was provided"}), 400
    if juice_under_away is None:
        return jsonify({"msg": "No juice_under_away was provided"}), 400
    if tt_home is None:
        return jsonify({"msg": "No tt_home was provided"}), 400
    if juice_over_home is None:
        return jsonify({"msg": "No juice_over_home was provided"}), 400
    if juice_under_home is None:
        return jsonify({"msg": "No juice_under_home was provided"}), 400
    if final_score_away is None:
        return jsonify({"msg": "No final_score_away was provided"}), 400
    if final_score_home is None:
        return jsonify({"msg": "No final_score_home was provided"}), 400
    if goal_away_1H is None:
        return jsonify({"msg": "No goal_away_1H was provided"}), 400
    if goal_home_1H is None:
        return jsonify({"msg": "No goal_home_1H was provided"}), 400
    if juice_goal_away_1H is None:
        return jsonify({"msg": "No juice_goal_away_1H was provided"}), 400
    if juice_goal_home_1H is None:
        return jsonify({"msg": "No juice_goal_home_1H was provided"}), 400
    if moneyLineAway_1H is None:
        return jsonify({"msg": "No moneyLineAway_1H was provided"}), 400
    if moneyLineHome_1H is None:
        return jsonify({"msg": "No moneyLineHome_1H was provided"}), 400
    if total_1H is None:
        return jsonify({"msg": "No total_1H was provided"}), 400
    if H1_juice_over is None:
        return jsonify({"msg": "No H1_juice_over was provided"}), 400
    if H1_juice_under is None:
        return jsonify({"msg": "No H1_juice_under was provided"}), 400
    if tt_away_1H is None:
        return jsonify({"msg": "No tt_away_1H was provided"}), 400
    if juice_over_away_1H is None:
        return jsonify({"msg": "No juice_over_away_1H was provided"}), 400
    if juice_under_away_1H is None:
        return jsonify({"msg": "No juice_under_away_1H was provided"}), 400
    if tt_home_1H is None:
        return jsonify({"msg": "No tt_home_1H was provided"}), 400
    if juice_over_home_1H is None:
        return jsonify({"msg": "No juice_over_home_1H was provided"}), 400
    if juice_under_home_1H is None:
        return jsonify({"msg": "No juice_under_home_1H was provided"}), 400

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

    # valida si estan vacios los ingresos
    if date is None:
        return jsonify({"msg": "No Date was provided"}), 400
    if hour is None:
        return jsonify({"msg": "No hour was provided"}), 400
    if status is None:
        return jsonify({"msg": "No status was provided"}), 400
    if away is None:
        return jsonify({"msg": "No away was provided"}), 400
    if home is None:
        return jsonify({"msg": "No home was provided"}), 400
    if goal_line_away is None:
        return jsonify({"msg": "No goal_line_away was provided"}), 400
    if goal_line_home is None:
        return jsonify({"msg": "No goal_line_home was provided"}), 400
    if juice_goal_away is None:
        return jsonify({"msg": "No juice_goal_away was provided"}), 400
    if juice_goal_home is None:
        return jsonify({"msg": "No juice_goal_home was provided"}), 400
    if moneyLineAway is None:
        return jsonify({"msg": "No moneyLineAway was provided"}), 400
    if moneyLineHome is None:
        return jsonify({"msg": "No moneyLineHome was provided"}), 400
    if total is None:
        return jsonify({"msg": "No total was provided"}), 400
    if juice_total_over is None:
        return jsonify({"msg": "No juice_total_over was provided"}), 400
    if juice_total_under is None:
        return jsonify({"msg": "No juice_total_under was provided"}), 400
    if tt_away is None:
        return jsonify({"msg": "No tt_away was provided"}), 400
    if juice_over_away is None:
        return jsonify({"msg": "No juice_over_away was provided"}), 400
    if juice_under_away is None:
        return jsonify({"msg": "No juice_under_away was provided"}), 400
    if tt_home is None:
        return jsonify({"msg": "No tt_home was provided"}), 400
    if juice_over_home is None:
        return jsonify({"msg": "No juice_over_home was provided"}), 400
    if juice_under_home is None:
        return jsonify({"msg": "No juice_under_home was provided"}), 400
    if final_score_away is None:
        return jsonify({"msg": "No final_score_away was provided"}), 400
    if final_score_home is None:
        return jsonify({"msg": "No final_score_home was provided"}), 400
    if goal_away_1H is None:
        return jsonify({"msg": "No goal_away_1H was provided"}), 400
    if goal_home_1H is None:
        return jsonify({"msg": "No goal_home_1H was provided"}), 400
    if juice_goal_away_1H is None:
        return jsonify({"msg": "No juice_goal_away_1H was provided"}), 400
    if juice_goal_home_1H is None:
        return jsonify({"msg": "No juice_goal_home_1H was provided"}), 400
    if moneyLineAway_1H is None:
        return jsonify({"msg": "No moneyLineAway_1H was provided"}), 400
    if moneyLineHome_1H is None:
        return jsonify({"msg": "No moneyLineHome_1H was provided"}), 400
    if total_1H is None:
        return jsonify({"msg": "No total_1H was provided"}), 400
    if H1_juice_over is None:
        return jsonify({"msg": "No H1_juice_over was provided"}), 400
    if H1_juice_under is None:
        return jsonify({"msg": "No H1_juice_under was provided"}), 400
    if tt_away_1H is None:
        return jsonify({"msg": "No tt_away_1H was provided"}), 400
    if juice_over_away_1H is None:
        return jsonify({"msg": "No juice_over_away_1H was provided"}), 400
    if juice_under_away_1H is None:
        return jsonify({"msg": "No juice_under_away_1H was provided"}), 400
    if tt_home_1H is None:
        return jsonify({"msg": "No tt_home_1H was provided"}), 400
    if juice_over_home_1H is None:
        return jsonify({"msg": "No juice_over_home_1H was provided"}), 400
    if juice_under_home_1H is None:
        return jsonify({"msg": "No juice_under_home_1H was provided"}), 400

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

    # valida si estan vacios los ingresos
    if date is None:
        return jsonify({"msg": "No Date was provided"}), 400
    if hour is None:
        return jsonify({"msg": "No hour was provided"}), 400
    if status is None:
        return jsonify({"msg": "No status was provided"}), 400
    if away is None:
        return jsonify({"msg": "No away was provided"}), 400
    if home is None:
        return jsonify({"msg": "No home was provided"}), 400
    if goal_line_away is None:
        return jsonify({"msg": "No goal_line_away was provided"}), 400
    if goal_line_home is None:
        return jsonify({"msg": "No goal_line_home was provided"}), 400
    if juice_goal_away is None:
        return jsonify({"msg": "No juice_goal_away was provided"}), 400
    if juice_goal_home is None:
        return jsonify({"msg": "No juice_goal_home was provided"}), 400
    if moneyLineAway is None:
        return jsonify({"msg": "No moneyLineAway was provided"}), 400
    if moneyLineHome is None:
        return jsonify({"msg": "No moneyLineHome was provided"}), 400
    if total is None:
        return jsonify({"msg": "No total was provided"}), 400
    if juice_total_over is None:
        return jsonify({"msg": "No juice_total_over was provided"}), 400
    if juice_total_under is None:
        return jsonify({"msg": "No juice_total_under was provided"}), 400
    if tt_away is None:
        return jsonify({"msg": "No tt_away was provided"}), 400
    if juice_over_away is None:
        return jsonify({"msg": "No juice_over_away was provided"}), 400
    if juice_under_away is None:
        return jsonify({"msg": "No juice_under_away was provided"}), 400
    if tt_home is None:
        return jsonify({"msg": "No tt_home was provided"}), 400
    if juice_over_home is None:
        return jsonify({"msg": "No juice_over_home was provided"}), 400
    if juice_under_home is None:
        return jsonify({"msg": "No juice_under_home was provided"}), 400
    if final_score_away is None:
        return jsonify({"msg": "No final_score_away was provided"}), 400
    if final_score_home is None:
        return jsonify({"msg": "No final_score_home was provided"}), 400
    if goal_away_1H is None:
        return jsonify({"msg": "No goal_away_1H was provided"}), 400
    if goal_home_1H is None:
        return jsonify({"msg": "No goal_home_1H was provided"}), 400
    if juice_goal_away_1H is None:
        return jsonify({"msg": "No juice_goal_away_1H was provided"}), 400
    if juice_goal_home_1H is None:
        return jsonify({"msg": "No juice_goal_home_1H was provided"}), 400
    if moneyLineAway_1H is None:
        return jsonify({"msg": "No moneyLineAway_1H was provided"}), 400
    if moneyLineHome_1H is None:
        return jsonify({"msg": "No moneyLineHome_1H was provided"}), 400
    if total_1H is None:
        return jsonify({"msg": "No total_1H was provided"}), 400
    if H1_juice_over is None:
        return jsonify({"msg": "No H1_juice_over was provided"}), 400
    if H1_juice_under is None:
        return jsonify({"msg": "No H1_juice_under was provided"}), 400
    if tt_away_1H is None:
        return jsonify({"msg": "No tt_away_1H was provided"}), 400
    if juice_over_away_1H is None:
        return jsonify({"msg": "No juice_over_away_1H was provided"}), 400
    if juice_under_away_1H is None:
        return jsonify({"msg": "No juice_under_away_1H was provided"}), 400
    if tt_home_1H is None:
        return jsonify({"msg": "No tt_home_1H was provided"}), 400
    if juice_over_home_1H is None:
        return jsonify({"msg": "No juice_over_home_1H was provided"}), 400
    if juice_under_home_1H is None:
        return jsonify({"msg": "No juice_under_home_1H was provided"}), 400

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

    # valida si estan vacios los ingresos
    if date is None:
        return jsonify({"msg": "No Date was provided"}), 400
    if hour is None:
        return jsonify({"msg": "No hour was provided"}), 400
    if status is None:
        return jsonify({"msg": "No status was provided"}), 400
    if away is None:
        return jsonify({"msg": "No away was provided"}), 400
    if home is None:
        return jsonify({"msg": "No home was provided"}), 400
    if goal_line_away is None:
        return jsonify({"msg": "No goal_line_away was provided"}), 400
    if goal_line_home is None:
        return jsonify({"msg": "No goal_line_home was provided"}), 400
    if juice_goal_away is None:
        return jsonify({"msg": "No juice_goal_away was provided"}), 400
    if juice_goal_home is None:
        return jsonify({"msg": "No juice_goal_home was provided"}), 400
    if moneyLineAway is None:
        return jsonify({"msg": "No moneyLineAway was provided"}), 400
    if moneyLineHome is None:
        return jsonify({"msg": "No moneyLineHome was provided"}), 400
    if total is None:
        return jsonify({"msg": "No total was provided"}), 400
    if juice_total_over is None:
        return jsonify({"msg": "No juice_total_over was provided"}), 400
    if juice_total_under is None:
        return jsonify({"msg": "No juice_total_under was provided"}), 400
    if tt_away is None:
        return jsonify({"msg": "No tt_away was provided"}), 400
    if juice_over_away is None:
        return jsonify({"msg": "No juice_over_away was provided"}), 400
    if juice_under_away is None:
        return jsonify({"msg": "No juice_under_away was provided"}), 400
    if tt_home is None:
        return jsonify({"msg": "No tt_home was provided"}), 400
    if juice_over_home is None:
        return jsonify({"msg": "No juice_over_home was provided"}), 400
    if juice_under_home is None:
        return jsonify({"msg": "No juice_under_home was provided"}), 400
    if final_score_away is None:
        return jsonify({"msg": "No final_score_away was provided"}), 400
    if final_score_home is None:
        return jsonify({"msg": "No final_score_home was provided"}), 400
    if goal_away_1H is None:
        return jsonify({"msg": "No goal_away_1H was provided"}), 400
    if goal_home_1H is None:
        return jsonify({"msg": "No goal_home_1H was provided"}), 400
    if juice_goal_away_1H is None:
        return jsonify({"msg": "No juice_goal_away_1H was provided"}), 400
    if juice_goal_home_1H is None:
        return jsonify({"msg": "No juice_goal_home_1H was provided"}), 400
    if moneyLineAway_1H is None:
        return jsonify({"msg": "No moneyLineAway_1H was provided"}), 400
    if moneyLineHome_1H is None:
        return jsonify({"msg": "No moneyLineHome_1H was provided"}), 400
    if total_1H is None:
        return jsonify({"msg": "No total_1H was provided"}), 400
    if H1_juice_over is None:
        return jsonify({"msg": "No H1_juice_over was provided"}), 400
    if H1_juice_under is None:
        return jsonify({"msg": "No H1_juice_under was provided"}), 400
    if tt_away_1H is None:
        return jsonify({"msg": "No tt_away_1H was provided"}), 400
    if juice_over_away_1H is None:
        return jsonify({"msg": "No juice_over_away_1H was provided"}), 400
    if juice_under_away_1H is None:
        return jsonify({"msg": "No juice_under_away_1H was provided"}), 400
    if tt_home_1H is None:
        return jsonify({"msg": "No tt_home_1H was provided"}), 400
    if juice_over_home_1H is None:
        return jsonify({"msg": "No juice_over_home_1H was provided"}), 400
    if juice_under_home_1H is None:
        return jsonify({"msg": "No juice_under_home_1H was provided"}), 400

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

    # valida si estan vacios los ingresos
    if date is None:
        return jsonify({"msg": "No Date was provided"}), 400
    if hour is None:
        return jsonify({"msg": "No hour was provided"}), 400
    if status is None:
        return jsonify({"msg": "No status was provided"}), 400
    if away is None:
        return jsonify({"msg": "No away was provided"}), 400
    if home is None:
        return jsonify({"msg": "No home was provided"}), 400
    if goal_line_away is None:
        return jsonify({"msg": "No goal_line_away was provided"}), 400
    if goal_line_home is None:
        return jsonify({"msg": "No goal_line_home was provided"}), 400
    if juice_goal_away is None:
        return jsonify({"msg": "No juice_goal_away was provided"}), 400
    if juice_goal_home is None:
        return jsonify({"msg": "No juice_goal_home was provided"}), 400
    if moneyLineAway is None:
        return jsonify({"msg": "No moneyLineAway was provided"}), 400
    if moneyLineHome is None:
        return jsonify({"msg": "No moneyLineHome was provided"}), 400
    if total is None:
        return jsonify({"msg": "No total was provided"}), 400
    if juice_total_over is None:
        return jsonify({"msg": "No juice_total_over was provided"}), 400
    if juice_total_under is None:
        return jsonify({"msg": "No juice_total_under was provided"}), 400
    if tt_away is None:
        return jsonify({"msg": "No tt_away was provided"}), 400
    if juice_over_away is None:
        return jsonify({"msg": "No juice_over_away was provided"}), 400
    if juice_under_away is None:
        return jsonify({"msg": "No juice_under_away was provided"}), 400
    if tt_home is None:
        return jsonify({"msg": "No tt_home was provided"}), 400
    if juice_over_home is None:
        return jsonify({"msg": "No juice_over_home was provided"}), 400
    if juice_under_home is None:
        return jsonify({"msg": "No juice_under_home was provided"}), 400
    if final_score_away is None:
        return jsonify({"msg": "No final_score_away was provided"}), 400
    if final_score_home is None:
        return jsonify({"msg": "No final_score_home was provided"}), 400
    if goal_away_1H is None:
        return jsonify({"msg": "No goal_away_1H was provided"}), 400
    if goal_home_1H is None:
        return jsonify({"msg": "No goal_home_1H was provided"}), 400
    if juice_goal_away_1H is None:
        return jsonify({"msg": "No juice_goal_away_1H was provided"}), 400
    if juice_goal_home_1H is None:
        return jsonify({"msg": "No juice_goal_home_1H was provided"}), 400
    if moneyLineAway_1H is None:
        return jsonify({"msg": "No moneyLineAway_1H was provided"}), 400
    if moneyLineHome_1H is None:
        return jsonify({"msg": "No moneyLineHome_1H was provided"}), 400
    if total_1H is None:
        return jsonify({"msg": "No total_1H was provided"}), 400
    if H1_juice_over is None:
        return jsonify({"msg": "No H1_juice_over was provided"}), 400
    if H1_juice_under is None:
        return jsonify({"msg": "No H1_juice_under was provided"}), 400
    if tt_away_1H is None:
        return jsonify({"msg": "No tt_away_1H was provided"}), 400
    if juice_over_away_1H is None:
        return jsonify({"msg": "No juice_over_away_1H was provided"}), 400
    if juice_under_away_1H is None:
        return jsonify({"msg": "No juice_under_away_1H was provided"}), 400
    if tt_home_1H is None:
        return jsonify({"msg": "No tt_home_1H was provided"}), 400
    if juice_over_home_1H is None:
        return jsonify({"msg": "No juice_over_home_1H was provided"}), 400
    if juice_under_home_1H is None:
        return jsonify({"msg": "No juice_under_home_1H was provided"}), 400

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

    # valida si estan vacios los ingresos
    if date is None:
        return jsonify({"msg": "No Date was provided"}), 400
    if hour is None:
        return jsonify({"msg": "No hour was provided"}), 400
    if status is None:
        return jsonify({"msg": "No status was provided"}), 400
    if away is None:
        return jsonify({"msg": "No away was provided"}), 400
    if home is None:
        return jsonify({"msg": "No home was provided"}), 400
    if goal_line_away is None:
        return jsonify({"msg": "No goal_line_away was provided"}), 400
    if goal_line_home is None:
        return jsonify({"msg": "No goal_line_home was provided"}), 400
    if juice_goal_away is None:
        return jsonify({"msg": "No juice_goal_away was provided"}), 400
    if juice_goal_home is None:
        return jsonify({"msg": "No juice_goal_home was provided"}), 400
    if moneyLineAway is None:
        return jsonify({"msg": "No moneyLineAway was provided"}), 400
    if moneyLineHome is None:
        return jsonify({"msg": "No moneyLineHome was provided"}), 400
    if total is None:
        return jsonify({"msg": "No total was provided"}), 400
    if juice_total_over is None:
        return jsonify({"msg": "No juice_total_over was provided"}), 400
    if juice_total_under is None:
        return jsonify({"msg": "No juice_total_under was provided"}), 400
    if tt_away is None:
        return jsonify({"msg": "No tt_away was provided"}), 400
    if juice_over_away is None:
        return jsonify({"msg": "No juice_over_away was provided"}), 400
    if juice_under_away is None:
        return jsonify({"msg": "No juice_under_away was provided"}), 400
    if tt_home is None:
        return jsonify({"msg": "No tt_home was provided"}), 400
    if juice_over_home is None:
        return jsonify({"msg": "No juice_over_home was provided"}), 400
    if juice_under_home is None:
        return jsonify({"msg": "No juice_under_home was provided"}), 400
    if final_score_away is None:
        return jsonify({"msg": "No final_score_away was provided"}), 400
    if final_score_home is None:
        return jsonify({"msg": "No final_score_home was provided"}), 400
    if goal_away_1H is None:
        return jsonify({"msg": "No goal_away_1H was provided"}), 400
    if goal_home_1H is None:
        return jsonify({"msg": "No goal_home_1H was provided"}), 400
    if juice_goal_away_1H is None:
        return jsonify({"msg": "No juice_goal_away_1H was provided"}), 400
    if juice_goal_home_1H is None:
        return jsonify({"msg": "No juice_goal_home_1H was provided"}), 400
    if moneyLineAway_1H is None:
        return jsonify({"msg": "No moneyLineAway_1H was provided"}), 400
    if moneyLineHome_1H is None:
        return jsonify({"msg": "No moneyLineHome_1H was provided"}), 400
    if total_1H is None:
        return jsonify({"msg": "No total_1H was provided"}), 400
    if H1_juice_over is None:
        return jsonify({"msg": "No H1_juice_over was provided"}), 400
    if H1_juice_under is None:
        return jsonify({"msg": "No H1_juice_under was provided"}), 400
    if tt_away_1H is None:
        return jsonify({"msg": "No tt_away_1H was provided"}), 400
    if juice_over_away_1H is None:
        return jsonify({"msg": "No juice_over_away_1H was provided"}), 400
    if juice_under_away_1H is None:
        return jsonify({"msg": "No juice_under_away_1H was provided"}), 400
    if tt_home_1H is None:
        return jsonify({"msg": "No tt_home_1H was provided"}), 400
    if juice_over_home_1H is None:
        return jsonify({"msg": "No juice_over_home_1H was provided"}), 400
    if juice_under_home_1H is None:
        return jsonify({"msg": "No juice_under_home_1H was provided"}), 400

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

    # valida si estan vacios los ingresos
    if date is None:
        return jsonify({"msg": "No Date was provided"}), 400
    if hour is None:
        return jsonify({"msg": "No hour was provided"}), 400
    if status is None:
        return jsonify({"msg": "No status was provided"}), 400
    if away is None:
        return jsonify({"msg": "No away was provided"}), 400
    if home is None:
        return jsonify({"msg": "No home was provided"}), 400
    if goal_line_away is None:
        return jsonify({"msg": "No goal_line_away was provided"}), 400
    if goal_line_home is None:
        return jsonify({"msg": "No goal_line_home was provided"}), 400
    if juice_goal_away is None:
        return jsonify({"msg": "No juice_goal_away was provided"}), 400
    if juice_goal_home is None:
        return jsonify({"msg": "No juice_goal_home was provided"}), 400
    if moneyLineAway is None:
        return jsonify({"msg": "No moneyLineAway was provided"}), 400
    if moneyLineHome is None:
        return jsonify({"msg": "No moneyLineHome was provided"}), 400
    if total is None:
        return jsonify({"msg": "No total was provided"}), 400
    if juice_total_over is None:
        return jsonify({"msg": "No juice_total_over was provided"}), 400
    if juice_total_under is None:
        return jsonify({"msg": "No juice_total_under was provided"}), 400
    if tt_away is None:
        return jsonify({"msg": "No tt_away was provided"}), 400
    if juice_over_away is None:
        return jsonify({"msg": "No juice_over_away was provided"}), 400
    if juice_under_away is None:
        return jsonify({"msg": "No juice_under_away was provided"}), 400
    if tt_home is None:
        return jsonify({"msg": "No tt_home was provided"}), 400
    if juice_over_home is None:
        return jsonify({"msg": "No juice_over_home was provided"}), 400
    if juice_under_home is None:
        return jsonify({"msg": "No juice_under_home was provided"}), 400
    if final_score_away is None:
        return jsonify({"msg": "No final_score_away was provided"}), 400
    if final_score_home is None:
        return jsonify({"msg": "No final_score_home was provided"}), 400
    if goal_away_1H is None:
        return jsonify({"msg": "No goal_away_1H was provided"}), 400
    if goal_home_1H is None:
        return jsonify({"msg": "No goal_home_1H was provided"}), 400
    if juice_goal_away_1H is None:
        return jsonify({"msg": "No juice_goal_away_1H was provided"}), 400
    if juice_goal_home_1H is None:
        return jsonify({"msg": "No juice_goal_home_1H was provided"}), 400
    if moneyLineAway_1H is None:
        return jsonify({"msg": "No moneyLineAway_1H was provided"}), 400
    if moneyLineHome_1H is None:
        return jsonify({"msg": "No moneyLineHome_1H was provided"}), 400
    if total_1H is None:
        return jsonify({"msg": "No total_1H was provided"}), 400
    if H1_juice_over is None:
        return jsonify({"msg": "No H1_juice_over was provided"}), 400
    if H1_juice_under is None:
        return jsonify({"msg": "No H1_juice_under was provided"}), 400
    if tt_away_1H is None:
        return jsonify({"msg": "No tt_away_1H was provided"}), 400
    if juice_over_away_1H is None:
        return jsonify({"msg": "No juice_over_away_1H was provided"}), 400
    if juice_under_away_1H is None:
        return jsonify({"msg": "No juice_under_away_1H was provided"}), 400
    if tt_home_1H is None:
        return jsonify({"msg": "No tt_home_1H was provided"}), 400
    if juice_over_home_1H is None:
        return jsonify({"msg": "No juice_over_home_1H was provided"}), 400
    if juice_under_home_1H is None:
        return jsonify({"msg": "No juice_under_home_1H was provided"}), 400

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

    # valida si estan vacios los ingresos
    if date is None:
        return jsonify({"msg": "No Date was provided"}), 400
    if hour is None:
        return jsonify({"msg": "No hour was provided"}), 400
    if status is None:
        return jsonify({"msg": "No status was provided"}), 400
    if away is None:
        return jsonify({"msg": "No away was provided"}), 400
    if home is None:
        return jsonify({"msg": "No home was provided"}), 400
    if goal_line_away is None:
        return jsonify({"msg": "No goal_line_away was provided"}), 400
    if goal_line_home is None:
        return jsonify({"msg": "No goal_line_home was provided"}), 400
    if juice_goal_away is None:
        return jsonify({"msg": "No juice_goal_away was provided"}), 400
    if juice_goal_home is None:
        return jsonify({"msg": "No juice_goal_home was provided"}), 400
    if moneyLineAway is None:
        return jsonify({"msg": "No moneyLineAway was provided"}), 400
    if moneyLineHome is None:
        return jsonify({"msg": "No moneyLineHome was provided"}), 400
    if total is None:
        return jsonify({"msg": "No total was provided"}), 400
    if juice_total_over is None:
        return jsonify({"msg": "No juice_total_over was provided"}), 400
    if juice_total_under is None:
        return jsonify({"msg": "No juice_total_under was provided"}), 400
    if tt_away is None:
        return jsonify({"msg": "No tt_away was provided"}), 400
    if juice_over_away is None:
        return jsonify({"msg": "No juice_over_away was provided"}), 400
    if juice_under_away is None:
        return jsonify({"msg": "No juice_under_away was provided"}), 400
    if tt_home is None:
        return jsonify({"msg": "No tt_home was provided"}), 400
    if juice_over_home is None:
        return jsonify({"msg": "No juice_over_home was provided"}), 400
    if juice_under_home is None:
        return jsonify({"msg": "No juice_under_home was provided"}), 400
    if final_score_away is None:
        return jsonify({"msg": "No final_score_away was provided"}), 400
    if final_score_home is None:
        return jsonify({"msg": "No final_score_home was provided"}), 400
    if goal_away_1H is None:
        return jsonify({"msg": "No goal_away_1H was provided"}), 400
    if goal_home_1H is None:
        return jsonify({"msg": "No goal_home_1H was provided"}), 400
    if juice_goal_away_1H is None:
        return jsonify({"msg": "No juice_goal_away_1H was provided"}), 400
    if juice_goal_home_1H is None:
        return jsonify({"msg": "No juice_goal_home_1H was provided"}), 400
    if moneyLineAway_1H is None:
        return jsonify({"msg": "No moneyLineAway_1H was provided"}), 400
    if moneyLineHome_1H is None:
        return jsonify({"msg": "No moneyLineHome_1H was provided"}), 400
    if total_1H is None:
        return jsonify({"msg": "No total_1H was provided"}), 400
    if H1_juice_over is None:
        return jsonify({"msg": "No H1_juice_over was provided"}), 400
    if H1_juice_under is None:
        return jsonify({"msg": "No H1_juice_under was provided"}), 400
    if tt_away_1H is None:
        return jsonify({"msg": "No tt_away_1H was provided"}), 400
    if juice_over_away_1H is None:
        return jsonify({"msg": "No juice_over_away_1H was provided"}), 400
    if juice_under_away_1H is None:
        return jsonify({"msg": "No juice_under_away_1H was provided"}), 400
    if tt_home_1H is None:
        return jsonify({"msg": "No tt_home_1H was provided"}), 400
    if juice_over_home_1H is None:
        return jsonify({"msg": "No juice_over_home_1H was provided"}), 400
    if juice_under_home_1H is None:
        return jsonify({"msg": "No juice_under_home_1H was provided"}), 400

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

    # valida si estan vacios los ingresos
    if date is None:
        return jsonify({"msg": "No Date was provided"}), 400
    if hour is None:
        return jsonify({"msg": "No hour was provided"}), 400
    if status is None:
        return jsonify({"msg": "No status was provided"}), 400
    if away is None:
        return jsonify({"msg": "No away was provided"}), 400
    if home is None:
        return jsonify({"msg": "No home was provided"}), 400
    if goal_line_away is None:
        return jsonify({"msg": "No goal_line_away was provided"}), 400
    if goal_line_home is None:
        return jsonify({"msg": "No goal_line_home was provided"}), 400
    if juice_goal_away is None:
        return jsonify({"msg": "No juice_goal_away was provided"}), 400
    if juice_goal_home is None:
        return jsonify({"msg": "No juice_goal_home was provided"}), 400
    if moneyLineAway is None:
        return jsonify({"msg": "No moneyLineAway was provided"}), 400
    if moneyLineHome is None:
        return jsonify({"msg": "No moneyLineHome was provided"}), 400
    if total is None:
        return jsonify({"msg": "No total was provided"}), 400
    if juice_total_over is None:
        return jsonify({"msg": "No juice_total_over was provided"}), 400
    if juice_total_under is None:
        return jsonify({"msg": "No juice_total_under was provided"}), 400
    if tt_away is None:
        return jsonify({"msg": "No tt_away was provided"}), 400
    if juice_over_away is None:
        return jsonify({"msg": "No juice_over_away was provided"}), 400
    if juice_under_away is None:
        return jsonify({"msg": "No juice_under_away was provided"}), 400
    if tt_home is None:
        return jsonify({"msg": "No tt_home was provided"}), 400
    if juice_over_home is None:
        return jsonify({"msg": "No juice_over_home was provided"}), 400
    if juice_under_home is None:
        return jsonify({"msg": "No juice_under_home was provided"}), 400
    if final_score_away is None:
        return jsonify({"msg": "No final_score_away was provided"}), 400
    if final_score_home is None:
        return jsonify({"msg": "No final_score_home was provided"}), 400
    if goal_away_1H is None:
        return jsonify({"msg": "No goal_away_1H was provided"}), 400
    if goal_home_1H is None:
        return jsonify({"msg": "No goal_home_1H was provided"}), 400
    if juice_goal_away_1H is None:
        return jsonify({"msg": "No juice_goal_away_1H was provided"}), 400
    if juice_goal_home_1H is None:
        return jsonify({"msg": "No juice_goal_home_1H was provided"}), 400
    if moneyLineAway_1H is None:
        return jsonify({"msg": "No moneyLineAway_1H was provided"}), 400
    if moneyLineHome_1H is None:
        return jsonify({"msg": "No moneyLineHome_1H was provided"}), 400
    if total_1H is None:
        return jsonify({"msg": "No total_1H was provided"}), 400
    if H1_juice_over is None:
        return jsonify({"msg": "No H1_juice_over was provided"}), 400
    if H1_juice_under is None:
        return jsonify({"msg": "No H1_juice_under was provided"}), 400
    if tt_away_1H is None:
        return jsonify({"msg": "No tt_away_1H was provided"}), 400
    if juice_over_away_1H is None:
        return jsonify({"msg": "No juice_over_away_1H was provided"}), 400
    if juice_under_away_1H is None:
        return jsonify({"msg": "No juice_under_away_1H was provided"}), 400
    if tt_home_1H is None:
        return jsonify({"msg": "No tt_home_1H was provided"}), 400
    if juice_over_home_1H is None:
        return jsonify({"msg": "No juice_over_home_1H was provided"}), 400
    if juice_under_home_1H is None:
        return jsonify({"msg": "No juice_under_home_1H was provided"}), 400

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

    # valida si estan vacios los ingresos
    if date is None:
        return jsonify({"msg": "No Date was provided"}), 400
    if hour is None:
        return jsonify({"msg": "No hour was provided"}), 400
    if status is None:
        return jsonify({"msg": "No status was provided"}), 400
    if away is None:
        return jsonify({"msg": "No away was provided"}), 400
    if home is None:
        return jsonify({"msg": "No home was provided"}), 400
    if goal_line_away is None:
        return jsonify({"msg": "No goal_line_away was provided"}), 400
    if goal_line_home is None:
        return jsonify({"msg": "No goal_line_home was provided"}), 400
    if juice_goal_away is None:
        return jsonify({"msg": "No juice_goal_away was provided"}), 400
    if juice_goal_home is None:
        return jsonify({"msg": "No juice_goal_home was provided"}), 400
    if moneyLineAway is None:
        return jsonify({"msg": "No moneyLineAway was provided"}), 400
    if moneyLineHome is None:
        return jsonify({"msg": "No moneyLineHome was provided"}), 400
    if total is None:
        return jsonify({"msg": "No total was provided"}), 400
    if juice_total_over is None:
        return jsonify({"msg": "No juice_total_over was provided"}), 400
    if juice_total_under is None:
        return jsonify({"msg": "No juice_total_under was provided"}), 400
    if tt_away is None:
        return jsonify({"msg": "No tt_away was provided"}), 400
    if juice_over_away is None:
        return jsonify({"msg": "No juice_over_away was provided"}), 400
    if juice_under_away is None:
        return jsonify({"msg": "No juice_under_away was provided"}), 400
    if tt_home is None:
        return jsonify({"msg": "No tt_home was provided"}), 400
    if juice_over_home is None:
        return jsonify({"msg": "No juice_over_home was provided"}), 400
    if juice_under_home is None:
        return jsonify({"msg": "No juice_under_home was provided"}), 400
    if final_score_away is None:
        return jsonify({"msg": "No final_score_away was provided"}), 400
    if final_score_home is None:
        return jsonify({"msg": "No final_score_home was provided"}), 400
    if goal_away_1H is None:
        return jsonify({"msg": "No goal_away_1H was provided"}), 400
    if goal_home_1H is None:
        return jsonify({"msg": "No goal_home_1H was provided"}), 400
    if juice_goal_away_1H is None:
        return jsonify({"msg": "No juice_goal_away_1H was provided"}), 400
    if juice_goal_home_1H is None:
        return jsonify({"msg": "No juice_goal_home_1H was provided"}), 400
    if moneyLineAway_1H is None:
        return jsonify({"msg": "No moneyLineAway_1H was provided"}), 400
    if moneyLineHome_1H is None:
        return jsonify({"msg": "No moneyLineHome_1H was provided"}), 400
    if total_1H is None:
        return jsonify({"msg": "No total_1H was provided"}), 400
    if H1_juice_over is None:
        return jsonify({"msg": "No H1_juice_over was provided"}), 400
    if H1_juice_under is None:
        return jsonify({"msg": "No H1_juice_under was provided"}), 400
    if tt_away_1H is None:
        return jsonify({"msg": "No tt_away_1H was provided"}), 400
    if juice_over_away_1H is None:
        return jsonify({"msg": "No juice_over_away_1H was provided"}), 400
    if juice_under_away_1H is None:
        return jsonify({"msg": "No juice_under_away_1H was provided"}), 400
    if tt_home_1H is None:
        return jsonify({"msg": "No tt_home_1H was provided"}), 400
    if juice_over_home_1H is None:
        return jsonify({"msg": "No juice_over_home_1H was provided"}), 400
    if juice_under_home_1H is None:
        return jsonify({"msg": "No juice_under_home_1H was provided"}), 400

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

    # valida si estan vacios los ingresos
    if season is None:
        return jsonify({"msg": "No season was provided"}), 400
    if team is None:
        return jsonify({"msg": "No team was provided"}), 400
    if pts is None:
        return jsonify({"msg": "No pts was provided"}), 400
    if fmg is None:
        return jsonify({"msg": "No fmg was provided"}), 400
    if fga is None:
        return jsonify({"msg": "No fga was provided"}), 400
    if fg is None:
        return jsonify({"msg": "No fg was provided"}), 400
    if fg_AVG is None:
        return jsonify({"msg": "No fg_AVG was provided"}), 400
    if three_pm is None:
        return jsonify({"msg": "No three_pm was provided"}), 400
    if three_pa is None:
        return jsonify({"msg": "No three_pa was provided"}), 400
    if three_p_AVG is None:
        return jsonify({"msg": "No three_p_AVG was provided"}), 400
    if ftm is None:
        return jsonify({"msg": "No ftm was provided"}), 400
    if fta is None:
        return jsonify({"msg": "No fta was provided"}), 400
    if ft_AVG is None:
        return jsonify({"msg": "No ft_AVG was provided"}), 400
    if Or is None:
        return jsonify({"msg": "No Or was provided"}), 400
    if dr is None:
        return jsonify({"msg": "No dr was provided"}), 400
    if reb is None:
        return jsonify({"msg": "No reb was provided"}), 400
    if ast is None:
        return jsonify({"msg": "No ast was provided"}), 400
    if stl is None:
        return jsonify({"msg": "No stl was provided"}), 400
    if blk is None:
        return jsonify({"msg": "No blk was provided"}), 400
    if to is None:
        return jsonify({"msg": "No to was provided"}), 400
    if pf is None:
        return jsonify({"msg": "No pf was provided"}), 400

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

    # valida si estan vacios los ingresos
    if name is None:
        return jsonify({"msg": "No name was provided"}), 400
    if height is None:
        return jsonify({"msg": "No height was provided"}), 400
    if weight is None:
        return jsonify({"msg": "No weight was provided"}), 400
    if birth is None:
        return jsonify({"msg": "No birth was provided"}), 400
    if college is None:
        return jsonify({"msg": "No college was provided"}), 400
    if season is None:
        return jsonify({"msg": "No season was provided"}), 400
    if team is None:
        return jsonify({"msg": "No team was provided"}), 400
    if dorsal is None:
        return jsonify({"msg": "No dorsal was provided"}), 400
    if minutes is None:
        return jsonify({"msg": "No minutes was provided"}), 400
    if position is None:
        return jsonify({"msg": "No position was provided"}), 400
    if gp is None:
        return jsonify({"msg": "No gp was provided"}), 400
    if gs is None:
        return jsonify({"msg": "No gs was provided"}), 400
    if fg is None:
        return jsonify({"msg": "No fg was provided"}), 400
    if fg_AVG is None:
        return jsonify({"msg": "No fg_AVG was provided"}), 400
    if three_pt is None:
        return jsonify({"msg": "No three_pt was provided"}), 400
    if three_pt_AVG is None:
        return jsonify({"msg": "No three_pt_AVG was provided"}), 400
    if ft is None:
        return jsonify({"msg": "No ft was provided"}), 400
    if ft_AVG is None:
        return jsonify({"msg": "No ft_AVG was provided"}), 400
    if Or is None:
        return jsonify({"msg": "No Or was provided"}), 400
    if dr is None:
        return jsonify({"msg": "No dr was provided"}), 400
    if reb is None:
        return jsonify({"msg": "No reb was provided"}), 400
    if ast is None:
        return jsonify({"msg": "No ast was provided"}), 400
    if stl is None:
        return jsonify({"msg": "No stl was provided"}), 400
    if blk is None:
        return jsonify({"msg": "No blk was provided"}), 400
    if to is None:
        return jsonify({"msg": "No to was provided"}), 400
    if pf is None:
        return jsonify({"msg": "No pf was provided"}), 400
    if pts is None:
        return jsonify({"msg": "No pts was provided"}), 400
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

    # valida si estan vacios los ingresos
    if season is None:
        return jsonify({"msg": "No season was provided"}), 400
    if team is None:
        return jsonify({"msg": "No team was provided"}), 400
    if conference is None:
        return jsonify({"msg": "No conference was provided"}), 400
    if division is None:
        return jsonify({"msg": "No division was provided"}), 400
    if w is None:
        return jsonify({"msg": "No w was provided"}), 400
    if l is None:
        return jsonify({"msg": "No l was provided"}), 400
    if Ga_a is None:
        return jsonify({"msg": "No Ga_a was provided"}), 400
    if otl is None:
        return jsonify({"msg": "No otl was provided"}), 400
    if sa is None:
        return jsonify({"msg": "No sa was provided"}), 400
    if ga is None:
        return jsonify({"msg": "No ga was provided"}), 400
    if s is None:
        return jsonify({"msg": "No s was provided"}), 400
    if sv_AVG is None:
        return jsonify({"msg": "No sv_AVG was provided"}), 400
    if so is None:
        return jsonify({"msg": "No so was provided"}), 400
    if so_sa is None:
        return jsonify({"msg": "No so_sa was provided"}), 400
    if sos is None:
        return jsonify({"msg": "No sos was provided"}), 400
    if sos_AVG is None:
        return jsonify({"msg": "No sos_AVG was provided"}), 400

    # busca team en BBDD
    stats_nhl_team = Stats_nhl_team.query.filter_by(team=team, conference=conference, division=division).first()
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

    # valida si estan vacios los ingresos
    if name is None:
        return jsonify({"msg": "No name was provided"}), 400
    if height is None:
        return jsonify({"msg": "No height was provided"}), 400
    if weight is None:
        return jsonify({"msg": "No weight was provided"}), 400
    if birth is None:
        return jsonify({"msg": "No birth was provided"}), 400
    if season is None:
        return jsonify({"msg": "No season was provided"}), 400
    if team is None:
        return jsonify({"msg": "No team was provided"}), 400
    if dorsal is None:
        return jsonify({"msg": "No dorsal was provided"}), 400
    if position is None:
        return jsonify({"msg": "No position was provided"}), 400
    if gp is None:
        return jsonify({"msg": "No gp was provided"}), 400
    if g is None:
        return jsonify({"msg": "No g was provided"}), 400
    if a is None:
        return jsonify({"msg": "No a was provided"}), 400
    if pts is None:
        return jsonify({"msg": "No pts was provided"}), 400
    if p_m_rating is None:
        return jsonify({"msg": "No p_m_rating was provided"}), 400
    if pim is None:
        return jsonify({"msg": "No pim was provided"}), 400
    if sog is None:
        return jsonify({"msg": "No sog was provided"}), 400
    if spct is None:
        return jsonify({"msg": "No spct was provided"}), 400
    if ppg is None:
        return jsonify({"msg": "No ppg was provided"}), 400
    if ppa is None:
        return jsonify({"msg": "No ppa was provided"}), 400
    if shg is None:
        return jsonify({"msg": "No shg was provided"}), 400
    if sha is None:
        return jsonify({"msg": "No sha was provided"}), 400
    if gwg is None:
        return jsonify({"msg": "No gwg was provided"}), 400
    if gtg is None:
        return jsonify({"msg": "No gtg was provided"}), 400
    if toi_g is None:
        return jsonify({"msg": "No toi_g was provided"}), 400
    if prod is None:
        return jsonify({"msg": "No prod was provided"}), 400
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

    # valida si estan vacios los ingresos
    if season is None:
        return jsonify({"msg": "No season was provided"}), 400
    if team is None:
        return jsonify({"msg": "No team was provided"}), 400
    if league is None:
        return jsonify({"msg": "No league was provided"}), 400
    if division is None:
        return jsonify({"msg": "No division was provided"}), 400
    if w is None:
        return jsonify({"msg": "No w was provided"}), 400
    if l is None:
        return jsonify({"msg": "No l was provided"}), 400
    if pct is None:
        return jsonify({"msg": "No pct was provided"}), 400
    if gb is None:
        return jsonify({"msg": "No gb was provided"}), 400
    if home is None:
        return jsonify({"msg": "No home was provided"}), 400
    if away is None:
        return jsonify({"msg": "No away was provided"}), 400
    if rs is None:
        return jsonify({"msg": "No rs was provided"}), 400
    if ra is None:
        return jsonify({"msg": "No ra was provided"}), 400
    if diff is None:
        return jsonify({"msg": "No diff was provided"}), 400
    if strk is None:
        return jsonify({"msg": "No strk was provided"}), 400
    if L10 is None:
        return jsonify({"msg": "No L10 was provided"}), 400
    if poff is None:
        return jsonify({"msg": "No poff was provided"}), 400

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

    # valida si estan vacios los ingresos
    if name is None:
        return jsonify({"msg": "No name was provided"}), 400
    if height is None:
        return jsonify({"msg": "No height was provided"}), 400
    if weight is None:
        return jsonify({"msg": "No weight was provided"}), 400
    if birth is None:
        return jsonify({"msg": "No birth was provided"}), 400
    if season is None:
        return jsonify({"msg": "No season was provided"}), 400
    if team is None:
        return jsonify({"msg": "No team was provided"}), 400
    if dorsal is None:
        return jsonify({"msg": "No dorsal was provided"}), 400
    if position is None:
        return jsonify({"msg": "No position was provided"}), 400
    if gp is None:
        return jsonify({"msg": "No gp was provided"}), 400
    if ab is None:
        return jsonify({"msg": "No ab was provided"}), 400
    if r is None:
        return jsonify({"msg": "No r was provided"}), 400
    if h is None:
        return jsonify({"msg": "No h was provided"}), 400
    if two_b is None:
        return jsonify({"msg": "No two_b was provided"}), 400
    if three_b is None:
        return jsonify({"msg": "No three_b was provided"}), 400
    if hb is None:
        return jsonify({"msg": "No hb was provided"}), 400
    if rbi is None:
        return jsonify({"msg": "No rbi was provided"}), 400
    if tb is None:
        return jsonify({"msg": "No tb was provided"}), 400
    if bb is None:
        return jsonify({"msg": "No bb was provided"}), 400
    if so is None:
        return jsonify({"msg": "No so was provided"}), 400
    if sb is None:
        return jsonify({"msg": "No sb was provided"}), 400
    if avg is None:
        return jsonify({"msg": "No avg was provided"}), 400
    if obp is None:
        return jsonify({"msg": "No obp was provided"}), 400
    if slg is None:
        return jsonify({"msg": "No slg was provided"}), 400
    if ops is None:
        return jsonify({"msg": "No ops was provided"}), 400
    if war is None:
        return jsonify({"msg": "No war was provided"}), 400
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

    # valida si estan vacios los ingresos
    if name is None:
        return jsonify({"msg": "No name was provided"}), 400
    if nickname is None:
        return jsonify({"msg": "No nickname was provided"}), 400
    if height is None:
        return jsonify({"msg": "No height was provided"}), 400
    if weight is None:
        return jsonify({"msg": "No weight was provided"}), 400
    if birth is None:
        return jsonify({"msg": "No birth was provided"}), 400
    if country is None:
        return jsonify({"msg": "No country was provided"}), 400
    if association is None:
        return jsonify({"msg": "No association was provided"}), 400
    if category is None:
        return jsonify({"msg": "No category was provided"}), 400
    if w is None:
        return jsonify({"msg": "No w was provided"}), 400
    if w_by is None:
        return jsonify({"msg": "No w_by was provided"}), 400
    if L is None:
        return jsonify({"msg": "No L was provided"}), 400
    if L_by is None:
        return jsonify({"msg": "No L_by was provided"}), 400
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

    # valida si estan vacios los ingresos
    if name is None:
        return jsonify({"msg": "No name was provided"}), 400
    if nickname is None:
        return jsonify({"msg": "No nickname was provided"}), 400
    if height is None:
        return jsonify({"msg": "No height was provided"}), 400
    if weight is None:
        return jsonify({"msg": "No weight was provided"}), 400
    if birth is None:
        return jsonify({"msg": "No birth was provided"}), 400
    if country is None:
        return jsonify({"msg": "No country was provided"}), 400
    if association is None:
        return jsonify({"msg": "No association was provided"}), 400
    if category is None:
        return jsonify({"msg": "No category was provided"}), 400
    if w is None:
        return jsonify({"msg": "No w was provided"}), 400
    if w_by is None:
        return jsonify({"msg": "No w_by was provided"}), 400
    if L is None:
        return jsonify({"msg": "No L was provided"}), 400
    if L_by is None:
        return jsonify({"msg": "No L_by was provided"}), 400
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
    missing_params = [key for key, value in body.items() if value is None]
    error = f'No {", ".join(missing_params)} was provided'

    # busca team en BBDD
    stats_nfl_team = Stats_nfl_team.query.filter_by(
        home=home, away=away, date=date).first()
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
            kickoffs_t=H1_juice_under,
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

    # valida si estan vacios los ingresos
    missing_params = [key for key, value in body.items() if value is None]
    error = f'No {", ".join(missing_params)} was provided'

    # busca team en BBDD
    stats_defensive_player_nfl = Stats_defensive_player_nfl.query.filter_by(
        name=name, dorsal=dorsal, birth=birth).first()
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
    missing_params = [key for key, value in body.items() if value is None]
    error = f'No {", ".join(missing_params)} was provided'

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

    # valida si estan vacios los ingresos
    missing_params = [key for key, value in body.items() if value is None]
    error = f'No {", ".join(missing_params)} was provided'

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

    # valida si estan vacios los ingresos
    missing_params = [key for key, value in body.items() if value is None]
    error = f'No {", ".join(missing_params)} was provided'

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

    # valida si estan vacios los ingresos
    missing_params = [key for key, value in body.items() if value is None]
    error = f'No {", ".join(missing_params)} was provided'

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

    if date is None:
        return jsonify({"msg": "No date was provided"}), 400

    # valida si estan vacios los ingresos
    # missing_params = [key for key, value in body.items() if value is None]
    # error = f'No {", ".join(missing_params)} was provided'

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

@app.route('/news/<id>', methods=['PUT'])
def createnewsEdit(id):
    news = News.query.filter_by(id=id).first()
    date = request.json.get("date", None)
    title = request.json.get("title", None)
    url_image = request.json.get("url_image", None)
    short_description = request.json.get("short_description", None)
    news_post = request.json.get("news_post", None)
    written = request.json.get("written", None)

    if date is None:
        return jsonify({"msg": "No date was provided"}), 400

    # busca team en BBDD
    # the team was not found on the database
    if id in news:
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
    else:
        return jsonify({"msg": "news already exists", "title": news.title}), 401
