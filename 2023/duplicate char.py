str=input("Enter your string: ")
first_name=[]
dup=[]
for i in str:
    if i not in first_name:
        first_name.append(i)
    else:
        if i not in dup:
            dup.append(i)
print( "" .join(dup))            