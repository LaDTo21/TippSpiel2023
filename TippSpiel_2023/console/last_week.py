from TippSpiel2023.TippSpiel_2023.console.this_week import ThisWeek
from TippSpiel2023.TippSpiel_2023.data.statistics import Statistics
from TippSpiel2023.TippSpiel_2023.data.teams import Teams


class LastWeek:
    @staticmethod
    def check_results(team_name1, team_name2, score):
        team1 = 0
        team2 = 0
        for team in Teams.all:
            team = Teams.all[team]
            temp_string = 'Forty-Niners'
            if temp_string in team_name1:
                team_name1 = '49ers'
            elif temp_string in team_name2:
                team_name2 = '49ers'
            if team.short_name == team_name1.split()[0]:
                team1 = team
            if team.short_name == team_name2.split()[0]:
                team2 = team

        predicted_winner = Teams.all[ThisWeek.get_winner(team1, team2).split()[-1]].short_name
        actual_winner = team_name1 if int(score.split('‑')[0]) > int(score.split('‑')[-1]) else team_name2
        return 'Yup' if predicted_winner == actual_winner.split()[0] else 'Nope'

    @classmethod
    def results(cls):
        df = Statistics.last_week_results_df[11][['Home Team', 'Score', 'Visiting Team']]
        df['prediction'] = df.apply(
            lambda row: cls.check_results(row['Home Team'], row['Visiting Team'], row['Score']),  axis=1)
        print(df.to_markdown())
