import pandas as pd
from TippSpiel2023.TippSpiel2023.data.statistics import Statistics


def function(row, mean_list, bigger):
    count = -1
    for i, item in enumerate(row):
        count += 1
        row.iloc[i] = calc(item, mean_list[count], bigger)
    return row


def calc(n, mean, bigger):
    if n > mean and bigger is True or n < mean and bigger is False:
        return 1
    else:
        return 0


def weighting(data_frame, bigger1, bigger2):
    df = data_frame
    df = df.drop(columns=['Tm', 'Rk', 'G'], axis=1)
    mean_list = df.mean().tolist()
    df2 = df.iloc[16:]
    df = df.iloc[:16]
    df = df.apply(lambda row: function(row, mean_list, bigger1), axis=1)
    df2 = df2.apply(lambda row: function(row, mean_list, bigger2), axis=1)
    df = pd.concat([df, df2])
    #print(df.to_markdown())
    print(df.sum())


class Weighting:
    weighting(Statistics.defense_2022_df, False, True)
    weighting(Statistics.offense_2022_df, True, False)
    #Offense Y/P, 1stD, EXP
    #Defense PA, Rush TD,
