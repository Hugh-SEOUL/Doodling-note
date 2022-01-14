id_List = ["apple", "banana", "chicken","Dool"]
id_password = [1234, 1234, 1234, 1234]


id_input = input("input your ID: ")

if id_input in id_List:
    password_input = int(input("input your password: "))
#input function is always string type!
#it must be used int function as it's number
    if password_input in id_password:
        print(id_input + " has been logged in")
    else:
        print("invaild password")
else:
    print("invaild ID")