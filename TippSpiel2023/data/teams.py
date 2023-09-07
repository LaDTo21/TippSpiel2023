from dataclasses import dataclass
from TippSpiel2023.TippSpiel2023.data.statistics import Statistics


@dataclass()
class Team:
    name: str
    short_name: str
    qb: float
    #third_down_conversion: float
    #home_away: float
    #run_offense: float
    #pass_offense: float
    #run_defense: float
    #pass_defense: float
    #injuries: float
    #win_loss_streak: float

    def qb(self):
        self.qb = self.qb / Statistics.qb_df['EPA+CPOE composite'].max() * 100


class Teams:
    chiefs = Team(name="Kansas City Chiefs", short_name="ksc", qb=Statistics.qb_df.loc[Statistics.qb_df['Team'] == 'kc'])

