from dataclasses import dataclass
from TippSpiel2023.TippSpiel2023.data.statistics import Statistics


@dataclass
class Team:
    name: str
    short_name: str
    offense_exp: float
    offense_yp: float
    offense_1std: float
    offense_pass_td: float
    defense_pa: float
    defense_yp: float
    defense_1std: float
    defense_rush_td: float


@dataclass(frozen=True)
class Teams:
    chiefs = Team(name="Kansas City Chiefs", short_name="Chiefs", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    dolphins = Team(name="Miami Dolphins", short_name="Dolphins", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    eagles = Team(name="Philadelphia ", short_name="Chiefs", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    cardinals = Team(name="Arizona Cardinals", short_name="Cardinals", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    falcons = Team(name="Atlanta Falcons", short_name="Falcons", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    ravens = Team(name="Baltimore Ravens", short_name="Ravens", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    bills = Team(name="Buffalo Bills", short_name="Bills", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    panthers = Team(name="Carolina Panthers", short_name="Panthers", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    bears = Team(name="Chicago Bears", short_name="Bears", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    bengals = Team(name="Cincinnati Bengals", short_name="Bengals", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    browns = Team(name="Cleveland Browns", short_name="Browns", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    cowboys = Team(name="Dallas Cowboys", short_name="Cowboys", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    broncos = Team(name="Denver Broncos", short_name="Broncos", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    lions = Team(name="Detroit Lions", short_name="Lions", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    packers = Team(name="Green Bay Packers", short_name="Packers", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    texans = Team(name="Houston Texans", short_name="Texans", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    colts = Team(name="Indianapolis Colts", short_name="Colts", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    jaguars = Team(name="Jacksonville Jaguars", short_name="Jaguars", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    raiders = Team(name="Las Vegas Raiders", short_name="Raiders", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    chargers = Team(name="Los Angeles Chargers", short_name="Chargers", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    rams = Team(name="Los Angeles Rams", short_name="Rams", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    vikings = Team(name="Minnesota Vikings", short_name="Vikings", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    patriots = Team(name="New England Patriots", short_name="Patriots", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    saints = Team(name="New Orleans Saints", short_name="Saints", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    giants = Team(name="New York Giants", short_name="Giants", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    jets = Team(name="New York Jets", short_name="Jets", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    steelers = Team(name="Pittsburgh Steelers", short_name="Steelers", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    forty_nine_ers = Team(name="San Francisco 49ers", short_name="49ers", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    seahawks = Team(name="Seattle Seahawks", short_name="Seahawks", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    buccaneers = Team(name="Tampa Bay Buccaneers", short_name="Buccaneers", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    titans = Team(name="Tennessee Titans", short_name="Titans", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
    commanders = Team(name="Washington Commanders", short_name="Commanders", offense_exp=0, offense_yp=0, offense_1std=0, offense_pass_td=0, defense_pa=0, defense_yp=0, defense_1std=0, defense_rush_td=0)
