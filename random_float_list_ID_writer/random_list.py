import random
student_number = input("Write your student number: ")
last_two_digits = int(student_number[-2:])
lst = [round(random.uniform(0.0, 9.9), 2) for _ in range(last_two_digits)]
def check_conditions(number_list, student_number):
    repeated_numbers = []
    for i in range(1, len(number_list)):
        if number_list[i] == number_list[i - 1]:
            repeated_numbers.append((number_list[i], i))
    matching_numbers = []
    for num in number_list:
        if int(num) in [int(digit) for digit in student_number]:
            matching_numbers.append((num, number_list.index(num)))
    return repeated_numbers, matching_numbers
repeated_nums, matching_nums = check_conditions(lst, student_number)
if repeated_nums:
    print("Condition 1: True")
    print("Repeated numbers and their locations:", repeated_nums)
elif matching_nums:
    print("Condition 2: True")
    print("Numbers matching individual digits of the student number and their locations:", matching_nums)
else:
    print("No conditions met.")
print("Generated List:", lst)
