#created variable and emoty dictionary
contacts = dict()
#welcoming the user to the contact book
print("Welcome to the Contact Book!")

while True:
    #Lists options for a user to pick whether to add, delete, list, and exit contacts
    option = int(input(
        """
        Contact Book Menu:
        1. Add Contact
        2. Delete Contact
        3. List Contacts
        4. Exit
        Confirm choice:
        """
    ))
    #checks if user selected option 1
    if option == 1:
        #prompts user to input name of contact
        ac = (input("Type name you would like to add to contacts book:"))
        #prompts user to input the number for the contact
        noc = (int(input("Input number of contact:")))
        #adds new info to dictionary
        contacts[ac] = noc
        #Prints message that contact has been added
        print ("New contact has been added!")
    
    #checks if user selected option 2 in order to comense deleting a contact
    elif option == 2:
        #prompts user to input name of contact which they would like to delete
        dc = (input("Type name you would like to DELETE from contacts book:"))
        #Checks for the name of contact to delete it
        del contacts[dc]
        #prints that contact has been deleted
        print("Contact has been deleted!")
    #checks if user selected option 3
    elif option == 3:
        #prints all the contacts within dictionary
        print(contacts)
    #if user inputs option 4 to exit this code will carry out
    elif option == 4:
        print("Thank You for using Contact Book, goodbye for now!")
        break

