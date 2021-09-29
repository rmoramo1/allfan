from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Baseball(db.Model):
    __tablename__ = "baseball"
    id = db.Column(db.Integer, primary_key=True)
    home = db.Column(db.String(150), nullable=False)
    away = db.Column(db.String(150), nullable=False)
    spreadAway = db.Column(db.String(150), nullable=False)
    spreadHome = db.Column(db.String(150), nullable=False)
    moneyLineHome = db.Column(db.String(150), nullable=False)
    moneyLineAway = db.Column(db.String(150), nullable=False)
    scoreTotalHome = db.Column(db.Integer, nullable=False)
    scoreTotalAway = db.Column(db.Integer, nullable=False)
    firstFiveHome = db.Column(db.Integer, nullable=False)
    firstFiveAway = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    hour = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "home": self.home,
            "away": self.away,
            "spreadAway": self.spreadAway,
            "spreadHome": self.spreadHome,
            "moneyLineHome": self.moneyLineHome,
            "moneyLineAway": self.moneyLineAway,
            "scoreTotalHome": self.scoreTotalHome,
            "scoreTotalAway": self.scoreTotalAway,
            "firstFiveHome": self.firstFiveHome,
            "firstFiveAway": self.firstFiveAway,
            "date": self.date,
            "hour": self.hour
            # do not serialize the password, its a security breach
        }


class Nfl(db.Model):
    __tablename__ = "nfl"
    id = db.Column(db.Integer, primary_key=True)
    home = db.Column(db.String(150), nullable=False)
    away = db.Column(db.String(150), nullable=False)
    spreadAway = db.Column(db.String(150), nullable=False)
    spreadHome = db.Column(db.String(150), nullable=False)
    moneyLineHome = db.Column(db.String(150), nullable=False)
    moneyLineAway = db.Column(db.String(150), nullable=False)
    scoreTotalHome = db.Column(db.Integer, nullable=False)
    scoreTotalAway = db.Column(db.Integer, nullable=False)
    scoreQ1Home = db.Column(db.Integer, nullable=False)
    scoreQ1Away = db.Column(db.Integer, nullable=False)
    scoreQ2Home = db.Column(db.Integer, nullable=False)
    scoreQ2Away = db.Column(db.Integer, nullable=False)
    scoreQ3Home = db.Column(db.Integer, nullable=False)
    scoreQ3Away = db.Column(db.Integer, nullable=False)
    scoreQ4Home = db.Column(db.Integer, nullable=False)
    scoreQ4Away = db.Column(db.Integer, nullable=False)
    scoreSecondHalf = db.Column(db.Integer, nullable=False)
    scoreFirstHalf = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    hour = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "home": self.home,
            "away": self.away,
            "moneyLineHome": self.moneyLineHome,
            "moneyLineAway": self.moneyLineAway,
            "spreadAway": self.spreadAway,
            "spreadHome": self.spreadHome,
            "scoreTotalHome": self.scoreTotalHome,
            "scoreTotalAway": self.scoreTotalAway,
            "scoreQ1Home": self.scoreQ1Home,
            "scoreQ1Away": self.scoreQ1Away,
            "scoreQ2Home": self.scoreQ2Home,
            "scoreQ2Away": self.scoreQ2Away,
            "scoreQ3Home": self.scoreQ3Home,
            "scoreQ3Away": self.scoreQ3Away,
            "scoreQ4Home": self.scoreQ4Home,
            "scoreQ4Away": self.scoreQ4Away,
            "scoreSecondHalf": self.scoreSecondHalf,
            "scoreFirstHalf": self.scoreFirstHalf,
            "date": self.date,
            "hour": self.hour
            # do not serialize the password, its a security breach
        }


class Nba(db.Model):
    __tablename__ = "nba"
    id = db.Column(db.Integer, primary_key=True)
    home = db.Column(db.String(150), nullable=False)
    away = db.Column(db.String(150), nullable=False)
    spreadAway = db.Column(db.String(150), nullable=False)
    spreadHome = db.Column(db.String(150), nullable=False)
    moneyLineHome = db.Column(db.String(150), nullable=False)
    moneyLineAway = db.Column(db.String(150), nullable=False)
    scoreTotalHome = db.Column(db.Integer, nullable=False)
    scoreTotalAway = db.Column(db.Integer, nullable=False)
    scoreQ1Home = db.Column(db.Integer, nullable=False)
    scoreQ1Away = db.Column(db.Integer, nullable=False)
    scoreQ2Home = db.Column(db.Integer, nullable=False)
    scoreQ2Away = db.Column(db.Integer, nullable=False)
    scoreQ3Home = db.Column(db.Integer, nullable=False)
    scoreQ3Away = db.Column(db.Integer, nullable=False)
    scoreQ4Home = db.Column(db.Integer, nullable=False)
    scoreQ4Away = db.Column(db.Integer, nullable=False)
    scoreSecondHalf = db.Column(db.Integer, nullable=False)
    scoreFirstHalf = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    hour = db.Column(db.String(100), nullable=False)
    def serialize(self):
        return {
            "id": self.id,
            "home": self.home,
            "away": self.away,
            "moneyLineHome": self.moneyLineHome,
            "moneyLineAway": self.moneyLineAway,
            "spreadAway": self.spreadAway,
            "spreadHome": self.spreadHome,
            "scoreTotalHome": self.scoreTotalHome,
            "scoreTotalAway": self.scoreTotalAway,
            "scoreQ1Home": self.scoreQ1Home,
            "scoreQ1Away": self.scoreQ1Away,
            "scoreQ2Home": self.scoreQ2Home,
            "scoreQ2Away": self.scoreQ2Away,
            "scoreQ3Home": self.scoreQ3Home,
            "scoreQ3Away": self.scoreQ3Away,
            "scoreQ4Home": self.scoreQ4Home,
            "scoreQ4Away": self.scoreQ4Away,
            "scoreSecondHalf": self.scoreSecondHalf,
            "scoreFirstHalf": self.scoreFirstHalf,
            "date": self.date,
            "hour": self.hour
            # do not serialize the password, its a security breach
        }


class Nhl(db.Model):
    __tablename__ = "nhl"
    id = db.Column(db.Integer, primary_key=True)
    home = db.Column(db.String(150), nullable=False)
    away = db.Column(db.String(150), nullable=False)
    pot_Line_Home = db.Column(db.String(150), nullable=False)
    pot_Line_Away = db.Column(db.String(150), nullable=False)
    scoreTotalHome = db.Column(db.Integer, nullable=False)
    scoreTotalAway = db.Column(db.Integer, nullable=False)
    scoreQ1Home = db.Column(db.Integer, nullable=False)
    scoreQ1Away = db.Column(db.Integer, nullable=False)
    scoreQ2Home = db.Column(db.Integer, nullable=False)
    scoreQ2Away = db.Column(db.Integer, nullable=False)
    scoreQ3Home = db.Column(db.Integer, nullable=False)
    scoreQ3Away = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    hour = db.Column(db.String(100), nullable=False)
    def serialize(self):
        return {
            "id": self.id,
            "home": self.home,
            "away": self.away,
            "pot_Line_Home": self.pot_Line_Home,
            "pot_Line_Away": self.pot_Line_Away,
            "scoreTotalHome": self.scoreTotalHome,
            "scoreTotalAway": self.scoreTotalAway,
            "scoreQ1Home": self.scoreQ1Home,
            "scoreQ1Away": self.scoreQ1Away,
            "scoreQ2Home": self.scoreQ2Home,
            "scoreQ2Away": self.scoreQ2Away,
            "scoreQ3Home": self.scoreQ3Home,
            "scoreQ3Away": self.scoreQ3Away,
            "date": self.date,
            "hour": self.hour
            # do not serialize the password, its a security breach
        }

class Boxeo(db.Model):
    __tablename__ = "boxeo"
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.String(150), nullable=False)
    rounds = db.Column(db.Integer, nullable=False)
    fighter_One = db.Column(db.String(150), nullable=False)
    fighter_Two = db.Column(db.String(150), nullable=False)
    fighter_One_Country = db.Column(db.String(150), nullable=False)
    fighter_Two_Country = db.Column(db.String(150), nullable=False)
    fighter_One_streak = db.Column(db.String(150), nullable=False)
    fighter_Two_streak = db.Column(db.String(150), nullable=False)
    fighter_One_Age = db.Column(db.Integer, nullable=False)
    fighter_Two_Age = db.Column(db.Integer, nullable=False)
    money_Line_One = db.Column(db.String(150), nullable=False)
    money_Line_Two = db.Column(db.String(150), nullable=False)
    winner = db.Column(db.String(150), nullable=False)
    looser = db.Column(db.String(150), nullable=False)
    finish_Type = db.Column(db.String(150), nullable=False)
    final_round = db.Column(db.Integer, nullable=False)
    time_final_round = db.Column(db.String(100), nullable=False)
    event = db.Column(db.String(100), nullable=False)
    fighter_One_experience = db.Column(db.String(100), nullable=False)
    fighter_Two_experience = db.Column(db.String(100), nullable=False)
    country_Fight = db.Column(db.String(100), nullable=False)
    location_Fight = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    hour = db.Column(db.String(100), nullable=False)
    def serialize(self):
        return {
            "id": self.id,
            "event_id": self.event_id,
            "rounds": self.rounds,
            "fighter_One": self.fighter_One,
            "fighter_Two": self.fighter_Two,
            "fighter_One_Country": self.fighter_One_Country,
            "fighter_Two_Country": self.fighter_Two_Country,
            "fighter_One_streak": self.fighter_One_streak,
            "fighter_Two_streak": self.fighter_Two_streak,
            "fighter_One_Age": self.fighter_One_Age,
            "fighter_Two_Age": self.fighter_Two_Age,
            "money_Line_One": self.money_Line_One,
            "money_Line_Two": self.money_Line_Two,
            "winner": self.winner,
            "looser": self.looser,
            "finish_Type": self.finish_Type,
            "final_round": self.final_round,
            "fighter_One_experience": self.fighter_One_experience,
            "fighter_Two_experience": self.fighter_Two_experience,
            "country_Fight": self.country_Fight,
            "location_Fight": self.location_Fight,
            "date": self.date,
            "hour": self.hour
            # do not serialize the password, its a security breach
        }


class Mma(db.Model):
    __tablename__ = "mma"
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.String(150), nullable=False)
    rounds = db.Column(db.Integer, nullable=False)
    fighter_One = db.Column(db.String(150), nullable=False)
    fighter_Two = db.Column(db.String(150), nullable=False)
    fighter_One_Country = db.Column(db.String(150), nullable=False)
    fighter_Two_Country = db.Column(db.String(150), nullable=False)
    fighter_One_streak = db.Column(db.String(150), nullable=False)
    fighter_Two_streak = db.Column(db.String(150), nullable=False)
    fighter_One_Age = db.Column(db.Integer, nullable=False)
    fighter_Two_Age = db.Column(db.Integer, nullable=False)
    money_Line_One = db.Column(db.String(150), nullable=False)
    money_Line_Two = db.Column(db.String(150), nullable=False)
    winner = db.Column(db.String(150), nullable=False)
    looser = db.Column(db.String(150), nullable=False)
    finish_Type = db.Column(db.String(150), nullable=False)
    final_round = db.Column(db.Integer, nullable=False)
    time_final_round = db.Column(db.String(100), nullable=False)
    event = db.Column(db.String(100), nullable=False)
    fighter_One_experience = db.Column(db.String(100), nullable=False)
    fighter_Two_experience = db.Column(db.String(100), nullable=False)
    country_Fight = db.Column(db.String(100), nullable=False)
    location_Fight = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    hour = db.Column(db.String(100), nullable=False)
    def serialize(self):
        return {
            "id": self.id,
            "event_id": self.event_id,
            "rounds": self.rounds,
            "fighter_One": self.fighter_One,
            "fighter_Two": self.fighter_Two,
            "fighter_One_Country": self.fighter_One_Country,
            "fighter_Two_Country": self.fighter_Two_Country,
            "fighter_One_streak": self.fighter_One_streak,
            "fighter_Two_streak": self.fighter_Two_streak,
            "fighter_One_Age": self.fighter_One_Age,
            "fighter_Two_Age": self.fighter_Two_Age,
            "money_Line_One": self.money_Line_One,
            "money_Line_Two": self.money_Line_Two,
            "winner": self.winner,
            "looser": self.looser,
            "finish_Type": self.finish_Type,
            "final_round": self.final_round,
            "fighter_One_experience": self.fighter_One_experience,
            "fighter_Two_experience": self.fighter_Two_experience,
            "country_Fight": self.country_Fight,
            "location_Fight": self.location_Fight,
            "date": self.date,
            "hour": self.hour
            # do not serialize the password, its a security breach
        }


class Nascar(db.Model):
    __tablename__ = "nascar"
    id = db.Column(db.Integer, primary_key=True)
    id_carrera = db.Column(db.Integer, nullable=False)
    race = db.Column(db.String(150), nullable=False)
    track = db.Column(db.Integer, nullable=False)
    country = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    winner = db.Column(db.String(150), nullable=False)
    money_Line = db.Column(db.String(150), nullable=False)
    date = db.Column(db.Date, nullable=False)
    hour = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            "id_carrera": self.id_carrera,
            "race": self.race,
            "track": self.track,
            "country": self.country,
            "location": self.location,
            "winner": self.winner,
            "money_Line": self.money_Line,
            "date": self.date,
            "hour": self.hour,
            # do not serialize the password, its a security breach
        }


class Nascar_drivers(db.Model):
    __tablename__ = "nascar_drivers"
    id = db.Column(db.Integer, primary_key=True)
    id_driver = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(150), nullable=False)
    country = db.Column(db.String(150), nullable=False)
    sponsor = db.Column(db.String(100), nullable=False)
    engine = db.Column(db.String(150), nullable=False)
    number_car = db.Column(db.Integer, nullable=False)
    def serialize(self):
        return {
            "id_driver": self.id_driver,
            "name": self.name,
            "country": self.country,
            "sponsor": self.sponsor,
            "engine": self.engine,
            "number_car": self.number_car,
            # do not serialize the password, its a security breach
        }

class Golf(db.Model):
    __tablename__ = "golf"
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    date = db.Column(db.Date, nullable=False)
    hour = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            "event": self.event,
            "date": self.date,
            "hour": self.hour,
            "location": self.location
            # do not serialize the password, its a security breach
        }


class Golfer(db.Model):
    __tablename__ = "golfer"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    country = db.Column(db.String(150), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    spread = db.Column(db.String(150), nullable=False)
    money_line = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            "name": self.name,
            "age": self.age,
            "country": self.country,
            "spread": self.spread,
            "money_line": self.money_line
            # do not serialize the password, its a security breach
        }


class News(db.Model):
    __tablename__ = "news"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    short_description = db.Column(db.String(1000), nullable=False)
    news_post = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date, nullable=False)

    def serialize(self):
        return {
            "title": self.title,
            "short_description": self.short_description,
            "url_image": self.url_image,
            "news_post": self.news_post,
            "date": self.date
            # do not serialize the password, its a security breach
        }
