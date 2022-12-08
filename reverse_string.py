#METHOD 1
num =input("enter a string which is to be reversed : ")
print(str(num)[::-1])






#METHOD 2
num = input("enter a string which is to be reversed : ")
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))
