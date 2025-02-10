#PARENT/SUPER/BASE CLASS
class Animal:
  def speak(self):
    print("animal is speaking")

#child/sub/derived class
class Dog(Animal) :
  def bark(self):
    print("dog is barking")


class Cat(Dog):
  def meow(self):
    print("cat is meowing")




a = Animal()

d = Dog()
d.speak()

c = Cat()
c.meow()
