from TippSpiel2023.TippSpiel2023.data.statistics import Statistics

print(Statistics.qb_df.loc[Statistics.qb_df['Team'] == 'Chiefs', 'EPA+CPOE composite'].values[0])
