import datetime

import pytz

from TippSpiel2023.TippSpiel2023.data.statistics import Statistics


def change_column_dates_to_week_count():
    timezone = pytz.timezone('Europe/Berlin')
    for i in range(1, (Statistics.schedule_df.shape[1] - 1)):
        print(Statistics.schedule_df.columns[i])
        print(f'{datetime.datetime.now(tz=timezone).strftime("%Y")} '
                                         f'{Statistics.schedule_df.columns[i]}')
        print(datetime.datetime.strptime(f'{datetime.datetime.now(tz=timezone).strftime("%Y")} '
                                         f'{Statistics.schedule_df.columns[i]}', "%Y %b %d").isocalendar()[1])

    print((Statistics.schedule_df.shape[1] - 1))
    print(Statistics.schedule_df.shape)
    print(Statistics.qb_df.shape)


change_column_dates_to_week_count()
