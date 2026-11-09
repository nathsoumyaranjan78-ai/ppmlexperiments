minutes = int(input("Enter time in minutes: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print("Time =", hours, "hours and", remaining_minutes, "minutes")