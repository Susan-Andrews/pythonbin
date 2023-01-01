ch=0 
lp=1
while lp==1:
    print("WELCOME")
    print("Your options are:")
    print(" ")
    print(" 1. Demonstrate Conversions")
    print(" 2. Integer to Float conversion") 
    print(" 3. Mathematical Functions")
    print(" 4. Date and Time")
    print(" 5. Quit")
    print(" ")

    ch=int(input("Enter your choice: "))

    if ch==1:
        print(" 1. Demonstrate Conversions")
        decnum=int(input("Enter a decimal value to be converted:"))
        print(bin(decnum)," :binary equivalent")
        print(oct(decnum)," :octal equivalent")
        print(hex(decnum)," :hexadecimal equivalent")  
    elif ch==2:
        print(" 2. Integer to Float conversion") 
        decnum2=int(input("Enter an integer value to be converted:"))
        flotnum=float(decnum2)
        print("Value is :" , flotnum)

    elif ch==3:
        print(" 3. Mathematical Functions")
        import math
        num=float(input("Enter n in float:"))
        print(" Floor Value is : ",math.floor(num))
        print(" Round Value is : ",round(num))
        print(" Ceil Value is : ",math.ceil(num))

        num2=int(input("Enter an integer value :"))
        print(" Absolute  Value is : ",abs(num2))
        print(" square root  Value is : ",math.sqrt(num2))

    elif ch==4:
        import datetime
        today=datetime.date.today()
        print(today)
        print("ctime:" , today.ctime())
        print("Tuple: ", today.timetuple() )
        print("ordinal:" , today.toordinal())
        print("Year: " , today.year)
        print("Month: " ,today.month )
        print("Day: ", today.day)
    elif ch==5:
        lp=0
    print("Thankyou! ")
    print(" ")

  
