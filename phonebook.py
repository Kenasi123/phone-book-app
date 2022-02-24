hasQuit = False
phonebook = {}

menu = """" 
Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit

""" 

while not(hasQuit):
    print(menu)

    select_option = input("What do you want to do (1-5?)")

    if select_option == "2": 
        name = input("What is the contacts name?") 
        phone_number = input("What is the contacts phone number?") 
        phonebook[name] = phone_number 
        print("Contacts added ssuccesfully")
    elif select_option == "1":
        name = input("What contact's number would you like?") 
        if phonebook.get(name) == None: 
             print("There's no contact with that name...")
        else: 
             print("Here's their number: ", phonebook[name]) 
    elif select_option == "5": 
        hasQuit = True 