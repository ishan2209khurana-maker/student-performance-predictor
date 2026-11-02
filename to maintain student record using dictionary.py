# Program to maintain student records using dictionary data structure
students={}
n=int(input("Enter the  number of students:"))
for i in range(n):
    name=input("Enter name: ")
    roll=int(input("Enter the roll number: "))
    marks=int(input("Enter the marks: "))
    students[roll]={"name":name,"marks":marks}
print("\n Student records: ")
for roll,details in students.items():
        print("Name: ",details["name"])
        print("Roll number: ",roll)
        print("Marks: ",details["marks"])
