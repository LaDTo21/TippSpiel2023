import pandas as pd
from dataclasses import dataclass
import datetime
import pytz
from pandas import DataFrame


class Statistics:
    qb_df_url = "https://raw.githubusercontent.com/LaDTo21/TippSpiel2023/main/rbsdm.comstats.csv"
    schedule_df_url = "https://raw.githubusercontent.com/LaDTo21/TippSpiel2023/main/2023_NFL_Schedule.csv"
    qb_df = pd.read_csv(qb_df_url)
    schedule_df = pd.read_csv(schedule_df_url, sep=';')

    def __post_init__(self):
        timezone = pytz.timezone('Europe/Berlin')
        for i in range(1, (self.schedule_df.shape[1])):
            self.schedule_df.rename(columns={self.schedule_df.columns[i]: datetime.datetime.strptime(
                f'{datetime.datetime.now(tz=timezone).strftime("%Y")} {self.schedule_df.columns[i]}',
                "%Y %b %d").isocalendar()[1]}, inplace=True)


