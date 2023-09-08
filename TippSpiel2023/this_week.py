import pandas as pd
import datetime
import pytz

#eine Methode die den nächst größeren, bzw. kleineren Wert für local sucht
timezone = pytz.timezone('Europe/Berlin')
local = datetime.datetime.now(tz=timezone).strftime("%b. %w")
week_count = datetime.datetime.now(tz=timezone).strftime("%U")

url = "https://raw.githubusercontent.com/LaDTo21/TippSpiel2023/main/2023_NFL_Schedule.csv"
df = pd.read_csv(url)


print()
