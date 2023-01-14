list1=['java','cloud',1995,2010]
list2=[3,6,9,12,15]
list3=['p','q','r','s']

print(list1)
print(list2)
print(list3)
print(" ")

print("Various list operations ")
print(" ")
print("list1[0]: ",list1[0])

print("Slicing")
print("list2[1:5]: ",list2[1:5] )
print("Value at index at 2 of list 1 ", list1[2])

print("Insert elements into list")
list1[2]=2001
print("New value in list1 at index 2 is : ")
print(list1[2])

print("Modified list1: " , list1)
print("Delete from list1")
del list1[2]
print("After deletion at index 2 is ",list1)
print(len(list1),"is the length of list 1")
print(" Max and min on second list:" )
print(max(list2))
print(min(list2))
print("Sum  of list 2 is : ", sum(list2))
print("Delete for multiple elements in the list: ")
del list1[1:4]
print("Modified list: ", list1)
print("Removing from  list3 : p")
list3.remove('p')
print(list3)
print(" ")

print("Sorting list 2")
list2.sort()
print("After sorting: ", list2)

print("Appending in list 2")
list2.append(18)
print("After appending: " , list2)

print("Split operations")
list1[2:4]
list2[1:5]
list3[2:]
print( "Aftr splitting: list1,list2,list3 : ",list1,list2,list3)


print("for loop in lists")
for i in range(len(list2)):
    list2[i]=list2[i] * 3
print("list 2 : ", list2)

print("Creating list in another way")    
a="python"
b=list(a)
print(b)

print(" ")
h='python-program-is-easy'
print(h)
delim='-'
a=h.split(delim)
print("Aftr splitting and delim:", a)

delim='***'
delim.join(a)
print(" ")
print("join on lists")
print(a)

print(" ")
print("Pop on lists")
print("list1 after pop:", list1.pop())

print(" ")
print("Reverse on lists")
v=list2.reverse()
print("list1 after reverse:", v)
