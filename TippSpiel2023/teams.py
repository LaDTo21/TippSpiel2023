from dataclasses import dataclass


@dataclass
class Team:
    name: str
    qb: float
    third_down_conversion: float
    #home_away: float
    run_offense: float
    pass_offense: float
    run_defense: float
    pass_defense: float
    #injuries: float
    #win_loss_streak: float
