#opens the todo list file
with open("Projects/todo.txt") as file:
    #will read the lines saved within the file
    todo = file.readlines()
#Will loop infinetly in order for user to keep modifying their list
while True:
    #will print their current to do list
    print (f"Your current tasks are: ")
    #iterates over list
    for x in todo:
        #prints items stacked over another
        print(x)
    #Prompts the user to pick from either adding, removing, clearing, or closing their current list
    modify = (input("Would you like to add, remove, clear, or close?(type add , remove, clear, or close)").lower())
    #checks if the users wants to add to their list
    if modify == 'add':
        #Will add whatever the user inputs into their current list
        todo.append (input("What task would you like to add?" +"\n"))
    #checks if the users wants to remove something from their list
    if modify == 'remove':
        #will remove whichever item the user wishes to remove and prints modifies list
        todo.remove (input("What task would you like to remove?")) 
    #checks if user input clear
    if modify == 'clear':
        #clears list completely
        todo.clear()
    #if the user chooses to close the todo list this code will carry
    elif modify == 'close':
        #Will open the file to write and save the current to do list in
        with open ("todo.txt","w") as file:
            file.writelines(todo)
        #will stop the loop so the user can exit 
        break
