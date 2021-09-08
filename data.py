import requests 
import json 

URL_1 = "http://127.0.0.1:8000/login"
URL_2 = "http://127.0.0.1:8000/register"

def get_data():
    email = str(input("Enter your registered email :: "))
    password = str(input("Eneter your passsword :: "))
    data = {"email" : email , "pass_1" : password}
    json_data = json.dumps(data)
    r = requests.post(url = URL_1 , data = json_data)
    data = r.json()
    print(data)
        

def post_data():
    fname = str(input("Enter your first name  : "))
    lname = str(input("Enter your last name  : "))
    Phone = str(input("Enter your Phone number  : "))
    e_mail = str(input("Enter your email : "))
    pass1 = str(input("Enter your password name  : "))
    city= str(input("Enter your City name  : "))
    State = str(input("Enter your State name  : "))
    Country = str(input("Enter your country name  :  "))
    Zip_code = int(input("Enter your postal code : "))
    dat = {"f_name" : fname,"l_name" : lname,"Phone" : Phone,"email" : e_mail,"pass_1" : pass1,"City" : city,"State" : State,"Country" : Country,"Zip_code": Zip_code }
    json_data = json.dumps(dat)
    print(json_data)
    r = requests.post(url=URL_2, data = json_data) 
    data = r.json()
    print(data)

print("[1] Register " )
print("[2] Login " )
print("Press any key to exit !!")
Choice = int(input("Choose according to your need."))
if Choice == 1 :
    post_data()
elif Choice == 2 :
    get_data()
else :
    exit()
