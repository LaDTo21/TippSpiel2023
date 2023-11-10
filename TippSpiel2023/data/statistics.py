import pandas as pd
from dataclasses import dataclass
import datetime
import pytz
import requests
from pandas import DataFrame


class Statistics:
    timezone = pytz.timezone('Europe/Berlin')

    qb_df_url = "https://raw.githubusercontent.com/LaDTo21/TippSpiel2023/main/rbsdm.comstats.csv"
    schedule_df_url = "https://raw.githubusercontent.com/LaDTo21/TippSpiel2023/main/2023_NFL_Schedule.csv"
    defense_url = "https://www.pro-football-reference.com/years/2023/opp.htm"
    offense_url = "http://www.ffiec.gov/census/report.aspx?year=2011&state=01&report=demographic&msa=11500"
    defense_2022_url = "https://raw.githubusercontent.com/LaDTo21/TippSpiel2023/main/Defense_2022.csv"
    offense_2022_url = "https://raw.githubusercontent.com/LaDTo21/TippSpiel2023/main/Offense_2022.csv"
    qb_df = pd.read_csv(qb_df_url)
    schedule_df = pd.read_csv(schedule_df_url, sep=';')
    defense_df = pd.read_html(defense_url, match='Team Defense')[0]
#    offense_df = pd.read_html(requests.get(offense_url).content)[-1]
    defense_2022_df = pd.read_csv(defense_2022_url)
    offense_2022_df = pd.read_csv(offense_2022_url)
    defense_2022_ranks_df = defense_2022_df[['Tm', 'G', 'PA']].copy()

    for i in range(1, (schedule_df.shape[1])):
        schedule_df.rename(columns={schedule_df.columns[i]: datetime.datetime.strptime(
            f'{datetime.datetime.now(tz=timezone).strftime("%Y")} {schedule_df.columns[i]}',
            "%Y %b %d").isocalendar()[1]}, inplace=True)
