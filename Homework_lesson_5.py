"""
# Task 1

my_string = "0123456789"
for h in my_string:
    for v in my_string:
        if h == "0":
            print(int(v), end=",  ")
        elif h == "9" and v == "9":
            print(int(h), int(v), sep="", end=".")
        else:
            print(int(h), int(v), sep="", end=", ")
    print()
"""
"""
# Task 2_b

height = int(input("enter height: "))
for i in range(height):
    for _ in range(2 * (height - i - 1)):
        print(end=" ")
    for _ in range(1 + i * 2):
        print("*", end=" ")

    print()
"""
# Task 2

"""height = 5
for i in range(height):
    for _ in range(2 * (height - i - 1)):
        print(end=" ")
    print("*", end="  ")
    for _ in range(i * 2 - 1):
        print("", end="  ")
    print("*")
"""