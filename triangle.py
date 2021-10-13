a=int(input())
b=int(input())
c=int(input())
if a+b>c and b+c>a and a+c>b:
    if c>a and c>b:
        c**2==a**2+b**2
        print("Right triangle")
    elif c**2<a**2+b**2:
        print("Acute traingle")
    elif c**2>a**2+b**2:
        print("Obuse triangle")
    if a > b and a > c:
        if a ** 2 == c ** 2 + b ** 2:
            print("Right triangle")
        elif a ** 2 < c ** 2 + b ** 2:
            print("Acute triangle")
        elif a ** 2 > c ** 2 + b ** 2:
            print("Obuse triangle")
    if b > a and b > c:
        if b ** 2 == a ** 2 + c ** 2:
            print("Right trangle")
        elif b ** 2 < a ** 2 + c ** 2:
            print("Acute traingle")
        elif b ** 2 > a ** 2 + c ** 2:
            print("Obuse triangle")
    if a == b == c:
        print("Acute triangle")
else:
    print("No Triangle")