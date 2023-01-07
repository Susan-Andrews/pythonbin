sum=0
num=int(input("enter nay number:"))
temp=num
for i in range(temp):
    i=temp % 10
    sum=sum+ (i*i*i)
    temp=temp//10
if sum==num:
    print("YES")
else:
    print("NO")
