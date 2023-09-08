from dataclasses import dataclass
from TippSpiel2023.TippSpiel2023.data.statistics import Statistics


@dataclass
class Team:
    name: str
    short_name: str
    qb_name: str
    qb_value: float = 0

    # third_down_conversion: float
    # home_away: float
    # run_offense: float
    # pass_offense: float
    # run_defense: float
    # pass_defense: float
    # injuries: float
    # win_loss_streak: float

    def __post_init__(self):
        self.qb_value = \
            (Statistics.qb_df.loc[Statistics.qb_df['Player'] == self.qb_name, 'EPA+CPOE composite'].values[0]
             / Statistics.qb_df['EPA+CPOE composite'].max() * 100)


@dataclass(frozen=True)
class Teams:
    chiefs = Team(name="Kansas City Chiefs", short_name="Chiefs", qb_name="P.Mahomes")
    dolphins = Team(name="Miami Dolphins", short_name="Dolphins", qb_name="T.Tagovailoa")
    eagles = Team(name="Philadelphia ", short_name="Chiefs", qb_name="J.Hurts")
    cardinals = Team(name="Arizona Cardinals", short_name="Cardinals", qb_name="K.Murray")
    falcons = Team(name="Atlanta Falcons", short_name="Falcons", qb_name="M.Mariota")
    ravens = Team(name="Baltimore Ravens", short_name="Ravens", qb_name="L.Jackson")
    bills = Team(name="Buffalo Bills", short_name="Bills", qb_name="J.Allen")
    panthers = Team(name="Carolina Panthers", short_name="Panthers", qb_name="B.Mayfield")
    bears = Team(name="Chicago Bears", short_name="Bears", qb_name="J.Fields")
    bengals = Team(name="Cincinnati Bengals", short_name="Bengals", qb_name="J.Burrow")
    browns = Team(name="Cleveland Browns", short_name="Browns", qb_name="J.Brissett")
    cowboys = Team(name="Dallas Cowboys", short_name="Cowboys", qb_name="D.Prescott")
    broncos = Team(name="Denver Broncos", short_name="Broncos", qb_name="R.Wilson")
    lions = Team(name="Detroit Lions", short_name="Lions", qb_name="J.Goff")
    packers = Team(name="Green Bay Packers", short_name="Packers", qb_name="A.Rodgers")
    texans = Team(name="Houston Texans", short_name="Texans", qb_name="D.Mills")
    colts = Team(name="Indianapolis Colts", short_name="Colts", qb_name="M.Ryan")
    jaguars = Team(name="Jacksonville Jaguars", short_name="Jaguars", qb_name="T.Lawrence")
    raiders = Team(name="Las Vegas Raiders", short_name="Raiders", qb_name="D.Carr")
    chargers = Team(name="Los Angeles Chargers", short_name="Chargers", qb_name="J.Herbert")
    rams = Team(name="Los Angeles Rams", short_name="Rams", qb_name="M.Stafford")
    vikings = Team(name="Minnesota Vikings", short_name="Vikings", qb_name="K.Cousins")
    patriots = Team(name="New England Patriots", short_name="Patriots", qb_name="M.Jones")
    saints = Team(name="New Orleans Saints", short_name="Saints", qb_name="A.Dalton")
    giants = Team(name="New York Giants", short_name="Giants", qb_name="D.Jones")
    jets = Team(name="New York Jets", short_name="Jets", qb_name="A.Rodgers")
    steelers = Team(name="Pittsburgh Steelers", short_name="Steelers", qb_name="K.Pickett")
    forty_nine_ers = Team(name="San Francisco 49ers", short_name="49ers", qb_name="J.Garoppolo")
    seahawks = Team(name="Seattle Seahawks", short_name="Seahawks", qb_name="G.Smith")
    buccaneers = Team(name="Tampa Bay Buccaneers", short_name="Buccaneers", qb_name="T.Brady")
    titans = Team(name="Tennessee Titans", short_name="Titans", qb_name="R.Tannehill")
    commanders = Team(name="Washington Commanders", short_name="Commanders", qb_name="C.Wentz")

