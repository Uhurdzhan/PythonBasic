# Task 3

my_list_1 = []

n = int(input("Enter number of elements for first list: "))
for i in range(0, n):
    user_input = int(input())
    my_list_1.append(user_input)

my_list_2 = []
n = int(input("Enter number of elements for second list: "))
for i in range(0, n):
    user_input = int(input())
    my_list_2.append(user_input)

my_result = []
for num in my_list_1:
    if my_list_1.index(num) % 2 == 0:
        my_result.append(num)

for num in my_list_2:
    if my_list_2.index(num) % 2 != 0:
        my_result.append(num)
print(my_result)

# Task 11

my_str = input("enter string: ")
my_str_1 = []
for i in my_str:
    if my_str.count(i) == 1:
        my_str_1.append(i)
print(my_str_1)
