"""# Task 1

operand_1 = int(input("enter an operand: "))
operator = str(input("enter an operator: "))
operand_2 = int(input("enter an operand: "))
result = 0
if operator == "+":
    result = operand_1 + operand_2
elif operator == "-":
    result = operand_1 - operand_2
elif operator == "*":
    result = operand_1 * operand_2
elif operator == "/":
    result = operand_1 / operand_2
elif operator == "**":
    result = operand_1 ** operand_2
else:
    exit("error")
print(operand_1, operator, operand_2, "=", result)

# Task 2

n = int(input("enter N: "))
print(n, end="\t\t")
n += 1
for i in range(1, n):
    if i * i < n:
        print(i * i, end=" ")

# Task 3

check_number = int(input("\nenter the number: "))
b = 0
for i in range(1, check_number + 1):
    if check_number % i == 0:
        b += 1
if b == 2:
    print(check_number, "is a prime number")
else:
    print(check_number, "- is not a prime number")"""

"""# Task *_V_1

count_mushroom = input("Скільки Маша знайшла грибів?: ")
if not count_mushroom.isnumeric():
    exit("error")
if count_mushroom.endswith("11") or count_mushroom.endswith("12") or count_mushroom.endswith("13") \
        or count_mushroom.endswith("14"):
    print(f"Маша знайшла в лісі {count_mushroom} грибів")
elif count_mushroom.endswith("1"):
    print(f"Маша знайшла в лісі {count_mushroom} гриб")
elif count_mushroom.endswith("2") or count_mushroom.endswith("3") or count_mushroom.endswith("4"):
    print(f"Маша знайшла в лісі {count_mushroom} гриба")
else:
    print(f"Маша знайшла в лісі {count_mushroom} грибів")


# Task *_V_2
count_mushroom = int(input("Скільки Маша знайшла грибів?: "))
if count_mushroom % 100 == 11 or count_mushroom % 100 == 12 or count_mushroom % 100 == 13 or count_mushroom % 100 == 14:
    print(f"Маша знайшла в лісі {count_mushroom} грибів")
elif count_mushroom % 10 == 1:
    print(f"Маша знайшла в лісі {count_mushroom} гриб")
elif count_mushroom % 10 == 2 or count_mushroom % 10 == 3 or count_mushroom % 10 == 4:
    print(f"Маша знайшла в лісі {count_mushroom} гриба")
else:
    print(f"Маша знайшла в лісі {count_mushroom} грибів")"""
