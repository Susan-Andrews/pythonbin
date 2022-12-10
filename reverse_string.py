#METHOD 1
str_rev =input("enter a string which is to be reversed : ")
print(str(str_rev)[::-1])






#METHOD 2
str_rev= input("enter a string which is to be reversed : ")
reversed_num = 0

while str_rev != 0:
    digit = str_rev % 10
    reversed_num = reversed_num * 10 + digit
    str_rev //= 10

print("Reversed Number: " + str(reversed_num))
