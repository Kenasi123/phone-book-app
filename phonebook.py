hasQuit = False
phonebook = {"Kenasia": "7708414156"
"Drake":"9175553249"}

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
        phonebook.update({"Name": name})
        phone_number = input("What is the contacts phone number?")
        phonebook.update({"Phone number": phone_number}) 
        phonebook[name] = phone_number 
        print(phonebook)
        print("Contacts added succesfully")
    elif select_option == "1":
        name = input("What contact's number would you like?") 
        if phonebook.get(name) == None: 
             print("There's no contact with that name...")
        else: 
             print("Here's their number: ", phonebook[name]) 
    elif select_option == "5": 
        hasQuit = True  
    elif select_option == "3": 
        name = input("Which contact do you want to remove?") 
        if  phonebook.get(name) != None:
            del phonebook[name] 
            print("Contact removed")
        else:
            print("Theres no contact with that name.")  
    elif select_option == "4": 
        print("Contacts displayed below")
        print(phonebook) 

            
  