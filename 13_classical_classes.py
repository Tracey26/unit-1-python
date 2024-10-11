"""
Task 0: Class We-do

Create a class for video game, that tracks its health,
    -Create methods for damage 

Then create a subclass called the "Player" that has more health
    - Create a method for healing
"""
class Character:
    health = 20

    def __init__(self, name,): 
        self.name = name
       
    def damage(self, dmg=1):
        self.health = self.health - dmg

class Player(Character):
    health = 50

    def healing(self):
        if self.health < 50:
            self.health = self.health + 1

enemy1 = Character("Balthazar")
enemy1.damage()
print(enemy1.health)

player = Player("Frank")
player.healing()
print(player.health)



"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
class Person:
    def __init__(self, name, age): 
        self.name = name
        self.age = age

    def hello(self):
        print("Hello I am Franklin")


franklin = Person("Franklin", 101)
franklin.hello()

print(franklin.name)
print(franklin.age)
"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
class Animals:
    def speak(self, speak):
        self.speak = speak
       

class Dog(Animals):
    def speak(self):
        print("WOOFFFFF")

dog = Dog("DOG")
Dog.speak()
print(Dog.speak)









class Animals:
    def speak(self, speak):
        self.speak = speak

class Dog(Animals):
    def speak(self):
        print("WOOFFFFF")
        

Dog = Animals()
Dog.speak()
print(Dog.speak)




"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""