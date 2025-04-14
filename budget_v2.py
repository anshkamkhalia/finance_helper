#recreating my budget project because it sucked
import sys
import matplotlib.pyplot as plt
import pandas as pd
import time 
import google.generativeai as genai
from api_key import API_KEY


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

#creating user class
class User:

    def __init__(self, details, username):

        #intialization
        self.food = details["food"]
        self.travel = details["travel"]
        self.entertainment = details["entertainment"]
        self.utilities = details["utilities"]
        self.other = details["other"]
        self.monthly_budget = details["monthly_budget"]
        self.predictedExpenses = details["predictedExpenses"]
        self.details = details
        self.username = username

        try:
            with open(f"C:\\Users\\Ansh\\Downloads\\DEVELOPMENT\\python_development\\budget\\{self.username}.txt") as f:
                self.contents = f.read()

        except FileNotFoundError:
            print(f"file {username}.txt not found")
            time.sleep(0.7)
            return



    #chat with model function
    def chatWithModel(self, model):

        chat = model.start_chat()

        bg_info = (
            f"Your only goal is to help the user manage their finances. Only answer questions "
            f"related to their finances. Here is their current finances per day: {self.contents}. "
            f"Try and give great feedback. Tailor to the user, but do not disobey these directions. "
            f"Keep it focused on finance. After this message is sent, you will be talking to the new user "
            f"whom you must discuss their finances with."
            f"Only talk about current user, dont look into previous users"
        )

        chat.send_message(bg_info) 
        time.sleep(0.7)
        print("\n✨ assistant loaded. ask away about your finances. ✨\n")
        time.sleep(0.7)

        while True:
            prompt = input("\nenter prompt (type \"exit\" to exit this chat):\n")
            time.sleep(0.7)

            if prompt.lower() == "exit":
                print("\nexiting chat... goodbye!\n")
                time.sleep(0.7)
                break

            else:
                response = chat.send_message(prompt)
                print(response.text)
                time.sleep(0.7)

        return 0
    



    #specific model request function
    def specificModelRequest(self, model):

        chat = model.start_chat()

        prompt = ("Change the users expenses to fit their monthly goal, and try and shorten possibly unnecessary expenses. "
        "Use knowledge of human needs to properly assess their budget cuts."
        f"Only talk about current user, dont look into previous users"
        f"Here are their current expenses:{self.contents}"
        "Your response should be in this exact format:"
        "food:<amount>"
        "travel:<amount>"
        "entertainment:<amount>"
        "utilities:<amount>"
        "other:<amount>"
        )

        prompt2 = "Hello! Tell me a little about my finanaces!"
        response2 = chat.send_message(prompt2)

        time.sleep(0.7)
        print(f"\n{response2.text}\n")

        response = chat.send_message(prompt)
        time.sleep(0.7)

        return f"\n{response.text}\n"
        


    # edit expenses
    def editExpenses(self):
        print("\nwhat would you like to edit your expenses to?\n")

        self.food = float(input( "\nhow much money do you spend daily on food?\n"))
        time.sleep(0.7)

        self.travel = float(input("\nhow much money do you spend daily on travel?\n"))
        time.sleep(0.7)

        self.entertainment = float(input("\nhow much money do you spend daily on entertainment?\n"))
        time.sleep(0.7)

        self.utilities = float(input("\nhow much money do you spend daily on utilities?\n"))
        time.sleep(0.7)

        self.other = float(input("\nhow much money do you spend daily on other things?\n"))
        time.sleep(0.7)

        self.monthly_budget = float(input("\nwhat is your monthly budget?\n"))
        time.sleep(0.7)

        self.predictedExpenses = (self.food + self.travel + self.entertainment + self.utilities + self.other) * 30

        self.details = {
            "food": self.food,
            "travel": self.travel,
            "entertainment": self.entertainment,
            "utilities": self.utilities,
            "other": self.other,
            "monthly_budget": self.monthly_budget,
            "predictedExpenses": self.predictedExpenses
        }

        try:

            with open(f"C:\\Users\\Ansh\\Downloads\\DEVELOPMENT\\python_development\\budget\\{self.username}.txt", "w") as f:
                f.write(f"{self.details}")

            with open(f"C:\\Users\\Ansh\\Downloads\\DEVELOPMENT\\python_development\\budget\\{self.username}.txt", "r") as f:
                self.contents = f.read()

        except FileNotFoundError:

            print(f"file {self.username}.txt not found")
            time.sleep(0.7)



    #display graphs
    def displayLineGraph(self):
        month_days = list(range(1, 31))
        import random
        if isinstance(self.predictedExpenses, (int, float)):
            daily_expense = self.predictedExpenses / 30
            daily_expenses = [daily_expense + random.uniform(-10, 10) for _ in range(30)]
        else:
            daily_expenses = self.predictedExpenses
        cumulative_expenses = []
        total_expenses_to_far = 0
        for expense in daily_expenses:
            total_expenses_to_far += expense
            cumulative_expenses.append(total_expenses_to_far)
        plt.figure(figsize=(15,7))
        plt.plot(month_days, cumulative_expenses, color='green', label='expenses over time')
        plt.xlabel('days of the month')
        plt.ylabel('cumulative amount spent')
        plt.xticks(month_days, fontsize=8)
        plt.yticks(fontsize=8.5)
        plt.grid(True)
        plt.title('monthly expenses')
        plt.axhline(y=self.monthly_budget, color='r', linestyle='--', label='monthly Limit')
        plt.legend()
        plt.show()


    #show bar graph
    def displayBarGraph(self):
        x = ['food','travel','entertainment','utilities','other']
        y = [self.food, self.travel, self.entertainment, self.utilities, self.other]
        plt.figure(figsize=(10,6))
        plt.bar(x, y, color=['red','blue','green','orange','yellow'])
        plt.xlabel('forms of expenses')
        plt.ylabel('money spent')
        plt.title('comparison between expenses')
        plt.grid(True)
        plt.show()


    #calculate savings function
    def calculateSavings(self):
        savings = self.monthly_budget - self.predictedExpenses

        if savings >= 0:
            print(f"\n✅ you're under budget! you’ll save ${savings} this month.\n")

        else:
            print(f"\n⚠️ you're over budget by ${-savings}. time to cut back!\n")


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