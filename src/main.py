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
from models import db, Nfl, Mlb, Nba, Nhl, Boxeo, Mma, Nascar, Nascar_drivers, Match_Ups_Nacar, Golf, Golfer, News, Ncaa_Baseball,Ncaa_Football,Ncaa_Basketball,Champions_League,Confederations_Cup,W_C_Qualifying,CONCACAF,Europa_League,International_Friendlies,France_League,Bundesliga,International_Matches,Italia_Serie_A,Mx_Expansion,Mx_Apertura,Spain_Primera_Liga,USA_MLS,Brazil_Serie_A,Colombia_Primera_A
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
#----------------------------------------------------------------------------
@app.route("/mlb", methods=["GET"])
#   @limiter.limit("12 per hour")
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
@app.route("/news", methods=["GET"])
def news():
    if request.method == "GET":
        records = News().query.all()
        return jsonify([News.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
