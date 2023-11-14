import io

import pandas as pd
from dataclasses import dataclass
import datetime
import pytz
import requests
from pandas import DataFrame


class Renamer:
    def __init__(self):
        self.d = dict()

    def __call__(self, x):
        if x not in self.d:
            self.d[x] = 0
            return x
        else:
            self.d[x] += 1
            return "%s_%d" % (x, self.d[x])


class Statistics:
    @staticmethod
    def prepare_tables(url, table_count):
        df = (pd.read_html(io.StringIO(requests.get(url).text
                                       .replace("<!--", "")
                                       .replace("-->", "")))[table_count]
              .iloc[:-3]
              .rename(columns=Renamer()))
        df.columns = df.columns.droplevel(0)
        return df

    schedule_df_url = 'https://raw.githubusercontent.com/LaDTo21/TippSpiel2023/main/2023_NFL_Schedule.csv'
    defense_url = 'https://www.pro-football-reference.com/years/2023/opp.htm#team_stats'
    offense_url = 'https://www.pro-football-reference.com/years/2023/#team_stats'
    defense_2022_url = 'https://www.pro-football-reference.com/years/2022/opp.htm#team_stats'
    offense_2022_url = 'https://www.pro-football-reference.com/years/2022/#all_team_stats'
    schedule_df = pd.read_csv(schedule_df_url, sep=';')
    defense_df = prepare_tables(defense_url, 0)
    offense_df = prepare_tables(offense_url, 4)
    defense_2022_df = prepare_tables(defense_2022_url, 0)
    offense_2022_df = prepare_tables(offense_2022_url, 5)

    timezone = pytz.timezone('Europe/Berlin')

    for i in range(1, (schedule_df.shape[1])):
        schedule_df.rename(columns={schedule_df.columns[i]: datetime.datetime.strptime(
            f'{datetime.datetime.now(tz=timezone).strftime("%Y")} {schedule_df.columns[i]}',
            "%Y %b %d").isocalendar()[1]}, inplace=True)
