print("a=")
a=float(input())
print("b=")
b=float(input())
print("c=")
c=float(input())
disk=b**2-4*a*c
if a==0 and b!=0:
    print("print non quadratic")
    print("solution is ",-c/b)
if disk>=0 and a!=0:
   print("quadratic")
   print("solutinons,",(-b+disk**0.5)/2*a,(-b-disk**0.5)/2*a)
elif disk<0 and a!=0:
    print("quadratic")
    print("No solution")
