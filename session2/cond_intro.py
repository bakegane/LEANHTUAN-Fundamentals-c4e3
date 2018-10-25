yob = int(input("Your year of birth? "))
age = 2018 - yob
print(age)
if age < 10:
    print("Baby")
elif age < 18:
    print("Teen")
else:
    print("Adult")