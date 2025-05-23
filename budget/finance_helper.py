#recreating my budget project because it sucked
import sys
import matplotlib.pyplot as plt
import time 
import google.generativeai as genai
from api_key import API_KEY
from user import User
#----------------------------user authentication--------------------------------------

print("whats good bro\n")
time.sleep(0.7)
print("welcome to the budget tracker 2.0 which is way better than the old one trust me\n")
time.sleep(0.7)

#checking if there are existing usernames
def read_txt_file(path_name): 

    f = open(f"{path_name}","r")
    currentUsers = f.read()
    f.close()
    return currentUsers

isFileEmpty = read_txt_file("C:\\Users\\Ansh\\Downloads\\DEVELOPMENT\\python_development\\budget\\accounts.txt")

#prompt user for their username
def new_username():
    print("\nlets get you started!\n")
    time.sleep(0.7)
    print("\nwhats ur name?\n")
    while True:
        new_username = input()
        time.sleep(0.7)
        if len(new_username) < 2:
            print("try again")
            time.sleep(0.7)
            continue
        else:
            print(f"\nwelcome {new_username}\n")
            time.sleep(0.7)
            return new_username    

#prompt user for password
def new_password():
    print("\nnow its time for your password\n")
    time.sleep(0.7)

    print("\nyour password must be more than 7 characters\n")
    time.sleep(0.7)

    while True:
        new_password = input("\nwhat is your password:\n")
        time.sleep(0.7)
        if len(new_password) > 7:
            return new_password
        else:
            print("password too short, try again")
            time.sleep(0.7)

#log in
if True:
    print("\nwould you like to sign in to an old account, or create a new one?\n")
    time.sleep(0.7)
    logIn_or_signUp = int(input("log in(1) or sign up(2):\n"))
    time.sleep(0.7)

    if logIn_or_signUp == 1:
        attempts = 0
        username_found = False

        #ask for username
        while attempts < 3:
            username = input("\nenter username:\n")
            time.sleep(0.7)
            accounts = read_txt_file("accounts.txt")

            if username not in accounts.split():
                print("username not found, try again")
                time.sleep(0.7)
                attempts += 1
            else:
                username_found = True
                break
        
        if not username_found:
            time.sleep(0.7)
            sys.exit("\nusername not found\n")

        attempts = 0
        password_found = False

        #ask for password
        while attempts < 3:
            print(f"\nhey {username}, we just need your password\n")
            time.sleep(0.7)
            password = input("\nenter password:\n")
            time.sleep(0.7)

            if password not in accounts.split():
                print("password incorrect, try again")
                time.sleep(0.7)
                attempts += 1
            else:
                password_found = True
                break

        if not password_found:
            time.sleep(0.7)
            sys.exit("\npassword not found\n")

    #sign up
    else:
        username = new_username()
        password = new_password()

        f = open("accounts.txt", "a")
        time.sleep(0.7)
        f.write(f"{username} {password}\n\n")
        f.seek(0)
        f.close()
        time.sleep(0.7)

#---------------------------------personalized files--------------------------------
print(f"\nwe're ready to go {username}!\n")
time.sleep(0.7)

print("\nnow we need to know some of your spending habits\n")
time.sleep(0.7)

fileNotFound = False

#checking if current user already has a personalized file
try:
    f = open(f"{username}.txt", "r")
    f.read()
except:
    fileNotFound = True

#configuring model
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

#------------------------------------------data----------------------------------

#obtaining expenses
food = float(input("\nhow much money do you spend daily on food?\n"))
time.sleep(0.7)

travel = float(input("\nhow much money do you spend daily on travel?\n"))
time.sleep(0.7)

entertainment = float(input("\nhow much money do you spend daily on entertainment?\n"))
time.sleep(0.7)

utilities = float(input("\nhow much money do you spend daily on utilities?\n"))
time.sleep(0.7)

other = float(input("\nhow much money do you spend daily on other things?\n"))
time.sleep(0.7)

monthly_budget = float(input("\nwhat is your monthly budget?\n"))
time.sleep(0.7)

predictedExpenses = (food + travel + entertainment + utilities + other) * 30

details = {
    "food": food,
    "travel": travel,
    "entertainment": entertainment,
    "utilities": utilities,
    "other": other,
    "monthly_budget": monthly_budget,
    "predictedExpenses": predictedExpenses
}

#save files and stuff
path = f"C:\\Users\\Ansh\\Downloads\\DEVELOPMENT\\python_development\\budget\\{username}.txt"

try:
    with open (f"C:\\Users\\Ansh\\Downloads\\DEVELOPMENT\\python_development\\budget\\{username}.txt","w"):
        pass
except:
    pass


if not fileNotFound:

    f = open(path, "a")
    f.write(f"{details}")
    f.close()

else:

    f = open(path, "w")
    f.write(f"{details}")
    f.close()

time.sleep(0.7)
print("\ndata saved successfully 🎉\n")
time.sleep(0.7)
#----------------------------------------main loop---------------------------------------------------

#intializing current user
currentUser = User(details, username)

#command line interface
while True:
    action = int(input("\nchat with model(1)\nspecificmodelrequests(2)\nedit expenses(3)\ndisplay line graph(4)\ndisplay bar graph(5)\ncalculate savings(6)\n"))
    time.sleep(0.7)

    if action == 1:
        result = currentUser.chatWithModel(model)
        print(result)
        time.sleep(0.7)

    if action == 2:
        result = currentUser.specificModelRequest(model)
        print(result)
        time.sleep(0.7)

    if action == 3:
        currentUser.editExpenses()
        time.sleep(0.7)

    if action == 4:
        currentUser.displayLineGraph()
        time.sleep(0.7)

    if action == 5:
        currentUser.displayBarGraph()
        time.sleep(0.7)

    if action == 6:
        currentUser.calculateSavings()
        time.sleep(0.7)

    if action not in [1,2,3,4,5,6]:
        sys.exit("dont waste my time lil boi")

    time.sleep(0.7)