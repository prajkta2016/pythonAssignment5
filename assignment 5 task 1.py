m1={"alice":85,"bob":45,"alia":95,"bobby":87}
print("name & students mark are :",m1)
a=input("enter  name to be searched ")
if a in m1:
    print("marks of student are :",m1[a])
else:
    print("this is not a student")
