


FN= input("Enter Your First Name: ")
LN= input("Enter Your Last Name: ")
SN= (input("Enter Student Number: "))

print(" --------------Conestoga College-------------------------")
Courses= {
    "PROG1783" : " Programing ", 
    "INFO1385" : " Networking 1 ",
    "COMM1085" : " Reading and Writing",
    "COMM1145" : " Information Technology Documentation"
}
print(" Course code         Subject names ")
for key in Courses:
    print(key + "       "+ Courses[key])

Register =  input("Enter Course Code To get registered: ").split(", ")

print(FN+  " "  +  LN  +  "      "  +  SN)
for code in Register:
    print(code+ " " + Courses[code])