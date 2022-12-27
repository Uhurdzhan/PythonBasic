# Task 1

my_list = [1, 42, 53, 744, 293, 100, 43, 17, -434]
for i in my_list:
    if i > 100:
        print(i, end=" ")

# Task 2

my_list = [57, -262, 571, 758, 2, 23, 73, 11, 100]
my_results = []
for i in my_list:
    if i > 100:
        my_results.append(i)
print(my_results)

# Task 3

my_list = [57]
count_elements = len(my_list)
if count_elements < 2:
    my_list.append(0)
    count_elements += 1
last_element = count_elements - 1
penultimate_element = count_elements - 2
if count_elements >= 2:
    my_list.append(my_list[last_element] + my_list[penultimate_element])
print(my_list)
