from TippSpiel2023.TippSpiel2023.data.statistics import Statistics

for i in range(1, (Statistics.schedule_df.shape[1] - 1)):
    print(Statistics.schedule_df.columns[i])

print((Statistics.schedule_df.shape[1] - 1))
print(Statistics.schedule_df.shape)
