# Program to find sum of two numbers
a=5
b=6
s=a+b
print(s)

# output
11


# Program to perform arithmetic operation on two numbers
a=10
b=6
s=a+b
diff=a-b
m=a*b
dn=a/b
print (a,b)
print (s)
print (diff)
print (m)
print (dn)

# output
10 6
16
4
60
1.6666666666666667

# Program to find highest of two numbers
x=10
y=10
if x < y:
   print('x is less than y')
elif x > y:
   print('x is greater than y')
else:
   print('x and y are equal')


# output
x and y are equal

# Program to input two numbers and find highest.
x=input('enter a number x')
y=input('enter a number y')
if x < y:
   print('x is less than y')
elif x > y:
   print('x is greater than y')
else:
   print('x and y are equal')

# Program to input three numbers and find highest.
x=int(input('enter a number x'))
y=int(input('enter a number y'))
z=int(input('enter a number z'))
if x > y:
    big=x
else:
    big=y
if big< z:
  big=z
print('highest is ', big)

# Program grade calculation
m=int(input("enter marks  "))
if m>80:
    print("Distinction")
elif m>60:
    print("First Class")
elif m>50:
    print("Secod Class")    
else:
    print("pass ")



# Program using switch statement.
def monday():
    return "monday"
def tuesday():
    return "tuesday"
def wednesday():
    return "wednesday"
def thursday():
    return "thursday"
def friday():
    return "friday"
def saturday():
    return "saturday"
def sunday():
    return "sunday"
def default():
    return "Incorrect day"
switcher = {
    1: monday,
    2: tuesday,
    3: wednesday,
    4: thursday,
    5: friday,
    6: saturday,
    7: sunday
    }

def switch(dayOfWeek):
    return switcher.get(dayOfWeek, default)()
n=4
print(switch(n))




# Program to print n numbers.
n=10
for i in range(0,n):
   print (i),

# output
0
1
2
3
4
5
6
7
8
9


#Program sum of 10 numbers
n=10
s=0
for i in range(0,n):
  x=int(input('enter a number'))
  s=s+x
print (s)

# Program to find factorial of a number.
n=5
for i in range(1,n):
  n=n*i
print (n)


# Program to find sum of all numbers between 0 and 1 using while loop.
n=10
i=1
sum=0
while i<n:
  sum=sum+i
  i=i+1
print(sum) 