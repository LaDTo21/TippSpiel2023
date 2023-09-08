import pandas as pd

from TippSpiel2023.TippSpiel2023.data.teams import Teams

url = "https://raw.githubusercontent.com/LaDTo21/TippSpiel2023/main/rbsdm.comstats.csv"
df = pd.read_csv(url)

print(Teams.chiefs)

