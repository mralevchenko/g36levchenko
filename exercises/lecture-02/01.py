str1 = input("Enter a string: ")

first = str1[0]
middle = str1[len(str1) // 2]
last = str1[-1]
new_string = first + middle + last
print("New string:", new_string)


length = len(str1)
if length % 2 == 0:
    first_half = str1[:length // 2]
    second_half = str1[length // 2:]
else:
    first_half = str1[:length // 2]
    second_half = str1[length // 2 + 1:]

if first_half == second_half:
    print("The entered string is symmetrical")
else:
    print("The entered string is not symmetrical")
