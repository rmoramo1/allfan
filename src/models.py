from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Mbl(db.Model):
    __tablename__ = "mbl"
    id = db.Column(db.Integer, primary_key=True)
    away = db.Column(db.String(150), nullable=False)
    home = db.Column(db.String(150), nullable=False)

    rl_away = db.Column(db.DECIMAL(7,2), nullable=False)
    juice_rl_away = db.Column(db.String(150), default=-110, nullable=False)
    moneyLineAway = db.Column(db.String(150), nullable=False)
    total = db.Column(db.Integer, nullable=False)
    juice_total = db.Column(db.String(150), default=-110, nullable=False)
    tt_away = db.Column(db.DECIMAL(7,2), nullable=False)
    juice_over_away = db.Column(db.String(150), default=-110, nullable=False)
    juice_under_away = db.Column(db.String(150), default=-110, nullable=False)
    final_score_away = db.Column(db.Integer,default=0, nullable=False)

    rl_home = db.Column(db.DECIMAL(7,2), nullable=False)
    juice_rl_home = db.Column(db.String(150), default=-110, nullable=False)
    moneyLineHome = db.Column(db.String(150), nullable=False)
    tt_home = db.Column(db.DECIMAL(7,2), nullable=False)
    juice_over_home = db.Column(db.String(150), default=-110, nullable=False)
    juice_under_home = db.Column(db.String(150), default=-110, nullable=False)
    final_score_home = db.Column(db.Integer,default=0, nullable=False)

    # ------------------------------------------------------------------------
    rl_away_f5 = db.Column(db.DECIMAL(7,2), nullable=False)
    juice_rl_away_f5 = db.Column(db.String(150), default=-110, nullable=False)
    moneyLineAway_f5 = db.Column(db.String(150), nullable=False)
    total_f5 = db.Column(db.DECIMAL(7,2), nullable=False)
    juice_total_f5 = db.Column(db.String(150), default=-110, nullable=False)
    tt_away_f5 = db.Column(db.DECIMAL(7,2), nullable=False)
    juice_over_away_f5 = db.Column(db.String(150), default=-110, nullable=False)
    juice_under_away_f5 = db.Column(db.String(150), default=-110, nullable=False)
    fs_away_f5 = db.Column(db.Integer, nullable=False)

    rl_home_f5 = db.Column(db.DECIMAL(7,2), nullable=False)
    juice_rl_home_f5 = db.Column(db.String(150), default=-110, nullable=False)
    moneyLineHome_f5 = db.Column(db.String(150), nullable=False)
    tt_home_f5 = db.Column(db.DECIMAL(7,2), nullable=False)
    juice_over_home_f5 = db.Column(db.String(150), default=-110, nullable=False)
    juice_under_home_f5 = db.Column(db.String(150), default=-110, nullable=False)
    fs_home_f5 = db.Column(db.Integer, nullable=False)

    # ----------------------------------------------------------------------

    sa_1inning = db.Column(db.Integer, default=0, nullable=False)
    sh_1inning = db.Column(db.Integer, default=0, nullable=False)
    sa_2inning = db.Column(db.Integer, default=0, nullable=False)
    sh_2inning = db.Column(db.Integer, default=0, nullable=False)
    sa_3inning = db.Column(db.Integer, default=0, nullable=False)
    sh_3inning = db.Column(db.Integer, default=0, nullable=False)
    sa_4inning = db.Column(db.Integer, default=0, nullable=False)
    sh_4inning = db.Column(db.Integer, default=0, nullable=False)
    sa_5inning = db.Column(db.Integer, default=0, nullable=False)
    sh_5inning = db.Column(db.Integer, default=0, nullable=False)
    sa_6inning = db.Column(db.Integer, default=0, nullable=False)
    sh_6inning = db.Column(db.Integer, default=0, nullable=False)
    sa_7inning = db.Column(db.Integer, default=0, nullable=False)
    sh_7inning = db.Column(db.Integer, default=0, nullable=False)
    sa_8inning = db.Column(db.Integer, default=0, nullable=False)
    sh_8inning = db.Column(db.Integer, default=0, nullable=False)
    sa_9inning = db.Column(db.Integer, default=0, nullable=False)
    sh_9inning = db.Column(db.Integer, default=0, nullable=False)
    sa_10inning = db.Column(db.Integer, default=0, nullable=False)
    sh_10inning = db.Column(db.Integer, default=0, nullable=False)
    sa_11inning = db.Column(db.Integer, default=0, nullable=False)
    sh_11inning = db.Column(db.Integer, default=0, nullable=False)
    sa_12inning = db.Column(db.Integer, default=0, nullable=False)
    sh_12inning = db.Column(db.Integer, default=0, nullable=False)
    sa_13inning = db.Column(db.Integer, default=0, nullable=False)
    sh_13inning = db.Column(db.Integer, default=0, nullable=False)
    sa_14inning = db.Column(db.Integer, default=0, nullable=False)
    sh_14inning = db.Column(db.Integer, default=0, nullable=False)
    sa_15inning = db.Column(db.Integer, default=0, nullable=False)
    sh_15inning = db.Column(db.Integer, default=0, nullable=False)
    sa_16inning = db.Column(db.Integer, default=0, nullable=False)
    sh_16inning = db.Column(db.Integer, default=0, nullable=False)
    sa_17inning = db.Column(db.Integer, default=0, nullable=False)
    sh_17inning = db.Column(db.Integer, default=0, nullable=False)
    sa_18inning = db.Column(db.Integer, default=0, nullable=False)
    sh_18inning = db.Column(db.Integer, default=0, nullable=False)
    sa_19inning = db.Column(db.Integer, default=0, nullable=False)
    sh_19inning = db.Column(db.Integer, default=0, nullable=False)
    sa_20inning = db.Column(db.Integer, default=0, nullable=False)
    sh_20inning = db.Column(db.Integer, default=0, nullable=False)
    sa_21inning = db.Column(db.Integer, default=0, nullable=False)
    sh_21inning = db.Column(db.Integer, default=0, nullable=False)
    sa_22inning = db.Column(db.Integer, default=0, nullable=False)
    sh_22inning = db.Column(db.Integer, default=0, nullable=False)
    sa_23inning = db.Column(db.Integer, default=0, nullable=False)
    sh_23inning = db.Column(db.Integer, default=0, nullable=False)
    sa_24inning = db.Column(db.Integer, default=0, nullable=False)
    sh_24inning = db.Column(db.Integer, default=0, nullable=False)
    sa_1inning = db.Column(db.Integer, default=0, nullable=False)
    sh_1inning = db.Column(db.Integer, default=0, nullable=False)

    date = db.Column(db.String(100), nullable=False)
    hour = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "away": self.away,
            "home": self.home,

            "rl_away": self.rl_away,
            "rl_home": self.rl_home,

            "juice_rl_away": self.juice_rl_away,
            "juice_rl_home": self.juice_rl_home,

            "moneyLineHome": self.moneyLineHome,
            "moneyLineAway": self.moneyLineAway,

            "total": self.total,
            "juice_total": self.juice_total,

            "tt_away": self.tt_away,
            "tt_home": self.tt_home,

            "juice_over_away": self.juice_over_away,
            "juice_over_home": self.juice_over_home,

            "juice_under_away": self.juice_under_away,
            "juice_under_home": self.juice_under_home,

            "final_score_away": self.final_score_away,
            "final_score_home": self.final_score_home,

            "rl_away_f5": self.rl_away_f5,
            "rl_home_f5": self.rl_home_f5,

            "juice_rl_away_f5": self.juice_rl_away_f5,
            "juice_rl_home_f5": self.juice_rl_home_f5,

            "moneyLineHome_f5": self.moneyLineHome_f5,
            "moneyLineAway_f5": self.moneyLineAway_f5,

            "total_f5": self.total_f5,
            "tt_home_f5": self.tt_home_f5,

            "tt_away_f5": self.tt_away_f5,
            "tt_home_f5": self.tt_home_f5,

            "juice_over_away_f5": self.juice_over_away_f5,
            "juice_over_home_f5": self.juice_over_home_f5,

            "juice_under_away_f5": self.juice_under_away_f5,
            "juice_under_home_f5": self.juice_under_home_f5,

            "fs_away_f5": self.fs_away_f5,
            "fs_home_f5": self.fs_home_f5,

            "sa_1inning": self.sa_1inning,
            "sh_1inning": self.sh_1inning,
            "sa_2inning": self.sa_2inning,
            "sh_2inning": self.sh_2inning,
            "sa_3inning": self.sa_3inning,
            "sh_3inning": self.sh_3inning,
            "sa_4inning": self.sa_4inning,
            "sh_4inning": self.sh_4inning,
            "sa_5inning": self.sa_5inning,
            "sh_5inning": self.sh_5inning,
            "sa_6inning": self.sa_6inning,
            "sh_6inning": self.sh_6inning,
            "sa_7inning": self.sa_7inning,
            "sh_7inning": self.sh_7inning,
            "sa_8inning": self.sa_8inning,
            "sh_8inning": self.sh_8inning,
            "sa_9inning": self.sa_9inning,
            "sh_9inning": self.sh_9inning,
            "sa_10inning": self.sa_10inning,
            "sh_10inning": self.sh_10inning,
            "sa_11inning": self.sa_11inning,
            "sh_11inning": self.sh_11inning,
            "sa_12inning": self.sa_12inning,
            "sh_12inning": self.sh_12inning,
            "sa_13inning": self.sa_13inning,
            "sh_13inning": self.sh_13inning,
            "sa_14inning": self.sa_14inning,
            "sh_14inning": self.sh_14inning,
            "sa_15inning": self.sa_15inning,
            "sh_15inning": self.sh_15inning,
            "sa_16inning": self.sa_16inning,
            "sh_16inning": self.sh_16inning,
            "sa_17inning": self.sa_17inning,
            "sh_17inning": self.sh_17inning,
            "sa_18inning": self.sa_18inning,
            "sh_18inning": self.sh_18inning,
            "sa_19inning": self.sa_19inning,
            "sh_19inning": self.sh_19inning,
            "sa_20inning": self.sa_20inning,
            "sh_20inning": self.sh_20inning,
            "sa_21inning": self.sa_21inning,
            "sh_21inning": self.sh_21inning,
            "sa_22inning": self.sa_22inning,
            "sh_22inning": self.sh_22inning,
            "sa_23inning": self.sa_23inning,
            "sh_23inning": self.sh_23inning,
            "sa_24inning": self.sa_24inning,
            "sh_24inning": self.sh_24inning,

            "date": self.date,
            "hour": self.hour
            # do not serialize the password, its a security breach
        }


class Nfl(db.Model):
    __tablename__ = "nfl"
    id = db.Column(db.Integer, primary_key=True)
    away = db.Column(db.String(150), nullable=False)
    spread_away = db.Column(db.DECIMAL(7,2), nullable=False)
    juice_spread_away = db.Column(db.String(150), default=-110, nullable=False)
    moneyLineAway = db.Column(db.String(150), nullable=False)
    total = db.Column(db.DECIMAL(7,2), nullable=False)
    juice_total = db.Column(db.String(150), default=-110, nullable=False)
    tt_away = db.Column(db.DECIMAL(7,2), nullable=False)
    juice_over_away = db.Column(db.String(150), default=-110, nullable=False)
    juice_under_away = db.Column(db.String(150), default=-110, nullable=False)
    final_score_away = db.Column(db.Integer,default=0, nullable=False)

    home = db.Column(db.String(150), nullable=False)
    spread_home = db.Column(db.DECIMAL(7,2), nullable=False)
    juice_spread_home = db.Column(db.String(150), default=-110, nullable=False)
    moneyLineHome = db.Column(db.String(150), nullable=False)
    tt_home = db.Column(db.DECIMAL(7,2), nullable=False)
    juice_over_home = db.Column(db.String(150), default=-110, nullable=False)
    juice_under_home = db.Column(db.String(150), default=-110, nullable=False)
    final_score_home = db.Column(db.Integer,default=0, nullable=False)
# ----------
    first_half_spread_away = db.Column(db.DECIMAL(7,2), nullable=False)
    first_half_juice_spread_away = db.Column(db.String(150), default=-110, nullable=False)
    first_half_moneyLineHome = db.Column(db.String(150), nullable=False)
    first_half_total = db.Column(db.Integer, nullable=False)
    first_half_juice_total = db.Column(db.String(150), default=-110, nullable=False)
    first_half_tt_away = db.Column(db.Integer,default=0, nullable=False)
    first_half_juice_over_away = db.Column(db.String(150), default=-110, nullable=False)
    first_half_juice_under_away = db.Column(db.String(150), default=-110, nullable=False)
    first_half_final_score_away = db.Column(db.Integer,default=0, nullable=False)

    first_half_spread_home = db.Column(db.DECIMAL(7,2), nullable=False)
    first_half_juice_spread_home = db.Column(db.String(150), default=-110, nullable=False)
    first_half_moneyLineAway = db.Column(db.String(150), nullable=False)
    first_half_tt_home = db.Column(db.Integer,default=0, nullable=False)
    first_half_juice_over_home = db.Column(db.String(150), default=-110, nullable=False)
    first_half_juice_under_home = db.Column(db.String(150), default=-110, nullable=False)
    first_half_final_score_home = db.Column(db.Integer,default=0, nullable=False)
# ------------------------------------------------------------------------------
    second_half_spread_away = db.Column(db.DECIMAL(7,2), nullable=False)
    second_half_juice_spread_away = db.Column(db.String(150), default=-110, nullable=False)
    second_half_moneyLineHome = db.Column(db.String(150), nullable=False)
    second_half_total = db.Column(db.DECIMAL(7,2),default=0, nullable=False)
    second_half_juice_total = db.Column(db.String(150), default=-110, nullable=False)
    second_half_tt_away = db.Column(db.DECIMAL(7,2),default=0, nullable=False)
    second_half_juice_over_away = db.Column(db.String(150), default=-110, nullable=False)
    second_half_juice_under_away = db.Column(db.String(150), default=-110, nullable=False)
    second_half_final_score_away = db.Column(db.Integer,default=0, nullable=False)

    second_half_spread_home = db.Column(db.DECIMAL(7,2), nullable=False)
    second_half_juice_spread_home = db.Column(db.String(150), default=-110, nullable=False)
    second_half_moneyLineAway = db.Column(db.String(150), nullable=False)
    second_half_tt_home = db.Column(db.DECIMAL(7,2),default=0, nullable=False)
    second_half_juice_over_home = db.Column(db.String(150), default=-110, nullable=False)
    second_half_juice_under_home = db.Column(db.String(150), default=-110, nullable=False)
    second_half_final_score_home = db.Column(db.Integer,default=0, nullable=False)

# ------------------------------------------------------------------------------
    q1_half_spread_away = db.Column(db.DECIMAL(7,2), nullable=False)
    q1_half_juice_spread_away = db.Column(db.String(150), default=-110, nullable=False)
    q1_half_moneyLineHome = db.Column(db.String(150), nullable=False)
    q1_half_total = db.Column(db.DECIMAL(7,2),default=0, nullable=False)
    q1_half_juice_total = db.Column(db.String(150), default=-110, nullable=False)
    q1_half_tt_away = db.Column(db.DECIMAL(7,2),default=0, nullable=False)
    q1_half_juice_over_away = db.Column(db.String(150), default=-110, nullable=False)
    q1_half_juice_under_away = db.Column(db.String(150), default=-110, nullable=False)
    q1_half_final_score_away = db.Column(db.Integer,default=0, nullable=False)

    q1_half_spread_home = db.Column(db.DECIMAL(7,2), nullable=False)
    q1_half_juice_spread_home = db.Column(db.String(150), default=-110, nullable=False)
    q1_half_moneyLineAway = db.Column(db.String(150), nullable=False)
    q1_half_tt_home = db.Column(db.DECIMAL(7,2),default=0, nullable=False)
    q1_half_juice_over_home = db.Column(db.String(150), default=-110, nullable=False)
    q1_half_juice_under_home = db.Column(db.String(150), default=-110, nullable=False)
    q1_half_final_score_home = db.Column(db.Integer,default=0, nullable=False)

    # -----------------------------------------------------------------------
    q2_half_spread_away = db.Column(db.DECIMAL(7,2), nullable=False)
    q2_half_juice_spread_away = db.Column(db.String(150), default=-110, nullable=False)
    q2_half_moneyLineHome = db.Column(db.String(150), nullable=False)
    q2_half_total = db.Column(db.DECIMAL(7,2), nullable=False)
    q2_half_juice_total = db.Column(db.String(150), default=-110, nullable=False)
    q2_half_tt_away = db.Column(db.DECIMAL(7,2),default=0, nullable=False)
    q2_half_juice_over_away = db.Column(db.String(150), default=-110, nullable=False)
    q2_half_juice_under_away = db.Column(db.String(150), default=-110, nullable=False)
    q2_half_final_score_away = db.Column(db.Integer,default=0, nullable=False)

    q2_half_spread_home = db.Column(db.DECIMAL(7,2), nullable=False)
    q2_half_juice_spread_home = db.Column(db.String(150), default=-110, nullable=False)
    q2_half_moneyLineAway = db.Column(db.String(150), nullable=False)
    q2_half_tt_home = db.Column(db.DECIMAL(7,2), nullable=False)
    q2_half_juice_over_home = db.Column(db.String(150), default=-110, nullable=False)
    q2_half_juice_under_home = db.Column(db.String(150), default=-110, nullable=False)
    q2_half_final_score_home = db.Column(db.Integer,default=0, nullable=False)

# -------------------------------------------------------------------------------
    q3_half_spread_away = db.Column(db.DECIMAL(7,2), nullable=False)
    q3_half_juice_spread_away = db.Column(db.String(150), default=-110, nullable=False)
    q3_half_moneyLineHome = db.Column(db.String(150), nullable=False)
    q3_half_total = db.Column(db.DECIMAL(7,2), nullable=False)
    q3_half_juice_total = db.Column(db.String(150), default=-110, nullable=False)
    q3_half_tt_away = db.Column(db.DECIMAL(7,2),default=0, nullable=False)
    q3_half_juice_over_away = db.Column(db.String(150), default=-110, nullable=False)
    q3_half_juice_under_away = db.Column(db.String(150), default=-110, nullable=False)
    q3_half_final_score_away = db.Column(db.Integer,default=0, nullable=False)

    q3_half_spread_home = db.Column(db.DECIMAL(7,2), nullable=False)
    q3_half_juice_spread_home = db.Column(db.String(150), default=-110, nullable=False)
    q3_half_moneyLineAway = db.Column(db.String(150), nullable=False)
    q3_half_tt_home = db.Column(db.DECIMAL(7,2), nullable=False)
    q3_half_juice_over_home = db.Column(db.String(150), default=-110, nullable=False)
    q3_half_juice_under_home = db.Column(db.String(150), default=-110, nullable=False)
    q3_half_final_score_home = db.Column(db.Integer,default=0, nullable=False)

# ----------------------------------------------------------------------------------
    q4_half_spread_away = db.Column(db.DECIMAL(7,2), nullable=False)
    q4_half_juice_spread_away = db.Column(db.String(150), default=-110, nullable=False)
    q4_half_moneyLineHome = db.Column(db.String(150), nullable=False)
    q4_half_total = db.Column(db.DECIMAL(7,2),default=0, nullable=False)
    q4_half_juice_total = db.Column(db.String(150), default=-110, nullable=False)
    q4_half_tt_away = db.Column(db.DECIMAL(7,2), nullable=False)
    q4_half_juice_over_away = db.Column(db.String(150), default=-110, nullable=False)
    q4_half_juice_under_away = db.Column(db.String(150), default=-110, nullable=False)
    q4_half_final_score_away = db.Column(db.Integer,default=0, nullable=False)

    q4_half_spread_home = db.Column(db.DECIMAL(7,2), nullable=False)
    q4_half_juice_spread_home = db.Column(db.String(150), default=-110, nullable=False)
    q4_half_moneyLineAway = db.Column(db.String(150), nullable=False)
    q4_half_tt_home = db.Column(db.DECIMAL(7,2), nullable=False)
    q4_half_juice_over_home = db.Column(db.String(150), default=-110, nullable=False)
    q4_half_juice_under_home = db.Column(db.String(150), default=-110, nullable=False)
    q4_half_final_score_home = db.Column(db.Integer,default=0, nullable=False)

    date = db.Column(db.String(100), nullable=False)
    hour = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "home": self.home,
            "away": self.away,

            "spread_away": self.spread_away,
            "spread_home": self.spread_home,

            "juice_spread_away": self.juice_spread_away,
            "juice_spread_home": self.juice_spread_home,

            "moneyLineHome": self.moneyLineHome,
            "moneyLineAway": self.moneyLineAway,

            "total": self.total,
            "juice_total": self.juice_total,

            "tt_away": self.tt_away,
            "tt_home": self.tt_home,

            "juice_over_away": self.juice_over_away,
            "juice_over_home": self.juice_over_home,

            "juice_under_away": self.juice_under_away,
            "juice_under_home": self.juice_under_home,

            "final_score_away": self.final_score_away,
            "final_score_home": self.final_score_home,

            "first_half_spread_away": self.first_half_spread_away,
            "first_half_spread_home": self.first_half_spread_home,

            "first_half_juice_spread_away": self.first_half_juice_spread_away,
            "first_half_juice_spread_home": self.first_half_juice_spread_home,

            "first_half_moneyLineHome": self.first_half_moneyLineHome,
            "first_half_moneyLineAway": self.first_half_moneyLineAway,

            "first_half_total": self.first_half_total,
            "first_half_juice_total": self.final_score_home,

            "first_half_tt_away": self.first_half_tt_away,
            "first_half_tt_home": self.first_half_tt_home,

            "first_half_juice_over_away": self.first_half_juice_over_away,
            "first_half_juice_over_home": self.first_half_juice_over_home,

            "first_half_juice_under_away": self.first_half_juice_under_away,
            "first_half_juice_under_home": self.first_half_juice_under_home,

            "first_half_juice_over_away": self.first_half_juice_over_away,
            "first_half_juice_over_home": self.first_half_juice_over_home,

            "first_half_juice_under_away": self.first_half_juice_under_away,
            "first_half_juice_under_home": self.first_half_juice_under_home,

            "first_half_final_score_away": self.first_half_final_score_away,
            "first_half_final_score_home": self.first_half_final_score_home,

            "second_half_spread_away": self.second_half_spread_away,
            "second_half_spread_home": self.second_half_spread_home,

            "second_half_juice_spread_away": self.second_half_juice_spread_away,
            "second_half_juice_spread_home": self.second_half_juice_spread_home,

            "second_half_moneyLineHome": self.second_half_moneyLineHome,
            "second_half_moneyLineAway": self.second_half_moneyLineAway,

            "second_half_total": self.second_half_total,
            "second_half_juice_total": self.first_half_juice_over_home,

            "second_half_tt_away": self.first_half_juice_over_away,
            "second_half_tt_home": self.first_half_juice_over_home,

            "second_half_juice_over_away": self.second_half_juice_over_away,
            "second_half_juice_over_home": self.second_half_juice_over_home,

            "second_half_juice_under_away": self.second_half_juice_under_away,
            "second_half_juice_under_home": self.second_half_juice_under_home,

            "second_half_final_score_away": self.second_half_final_score_away,
            "second_half_final_score_home": self.second_half_final_score_home,

            "q1_half_spread_away": self.q1_half_spread_away,
            "q1_half_spread_home": self.q1_half_spread_home,
            "q1_half_juice_spread_away": self.q1_half_juice_spread_away,
            "q1_half_juice_spread_home": self.q1_half_juice_spread_home,
            "q1_half_moneyLineHome": self.q1_half_moneyLineHome,
            "q1_half_moneyLineAway": self.q1_half_moneyLineAway,
            "q1_half_total": self.q1_half_total,
            "q1_half_juice_total": self.q1_half_juice_total,
            "q1_half_tt_away": self.q1_half_tt_away,
            "q1_half_tt_home": self.q1_half_tt_home,
            "q1_half_juice_over_away": self.q1_half_juice_over_away,
            "q1_half_juice_over_home": self.q1_half_juice_over_home,
            "q1_half_final_score_away": self.q1_half_final_score_away,
            "q1_half_final_score_home": self.q1_half_final_score_home,

            "q2_half_spread_away": self.q2_half_spread_away,
            "q2_half_spread_home": self.q2_half_spread_home,
            "q2_half_juice_spread_away": self.q2_half_juice_spread_away,
            "q2_half_juice_spread_home": self.q2_half_juice_spread_home,
            "q2_half_moneyLineHome": self.q2_half_moneyLineHome,
            "q2_half_moneyLineAway": self.q2_half_moneyLineAway,
            "q2_half_total": self.q2_half_total,
            "q2_half_juice_total": self.q2_half_juice_total,
            "q2_half_tt_away": self.q2_half_tt_away,
            "q2_half_tt_home": self.q2_half_tt_home,
            "q2_half_juice_over_away": self.q2_half_juice_over_away,
            "q2_half_juice_over_home": self.q2_half_juice_over_home,
            "q2_half_final_score_away": self.q2_half_final_score_away,
            "q2_half_final_score_home": self.q2_half_final_score_home,

            "q3_half_spread_away": self.q3_half_spread_away,
            "q3_half_spread_home": self.q3_half_spread_home,
            "q3_half_juice_spread_away": self.q3_half_juice_spread_away,
            "q3_half_juice_spread_home": self.q3_half_juice_spread_home,
            "q3_half_moneyLineHome": self.q3_half_moneyLineHome,
            "q3_half_moneyLineAway": self.q3_half_moneyLineAway,
            "q3_half_total": self.q3_half_total,
            "q3_half_juice_total": self.q3_half_juice_total,
            "q3_half_tt_away": self.q3_half_tt_away,
            "q3_half_tt_home": self.q3_half_tt_home,
            "q3_half_juice_over_away": self.q3_half_juice_over_away,
            "q3_half_juice_over_home": self.q3_half_juice_over_home,
            "q3_half_final_score_away": self.q3_half_final_score_away,
            "q3_half_final_score_home": self.q3_half_final_score_home,

            "q4_half_spread_away": self.q4_half_spread_away,
            "q4_half_spread_home": self.q4_half_spread_home,
            "q4_half_juice_spread_away": self.q4_half_juice_spread_away,
            "q4_half_juice_spread_home": self.q4_half_juice_spread_home,
            "q4_half_moneyLineHome": self.q4_half_moneyLineHome,
            "q4_half_moneyLineAway": self.q4_half_moneyLineAway,
            "q4_half_total": self.q4_half_total,
            "q4_half_juice_total": self.q4_half_juice_total,
            "q4_half_tt_away": self.q4_half_tt_away,
            "q4_half_tt_home": self.q4_half_tt_home,
            "q4_half_juice_over_away": self.q4_half_juice_over_away,
            "q4_half_juice_over_home": self.q4_half_juice_over_home,
            "q4_half_final_score_away": self.q4_half_final_score_away,
            "q4_half_final_score_home": self.q4_half_final_score_home,

            "date": self.date,
            "hour": self.hour
            # do not serialize the password, its a security breach
        }


class Nba(db.Model):
    __tablename__ = "nba"
    id = db.Column(db.Integer, primary_key=True)
    away = db.Column(db.String(150), nullable=False)
    spread_away = db.Column(db.DECIMAL(7,2), nullable=False)
    juice_spread_away = db.Column(db.String(150), default=-110, nullable=False)
    moneyLineAway = db.Column(db.String(150), nullable=False)
    total = db.Column(db.DECIMAL(7,2),default=0, nullable=False)
    juice_total = db.Column(db.String(150), default=-110, nullable=False)
    tt_away = db.Column(db.DECIMAL(7,2),default=0, nullable=False)
    juice_over_away = db.Column(db.String(150), default=-110, nullable=False)
    juice_under_away = db.Column(db.String(150), default=-110, nullable=False)
    final_score_away = db.Column(db.Integer,default=0, nullable=False)

    home = db.Column(db.String(150), nullable=False)
    spread_home = db.Column(db.DECIMAL(7,2), nullable=False)
    juice_spread_home = db.Column(db.String(150), default=-110, nullable=False)
    moneyLineHome = db.Column(db.String(150), nullable=False)
    tt_home = db.Column(db.DECIMAL(7,2),default=0, nullable=False)
    juice_over_home = db.Column(db.String(150), default=-110, nullable=False)
    juice_under_home = db.Column(db.String(150), default=-110, nullable=False)
    final_score_home = db.Column(db.Integer,default=0, nullable=False)
# ----------
    first_half_spread_away = db.Column(db.DECIMAL(7,2), nullable=False)
    first_half_juice_spread_away = db.Column(db.String(150), default=-110, nullable=False)
    first_half_moneyLineAway = db.Column(db.String(150), nullable=False)
    first_half_total = db.Column(db.DECIMAL(7,2),default=0, nullable=False)
    first_half_juice_total = db.Column(db.String(150), default=-110, nullable=False)
    first_half_tt_away = db.Column(db.DECIMAL(7,2), nullable=False)
    first_half_juice_over_away = db.Column(db.String(150), default=-110, nullable=False)
    first_half_juice_under_away = db.Column(db.String(150), default=-110, nullable=False)
    first_half_final_score_away = db.Column(db.Integer,default=0, nullable=False)

    first_half_spread_home = db.Column(db.DECIMAL(7,2), nullable=False)
    first_half_juice_spread_home = db.Column(db.String(150), default=-110, nullable=False)
    first_half_moneyLineHome = db.Column(db.String(150), nullable=False)
    first_half_tt_home = db.Column(db.DECIMAL(7,2), nullable=False)
    first_half_juice_over_home = db.Column(db.String(150), default=-110, nullable=False)
    first_half_juice_under_home = db.Column(db.String(150), default=-110, nullable=False)
    first_half_final_score_home = db.Column(db.Integer,default=0, nullable=False)

# ------------------------------------------------------------------------------
    second_half_spread_away = db.Column(db.DECIMAL(7,2), nullable=False)
    second_half_juice_spread_away = db.Column(db.String(150), default=-110, nullable=False)
    second_half_moneyLineHome = db.Column(db.String(150), nullable=False)
    second_half_total = db.Column(db.DECIMAL(7,2),default=0, nullable=False)
    second_half_juice_total = db.Column(db.String(150), default=-110, nullable=False)
    second_half_tt_away = db.Column(db.DECIMAL(7,2), nullable=False)
    second_half_juice_over_away = db.Column(db.String(150), default=-110, nullable=False)
    second_half_juice_under_away = db.Column(db.String(150), default=-110, nullable=False)
    second_half_final_score_away = db.Column(db.Integer,default=0, nullable=False)

    second_half_spread_home = db.Column(db.DECIMAL(7,2), nullable=False)
    second_half_juice_spread_home = db.Column(db.String(150), default=-110, nullable=False)
    second_half_moneyLineAway = db.Column(db.String(150), nullable=False)
    second_half_tt_home = db.Column(db.DECIMAL(7,2), nullable=False)
    second_half_juice_over_home = db.Column(db.String(150), default=-110, nullable=False)
    second_half_juice_under_home = db.Column(db.String(150), default=-110, nullable=False)
    second_half_final_score_home = db.Column(db.Integer,default=0, nullable=False)

# ------------------------------------------------------------------------------
    q1_half_spread_away = db.Column(db.DECIMAL(7,2), nullable=False)
    q1_half_juice_spread_away = db.Column(db.String(150), default=-110, nullable=False)
    q1_half_moneyLineHome = db.Column(db.String(150), nullable=False)
    q1_half_total = db.Column(db.Integer,default=0, nullable=False)
    q1_half_juice_total = db.Column(db.String(150), default=-110, nullable=False)
    q1_half_tt_away = db.Column(db.Integer,default=0, nullable=False)
    q1_half_juice_over_away = db.Column(db.String(150), default=-110, nullable=False)
    q1_half_juice_under_away = db.Column(db.String(150), default=-110, nullable=False)
    q1_half_final_score_away = db.Column(db.Integer,default=0, nullable=False)

    q1_half_spread_home = db.Column(db.DECIMAL(7,2), nullable=False)
    q1_half_juice_spread_home = db.Column(db.String(150), default=-110, nullable=False)
    q1_half_moneyLineAway = db.Column(db.String(150), nullable=False)
    q1_half_tt_home = db.Column(db.Integer,default=0, nullable=False)
    q1_half_juice_over_home = db.Column(db.String(150), default=-110, nullable=False)
    q1_half_juice_under_home = db.Column(db.String(150), default=-110, nullable=False)
    q1_half_final_score_home = db.Column(db.Integer,default=0, nullable=False)

    # -----------------------------------------------------------------------
    q2_half_spread_away = db.Column(db.DECIMAL(7,2), nullable=False)
    q2_half_juice_spread_away = db.Column(db.String(150), default=-110, nullable=False)
    q2_half_moneyLineAway = db.Column(db.String(150), nullable=False)
    q2_half_total = db.Column(db.DECIMAL(7,2),default=0, nullable=False)
    q2_half_juice_total = db.Column(db.String(150), default=-110, nullable=False)
    q2_half_tt_away = db.Column(db.Integer,default=0, nullable=False)
    q2_half_juice_over_away = db.Column(db.String(150), default=-110, nullable=False)
    q2_half_juice_under_away = db.Column(db.String(150), default=-110, nullable=False)
    q2_half_final_score_away = db.Column(db.Integer,default=0, nullable=False)

    q2_half_spread_home = db.Column(db.DECIMAL(7,2), nullable=False)
    q2_half_juice_spread_home = db.Column(db.String(150), default=-110, nullable=False)
    q2_half_moneyLineHome = db.Column(db.String(150), nullable=False)
    q2_half_tt_home = db.Column(db.Integer,default=0, nullable=False)
    q2_half_juice_over_home = db.Column(db.String(150), default=-110, nullable=False)
    q2_half_juice_under_home = db.Column(db.String(150), default=-110, nullable=False)
    q2_half_final_score_home = db.Column(db.Integer,default=0, nullable=False)

# -------------------------------------------------------------------------------
    q3_half_spread_away = db.Column(db.DECIMAL(7,2), nullable=False)
    q3_half_juice_spread_away = db.Column(db.String(150), default=-110, nullable=False)
    q3_half_moneyLineAway = db.Column(db.String(150), nullable=False)
    q3_half_total = db.Column(db.DECIMAL(7,2), nullable=False)
    q3_half_juice_total = db.Column(db.String(150), default=-110, nullable=False)
    q3_half_tt_away = db.Column(db.DECIMAL(7,2),default=0, nullable=False)
    q3_half_juice_over_away = db.Column(db.String(150), default=-110, nullable=False)
    q3_half_juice_under_away = db.Column(db.String(150), default=-110, nullable=False)
    q3_half_final_score_away = db.Column(db.Integer,default=0, nullable=False)

    q3_half_spread_home = db.Column(db.DECIMAL(7,2), nullable=False)
    q3_half_juice_spread_home = db.Column(db.String(150), default=-110, nullable=False)
    q3_half_moneyLineHome = db.Column(db.String(150), nullable=False)
    q3_half_tt_home = db.Column(db.DECIMAL(7,2), nullable=False)
    q3_half_juice_over_home = db.Column(db.String(150), default=-110, nullable=False)
    q3_half_juice_under_home = db.Column(db.String(150), default=-110, nullable=False)
    q3_half_final_score_home = db.Column(db.Integer,default=0, nullable=False)

# ----------------------------------------------------------------------------------
    q4_half_spread_away = db.Column(db.DECIMAL(7,2), nullable=False)
    q4_half_juice_spread_away = db.Column(db.String(150), default=-110, nullable=False)
    q4_half_moneyLineHome = db.Column(db.String(150), nullable=False)
    q4_half_total = db.Column(db.Integer,default=0, nullable=False)
    q4_half_juice_total = db.Column(db.String(150), default=-110, nullable=False)
    q4_half_tt_away = db.Column(db.DECIMAL(7,2), nullable=False)
    q4_half_juice_over_away = db.Column(db.String(150), default=-110, nullable=False)
    q4_half_juice_under_away = db.Column(db.String(150), default=-110, nullable=False)
    q4_half_final_score_away = db.Column(db.Integer,default=0, nullable=False)

    q4_half_spread_home = db.Column(db.DECIMAL(7,2), nullable=False)
    q4_half_juice_spread_home = db.Column(db.String(150), default=-110, nullable=False)
    q4_half_moneyLineAway = db.Column(db.String(150), nullable=False)
    q4_half_tt_home = db.Column(db.DECIMAL(7,2), nullable=False)
    q4_half_juice_over_home = db.Column(db.String(150), default=-110, nullable=False)
    q4_half_juice_under_home = db.Column(db.String(150), default=-110, nullable=False)
    q4_half_final_score_home = db.Column(db.Integer,default=0, nullable=False)

    date = db.Column(db.String(100), nullable=False)
    hour = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "home": self.home,
            "away": self.away,

            "spread_away": self.spread_away,
            "spread_home": self.spread_home,

            "juice_spread_away": self.juice_spread_away,
            "juice_spread_home": self.juice_spread_home,

            "moneyLineHome": self.moneyLineHome,
            "moneyLineAway": self.moneyLineAway,

            "total": self.total,
            "juice_total": self.juice_total,

            "tt_away": self.tt_away,
            "tt_home": self.tt_home,

            "juice_over_away": self.juice_over_away,
            "juice_over_home": self.juice_over_home,

            "juice_under_away": self.juice_under_away,
            "juice_under_home": self.juice_under_home,

            "final_score_away": self.final_score_away,
            "final_score_home": self.final_score_home,

            "first_half_spread_away": self.first_half_spread_away,
            "first_half_spread_home": self.first_half_spread_home,

            "first_half_juice_spread_away": self.first_half_juice_spread_away,
            "first_half_juice_spread_home": self.first_half_juice_spread_home,

            "first_half_moneyLineHome": self.first_half_moneyLineHome,
            "first_half_moneyLineAway": self.first_half_moneyLineAway,

            "first_half_total": self.first_half_total,
            "first_half_juice_total": self.final_score_home,

            "first_half_tt_away": self.first_half_tt_away,
            "first_half_tt_home": self.first_half_tt_home,

            "first_half_juice_over_away": self.first_half_juice_over_away,
            "first_half_juice_over_home": self.first_half_juice_over_home,

            "first_half_juice_under_away": self.first_half_juice_under_away,
            "first_half_juice_under_home": self.first_half_juice_under_home,

            "first_half_juice_over_away": self.first_half_juice_over_away,
            "first_half_juice_over_home": self.first_half_juice_over_home,

            "first_half_juice_under_away": self.first_half_juice_under_away,
            "first_half_juice_under_home": self.first_half_juice_under_home,

            "first_half_final_score_away": self.first_half_final_score_away,
            "first_half_final_score_home": self.first_half_final_score_home,

            "second_half_spread_away": self.second_half_spread_away,
            "second_half_spread_home": self.second_half_spread_home,

            "second_half_juice_spread_away": self.second_half_juice_spread_away,
            "second_half_juice_spread_home": self.second_half_juice_spread_home,

            "second_half_moneyLineHome": self.second_half_moneyLineHome,
            "second_half_moneyLineAway": self.second_half_moneyLineAway,

            "second_half_total": self.second_half_total,
            "second_half_juice_total": self.first_half_juice_over_home,

            "second_half_tt_away": self.first_half_juice_over_away,
            "second_half_tt_home": self.first_half_juice_over_home,

            "second_half_juice_over_away": self.second_half_juice_over_away,
            "second_half_juice_over_home": self.second_half_juice_over_home,

            "second_half_juice_under_away": self.second_half_juice_under_away,
            "second_half_juice_under_home": self.second_half_juice_under_home,

            "second_half_final_score_away": self.second_half_final_score_away,
            "second_half_final_score_home": self.second_half_final_score_home,

            "q1_half_spread_away": self.q1_half_spread_away,
            "q1_half_spread_home": self.q1_half_spread_home,
            "q1_half_juice_spread_away": self.q1_half_juice_spread_away,
            "q1_half_juice_spread_home": self.q1_half_juice_spread_home,
            "q1_half_moneyLineHome": self.q1_half_moneyLineHome,
            "q1_half_moneyLineAway": self.q1_half_moneyLineAway,
            "q1_half_total": self.q1_half_total,
            "q1_half_juice_total": self.q1_half_juice_total,
            "q1_half_tt_away": self.q1_half_tt_away,
            "q1_half_tt_home": self.q1_half_tt_home,
            "q1_half_juice_over_away": self.q1_half_juice_over_away,
            "q1_half_juice_over_home": self.q1_half_juice_over_home,
            "q1_half_final_score_away": self.q1_half_final_score_away,
            "q1_half_final_score_home": self.q1_half_final_score_home,

            "q2_half_spread_away": self.q2_half_spread_away,
            "q2_half_spread_home": self.q2_half_spread_home,
            "q2_half_juice_spread_away": self.q2_half_juice_spread_away,
            "q2_half_juice_spread_home": self.q2_half_juice_spread_home,
            "q2_half_moneyLineHome": self.q2_half_moneyLineHome,
            "q2_half_moneyLineAway": self.q2_half_moneyLineAway,
            "q2_half_total": self.q2_half_total,
            "q2_half_juice_total": self.q2_half_juice_total,
            "q2_half_tt_away": self.q2_half_tt_away,
            "q2_half_tt_home": self.q2_half_tt_home,
            "q2_half_juice_over_away": self.q2_half_juice_over_away,
            "q2_half_juice_over_home": self.q2_half_juice_over_home,
            "q2_half_final_score_away": self.q2_half_final_score_away,
            "q2_half_final_score_home": self.q2_half_final_score_home,

            "q3_half_spread_away": self.q3_half_spread_away,
            "q3_half_spread_home": self.q3_half_spread_home,
            "q3_half_juice_spread_away": self.q3_half_juice_spread_away,
            "q3_half_juice_spread_home": self.q3_half_juice_spread_home,
            "q3_half_moneyLineHome": self.q3_half_moneyLineHome,
            "q3_half_moneyLineAway": self.q3_half_moneyLineAway,
            "q3_half_total": self.q3_half_total,
            "q3_half_juice_total": self.q3_half_juice_total,
            "q3_half_tt_away": self.q3_half_tt_away,
            "q3_half_tt_home": self.q3_half_tt_home,
            "q3_half_juice_over_away": self.q3_half_juice_over_away,
            "q3_half_juice_over_home": self.q3_half_juice_over_home,
            "q3_half_final_score_away": self.q3_half_final_score_away,
            "q3_half_final_score_home": self.q3_half_final_score_home,

            "q4_half_spread_away": self.q4_half_spread_away,
            "q4_half_spread_home": self.q4_half_spread_home,
            "q4_half_juice_spread_away": self.q4_half_juice_spread_away,
            "q4_half_juice_spread_home": self.q4_half_juice_spread_home,
            "q4_half_moneyLineHome": self.q4_half_moneyLineHome,
            "q4_half_moneyLineAway": self.q4_half_moneyLineAway,
            "q4_half_total": self.q4_half_total,
            "q4_half_juice_total": self.q4_half_juice_total,
            "q4_half_tt_away": self.q4_half_tt_away,
            "q4_half_tt_home": self.q4_half_tt_home,
            "q4_half_juice_over_away": self.q4_half_juice_over_away,
            "q4_half_juice_over_home": self.q4_half_juice_over_home,
            "q4_half_final_score_away": self.q4_half_final_score_away,
            "q4_half_final_score_home": self.q4_half_final_score_home,

            "date": self.date,
            "hour": self.hour
            # do not serialize the password, its a security breach
        }


class Nhl(db.Model):
    __tablename__ = "nhl"
    id = db.Column(db.Integer, primary_key=True)
    away = db.Column(db.String(150), nullable=False)
    pot_line_away = db.Column(db.DECIMAL(7,2), nullable=False)
    juice_pot_away = db.Column(db.String(150), default=-110, nullable=False)
    moneyLineAway = db.Column(db.String(150), nullable=False)
    total = db.Column(db.DECIMAL(7,2),default=0, nullable=False)
    juice_total = db.Column(db.String(150), default=-110, nullable=False)
    tt_away = db.Column(db.DECIMAL(7,2),default=0, nullable=False)
    juice_over_away = db.Column(db.String(150), default=-110, nullable=False)
    juice_under_away = db.Column(db.String(150), default=-110, nullable=False)
    final_score_away = db.Column(db.Integer,default=0, nullable=False)

    home = db.Column(db.String(150), nullable=False)
    pot_line_home = db.Column(db.DECIMAL(7,2), nullable=False)
    juice_pot_home = db.Column(db.String(150), default=-110, nullable=False)
    moneyLineHome = db.Column(db.String(150), nullable=False)
    tt_home = db.Column(db.DECIMAL(7,2),default=0, nullable=False)
    juice_over_home = db.Column(db.String(150), default=-110, nullable=False)
    juice_under_home = db.Column(db.String(150), default=-110, nullable=False)
    final_score_home = db.Column(db.Integer,default=0, nullable=False)

#-----------------------------------------------------------------------
    pot_away_1Q = db.Column(db.DECIMAL(7,2),default=0, nullable=False)
    juice_pot_away_1Q = db.Column(db.String(150), default=-110, nullable=False)
    moneyLineHome_1Q = db.Column(db.String(150), nullable=False)
    total_1Q = db.Column(db.DECIMAL(7,2),default=0, nullable=False)
    juice_total_1Q = db.Column(db.String(150), default=-110, nullable=False)
    tt_away_1Q = db.Column(db.DECIMAL(7,2), nullable=False)
    juice_over_away_1Q = db.Column(db.String(150), default=-110, nullable=False)
    juice_under_away_1Q = db.Column(db.String(150), default=-110, nullable=False)
    fs_away_1Q = db.Column(db.Integer,default=0, nullable=False)

    pot_home_1Q = db.Column(db.DECIMAL(7,2),default=0, nullable=False)
    juice_pot_home_1Q = db.Column(db.String(150), default=-110, nullable=False)
    moneyLineAway_1Q = db.Column(db.String(150), nullable=False)
    tt_home_1Q = db.Column(db.DECIMAL(7,2), nullable=False)
    juice_over_home_1Q = db.Column(db.String(150), default=-110, nullable=False)
    juice_under_home_1Q = db.Column(db.String(150), default=-110, nullable=False)
    fs_home_1Q = db.Column(db.Integer,default=0, nullable=False)

#----------------------------------------------------------------------
    sa_1Q= db.Column(db.Integer, default=0, nullable=False)
    sh_1Q= db.Column(db.Integer, default=0, nullable=False)
    sa_2Q= db.Column(db.Integer, default=0, nullable=False)
    sh_2Q= db.Column(db.Integer, default=0, nullable=False)
    sa_3Q= db.Column(db.Integer, default=0, nullable=False)
    sh_3Q= db.Column(db.Integer, default=0, nullable=False)

    date = db.Column(db.String(100), nullable=False)
    hour = db.Column(db.String(100), nullable=False)
    def serialize(self):
        return {
            "id": self.id,
            "away": self.away,
            "home": self.home,

            "pot_line_away": self.pot_line_away,
            "pot_line_home": self.pot_line_home,

            "juice_pot_away": self.juice_pot_away,
            "juice_pot_home": self.juice_pot_home,

            "moneyLineHome": self.moneyLineHome,
            "moneyLineAway": self.moneyLineAway,

            "total": self.total,
            "juice_total": self.juice_total,

            "tt_away": self.tt_away,
            "tt_home": self.tt_home,

            "juice_over_away": self.juice_over_away,
            "juice_over_home": self.juice_over_home,

            "juice_under_away": self.juice_under_away,
            "juice_under_home": self.juice_under_home,

            "final_score_away": self.final_score_away,
            "final_score_home": self.final_score_home,

            "pot_away_1Q": self.pot_away_1Q,
            "pot_home_1Q": self.pot_home_1Q,

            "juice_pot_away_1Q": self.juice_pot_away_1Q,
            "juice_pot_home_1Q": self.juice_pot_home_1Q,

            "moneyLineHome_1Q": self.moneyLineHome_1Q,
            "moneyLineAway_1Q": self.moneyLineAway_1Q,

            "total_1Q": self.total_1Q,
            "tt_home_1Q": self.tt_home_1Q,

            "tt_away_1Q": self.tt_away_1Q,
            "tt_home_1Q": self.tt_home_1Q,

            "juice_over_away_1Q": self.juice_over_away_1Q,
            "juice_over_home_1Q": self.juice_over_home_1Q,

            "juice_under_away_1Q": self.juice_under_away_1Q,
            "juice_under_home_1Q": self.juice_under_home_1Q,

            "fs_away_1Q": self.fs_away_1Q,
            "fs_home_1Q": self.fs_home_1Q,

            "sa_1Q": self.sa_1Q,
            "sh_1Q": self.sh_1Q,
            "sa_2Q": self.sa_2Q,
            "sh_2Q": self.sh_2Q,
            "sa_3Q": self.sa_3Q,
            "sh_3Q": self.sh_3Q,
            "date": self.date,
            "hour": self.hour
            # do not serialize the password, its a security breach
        }


class Boxeo(db.Model):
    __tablename__ = "boxeo"
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(150), nullable=False)
    rounds = db.Column(db.Integer, nullable=False)
    location_Fight = db.Column(db.String(100), nullable=False)
    fighter_One = db.Column(db.String(150), nullable=False)
    money_Line_One = db.Column(db.String(150), nullable=False)
    fighter_Two = db.Column(db.String(150), nullable=False)
    money_Line_Two = db.Column(db.String(150), nullable=False)
    winner = db.Column(db.String(150), nullable=False)
    finish_Type = db.Column(db.String(150), nullable=False)
    finish_by = db.Column(db.String(150), nullable=False)
    
    r1_result = db.Column(db.String(150), nullable=False)
    r2_result = db.Column(db.String(150), nullable=False)
    r3_result = db.Column(db.String(150), nullable=False)
    r4_result = db.Column(db.String(150), nullable=False)
    r5_result = db.Column(db.String(150), nullable=False)
    r6_result = db.Column(db.String(150), nullable=False)
    r7_result = db.Column(db.String(150), nullable=False)
    r8_result = db.Column(db.String(150), nullable=False)
    r9_result = db.Column(db.String(150), nullable=False)
    r10_result = db.Column(db.String(150), nullable=False)
    r11_result = db.Column(db.String(150), nullable=False)
    r12_result = db.Column(db.String(150), nullable=False)
    r13_result = db.Column(db.String(150), nullable=False)
    r14_result = db.Column(db.String(150), nullable=False)
    r15_result = db.Column(db.String(150), nullable=False)

    date = db.Column(db.String(100), nullable=False)
    hour = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "event": self.event,
            "rounds": self.rounds,
            "location_Fight": self.location_Fight,
            "fighter_One": self.fighter_One,
            "fighter_Two": self.fighter_Two,
            "money_Line_One": self.money_Line_One,
            "money_Line_Two": self.money_Line_Two,
            "winner": self.winner,
            "finish_Type": self.finish_Type,
            "finish_by": self.finish_by,

            "r1_result": self.r1_result,
            "r2_result": self.r2_result,
            "r3_result": self.r3_result,
            "r4_result": self.r4_result,
            "r5_result": self.r5_result,
            "r6_result": self.r6_result,
            "r7_result": self.r7_result,
            "r8_result": self.r8_result,
            "r9_result": self.r9_result,
            "r10_result": self.r10_result,
            "r11_result": self.r11_result,
            "r12_result": self.r12_result,
            "r13_result": self.r13_result,
            "r14_result": self.r14_result,
            "r15_result": self.r15_result,

            "date": self.date,
            "hour": self.hour
        }


class Mma(db.Model):
    __tablename__ = "mma"
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(150), nullable=False)
    rounds = db.Column(db.Integer, nullable=False)
    location_Fight = db.Column(db.String(100), nullable=False)
    fighter_One = db.Column(db.String(150), nullable=False)
    money_Line_One = db.Column(db.String(150), nullable=False)
    fighter_Two = db.Column(db.String(150), nullable=False)
    money_Line_Two = db.Column(db.String(150), nullable=False)
    winner = db.Column(db.String(150), nullable=False)
    finish_Type = db.Column(db.String(150), nullable=False)
    finish_by = db.Column(db.String(150), nullable=False)
    
    r1_result = db.Column(db.String(150), nullable=False)
    r2_result = db.Column(db.String(150), nullable=False)
    r3_result = db.Column(db.String(150), nullable=False)
    r4_result = db.Column(db.String(150), nullable=False)
    r5_result = db.Column(db.String(150), nullable=False)
    r6_result = db.Column(db.String(150), nullable=False)
    r7_result = db.Column(db.String(150), nullable=False)
    r8_result = db.Column(db.String(150), nullable=False)
    r9_result = db.Column(db.String(150), nullable=False)
    r10_result = db.Column(db.String(150), nullable=False)
    r11_result = db.Column(db.String(150), nullable=False)
    r12_result = db.Column(db.String(150), nullable=False)
    r13_result = db.Column(db.String(150), nullable=False)
    r14_result = db.Column(db.String(150), nullable=False)
    r15_result = db.Column(db.String(150), nullable=False)

    date = db.Column(db.String(100), nullable=False)
    hour = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "event": self.event,
            "rounds": self.rounds,
            "location_Fight": self.location_Fight,
            "fighter_One": self.fighter_One,
            "fighter_Two": self.fighter_Two,
            "money_Line_One": self.money_Line_One,
            "money_Line_Two": self.money_Line_Two,
            "winner": self.winner,
            "finish_Type": self.finish_Type,
            "finish_by": self.finish_by,

            "r1_result": self.r1_result,
            "r2_result": self.r2_result,
            "r3_result": self.r3_result,
            "r4_result": self.r4_result,
            "r5_result": self.r5_result,
            "r6_result": self.r6_result,
            "r7_result": self.r7_result,
            "r8_result": self.r8_result,
            "r9_result": self.r9_result,
            "r10_result": self.r10_result,
            "r11_result": self.r11_result,
            "r12_result": self.r12_result,
            "r13_result": self.r13_result,
            "r14_result": self.r14_result,
            "r15_result": self.r15_result,

            "date": self.date,
            "hour": self.hour
            # do not serialize the password, its a security breach
        }


class Nascar(db.Model):
    __tablename__ = "nascar"
    id = db.Column(db.Integer, primary_key=True)
    race = db.Column(db.String(150), nullable=False)
    track = db.Column(db.Integer, nullable=False)
    country = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    place1 = db.Column(db.String(150), nullable=False)
    place2 = db.Column(db.String(150), nullable=False)
    place3 = db.Column(db.String(150), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    hour = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            "race": self.race,
            "track": self.track,
            "country": self.country,
            "location": self.location,
            "place1": self.place1,
            "place2": self.place2,
            "place3": self.place3,
            "date": self.date,
            "hour": self.hour,
            # do not serialize the password, its a security breach
        }


class Nascar_drivers(db.Model):
    __tablename__ = "nascar_drivers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    country = db.Column(db.String(150), nullable=False)
    sponsor = db.Column(db.String(100), nullable=False)
    engine = db.Column(db.String(150), nullable=False)
    number_car = db.Column(db.Integer, nullable=False)
    odds = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            "name": self.name,
            "country": self.country,
            "sponsor": self.sponsor,
            "engine": self.engine,
            "number_car": self.number_car,
            "odds": self.odds,
            # do not serialize the password, its a security breach
        }
class Match_Ups_Nacar(db.Model):
    __tablename__ = "match_ups_nascar"
    id = db.Column(db.Integer, primary_key=True)
    name1 = db.Column(db.String(150), nullable=False)
    mu1 = db.Column(db.String(150), nullable=False)
    name2 = db.Column(db.String(150), nullable=False)
    mu2 = db.Column(db.String(150), nullable=False)

    def serialize(self):
        return {
            "name1": self.name1,
            "name2": self.name2,
            "mu1": self.mu1,
            "mu2": self.mu2,
            # do not serialize the password, its a security breach
        }

class Golf(db.Model):
    __tablename__ = "golf"
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    place1 = db.Column(db.String(150), nullable=False)
    place2 = db.Column(db.String(150), nullable=False)
    place3 = db.Column(db.String(150), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    hour = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            "event": self.event,
            "location": self.location,
            "place1": self.place1,
            "place2": self.place2,
            "place3": self.place3,
            "date": self.date,
            "hour": self.hour,
            # do not serialize the password, its a security breach
        }


class Golfer(db.Model):
    __tablename__ = "golfer"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    country = db.Column(db.String(150), nullable=False)
    odds = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            "name": self.name,
            "country": self.country,
            "odds": self.money_line
            # do not serialize the password, its a security breach
        }


class News(db.Model):
    __tablename__ = "news"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    url_image = db.Column(db.String(150), nullable=False)
    short_description = db.Column(db.String(1000), nullable=False)
    news_post = db.Column(db.Text, nullable=False)
    written = db.Column(db.String(150), nullable=False)
    date = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            "title": self.title,
            "short_description": self.short_description,
            "url_image": self.url_image,
            "news_post": self.news_post,
            "written": self.written,
            "date": self.date
            # do not serialize the password, its a security breach
        }
