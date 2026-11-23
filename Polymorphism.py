from abc import ABC, abstractmethod
class Animal (ABC):

    def move(self):
        pass
    

class Human (Animal):
    
    def move(self):
        print("I can walk and run")
    
class Snake (Animal):
    
    print("I can crawl")
    
class Dog (Animal):
    
    print("I can bark")
    
class Lion (Animal):
    
    print("I can roar")
    
R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
R.move()