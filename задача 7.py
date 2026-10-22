 a = float(input("Въведи първото число: "))
b = float(input("Въведи второто число: "))

print("Избери действие: +, -, *, /")
deistvie = input("Действие: ")

if deistvie == "+":
    print("Резултат:", a + b)
elif deistvie == "-":
    print("Резултат:", a - b)
elif deistvie == "*":
    print("Резултат:", a * b)
elif deistvie == "/":
    if b != 0:
        print("Резултат:", a / b)
    else:
        print("Грешка: деление на нула!")
else:
    print("Невалидно действие!")