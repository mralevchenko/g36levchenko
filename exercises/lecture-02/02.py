str1 = input("Enter a string: ")
half = len(str1) // 2
if str1[:half] == str1[-half:]:
    print("The entered string is symmetrical")
else:
    print("The entered string is not symmetrical")
