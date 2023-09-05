import manual_input as manual

choice = int(input('(1 = manual, 2 = last week, 3 = this week)\n'))

if choice == 1:
    manual.manual_input()
elif choice == 2:
    pass
elif choice == 3:
    pass
else:
    print("You suck")
