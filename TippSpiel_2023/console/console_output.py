from TippSpiel2023.TippSpiel_2023.console.last_week import LastWeek
from TippSpiel2023.TippSpiel_2023.console.manual_input import ManualInput
from TippSpiel2023.TippSpiel_2023.console.this_week import ThisWeek
from TippSpiel2023.TippSpiel_2023.data.statistics import Statistics


class ConsoleOutput:
    continue_loop = True
    while continue_loop:
        choice = input('(1 = manual, 2 = last week, 3 = this week, 4 = save current state)\n')

        match choice:
            case '1':
                ManualInput.manual_input()
            case '2':
                LastWeek.results()
            case '3':

                ThisWeek.matchups()
            case '4':
                Statistics.current_to_csv()
            case _:
                continue_loop = False
                print("You suck")
