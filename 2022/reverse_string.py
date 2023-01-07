#METHOD 1
str_rev =input("enter a string which is to be reversed : ")
print(str(str_rev)[::-1])






#METHOD 2
def reverse(string_rev):
    str = ""
    for i in string_rev:
        str = i + str
    return str
  

string_rev=input("Enter a string to be reversed: ")
print("The original string is : ", end="")
print(string_rev)
  
print("The reversed string  is : ", end="")
print(reverse(string_rev))
