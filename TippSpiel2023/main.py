import pandas as pd


url = "https://raw.githubusercontent.com/LaDTo21/TippSpiel2023/main/rbsdm.comstats.csv"
df = pd.read_csv(url)

print(df['Player'])
