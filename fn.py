# we use max function to return the maximum value.
big=max('hello world')
print(big)
h=min('HELLO WORLD')
print(h)
 
# functions are often specified on the top the program
def new_fun():
     print("hello")
def sec_fun():
    print("hai")
# simply defining function wont give any result .instead we need to do function call.
 
new_fun()
sec_fun()
new_fun()
new_fun()
sec_fun()

def say(name ,age):         # parameters are given
    print("hello " +name+ " ur age is  "  +age )

#say("sus")    if age not present
#say("alen") 
say("sus","22")               # instead if we pass without string , then add str(age) at print statement



def cube(n):
    return(n*n*n)
    
    print(cube(5))  


