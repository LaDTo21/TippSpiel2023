from dataclasses import fields

import pandas as pd

from TippSpiel2023.TippSpiel2023 import this_week
from TippSpiel2023.TippSpiel2023.data.statistics import Statistics
from TippSpiel2023.TippSpiel2023.data.teams import Teams

df = pd.read_csv("C:\\Users\\mstalgies\\PycharmProjects\\TippSpiel_2023\\TippSpiel2023\\Offense.csv")
##count = 0
#for field in fields(Teams):
   # field.__setattr__(__name='name', __value=Statistics.schedule_df['Teams'][count])
    #field.__getattribute__().offense_exp = df['EXP'].loc[df['Tm'] == field.name][0]
    #field.offense_yp = df['Y/P'].loc[df['Tm'] == field.name][0]
    #field.offense_1std = df['1stD'].loc[df['Tm'] == field.name][0]
    #field.offense_pass_td = df['TD'].loc[df['Tm'] == field.name][0]
    #field.defense_pa = df['PA'].loc[df['Tm'] == field.name][0]
    #field.defense_yp = df['Y/P'].loc[df['Tm'] == field.name][0]
    #field.defense_1std = df['1stD'].loc[df['Tm'] == field.name][0]
    #field.defense_rush_td = df['TD1'].loc[df['Tm'] == field.name][0]
   # count += 1
print(Teams.cardinals)
print(Teams.falcons)
print(Teams.ravens)
print(Teams.bills)
print(Teams.panthers)
print(Teams.bears)
print(Teams.bengals)
print(Teams.browns)
print(Teams.cowboys)
print(Teams.broncos)
print(Teams.lions)
print(Teams.packers)
print(Teams.texans)
print(Teams.colts)
print(Teams.jaguars)
print(Teams.chiefs)
print(Teams.raiders)
print(Teams.chargers)
print(Teams.rams)
print(Teams.dolphins)
print(Teams.vikings)
print(Teams.patriots)
print(Teams.saints)
print(Teams.giants)
print(Teams.jets)
print(Teams.eagles)
print(Teams.steelers)
print(Teams.forty_nine_ers)
print(Teams.seahawks)
print(Teams.buccaneers)
print(Teams.titans)
print(Teams.commanders)
print(this_week.get_winner(Teams.dolphins, Teams.jets))
print(Teams.all['cardinals'].name)
print(Statistics.schedule_df[46].loc[Statistics.schedule_df['Teams'] == Teams.all['cardinals'].name][0])
