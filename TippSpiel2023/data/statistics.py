import pandas as pd


def change_schedule_column_names():
    Statistics.schedule_df


class Statistics:
    def __init__(self):
        change_schedule_column_names()

    qb_df_url = "https://raw.githubusercontent.com/LaDTo21/TippSpiel2023/main/rbsdm.comstats.csv"
    schedule_df_url = "https://raw.githubusercontent.com/LaDTo21/TippSpiel2023/main/2023_NFL_Schedule.csv"
    qb_df = pd.read_csv(qb_df_url)
    schedule_df = pd.read_csv(schedule_df_url, sep=';')
