import datetime
import pytz
from TippSpiel2023.TippSpiel2023.data.statistics import Statistics
from TippSpiel2023.TippSpiel2023.data.teams import Teams, Team
from decimal import Decimal, ROUND_HALF_UP


def get_winner(team1: Team, team2: Team):
    score1 = score2 = 0
    score1 += Decimal(team1.offense_exp * 100 / Statistics.offense_df[team1.list[0]].max()).quantize(Decimal('1.1111'), rounding=ROUND_HALF_UP)
    score2 += Decimal(team2.offense_exp * 100 / Statistics.offense_df[team2.list[0]].max()).quantize(Decimal('1.1111'), rounding=ROUND_HALF_UP)
    score1 += Decimal(team1.offense_yp * 100 / Statistics.offense_df[team1.list[1]].max()).quantize(Decimal('1.1111'), rounding=ROUND_HALF_UP)
    score2 += Decimal(team2.offense_yp * 100 / Statistics.offense_df[team2.list[1]].max()).quantize(Decimal('1.1111'), rounding=ROUND_HALF_UP)
    score1 += Decimal(team1.offense_1std * 100 / Statistics.offense_df[team1.list[2]].max()).quantize(Decimal('1.1111'), rounding=ROUND_HALF_UP)
    score2 += Decimal(team2.offense_1std * 100 / Statistics.offense_df[team2.list[2]].max()).quantize(Decimal('1.1111'), rounding=ROUND_HALF_UP)
    score1 += Decimal(team1.offense_pass_td * 100 / Statistics.offense_df[team1.list[3]].max()).quantize(Decimal('1.1111'), rounding=ROUND_HALF_UP)
    score2 += Decimal(team2.offense_pass_td * 100 / Statistics.offense_df[team2.list[3]].max()).quantize(Decimal('1.1111'), rounding=ROUND_HALF_UP)
    score1 += Decimal(team1.defense_pa * 100 / Statistics.offense_df[team1.list[4]].max()).quantize(Decimal('1.1111'), rounding=ROUND_HALF_UP)
    score2 += Decimal(team2.defense_pa * 100 / Statistics.offense_df[team2.list[4]].max()).quantize(Decimal('1.1111'), rounding=ROUND_HALF_UP)
    score1 += Decimal((Statistics.defense_df[team1.list[5]].min() - team1.defense_yp) * 100 / Statistics.defense_df[team1.list[5]].min()).quantize(Decimal('1.1111'), rounding=ROUND_HALF_UP)
    score2 += Decimal((Statistics.defense_df[team2.list[5]].min() - team2.defense_yp) * 100 / Statistics.defense_df[team2.list[5]].min()).quantize(Decimal('1.1111'), rounding=ROUND_HALF_UP)
    score1 += Decimal((Statistics.defense_df[team1.list[6]].min() - team1.defense_1std) * 100 / Statistics.defense_df[team1.list[6]].min()).quantize(Decimal('1.1111'), rounding=ROUND_HALF_UP)
    score2 += Decimal((Statistics.defense_df[team2.list[6]].min() - team2.defense_1std) * 100 / Statistics.defense_df[team2.list[6]].min()).quantize(Decimal('1.1111'), rounding=ROUND_HALF_UP)
    print(score1, score2)
    score1 += Decimal((Statistics.defense_df[team1.list[7]].min() - team1.defense_rush_td) * 100 / Statistics.defense_df[team1.list[7]].min()).quantize(Decimal('1.1111'), rounding=ROUND_HALF_UP)
    score2 += Decimal((Statistics.defense_df[team2.list[7]].min() - team2.defense_rush_td) * 100 / Statistics.defense_df[team2.list[7]].min()).quantize(Decimal('1.1111'), rounding=ROUND_HALF_UP)
    print(score1, score2)
    winner = team1.name if score1 > score2 else team2.name
    return f'{team1.name} vs. {team2.name} : {winner}'


class ThisWeek:
    temp_team_list = Teams.all.copy()
    timezone = pytz.timezone('Europe/Berlin')
    week_count = int(datetime.datetime.now(tz=timezone).strftime("%U"))
    count = 0
    for team in Teams.all:
        team2 = 0
        temp_string = Statistics.schedule_df[45].loc[Statistics.schedule_df['Teams'] == Teams.all[team].name][count]
        if temp_string.startswith(('@', 'vs.')):
            temp_string = temp_string.split()[1]
            for team3 in Teams.all:
                if temp_string == Teams.all[team3].short_name and team3 in temp_team_list:
                    team2 = team3
                    print(get_winner(Teams.all[team], Teams.all[team2]))
                    del temp_team_list[team]
                    del temp_team_list[team2]
        count += 1

