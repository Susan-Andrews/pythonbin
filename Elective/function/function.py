#Program to define and call function

def my_function():
  print("Hello from a function")
my_function()



#Program function with list as argument
def my_function(food):
 for x in food:
   print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits) 

#Program finding highest of two numbers using function 
x= int(input("enter x"))
y= int(input("enter y"))           
def high2(p,q):
 if p>q:
       m=x
 else:
       m=y
 return m
print (" highest",high2(x,y))

#Program using recursion
l=int(input("enter lower range"))
u=int(input("enter upper range"))
def displayrange(lower,upper):
    if lower<=upper:
        print(lower)
        displayrange(lower+1,upper)

displayrange(l,u)
