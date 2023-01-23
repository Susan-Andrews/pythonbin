tuple="home"
print(type(tuple))               # class-str


tuple="home",
print(type(tuple))               # class-tuple

#x,y=1,2,3,4                      produces an error since the number of left side variables must equal to right side values

# TUPLE AS RETURN VALUES

a,b=map(int,input("enter two numbers: ").split())
def div_mod(a,b):
    quotient=a/b
    remainder=a%b
    return quotient,remainder 

print(div_mod(a,b))    # value return as a tuple


a=(10,20,30,40,50,1,2)
def max_min(t):
    return max(t),min(t)

print(max_min(a))        # output (50,1)
