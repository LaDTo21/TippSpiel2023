import io

import pandas as pd

from TippSpiel2023.TippSpiel_2023.console.last_week import LastWeek
from TippSpiel2023.TippSpiel_2023.data.statistics import Statistics

df = Statistics.last_week_results()[11][['Home Team', 'Score', 'Visiting Team']]
#df['prediction'] = df.apply(lambda row: LastWeek.check_results(row['Home Team'], row['Visiting Team'], row['Score']), axis = 1)
print('16‑13'.split('‑')[-1])
