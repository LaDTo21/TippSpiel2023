import datetime
import pytz
from TippSpiel2023.TippSpiel_2023.data.statistics import Statistics
from TippSpiel2023.TippSpiel_2023.data.teams import Teams, Team
from decimal import Decimal, ROUND_HALF_UP


class ThisWeek:
    @staticmethod
    def min_max_normalization(x, min_value, max_value):
        return Decimal((x - min_value) / (max_value - min_value)).quantize(Decimal('0.0000'), rounding=ROUND_HALF_UP)

    @staticmethod
    def get_winner(team1: Team, team2: Team):
        offense_df = Statistics.saved_offense_df
        defense_df = Statistics.saved_defense_df
        score1 = score2 = 0
        score1 += ThisWeek.min_max_normalization(team1.offense_scp, offense_df['Sc%'].min(), offense_df['Sc%'].max())
        score2 += ThisWeek.min_max_normalization(team2.offense_scp, offense_df['Sc%'].min(), offense_df['Sc%'].max())
        score1 += ThisWeek.min_max_normalization(team1.offense_yp, offense_df['Y/P'].min(), offense_df['Y/P'].max())
        score2 += ThisWeek.min_max_normalization(team2.offense_yp, offense_df['Y/P'].min(), offense_df['Y/P'].max())
        score1 += ThisWeek.min_max_normalization(team1.offense_1std, offense_df['1stD'].min(), offense_df['1stD'].max())
        score2 += ThisWeek.min_max_normalization(team2.offense_1std, offense_df['1stD'].min(), offense_df['1stD'].max())
        score1 += ThisWeek.min_max_normalization(team1.offense_pass_td, offense_df['TD'].min(), offense_df['TD'].max())
        score2 += ThisWeek.min_max_normalization(team2.offense_pass_td, offense_df['TD'].min(), offense_df['TD'].max())
        score1 += ThisWeek.min_max_normalization(team1.offense_nya, offense_df['NY/A'].min(), offense_df['NY/A'].max())
        score2 += ThisWeek.min_max_normalization(team2.offense_nya, offense_df['NY/A'].min(), offense_df['NY/A'].max())
        print(score1, score2)
        score1 += ThisWeek.min_max_normalization(team1.defense_scp, defense_df['Sc%'].min(), defense_df['Sc%'].max())
        score2 += ThisWeek.min_max_normalization(team2.defense_scp, defense_df['Sc%'].min(), defense_df['Sc%'].max())
        score1 += 1 - ThisWeek.min_max_normalization(team1.defense_yp, defense_df['Y/P'].min(), defense_df['Y/P'].max())
        score2 += 1 - ThisWeek.min_max_normalization(team2.defense_yp, defense_df['Y/P'].min(), defense_df['Y/P'].max())
        score1 += 1 - ThisWeek.min_max_normalization(team1.defense_1std, defense_df['1stD'].min(),
                                                     defense_df['1stD'].max())
        score2 += 1 - ThisWeek.min_max_normalization(team2.defense_1std, defense_df['1stD'].min(),
                                                     defense_df['1stD'].max())
        score1 += 1 - ThisWeek.min_max_normalization(team1.defense_rush_td, defense_df['TD_1'].min(),
                                                     defense_df['TD_1'].max())
        score2 += 1 - ThisWeek.min_max_normalization(team2.defense_rush_td, defense_df['TD_1'].min(),
                                                     defense_df['TD_1'].max())
        score1 += 1 - ThisWeek.min_max_normalization(team1.defense_rush_yds, defense_df['Yds_2'].min(),
                                                     defense_df['Yds_2'].max())
        score2 += 1 - ThisWeek.min_max_normalization(team2.defense_rush_yds, defense_df['Yds_2'].min(),
                                                     defense_df['Yds_2'].max())
        print(score1, score2)
        winner = team1.name if score1 > score2 else team2.name
        return f'{team1.name} vs. {team2.name} : {winner}'

    @classmethod
    def matchups(cls):
        temp_team_list = Teams.all.copy()
        timezone = pytz.timezone('Europe/Berlin')
        week_count = int(datetime.datetime.now(tz=timezone).strftime("%U"))
        count = 0
        for team in Teams.all:
            temp_string = Statistics.schedule_df[week_count - 1].loc[
                Statistics.schedule_df['Teams'] == Teams.all[team].name][count]
            if temp_string.startswith(('@', 'vs.')):
                temp_string = temp_string.split()[1]
                for team3 in Teams.all:
                    if temp_string == Teams.all[team3].short_name and team3 in temp_team_list:
                        print(cls.get_winner(Teams.all[team], Teams.all[team3]))
                        del temp_team_list[team]
                        del temp_team_list[team3]
            count += 1
