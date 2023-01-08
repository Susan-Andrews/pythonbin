# python program to demonstrate various functions and operations 
 
str1="python program"
str2="string operations"
print("in this line we print the single quotes '' ")
print("length of strings: str1 and str2")
print(len(str1))
print(len(str2))

print("first occurence of o in str1 and r in str2 are")
print(str1.index("o"))
print(str2.index("r"))

print("total count  of o in str1 and  i in str2 are")
print(str1.count("o"))
print(str2.count("i"))

print("String slicing operations ")
print(str1[2:9])
print(str1[2:9:2])
print(str1[2:7])
print(str1[2:9:1])
print(str1[::-1])

print(str2[1:6])
print(str2[2:8:2])
print(str2[2:8])
print(str2[2:8:1])
print(str2[::-1])

print("Upper case and lower case ")
print(str1.upper())
print(str2.upper())
print(str1.lower())
print(str2.lower())

print("str and str2 string functions start with")
print(str1.startswith("python"))
print(str2.startswith("hello"))
print("str and str2 string functions ends with")
print(str1.endswith("afdghdghdfvb"))
print(str2.endswith("operations"))

print("str1 and str2 split operations")
print(str1.split(" "))
print(str2.split(" "))

print("string concatenation")
print(str1 +str2)