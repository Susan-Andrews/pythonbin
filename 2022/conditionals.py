# if
#x=int(input( 'enter a number'))             use this by changing the settings for vscode
#code
x=5
if x==5:
    print('x is equal to 5')
if x<4 : 
    print('hai')

# elif
y=10
if y==10:
    print('next step if true')
elif y<10:
    print('still its true')
elif y>10:
    print('its not true')
else :
    print('i am gonna exit it')
print("ALL DONE")

# TRY AND EXCEPT
#  if try works then except fails and vice versa.
# try and except block cant have more than one statement.whether if it is print statement then should indent with try and except block
z='hai'
try:
    k=int(z)
except:
    k=-1
print(k)
z ='23'
try:
    k=int(z)
except:
    k=-1 
print(k)

