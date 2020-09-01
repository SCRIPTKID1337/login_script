user_name = "sourav"
password = 1234567890
name = input("Type user name : ")
passw = int(input("Type password : "))
login = False
while not login:
    if user_name == name and password == passw: 
        print ("**Hii sourav**")
        login = True
    else :
        print ("user name and password is not maching*")
        name = input("Type user name : ")
        passw = int(input("Type password : "))
        

