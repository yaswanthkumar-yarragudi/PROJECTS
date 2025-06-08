def calc(a,b,x):

    if(x=='+' or x=='1'):
        print(f"\n{a} + {b} = {a+b}\n")
        H=input("\nWant to continue enter ('Any number') else ('Any Alphabet') --> ")
    elif(x=='-' or x=='2'):
        print(f"\n{a} - {b} = {a-b}\n")
        H=input("\nWant to continue enter ('Any number') else ('Any Alphabet') --> ")
    
    elif(x=='*' or x=='3'):
        print(f"\n{a} * {b} = {a*b}\n")
        H=input("\nWant to continue enter ('Any number') else ('Any Alphabet') --> ")
    
    elif(x=='/' or x=='4'):
        if(b==0):
            print("\nUndefined")
        else:
            print(f"\n{a} / {b} = {a/b}\n")
        H=input("\nWant to continue enter ('Any number') else ('Any Alphabet') --> ")
    
    elif(x=='%' or x=='5'):
        if(b==0):
            print("\nUndefined")
        else:
            print(f"\n{a} % {b} = {a%b}\n")
        H=input("\nWant to continue enter ('Any number') else ('Any Alphabet') --> ")
    
    elif(x=='**' or x=='6'):
        print(f"\n{a} pow {b} = {a**b}\n")
        H=input("\nWant to continue enter ('Any number') else ('Any Alphabet') --> ")


    else:
        print("Sorry ! ,Wrong Input Try again...\n")
        a=int(input("Enter 1st Input:"))
        b=int(input("Enter 2nd Input:"))
        x=input("Enter Operator:")
        calc(a,b,x)

    if(H.isnumeric()):
        a=int(input("\nEnter 1st Input:"))
        b=int(input("Enter 2nd Input:"))
        x=input("Enter Operator:")
        calc(a,b,x)
    else:
        print("\n...... Thank YOU ......")
 

print("\n(+) or (1) -- Addition")
print("(-) or (2) -- Subtraction")
print("(*) or (3) -- Product")
print("(/) or (4) -- Division")
print("(%) ""or (5) -- Remainder")
print("(**) or (6) -- Power\n")


a=int(input("Enter 1st Input:"))
b=int(input("Enter 2nd Input:"))
x=input("Enter Operator:")
calc(a,b,x)
