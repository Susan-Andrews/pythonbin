fruit="banana"
print(fruit[2])
phrase="Giraffe Academy"
print(phrase.upper())
print(phrase.lower())
print(phrase.replace("Giraffe","elephant"))
print(phrase.index("G"))
print(phrase[0])
print(len(phrase))
print(phrase.upper().isupper())
print(phrase.lstrip())
print(phrase.rstrip())
print(phrase.strip())
print(phrase.startswith('giraffe'))
print(phrase.endswith("s"))
print(phrase.find("ra"))

# python variables should start with words or underscore 2**3 is 8 and 2*3 is 6

# using a while loop and len function we can loop or iterate through through a string..
fruit='banana'
index=0
while index<len(fruit):
    letter=fruit[index]
    print(index,letter)
    index=index+1
#instead for loop can be used
fruit="banana"
for i in fruit:
    print(i)


# to count number of letters in a word

word="banana"
i=0
for s in word:
    if s=="a":
        i=i+1
print(i)    


# SLICING
new="monty python"
'm' in new
print(new[0:3])
print(new[6:20])
print(new[:])


# in strings space bar not automatically alocated.so add  ' ' in btween and a + sign to add them.
#  parsing and extrating             .find
