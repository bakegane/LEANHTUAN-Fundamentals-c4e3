m = int(input("Enter a number? "))

for i in range (m):
    if i%2==0:
        print('x',end='')
    else:
        print('*',end='')