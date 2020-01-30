username = input("Username : ")
password = input("Password : ")
if username == "admin" and password == "12345":
    print("Welcone :)")
    print("pencil = 5 THB")
    pencil = 5
    print("book   = 50 THB")
    book = 50
    print("pen    = 15 THB")
    pen = 15
    print("How many ?")
    a = int(input("pencil : "))
    b = int(input("book : "))
    c = int(input("pencil : "))
    total = (5*a)+(50*b)+(15*c)
    print("Total",total,"THB")
else :
    print("ERROR !!")

