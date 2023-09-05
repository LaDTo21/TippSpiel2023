import pandas as pd
import time

#eine Methode die den nächst größeren, bzw. kleineren Wert für local sucht
local = time.strftime("%b. %w")
url = "https://raw.githubusercontent.com/LaDTo21/TippSpiel2023/main/2023_NFL_Schedule_Grid.csv"
df = pd.read_csv(url)

print(df.info())
