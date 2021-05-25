# Health Management System
def getdate():
    import datetime
    return datetime.datetime.now()
def take():
    name=list(input("Enter Your name"))
    name=inp.lower()

    c=int(input("Enter 1 for ex and 2 for diet"))
    if (c == 1):
        value = input("type here\n")
        with open(str(name)+ '.txt', "a") as op:
            op.write(str([str(getdate())]) + ": " + value + "\n")
        print("successfully written")
    elif (c == 2):
        value = input("type here\n")
        with open(str(name)+ '.txt' "a") as op:
            op.write(str([str(getdate())]) + ": " + value + "\n")
        print("successfully written")
    else:
        print("plz enter valid input (1(harry),2(rohan),3(hammad)")

def retrieve():
    name = list(input("Enter Your name"))
    name=inp.lower()

    c = int(input("enter 1 for excersise and 2 for food"))
    if (c == 1):
        with open(str(name)+'.txt') as op:
            for i in op:
                    print(i, end="")
    elif (c == 2):
        with open(str(name)+'.txt') as op:
            for i in op:
                print(i, end="")

    else:
        print("plz enter valid input ")
print("health management system: ")
a = int(input("press 1 to add the excercise and diet and 2 to retrieve "))

if a == 1:
    take()
else:
   retrieve()
