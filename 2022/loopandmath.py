#indentation shows the end of loop.just like{} 
#                WHILE
n=5
while n>0:                                     # colon
    print("hai")
    print(n)
    n=n-1
print("stopped")                             # end of loop so no indentation 
print(n)


#               BREAK:AFTER IT DO NOT ITERATE THROUGH THE LOOP,CONTINUE IS VIE VERSA
n=0
while True:
    if n==3:              #every number is true if it is not zero and other values are true if not empty
        break
    print(n)
    n=n+1

#  IF

for i in [1,2,3,4,5] :              # colon
    print (i)
    print ("its",i)
print("blastoff")    
------------------------------------------------------------------------------------------------------------------------------------------------

# any work with numbers integers result in floating point value . can use int() and float() to control this
abc='123'
print(abc)
de=int(abc)
print(de+1)
h=5
w=12
print(w/3)

  # finding the largest number
largest_number=-1
print("before",largest_number)
for number  in [2,22,56,45,2,78,99,12,48,3]:
    if largest_number < number:
        largest_number=number
    print( largest_number,number) 
print("after", largest_number)    
# 0 is 0.0 FALSE but 0==0.0


from math import *
n=-5                          # TO DO THIS WE NEED TO IMPORT A EXTENSION.
print(abs(n))                 # from math import *
print(pow(3,2))
print(max(10,5))
print(round(4.2678))
print(floor(3.456))  # modifiies by removing the point
print(ceil(3.7)) #round the number
print(sqrt(36))
