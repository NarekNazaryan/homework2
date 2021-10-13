def summofdigit(n):
    summ=0
    while n>0:
        digit=n%10
        n=n//10
        summ=summ+digit
    return(summ)
n=int(input())
d=summofdigit(n)
while d>10:
    d=summofdigit(d)
print(d)