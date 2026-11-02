n=int(input("Enter number of students: "))
student={}
for i in range(n):
    name=input("Enter name: ")
    rollno=int(input("Enter roll number: "))
    marks=int(input("Enter marks: "))
    student[rollno]={"Name":name,"Marks":marks}
rollno=int(input("\n Enter roll number to search: "))
if rollno in student:
       print("\n Student record: ")
       print("\nName: ",student[rollno]["Name"])
       print("\nMarks: ",student[rollno]["Marks"])
       print("\nRoll number: ",rollno) 
else:
      print("Student record not found")
