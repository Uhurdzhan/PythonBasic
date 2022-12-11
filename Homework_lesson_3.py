# Task 1

count_students = int(input("How many students want apples?: "))
count_apples = int(input("And how many apples are in basket?: "))
print("one student get:", count_apples // count_students)
print("apples that stay in basket:", count_apples % count_students)

# Task 2

count_students_first_class = int(input("How many pupils in first class? "))
count_students_second_class = int(input("How many pupils in second class? "))
count_students_third_class = int(input("How many pupils in third class? "))
print("The number of desks for the first class:", count_students_first_class // 2 + count_students_first_class % 2)
print("The number of desks for the second class:", count_students_second_class // 2 + count_students_second_class % 2)
print("The number of desks for the third class:", count_students_third_class // 2 + count_students_third_class % 2)

# Task 3

three_digit_number = int(input("Enter three digit number: "))
third_digit = three_digit_number % 10
three_digit_number = three_digit_number // 10
second_digit = three_digit_number % 10
three_digit_number = three_digit_number // 10
new_three_digit_number = third_digit * 100 + second_digit * 10 + three_digit_number
print("reversed number:", new_three_digit_number)

# Task 4*

seconds = int(input("Count of seconds: "))
hours = seconds // (60 * 60)
minutes = (seconds - hours * (60 * 60)) // 60
print("time: ", hours, ":", minutes, ":", seconds - hours * (60 * 60) - minutes * 60, sep="")
