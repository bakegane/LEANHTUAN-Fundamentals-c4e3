a = int(input("a =? "))
b = int(input("b =? "))
c = int(input("c =? "))

d = b*b - 4*a*c
if d < 0:
    print("false")
elif d == 0:
    x = -b / (2 * a)
    print("1 solution: ", x)
else:
    x1 = (-b + d**0.5) / (2 * a)
    x2 = (-b - d**0.5) / (2 * a)
    print("2 solutions: ", x1, x2)