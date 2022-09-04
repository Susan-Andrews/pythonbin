# handle=open("file_name","mode") -> used to open a file
# take notepad file to python vscode then do the work
# how to count number of lines in a file
file_open=open("test.txt")
count=0
for line in file_open:
    count=count+1
    #print(" number of lines line count:",count)
print(" number of lines line count:",count)   
file_open.close()

# how to count number of characters
file_open=open("test.txt")
inp=file_open.read()
print(len(inp))
print(inp[:20])

# search something and printing them from the file
file_open=open("test.txt")
for line in file_open:
    if line.startswith('Setting'):
        print(line)
# to avoid white space or new line character ..we use strip function
# syntax is : line =line.strip() add this after for loop.or beg of for loop
#TAKING INPUT AS A FILE NAME      : as normal as taking character 

# how to read file here
employee_file=open("test.txt")
print(employee_file.read())
employee_file.close()


employee_file=open("test.txt","a")
print(employee_file.write("\nand it continues"))
employee_file.close()

# counting  pattern can be done also using the help of dictonary
#split is used to cut the line into diff words to smooth the use.
count=dict()
line=input('enter a line ')
words=line.split()
print('words:',words)
print('counting')
for word in words:
    count[word]=count.get(word,0)+1
    print('counts',count)


