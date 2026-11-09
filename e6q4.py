def check_value(lst, value):
    return value in lst


lst = list(map(int, input("Enter the list elements: ").split()))
value = int(input("Enter the value to search: "))

if check_value(lst, value):
    print("Value is present in the list")
else:
    print("Value is not present in the list")