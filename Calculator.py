print('''
    ADD +
    SUBTRACT -
    MULTIPLY *
    DIVIDE /
      ''')
Num1= int(input("ENTER THE VALUE a"))
Num2= int(input("ENTER THE VALUE b"))
Opr= input("ENTER THE OPERATORS")

if Opr== "+":
   print(Num1+Num2)

if Opr== "-":
   print(Num1-Num2)

if Opr== "*":
   print(Num1*Num2)

if Opr== "/":
   print(Num1/Num2)   

if Opr!="+" and Opr!="-" and Opr!="*" and Opr!="/":
   
   print("Syntax Error")