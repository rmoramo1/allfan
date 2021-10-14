"""empty message

Revision ID: 6c2c77f738b3
Revises: 
Create Date: 2021-10-14 15:51:16.599623

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c2c77f738b3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('boxeo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event', sa.String(length=150), nullable=False),
    sa.Column('rounds', sa.Integer(), nullable=False),
    sa.Column('location_Fight', sa.String(length=100), nullable=False),
    sa.Column('fighter_One', sa.String(length=150), nullable=False),
    sa.Column('money_Line_One', sa.String(length=150), nullable=False),
    sa.Column('fighter_Two', sa.String(length=150), nullable=False),
    sa.Column('money_Line_Two', sa.String(length=150), nullable=False),
    sa.Column('winner', sa.String(length=150), nullable=False),
    sa.Column('finish_Type', sa.String(length=150), nullable=False),
    sa.Column('finish_by', sa.String(length=150), nullable=False),
    sa.Column('r1_result', sa.String(length=150), nullable=False),
    sa.Column('r2_result', sa.String(length=150), nullable=False),
    sa.Column('r3_result', sa.String(length=150), nullable=False),
    sa.Column('r4_result', sa.String(length=150), nullable=False),
    sa.Column('r5_result', sa.String(length=150), nullable=False),
    sa.Column('r6_result', sa.String(length=150), nullable=False),
    sa.Column('r7_result', sa.String(length=150), nullable=False),
    sa.Column('r8_result', sa.String(length=150), nullable=False),
    sa.Column('r9_result', sa.String(length=150), nullable=False),
    sa.Column('r10_result', sa.String(length=150), nullable=False),
    sa.Column('r11_result', sa.String(length=150), nullable=False),
    sa.Column('r12_result', sa.String(length=150), nullable=False),
    sa.Column('r13_result', sa.String(length=150), nullable=False),
    sa.Column('r14_result', sa.String(length=150), nullable=False),
    sa.Column('r15_result', sa.String(length=150), nullable=False),
    sa.Column('date', sa.String(length=100), nullable=False),
    sa.Column('hour', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('golf',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event', sa.String(length=150), nullable=False),
    sa.Column('location', sa.String(length=150), nullable=False),
    sa.Column('place1', sa.String(length=150), nullable=False),
    sa.Column('place2', sa.String(length=150), nullable=False),
    sa.Column('place3', sa.String(length=150), nullable=False),
    sa.Column('date', sa.String(length=100), nullable=False),
    sa.Column('hour', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('golfer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('country', sa.String(length=150), nullable=False),
    sa.Column('odds', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('match_ups_nascar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name1', sa.String(length=150), nullable=False),
    sa.Column('mu1', sa.String(length=150), nullable=False),
    sa.Column('name2', sa.String(length=150), nullable=False),
    sa.Column('mu2', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mlb',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('away', sa.String(length=150), nullable=False),
    sa.Column('home', sa.String(length=150), nullable=False),
    sa.Column('rl_away', sa.String(length=150), nullable=False),
    sa.Column('rl_home', sa.String(length=150), nullable=False),
    sa.Column('juice_rl_away', sa.String(length=150), nullable=False),
    sa.Column('juice_rl_home', sa.String(length=150), nullable=False),
    sa.Column('moneyLineAway', sa.String(length=150), nullable=False),
    sa.Column('moneyLineHome', sa.String(length=150), nullable=False),
    sa.Column('total', sa.Integer(), nullable=False),
    sa.Column('juice_total_over', sa.String(length=150), nullable=False),
    sa.Column('juice_total_under', sa.String(length=150), nullable=False),
    sa.Column('tt_away', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('juice_over_away', sa.String(length=150), nullable=False),
    sa.Column('juice_under_away', sa.String(length=150), nullable=False),
    sa.Column('tt_home', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('juice_over_home', sa.String(length=150), nullable=False),
    sa.Column('juice_under_home', sa.String(length=150), nullable=False),
    sa.Column('final_score_away', sa.Integer(), nullable=False),
    sa.Column('final_score_home', sa.Integer(), nullable=False),
    sa.Column('rl_away_f5', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('juice_rl_away_f5', sa.String(length=150), nullable=False),
    sa.Column('moneyLineAway_f5', sa.String(length=150), nullable=False),
    sa.Column('total_f5', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('juice_total_f5', sa.String(length=150), nullable=False),
    sa.Column('tt_away_f5', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('juice_over_away_f5', sa.String(length=150), nullable=False),
    sa.Column('juice_under_away_f5', sa.String(length=150), nullable=False),
    sa.Column('fs_away_f5', sa.Integer(), nullable=False),
    sa.Column('rl_home_f5', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('juice_rl_home_f5', sa.String(length=150), nullable=False),
    sa.Column('moneyLineHome_f5', sa.String(length=150), nullable=False),
    sa.Column('tt_home_f5', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('juice_over_home_f5', sa.String(length=150), nullable=False),
    sa.Column('juice_under_home_f5', sa.String(length=150), nullable=False),
    sa.Column('fs_home_f5', sa.Integer(), nullable=False),
    sa.Column('sa_2inning', sa.Integer(), nullable=False),
    sa.Column('sh_2inning', sa.Integer(), nullable=False),
    sa.Column('sa_3inning', sa.Integer(), nullable=False),
    sa.Column('sh_3inning', sa.Integer(), nullable=False),
    sa.Column('sa_4inning', sa.Integer(), nullable=False),
    sa.Column('sh_4inning', sa.Integer(), nullable=False),
    sa.Column('sa_5inning', sa.Integer(), nullable=False),
    sa.Column('sh_5inning', sa.Integer(), nullable=False),
    sa.Column('sa_6inning', sa.Integer(), nullable=False),
    sa.Column('sh_6inning', sa.Integer(), nullable=False),
    sa.Column('sa_7inning', sa.Integer(), nullable=False),
    sa.Column('sh_7inning', sa.Integer(), nullable=False),
    sa.Column('sa_8inning', sa.Integer(), nullable=False),
    sa.Column('sh_8inning', sa.Integer(), nullable=False),
    sa.Column('sa_9inning', sa.Integer(), nullable=False),
    sa.Column('sh_9inning', sa.Integer(), nullable=False),
    sa.Column('sa_10inning', sa.Integer(), nullable=False),
    sa.Column('sh_10inning', sa.Integer(), nullable=False),
    sa.Column('sa_11inning', sa.Integer(), nullable=False),
    sa.Column('sh_11inning', sa.Integer(), nullable=False),
    sa.Column('sa_12inning', sa.Integer(), nullable=False),
    sa.Column('sh_12inning', sa.Integer(), nullable=False),
    sa.Column('sa_13inning', sa.Integer(), nullable=False),
    sa.Column('sh_13inning', sa.Integer(), nullable=False),
    sa.Column('sa_14inning', sa.Integer(), nullable=False),
    sa.Column('sh_14inning', sa.Integer(), nullable=False),
    sa.Column('sa_15inning', sa.Integer(), nullable=False),
    sa.Column('sh_15inning', sa.Integer(), nullable=False),
    sa.Column('sa_16inning', sa.Integer(), nullable=False),
    sa.Column('sh_16inning', sa.Integer(), nullable=False),
    sa.Column('sa_17inning', sa.Integer(), nullable=False),
    sa.Column('sh_17inning', sa.Integer(), nullable=False),
    sa.Column('sa_18inning', sa.Integer(), nullable=False),
    sa.Column('sh_18inning', sa.Integer(), nullable=False),
    sa.Column('sa_19inning', sa.Integer(), nullable=False),
    sa.Column('sh_19inning', sa.Integer(), nullable=False),
    sa.Column('sa_20inning', sa.Integer(), nullable=False),
    sa.Column('sh_20inning', sa.Integer(), nullable=False),
    sa.Column('sa_21inning', sa.Integer(), nullable=False),
    sa.Column('sh_21inning', sa.Integer(), nullable=False),
    sa.Column('sa_22inning', sa.Integer(), nullable=False),
    sa.Column('sh_22inning', sa.Integer(), nullable=False),
    sa.Column('sa_23inning', sa.Integer(), nullable=False),
    sa.Column('sh_23inning', sa.Integer(), nullable=False),
    sa.Column('sa_24inning', sa.Integer(), nullable=False),
    sa.Column('sh_24inning', sa.Integer(), nullable=False),
    sa.Column('sa_1inning', sa.Integer(), nullable=False),
    sa.Column('sh_1inning', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(length=100), nullable=False),
    sa.Column('hour', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mma',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event', sa.String(length=150), nullable=False),
    sa.Column('rounds', sa.Integer(), nullable=False),
    sa.Column('location_Fight', sa.String(length=100), nullable=False),
    sa.Column('fighter_One', sa.String(length=150), nullable=False),
    sa.Column('money_Line_One', sa.String(length=150), nullable=False),
    sa.Column('fighter_Two', sa.String(length=150), nullable=False),
    sa.Column('money_Line_Two', sa.String(length=150), nullable=False),
    sa.Column('winner', sa.String(length=150), nullable=False),
    sa.Column('finish_Type', sa.String(length=150), nullable=False),
    sa.Column('finish_by', sa.String(length=150), nullable=False),
    sa.Column('r1_result', sa.String(length=150), nullable=False),
    sa.Column('r2_result', sa.String(length=150), nullable=False),
    sa.Column('r3_result', sa.String(length=150), nullable=False),
    sa.Column('r4_result', sa.String(length=150), nullable=False),
    sa.Column('r5_result', sa.String(length=150), nullable=False),
    sa.Column('r6_result', sa.String(length=150), nullable=False),
    sa.Column('r7_result', sa.String(length=150), nullable=False),
    sa.Column('r8_result', sa.String(length=150), nullable=False),
    sa.Column('r9_result', sa.String(length=150), nullable=False),
    sa.Column('r10_result', sa.String(length=150), nullable=False),
    sa.Column('r11_result', sa.String(length=150), nullable=False),
    sa.Column('r12_result', sa.String(length=150), nullable=False),
    sa.Column('r13_result', sa.String(length=150), nullable=False),
    sa.Column('r14_result', sa.String(length=150), nullable=False),
    sa.Column('r15_result', sa.String(length=150), nullable=False),
    sa.Column('date', sa.String(length=100), nullable=False),
    sa.Column('hour', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('nascar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('race', sa.String(length=150), nullable=False),
    sa.Column('track', sa.Integer(), nullable=False),
    sa.Column('country', sa.String(length=150), nullable=False),
    sa.Column('location', sa.String(length=100), nullable=False),
    sa.Column('place1', sa.String(length=150), nullable=False),
    sa.Column('place2', sa.String(length=150), nullable=False),
    sa.Column('place3', sa.String(length=150), nullable=False),
    sa.Column('date', sa.String(length=100), nullable=False),
    sa.Column('hour', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('nascar_drivers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('country', sa.String(length=150), nullable=False),
    sa.Column('sponsor', sa.String(length=100), nullable=False),
    sa.Column('engine', sa.String(length=150), nullable=False),
    sa.Column('number_car', sa.Integer(), nullable=False),
    sa.Column('odds', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('nba',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('away', sa.String(length=150), nullable=False),
    sa.Column('home', sa.String(length=150), nullable=False),
    sa.Column('spread_away', sa.String(length=150), nullable=False),
    sa.Column('spread_home', sa.String(length=150), nullable=False),
    sa.Column('juice_spread_away', sa.String(length=150), nullable=False),
    sa.Column('juice_spread_home', sa.String(length=150), nullable=False),
    sa.Column('moneyLineAway', sa.String(length=150), nullable=False),
    sa.Column('moneyLineHome', sa.String(length=150), nullable=False),
    sa.Column('total', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('juice_total_over', sa.String(length=150), nullable=False),
    sa.Column('juice_total_under', sa.String(length=150), nullable=False),
    sa.Column('tt_away', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('juice_over_away', sa.String(length=150), nullable=False),
    sa.Column('juice_under_away', sa.String(length=150), nullable=False),
    sa.Column('tt_home', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('juice_over_home', sa.String(length=150), nullable=False),
    sa.Column('juice_under_home', sa.String(length=150), nullable=False),
    sa.Column('final_score_away', sa.Integer(), nullable=False),
    sa.Column('final_score_home', sa.Integer(), nullable=False),
    sa.Column('first_half_spread_away', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('first_half_juice_spread_away', sa.String(length=150), nullable=False),
    sa.Column('first_half_moneyLineAway', sa.String(length=150), nullable=False),
    sa.Column('first_half_total', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('first_half_juice_total', sa.String(length=150), nullable=False),
    sa.Column('first_half_tt_away', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('first_half_juice_over_away', sa.String(length=150), nullable=False),
    sa.Column('first_half_juice_under_away', sa.String(length=150), nullable=False),
    sa.Column('first_half_final_score_away', sa.Integer(), nullable=False),
    sa.Column('first_half_spread_home', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('first_half_juice_spread_home', sa.String(length=150), nullable=False),
    sa.Column('first_half_moneyLineHome', sa.String(length=150), nullable=False),
    sa.Column('first_half_tt_home', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('first_half_juice_over_home', sa.String(length=150), nullable=False),
    sa.Column('first_half_juice_under_home', sa.String(length=150), nullable=False),
    sa.Column('first_half_final_score_home', sa.Integer(), nullable=False),
    sa.Column('second_half_spread_away', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('second_half_juice_spread_away', sa.String(length=150), nullable=False),
    sa.Column('second_half_moneyLineHome', sa.String(length=150), nullable=False),
    sa.Column('second_half_total', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('second_half_juice_total', sa.String(length=150), nullable=False),
    sa.Column('second_half_tt_away', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('second_half_juice_over_away', sa.String(length=150), nullable=False),
    sa.Column('second_half_juice_under_away', sa.String(length=150), nullable=False),
    sa.Column('second_half_final_score_away', sa.Integer(), nullable=False),
    sa.Column('second_half_spread_home', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('second_half_juice_spread_home', sa.String(length=150), nullable=False),
    sa.Column('second_half_moneyLineAway', sa.String(length=150), nullable=False),
    sa.Column('second_half_tt_home', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('second_half_juice_over_home', sa.String(length=150), nullable=False),
    sa.Column('second_half_juice_under_home', sa.String(length=150), nullable=False),
    sa.Column('second_half_final_score_home', sa.Integer(), nullable=False),
    sa.Column('q1_half_spread_away', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q1_half_juice_spread_away', sa.String(length=150), nullable=False),
    sa.Column('q1_half_moneyLineHome', sa.String(length=150), nullable=False),
    sa.Column('q1_half_total', sa.Integer(), nullable=False),
    sa.Column('q1_half_juice_total', sa.String(length=150), nullable=False),
    sa.Column('q1_half_tt_away', sa.Integer(), nullable=False),
    sa.Column('q1_half_juice_over_away', sa.String(length=150), nullable=False),
    sa.Column('q1_half_juice_under_away', sa.String(length=150), nullable=False),
    sa.Column('q1_half_final_score_away', sa.Integer(), nullable=False),
    sa.Column('q1_half_spread_home', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q1_half_juice_spread_home', sa.String(length=150), nullable=False),
    sa.Column('q1_half_moneyLineAway', sa.String(length=150), nullable=False),
    sa.Column('q1_half_tt_home', sa.Integer(), nullable=False),
    sa.Column('q1_half_juice_over_home', sa.String(length=150), nullable=False),
    sa.Column('q1_half_juice_under_home', sa.String(length=150), nullable=False),
    sa.Column('q1_half_final_score_home', sa.Integer(), nullable=False),
    sa.Column('q2_half_spread_away', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q2_half_juice_spread_away', sa.String(length=150), nullable=False),
    sa.Column('q2_half_moneyLineAway', sa.String(length=150), nullable=False),
    sa.Column('q2_half_total', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q2_half_juice_total', sa.String(length=150), nullable=False),
    sa.Column('q2_half_tt_away', sa.Integer(), nullable=False),
    sa.Column('q2_half_juice_over_away', sa.String(length=150), nullable=False),
    sa.Column('q2_half_juice_under_away', sa.String(length=150), nullable=False),
    sa.Column('q2_half_final_score_away', sa.Integer(), nullable=False),
    sa.Column('q2_half_spread_home', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q2_half_juice_spread_home', sa.String(length=150), nullable=False),
    sa.Column('q2_half_moneyLineHome', sa.String(length=150), nullable=False),
    sa.Column('q2_half_tt_home', sa.Integer(), nullable=False),
    sa.Column('q2_half_juice_over_home', sa.String(length=150), nullable=False),
    sa.Column('q2_half_juice_under_home', sa.String(length=150), nullable=False),
    sa.Column('q2_half_final_score_home', sa.Integer(), nullable=False),
    sa.Column('q3_half_spread_away', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q3_half_juice_spread_away', sa.String(length=150), nullable=False),
    sa.Column('q3_half_moneyLineAway', sa.String(length=150), nullable=False),
    sa.Column('q3_half_total', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q3_half_juice_total', sa.String(length=150), nullable=False),
    sa.Column('q3_half_tt_away', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q3_half_juice_over_away', sa.String(length=150), nullable=False),
    sa.Column('q3_half_juice_under_away', sa.String(length=150), nullable=False),
    sa.Column('q3_half_final_score_away', sa.Integer(), nullable=False),
    sa.Column('q3_half_spread_home', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q3_half_juice_spread_home', sa.String(length=150), nullable=False),
    sa.Column('q3_half_moneyLineHome', sa.String(length=150), nullable=False),
    sa.Column('q3_half_tt_home', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q3_half_juice_over_home', sa.String(length=150), nullable=False),
    sa.Column('q3_half_juice_under_home', sa.String(length=150), nullable=False),
    sa.Column('q3_half_final_score_home', sa.Integer(), nullable=False),
    sa.Column('q4_half_spread_away', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q4_half_juice_spread_away', sa.String(length=150), nullable=False),
    sa.Column('q4_half_moneyLineHome', sa.String(length=150), nullable=False),
    sa.Column('q4_half_total', sa.Integer(), nullable=False),
    sa.Column('q4_half_juice_total', sa.String(length=150), nullable=False),
    sa.Column('q4_half_tt_away', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q4_half_juice_over_away', sa.String(length=150), nullable=False),
    sa.Column('q4_half_juice_under_away', sa.String(length=150), nullable=False),
    sa.Column('q4_half_final_score_away', sa.Integer(), nullable=False),
    sa.Column('q4_half_spread_home', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q4_half_juice_spread_home', sa.String(length=150), nullable=False),
    sa.Column('q4_half_moneyLineAway', sa.String(length=150), nullable=False),
    sa.Column('q4_half_tt_home', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q4_half_juice_over_home', sa.String(length=150), nullable=False),
    sa.Column('q4_half_juice_under_home', sa.String(length=150), nullable=False),
    sa.Column('q4_half_final_score_home', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(length=100), nullable=False),
    sa.Column('hour', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('news',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=False),
    sa.Column('url_image', sa.String(length=150), nullable=False),
    sa.Column('short_description', sa.String(length=1000), nullable=False),
    sa.Column('news_post', sa.Text(), nullable=False),
    sa.Column('written', sa.String(length=150), nullable=False),
    sa.Column('date', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('nfl',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('away', sa.String(length=150), nullable=False),
    sa.Column('home', sa.String(length=150), nullable=False),
    sa.Column('spread_away', sa.String(length=150), nullable=False),
    sa.Column('spread_home', sa.String(length=150), nullable=False),
    sa.Column('juice_spread_away', sa.String(length=150), nullable=False),
    sa.Column('juice_spread_home', sa.String(length=150), nullable=False),
    sa.Column('moneyLineAway', sa.String(length=150), nullable=False),
    sa.Column('moneyLineHome', sa.String(length=150), nullable=False),
    sa.Column('total', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('juice_total_over', sa.String(length=150), nullable=False),
    sa.Column('juice_total_under', sa.String(length=150), nullable=False),
    sa.Column('tt_away', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('juice_over_away', sa.String(length=150), nullable=False),
    sa.Column('juice_under_away', sa.String(length=150), nullable=False),
    sa.Column('tt_home', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('juice_over_home', sa.String(length=150), nullable=False),
    sa.Column('juice_under_home', sa.String(length=150), nullable=False),
    sa.Column('final_score_away', sa.Integer(), nullable=False),
    sa.Column('final_score_home', sa.Integer(), nullable=False),
    sa.Column('first_half_spread_away', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('first_half_juice_spread_away', sa.String(length=150), nullable=False),
    sa.Column('first_half_moneyLineHome', sa.String(length=150), nullable=False),
    sa.Column('first_half_total', sa.Integer(), nullable=False),
    sa.Column('first_half_juice_total', sa.String(length=150), nullable=False),
    sa.Column('first_half_tt_away', sa.Integer(), nullable=False),
    sa.Column('first_half_juice_over_away', sa.String(length=150), nullable=False),
    sa.Column('first_half_juice_under_away', sa.String(length=150), nullable=False),
    sa.Column('first_half_final_score_away', sa.Integer(), nullable=False),
    sa.Column('first_half_spread_home', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('first_half_juice_spread_home', sa.String(length=150), nullable=False),
    sa.Column('first_half_moneyLineAway', sa.String(length=150), nullable=False),
    sa.Column('first_half_tt_home', sa.Integer(), nullable=False),
    sa.Column('first_half_juice_over_home', sa.String(length=150), nullable=False),
    sa.Column('first_half_juice_under_home', sa.String(length=150), nullable=False),
    sa.Column('first_half_final_score_home', sa.Integer(), nullable=False),
    sa.Column('second_half_spread_away', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('second_half_juice_spread_away', sa.String(length=150), nullable=False),
    sa.Column('second_half_moneyLineHome', sa.String(length=150), nullable=False),
    sa.Column('second_half_total', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('second_half_juice_total', sa.String(length=150), nullable=False),
    sa.Column('second_half_tt_away', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('second_half_juice_over_away', sa.String(length=150), nullable=False),
    sa.Column('second_half_juice_under_away', sa.String(length=150), nullable=False),
    sa.Column('second_half_final_score_away', sa.Integer(), nullable=False),
    sa.Column('second_half_spread_home', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('second_half_juice_spread_home', sa.String(length=150), nullable=False),
    sa.Column('second_half_moneyLineAway', sa.String(length=150), nullable=False),
    sa.Column('second_half_tt_home', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('second_half_juice_over_home', sa.String(length=150), nullable=False),
    sa.Column('second_half_juice_under_home', sa.String(length=150), nullable=False),
    sa.Column('second_half_final_score_home', sa.Integer(), nullable=False),
    sa.Column('q1_half_spread_away', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q1_half_juice_spread_away', sa.String(length=150), nullable=False),
    sa.Column('q1_half_moneyLineHome', sa.String(length=150), nullable=False),
    sa.Column('q1_half_total', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q1_half_juice_total', sa.String(length=150), nullable=False),
    sa.Column('q1_half_tt_away', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q1_half_juice_over_away', sa.String(length=150), nullable=False),
    sa.Column('q1_half_juice_under_away', sa.String(length=150), nullable=False),
    sa.Column('q1_half_final_score_away', sa.Integer(), nullable=False),
    sa.Column('q1_half_spread_home', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q1_half_juice_spread_home', sa.String(length=150), nullable=False),
    sa.Column('q1_half_moneyLineAway', sa.String(length=150), nullable=False),
    sa.Column('q1_half_tt_home', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q1_half_juice_over_home', sa.String(length=150), nullable=False),
    sa.Column('q1_half_juice_under_home', sa.String(length=150), nullable=False),
    sa.Column('q1_half_final_score_home', sa.Integer(), nullable=False),
    sa.Column('q2_half_spread_away', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q2_half_juice_spread_away', sa.String(length=150), nullable=False),
    sa.Column('q2_half_moneyLineHome', sa.String(length=150), nullable=False),
    sa.Column('q2_half_total', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q2_half_juice_total', sa.String(length=150), nullable=False),
    sa.Column('q2_half_tt_away', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q2_half_juice_over_away', sa.String(length=150), nullable=False),
    sa.Column('q2_half_juice_under_away', sa.String(length=150), nullable=False),
    sa.Column('q2_half_final_score_away', sa.Integer(), nullable=False),
    sa.Column('q2_half_spread_home', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q2_half_juice_spread_home', sa.String(length=150), nullable=False),
    sa.Column('q2_half_moneyLineAway', sa.String(length=150), nullable=False),
    sa.Column('q2_half_tt_home', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q2_half_juice_over_home', sa.String(length=150), nullable=False),
    sa.Column('q2_half_juice_under_home', sa.String(length=150), nullable=False),
    sa.Column('q2_half_final_score_home', sa.Integer(), nullable=False),
    sa.Column('q3_half_spread_away', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q3_half_juice_spread_away', sa.String(length=150), nullable=False),
    sa.Column('q3_half_moneyLineHome', sa.String(length=150), nullable=False),
    sa.Column('q3_half_total', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q3_half_juice_total', sa.String(length=150), nullable=False),
    sa.Column('q3_half_tt_away', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q3_half_juice_over_away', sa.String(length=150), nullable=False),
    sa.Column('q3_half_juice_under_away', sa.String(length=150), nullable=False),
    sa.Column('q3_half_final_score_away', sa.Integer(), nullable=False),
    sa.Column('q3_half_spread_home', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q3_half_juice_spread_home', sa.String(length=150), nullable=False),
    sa.Column('q3_half_moneyLineAway', sa.String(length=150), nullable=False),
    sa.Column('q3_half_tt_home', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q3_half_juice_over_home', sa.String(length=150), nullable=False),
    sa.Column('q3_half_juice_under_home', sa.String(length=150), nullable=False),
    sa.Column('q3_half_final_score_home', sa.Integer(), nullable=False),
    sa.Column('q4_half_spread_away', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q4_half_juice_spread_away', sa.String(length=150), nullable=False),
    sa.Column('q4_half_moneyLineHome', sa.String(length=150), nullable=False),
    sa.Column('q4_half_total', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q4_half_juice_total', sa.String(length=150), nullable=False),
    sa.Column('q4_half_tt_away', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q4_half_juice_over_away', sa.String(length=150), nullable=False),
    sa.Column('q4_half_juice_under_away', sa.String(length=150), nullable=False),
    sa.Column('q4_half_final_score_away', sa.Integer(), nullable=False),
    sa.Column('q4_half_spread_home', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q4_half_juice_spread_home', sa.String(length=150), nullable=False),
    sa.Column('q4_half_moneyLineAway', sa.String(length=150), nullable=False),
    sa.Column('q4_half_tt_home', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('q4_half_juice_over_home', sa.String(length=150), nullable=False),
    sa.Column('q4_half_juice_under_home', sa.String(length=150), nullable=False),
    sa.Column('q4_half_final_score_home', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(length=100), nullable=False),
    sa.Column('hour', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('nhl',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('away', sa.String(length=150), nullable=False),
    sa.Column('home', sa.String(length=150), nullable=False),
    sa.Column('pot_line_away', sa.String(length=150), nullable=False),
    sa.Column('pot_line_home', sa.String(length=150), nullable=False),
    sa.Column('juice_pot_away', sa.String(length=150), nullable=False),
    sa.Column('juice_pot_home', sa.String(length=150), nullable=False),
    sa.Column('moneyLineAway', sa.String(length=150), nullable=False),
    sa.Column('moneyLineHome', sa.String(length=150), nullable=False),
    sa.Column('total', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('juice_total_over', sa.String(length=150), nullable=False),
    sa.Column('juice_total_under', sa.String(length=150), nullable=False),
    sa.Column('tt_away', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('juice_over_away', sa.String(length=150), nullable=False),
    sa.Column('juice_under_away', sa.String(length=150), nullable=False),
    sa.Column('final_score_away', sa.Integer(), nullable=False),
    sa.Column('tt_home', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('juice_over_home', sa.String(length=150), nullable=False),
    sa.Column('juice_under_home', sa.String(length=150), nullable=False),
    sa.Column('final_score_home', sa.Integer(), nullable=False),
    sa.Column('pot_away_1Q', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('juice_pot_away_1Q', sa.String(length=150), nullable=False),
    sa.Column('moneyLineHome_1Q', sa.String(length=150), nullable=False),
    sa.Column('total_1Q', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('juice_total_1Q', sa.String(length=150), nullable=False),
    sa.Column('tt_away_1Q', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('juice_over_away_1Q', sa.String(length=150), nullable=False),
    sa.Column('juice_under_away_1Q', sa.String(length=150), nullable=False),
    sa.Column('fs_away_1Q', sa.Integer(), nullable=False),
    sa.Column('pot_home_1Q', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('juice_pot_home_1Q', sa.String(length=150), nullable=False),
    sa.Column('moneyLineAway_1Q', sa.String(length=150), nullable=False),
    sa.Column('tt_home_1Q', sa.DECIMAL(precision=7, scale=2), nullable=False),
    sa.Column('juice_over_home_1Q', sa.String(length=150), nullable=False),
    sa.Column('juice_under_home_1Q', sa.String(length=150), nullable=False),
    sa.Column('fs_home_1Q', sa.Integer(), nullable=False),
    sa.Column('sa_1Q', sa.Integer(), nullable=False),
    sa.Column('sh_1Q', sa.Integer(), nullable=False),
    sa.Column('sa_2Q', sa.Integer(), nullable=False),
    sa.Column('sh_2Q', sa.Integer(), nullable=False),
    sa.Column('sa_3Q', sa.Integer(), nullable=False),
    sa.Column('sh_3Q', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(length=100), nullable=False),
    sa.Column('hour', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('nhl')
    op.drop_table('nfl')
    op.drop_table('news')
    op.drop_table('nba')
    op.drop_table('nascar_drivers')
    op.drop_table('nascar')
    op.drop_table('mma')
    op.drop_table('mlb')
    op.drop_table('match_ups_nascar')
    op.drop_table('golfer')
    op.drop_table('golf')
    op.drop_table('boxeo')
    # ### end Alembic commands ###
