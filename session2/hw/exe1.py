h = int(input("your height? "))
print(str(h)+ "(cm)")
w = int(input("your weight? "))
print(str(w)+ "(kg)")
bmi = w/((h/100)*(h/100))
if bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
elif bmi < 18.5:
    print("underweight")
elif bmi < 16:
    print("Serevely Underweight")
else:
    print("Obese")
