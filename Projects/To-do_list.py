#Asks user to input their tasks
todo = []
#Will loop infinetly in order for user to keep modifying their list
while True:
    #will print their current to do list
    print (f"Your current tasks are: ")
    #iterates over list
    for x in todo:
        #prints items stacked over another
        print(x)
    #Prompts the user to pick from either adding, removing, or clearing from their current list
    modify = (input("Would you like to add, remove, or clear all tasks? (type add , remove, or clear)").lower())
    #checks if the users wants to add to their list
    if modify == 'add':
        #Will add whatever the user inputs into their current list
        todo.append (input("What task would you like to add?"))
    #checks if the users wants to remove something from their list
    if modify == 'remove':
        #will remove whichever item the user wishes to remove and prints modifies list
        todo.remove (input("What task would you like to remove?")) 
    #checks if user input clear
    if modify == 'clear':
        #clears list completely
        todo.clear()
       



 

