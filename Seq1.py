import math
from fractions import Fraction
n=int(input("Enter the limit of the series  1+ 1/2 + 1/3 + 1/4 + ....  + 1/n  : "))
sum=1.0
i=2.0
while(i<=n):
    sum=sum+1.0/round(i,2)
    i=i+1
    
    print(Fraction(sum))
print(sum)    
