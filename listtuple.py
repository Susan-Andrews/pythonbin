from typing import Dict  # to use all fns


x=['s','d','r']           #lists
y=[1,2,33,4]
z=[6,7,8,9,66,123,456,4,2,54]
k=list()
for i in y:
     print(i)
number_grid=[ [1,2,3] ,[4,5,6] ,[7,8,9] ,[0] ] 
print(number_grid[2][1])  

y[2]=5                #changed the value
print(y) 
print(len(y))   
print(range(len(y)))
print(range(len(x)))
print(range(4))
print(x+y+z)               #concatenation
print(z[1:3])              # slicing         btw the range
print(z[:4])                                 # upto 4
print(z[3:])                                 # from 3
print(z[:])                                  # all
print(type(k))
print(dir(k))
k.append('hai')
9 in z
print(x.sort())

#split breaks the string into many pieces and produce a list of strings.
abc="with three words"
pqr=abc.split()
print(pqr)                   # shows a list of the string words
print(len(pqr))
print(len(abc))
print(pqr[1])
for w in pqr:
    print(w)
x='s;d;r'
print(x)
e=x.split(';') #instead of white spaces it splits using the semicolon
print(e)
list=list()
list.append(21)
list.append(340)
print(list)



purse=dict()                                 # dictionaries
purse['money']=200
purse['book']=3
purse['candy']=66
print(purse)


print(purse['candy'])
print(purse['candy']+3)

jjj={'money': 200, 'book': 3, 'candy': 66}
print(jjj.keys())
print(jjj.values())
print(jjj.items())  # show in tuple form
 # print(list(jjj))  here we had used list so error ow its a function.

for (aaa,bbb) in jjj.items():
     print(aaa,bbb)                           

d={ 'asus':2 ,'chai':3 , 'bthen':5}   
t=sorted(d.items())                     #to sort acc to alaph of key
print(t)
for (o,m) in t:
    print(o,m)
    # if we create a tuple then we can sort the thing using value..

b={ ('asus',32),('chai',33) , ('bthen',25) }
 



