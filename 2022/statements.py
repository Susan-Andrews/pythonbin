
is_male=False                                  # boolean expresssion can be given ie,T,F,T,F
is_tall=True                                      # TTFF
if is_male and is_male :                     # ABD IS TRUE IF BOTH TRUE,OR IS TRUE IF ANY ONE TRUE
    print("he is a tall male")
elif is_male and not(is_tall):
    print("he is not tall and a male")                                            # semicolon
elif not(is_male)  and is_tall:
    print("he is not male but tall")  
else :
    print("he is not a tall male")

                                                                      # since a function hence using retyurn
def max(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    elif c>a and c>b:
        return c


print(max(3,4,5))                

                 #calculator
a=int(input("enter first number:"))     
b=int(input("enter second number:"))     
c=int(input("choose any operator:\n1.+\n2.-\n3.*\n4./\n"))     
if c==1 :
    print(a+b)
elif c==2 :
    print(a-b)  
elif c==3:
    print(a*b)
else :
    c==4
    print(a/b)    

                 #guessing game
word="giraffe" 
guess="" #possible guess entered by user
guess_count=0
limit=4
out_of_limit=False #still have guesses
while guess!=word and not(out_of_limit):#guess not eq to word and still have limit
    if guess_count<=limit:
       guess=input("enter the guess")
       guess_count+=1
    else:
        out_of_limit=True

if out_of_limit:
    print(" out of limit.so you lose")    # no more guesses
else:
    print("you win!")


 #                                  FOR
for i in "susan andrews":
    print (i)


def raise_to_power(base_num,pow_num):
    result=1
    for i in range(pow_num):
        result=result*base_num
    return result

print(raise_to_power(3,2))        
