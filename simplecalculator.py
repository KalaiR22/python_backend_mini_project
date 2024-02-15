#create functions for add, sub, mul, div
#print the choice to the user
#get the inputs from the user to calculate
#call the function based on the calculation
#use loop to calculate continuosly


def add(a,b):
    res=a+b
    print(str(a) + " + " + str(b) + " = " + str(res) ,"\n")

def sub(a,b):
    res=a-b
    print(str(a) + " - " + str(b) + " = " + str(res) ,"\n")

def mul(a,b):
    res=a*b
    print(str(a) + " * " + str(b) + " = " + str(res) ,"\n")

def div(a,b):
    res=a/b
    print(str(a) + " / " + str(b) + " = " + str(res) ,"\n")


while True:
   
   print("A.Addition")
   print("B.Subtraction")    
   print("C.Multiplication")     
   print("D.Division")     
   print("E.Quit")     
   choice=input("Enter your choice:")
   if choice=="A" or choice=="a":
       print("Addition")
       a=int(input("Enter the value of a: "))
       b=int(input("Enter the value of b: "))
       add(a,b)
   elif choice=="B" or choice=="b":
        print("subtraction")
        a=int(input("Enter the value of a: "))
        b=int(input("Enter the value of b: "))
        sub(a,b)
   elif  choice=="C" or choice=="c":
        print("Multiplication")
        a=int(input("Enter the value of a: "))
        b=int(input("Enter the value of b: "))
        mul(a,b)
   elif  choice=="D" or choice=="d":
        print("Division")
        a=int(input("Enter the value of a: "))
        b=int(input("Enter the value of b: "))
        div(a,b)
   elif choice=="E" or choice=="e":
        print("Progam ended")  
        quit()
          
   
