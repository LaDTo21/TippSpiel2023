import manual_input as manual
from TippSpiel2023.TippSpiel2023.this_week import ThisWeek


class ConsoleOutput:
    choice = int(input('(1 = manual, 2 = last week, 3 = this week)\n'))

    if choice == 1:
        manual.manual_input()
    elif choice == 2:
        pass
    elif choice == 3:
        ThisWeek
    else:
        print("You suck")
