n = int(input("Enter a number:"))
print(f"You entered: {n}")

biggest_number = int(input("Enter the biggest number:"))

for i in range(n - 1):
    number = int(input("Enter a number:"))
    if number > biggest_number:
        biggest_number = number

print(f"The biggest number is: {biggest_number}")
