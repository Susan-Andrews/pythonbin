punc="~`!@#$%^&*()_-|\[]{}'"";:?/><.,+="
str=input("enter a string:")
no_punc=''
for char in str:
    if char not in punc:
        no_punc=no_punc+ char
print(no_punc) 
