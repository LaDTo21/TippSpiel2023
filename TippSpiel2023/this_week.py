from dataclasses import fields

import pandas as pd
import datetime
import pytz

from TippSpiel2023.TippSpiel2023.data.teams import Teams


class Matchups:
    timezone = pytz.timezone('Europe/Berlin')
    week_count = datetime.datetime.now(tz=timezone).strftime("%U")
