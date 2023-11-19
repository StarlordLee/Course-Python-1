username = "piper"
password = "12345"
if username == "piper" and password == "12345":
    print("Log in successful!")
else:
    print("Log in not successful!")



#Dve opcije za ovo, gornja, i donja. 
if username == "piper":
    if password == "12345":
        print("Log in successful!")
    else:
        print("Wrong password!")
else:
    print("Wrong username!")