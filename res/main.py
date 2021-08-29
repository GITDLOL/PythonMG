import json

def makenew(username:str, password:str):
    data = getdata()

    if username in data and password in data:
        print("Details Already Exist")
    else:
        data[username] = password
    with open("userinfo.json", "w") as j:
        json.dump(data,j)
    return True

def getdata():
    with open("userinfo.json", "r") as j:
        b = json.load(j)
    return b

active = True

print("[ PythonMG Version 0.0.1 ]")
print("[   Created by TorhteYT  ]\n")

while active:
    userinp = input("[PythonMG PROMPT]: ")

    if userinp == "add":
        username = input("Username: ")
        password = input("Password: ")

        makenew(username, password)
    elif userinp == "read D":
        a = input("Username: ")
        b = getdata()

        if a in b:
            print("username " + a)
            print("Password: " + b[a])
        else:
            print("User Doesnt't Exist")