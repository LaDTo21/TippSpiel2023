import pandas as pd
from TippSpiel2023.TippSpiel_2023.data.statistics import Statistics


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
    weighting(Statistics.defense_2022(), False, True)
    weighting(Statistics.defense_2021(), False, True)
    weighting(Statistics.defense_2020(), False, True)
    weighting(Statistics.defense_2019(), False, True)
    weighting(Statistics.offense_2022(), True, False)
    weighting(Statistics.offense_2021(), True, False)
    weighting(Statistics.offense_2020(), True, False)
    weighting(Statistics.offense_2019(), True, False)
    #Offense Y/P, 1stD, Pass TD, NY/A, Sc%
    #Defense Y/P, 1stD, Rush TD, Rush Yds, Sc%
    '''
        32.0 30.0 31.0 31.0 | 29.0 32.0 31.0 31.0 | 31 | 31 | 
        26.0 24.0 27.0 26.0 | 27.0 28.0 25.0 28.0 | 26 | 27 | 
        17.0 20.0 25.0 20.0 | 16.0 19.0 16.0 19.0 | 20 | 18 | 
        26.0 24.0 25.0 28.0 | 28.0 29.0 25.0 26.0 | 26 | 27 | Y/P
        12.0  7.0  8.0 10.0 | 10.0 10.0  8.0 12.0 |  9 | 10 | 
        14.0 12.0 14.0 15.0 | 19.0 12.0 11.0 16.0 | 14 | 15 | 
        25.0 25.0 22.0 27.0 | 26.0 27.0 24.0 25.0 | 25 | 26 | 1stD
        16.0 18.0 20.0 18.0 | 21.0 21.0 17.0 19.0 | 18 | 20 | 
        13.0 14.0 17.0 15.0 | 19.0 16.0 12.0 17.0 | 15 | 16 | 
        19.0 17.0 22.0 25.0 | 27.0 25.0 20.0 22.0 | 20 | 24 | 
        17.0 23.0 25.0 24.0 | 27.0 27.0 24.0 28.0 | 23 | 27 | Pass TD
        13.0  8.0  7.0 14.0 | 10.0  9.0  8.0 11.0 | 11 | 10 | 
        22.0 23.0 25.0 24.0 | 27.0 29.0 23.0 25.0 | 24 | 26 | NY/A
        20.0 21.0 22.0 25.0 | 25.0 22.0 19.0 21.0 | 22 | 22 | 
        23.0 27.0 21.0 24.0 | 14.0 17.0 20.0 22.0 | 24 | 19 | 
        25.0 24.0 24.0 26.0 | 18.0 19.0 22.0 20.0 | 25 | 20 | Rush Yds
        29.0 21.0 23.0 20.0 | 20.0 24.0 18.0 27.0 | 23 | 22 | 
        24.0 17.0 21.0 21.0 | 23.0 18.0 21.0 19.0 | 21 | 20 | 
        26.0 24.0 20.0 20.0 | 18.0 18.0 22.0 23.0 | 23 | 20 | 
        15.0 15.0 20.0 18.0 | 13.0 14.0 18.0 17.0 | 17 | 15 | 
        16.0 14.0 19.0 16.0 | 11.0 21.0 20.0 18.0 | 16 | 19 | 
        16.0 11.0 18.0 16.0 | 25.0 16.0 20.0 12.0 | 16 | 19 | 
        27.0 28.0 28.0 29.0 | 29.0 29.0 27.0 27.0 | 28 | 28 | Sc%
        14.0  8.0  8.0 13.0 | 12.0  9.0  8.0 12.0 | -- | -- | 
        4.0   5.0  8.0  5.0 | 31.0 31.0 27.0 26.0 | -- | -- | EXP
    '''