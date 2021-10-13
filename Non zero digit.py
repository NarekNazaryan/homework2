n=int(input())
product=1
while n!=0:
    lastdigit=n%10
    n=n//10
    if lastdigit!=0:
        product=lastdigit*product
print("product=",product)
