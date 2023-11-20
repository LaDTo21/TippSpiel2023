from TippSpiel2023.TippSpiel_2023.data.statistics import Statistics


class Team:
    name: str
    short_name: str
    offense_scp: float
    offense_yp: float
    offense_1std: int
    offense_pass_td: int
    offense_nya: float
    defense_scp: int
    defense_yp: float
    defense_1std: int
    defense_rush_td: int
    defense_rush_yds: int

    def __init__(self, name):
        self.name = name
        self.short_name = name.split()[-1]
        self.offense_scp = Statistics.saved_offense_df['Sc%'].loc[Statistics.saved_offense_df['Tm'] == name].values[0]
        self.offense_yp = Statistics.saved_offense_df['Y/P'].loc[Statistics.saved_offense_df['Tm'] == name].values[0]
        self.offense_1std = Statistics.saved_offense_df['1stD'].loc[Statistics.saved_offense_df['Tm'] == name].values[0]
        self.offense_pass_td = (
            Statistics.saved_offense_df['TD'].loc[Statistics.saved_offense_df['Tm'] == name].values)[0]
        self.offense_nya = Statistics.saved_offense_df['NY/A'].loc[Statistics.saved_offense_df['Tm'] == name].values[0]
        self.defense_scp = Statistics.saved_defense_df['Sc%'].loc[Statistics.saved_defense_df['Tm'] == name].values[0]
        self.defense_yp = Statistics.saved_defense_df['Y/P'].loc[Statistics.saved_defense_df['Tm'] == name].values[0]
        self.defense_1std = Statistics.saved_defense_df['1stD'].loc[Statistics.saved_defense_df['Tm'] == name].values[0]
        self.defense_rush_td = (
            Statistics.saved_defense_df['TD_1'].loc[Statistics.saved_defense_df['Tm'] == name].values)[0]
        self.defense_rush_yds = (
            Statistics.saved_defense_df['Yds_2'].loc[Statistics.saved_defense_df['Tm'] == name].values)[0]


class Teams:
    all = {'Cardinals': Team('Arizona Cardinals'),
           'Falcons': Team('Atlanta Falcons'),
           'Ravens': Team('Baltimore Ravens'),
           'Bills': Team('Buffalo Bills'),
           'Panthers': Team('Carolina Panthers'),
           'Bears': Team('Chicago Bears'),
           'Bengals': Team('Cincinnati Bengals'),
           'Browns': Team('Cleveland Browns'),
           'Cowboys': Team('Dallas Cowboys'),
           'Broncos': Team('Denver Broncos'),
           'Lions': Team('Detroit Lions'),
           'Packers': Team('Green Bay Packers'),
           'Texans': Team('Houston Texans'),
           'Colts': Team('Indianapolis Colts'),
           'Jaguars': Team('Jacksonville Jaguars'),
           'Chiefs': Team('Kansas City Chiefs'),
           'Raiders': Team('Las Vegas Raiders'),
           'Chargers': Team('Los Angeles Chargers'),
           'Rams': Team('Los Angeles Rams'),
           'Dolphins': Team('Miami Dolphins'),
           'Vikings': Team('Minnesota Vikings'),
           'Patriots': Team('New England Patriots'),
           'Saints': Team('New Orleans Saints'),
           'Giants': Team('New York Giants'),
           'Jets': Team('New York Jets'),
           'Eagles': Team('Philadelphia Eagles'),
           'Steelers': Team('Pittsburgh Steelers'),
           '49ers': Team('San Francisco 49ers'),
           'Seahawks': Team('Seattle Seahawks'),
           'Buccaneers': Team('Tampa Bay Buccaneers'),
           'Titans': Team('Tennessee Titans'),
           'Commanders': Team('Washington Commanders')}
