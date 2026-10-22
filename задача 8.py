
a = int(input("Въведи долната граница: "))
b = int(input("Въведи горната граница: "))

broi = 0

for i in range(10):
    chislo = int(input("Въведи число: "))

    if a <= chislo <= b:
        broi = broi + 1

print("Броят на числата в интервала е:", broi)
