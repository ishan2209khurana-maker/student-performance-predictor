# to design menu driven calculator using modular programming and control structures
exit_program=False
while not exit_program:
     a=int(input("Enter the number: ")) 
     b=int(input("Enter the number: "))
     print("------ Calculator menu --------\n")
     print("1.Addition \n")
     print("2.Subtraction \n")
     print("3.Multiplication \n")
     print("4.Division \n")
     print("5.Square of a number \n")
     print("6.Cube of a number \n") 
     print("7.Exit")
     c=int(input("Enter the choice:\n"))
     if(c==1):
      print("Addition of two numbers: ",a+b) 
     elif(c==2):
      print("Subtraction of two numbers: ",a-b)
     elif(c==3): 
       print("Multiplication of two numbers: ",a*b)
     elif(c==4):
       print("Division of two numbers: ",a/b)
     elif(c==5):
       print("Square of two numbers: ",a**2,b**2)
     elif(c==6):
      print("Cube of two number: ",a**3,b**3)
     elif(c==7):
        break
