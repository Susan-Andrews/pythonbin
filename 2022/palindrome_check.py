string_to_check =input("enter a string to check whether a string is palindrome : ")
reverse_string=str(string_to_check)[::-1]

if string_to_check==reverse_string:
    print("Its a Palindrome")
else:
    print("Its not a Palindrome")    
