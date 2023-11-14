from dataclasses import dataclass, fields, field
from typing import List

import pandas as pd

from TippSpiel2023.TippSpiel2023.data.statistics import Statistics


@dataclass
class Team:
    name: str = ""
    short_name: str = ""
    offense_exp: float = 0
    offense_yp: float = 0
    offense_1std: int = 0
    offense_pass_td: int = 0
    defense_exp: int = 0
    defense_yp: float = 0
    defense_1std: int = 0
    defense_rush_td: int = 0
    list: List = field(default_factory=lambda: [])

    def __init__(self, name):
        self.name = name
        self.short_name = name.split()[-1]
        self.offense_exp = Statistics.offense_df['EXP'].loc[Statistics.offense_df['Tm'] == name].values[0]
        self.offense_yp = Statistics.offense_df['Y/P'].loc[Statistics.offense_df['Tm'] == name].values[0]
        self.offense_1std = Statistics.offense_df['1stD'].loc[Statistics.offense_df['Tm'] == name].values[0]
        self.offense_pass_td = Statistics.offense_df['TD'].loc[Statistics.offense_df['Tm'] == name].values[0]
        self.defense_exp = Statistics.defense_df['EXP'].loc[Statistics.defense_df['Tm'] == name].values[0]
        self.defense_yp = Statistics.defense_df['Y/P'].loc[Statistics.defense_df['Tm'] == name].values[0]
        self.defense_1std = Statistics.defense_df['1stD'].loc[Statistics.defense_df['Tm'] == name].values[0]
        self.defense_rush_td = Statistics.defense_df['TD_1'].loc[Statistics.defense_df['Tm'] == name].values[0]
        self.list = ['EXP', 'Y/P', '1stD', 'TD', 'EXP', 'Y/P', '1stD', 'TD_1']


@dataclass()
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
           'Forty_nine_ers': Team('San Francisco 49ers'),
           'Seahawks': Team('Seattle Seahawks'),
           'Buccaneers': Team('Tampa Bay Buccaneers'),
           'Titans': Team('Tennessee Titans'),
           'Commanders': Team('Washington Commanders')}

