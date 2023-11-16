import io
import pandas as pd
import datetime
import pytz
import requests


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

    last_week_results_url = 'http://www.playoffstatus.com/nfl/nflschedule.html'
    schedule_df_url = 'https://raw.githubusercontent.com/LaDTo21/TippSpiel2023/main/2023_NFL_Schedule.csv'
    defense_url = 'https://www.pro-football-reference.com/years/2023/opp.htm#team_stats'
    offense_url = 'https://www.pro-football-reference.com/years/2023/#team_stats'

    schedule_df = pd.read_csv(schedule_df_url, sep=';')
    last_week_results_df = pd.read_html(last_week_results_url)
    saved_defense_df = pd.read_csv('C:\\Users\\mstalgies\\PycharmProjects\\TippSpiel_2023\\TippSpiel2023\\'
                                   'TippSpiel_2023\\data\\saved_defense.csv')
    saved_offense_df = pd.read_csv('C:\\Users\\mstalgies\\PycharmProjects\\TippSpiel_2023\\TippSpiel2023\\'
                                   'TippSpiel_2023\\data\\saved_offense.csv')
    defense_df = prepare_tables(defense_url, 0)
    offense_df = prepare_tables(offense_url, 4)

    timezone = pytz.timezone('Europe/Berlin')
    for i in range(1, (schedule_df.shape[1])):
        schedule_df.rename(columns={schedule_df.columns[i]: datetime.datetime.strptime(
            f'{datetime.datetime.now(tz=timezone).strftime("%Y")} {schedule_df.columns[i]}',
            "%Y %b %d").isocalendar()[1]}, inplace=True)

    @classmethod
    def current_to_csv(cls):
        cls.defense_df.to_csv('C:\\Users\\mstalgies\\PycharmProjects\\TippSpiel_2023\\TippSpiel2023\\'
                              'TippSpiel_2023\\data\\saved_defense.csv')
        cls.offense_df.to_csv('C:\\Users\\mstalgies\\PycharmProjects\\TippSpiel_2023\\TippSpiel2023\\'
                              'TippSpiel_2023\\data\\saved_offense.csv')

    @classmethod
    def defense_2022(cls):
        defense_2022_url = 'https://www.pro-football-reference.com/years/2022/opp.htm#team_stats'
        return cls.prepare_tables(defense_2022_url, 0)

    @classmethod
    def defense_2021(cls):
        defense_2021_url = 'https://www.pro-football-reference.com/years/2021/opp.htm'
        return cls.prepare_tables(defense_2021_url, 0)

    @classmethod
    def defense_2020(cls):
        defense_2020_url = 'https://www.pro-football-reference.com/years/2020/opp.htm'
        return cls.prepare_tables(defense_2020_url, 0)

    @classmethod
    def defense_2019(cls):
        defense_2019_url = 'https://www.pro-football-reference.com/years/2019/opp.htm'
        return cls.prepare_tables(defense_2019_url, 0)

    @classmethod
    def offense_2022(cls):
        offense_2022_url = 'https://www.pro-football-reference.com/years/2022/#all_team_stats'
        return cls.prepare_tables(offense_2022_url, 0)

    @classmethod
    def offense_2021(cls):
        offense_2021_url = 'https://www.pro-football-reference.com/years/2021/index.htm'
        return cls.prepare_tables(offense_2021_url, 5)

    @classmethod
    def offense_2020(cls):
        offense_2020_url = 'https://www.pro-football-reference.com/years/2020/index.htm'
        return cls.prepare_tables(offense_2020_url, 5)

    @classmethod
    def offense_2019(cls):
        offense_2019_url = 'https://www.pro-football-reference.com/years/2019/index.htm'
        return cls.prepare_tables(offense_2019_url, 5)
