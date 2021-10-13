n=int(input())
newlist=[]
def division(n):
    k=n
    t=0
    while k>0:
        if n%k==0:
         newlist.append(k)
         t=t+1
        k=k-1
    print(newlist,t)



print(division(n))