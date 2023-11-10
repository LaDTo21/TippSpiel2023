from TippSpiel2023.TippSpiel2023.data import weighting
from TippSpiel2023.TippSpiel2023.data.statistics import Statistics
import pandas as pd
from tabulate import tabulate


weighting.weighting(Statistics.defense_2022_df, False, True)
weighting.weighting(Statistics.offense_2022_df, True, False)

