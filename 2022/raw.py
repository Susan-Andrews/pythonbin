#                                                                                 CALCULATOR

#n1=int(input("enter first number:"))
#n2=int(input("enter the second number:"))
#result=n1+n2
#print(result)                   # int is changed to float to add float numbER

#                                                                                 MAD LIBS GAME
#color=input("enter the color")
#plural_noun=input("enter a plural noun")
#celebrity=input("enter any name")
#print("roses are"+color)
#print(plural_noun + "color is blue")
#print("i know "+celebrity)
#                                                                               LANGUAGE TRANSLATOR

def translate(phrase):
    translation=""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translation=translation="G"
            else:
                translation=translation+"g"
        else :
            translation=translation+letter
    return translation
print(translate(input("enter a phrase")))         
#                                                                             DICTONARY

print("This is a dictionary")
dict = {"aman" : "peace", "condemn" : "to deny", "polishing" : "to grind"}
print("Enter Your Query")
w1 = input()
print("the meaning is", dict[w1])








