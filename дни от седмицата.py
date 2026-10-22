n = int(input("Enter a number between 1 and 7:"))

if n == 1:
    day = "Monday"
elif n == 2:
    day = "Tuesday"
elif n == 3:
    day = "Wednesday"
elif n == 4:
    day = "Thursday"
elif n == 5:
    day = "Friday"
elif n == 6:
    day = "Saturday"
elif n == 7:
    day = "Sunday"
else:
    print("Invalid input. Please enter a number between 1 and 7.")

if 1 <= n <= 7:
    print(day)
    print("The entered number", n, "corresponds to", day)