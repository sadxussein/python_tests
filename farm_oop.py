def spot(anim):
    anim.make_sound()

class animal:   
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight        
    
    isFed = False
    
    def feed(self):
        isFed = True    
        
class bird(animal):
    hasEggs = True
    def collect_eggs(self):
        hasEggs = False
        
class mammal(animal):
    isMilked = False
    def milk(self):
        isMilked = True
        
class sheep(mammal):
    isSreared = False
    def shear(self):
        isSreared = True
    def make_sound(self):
        print("baaaa")
        
class cow(mammal):
    def make_sound(self):
        print("moooo")
        
class goat(mammal):
    def make_sound(self):
        print("beeee")

class chick(bird):
    def make_sound(self):
        print("cluck")

class goose(bird):
    def make_sound(self):
        print("honk")

class duck(bird):
    def make_sound(self):
        print("quack")

animals = []
animals.append(goose("Белый", 5))
animals.append(goose("Серый", 6))
animals.append(chick("Ко-ко", 3))
animals.append(chick("Кукареку", 4))
animals.append(duck("Кряква", 8))
animals.append(cow("Манька", 120))
animals.append(goat("Рога", 50))
animals.append(goat("Копыта", 60))
animals.append(sheep("Барашек", 65))
animals.append(sheep("Кудрявый", 55))
  
# for a in animals:
    # a.feed()
    # print(a.name, "is fed. Its weight is", a.weight)    
    # if bird in a.__class__.__bases__ and a.hasEggs:
        # a.collect_eggs()
        # print("Collected eggs")
    # if mammal in a.__class__.__bases__ and not a.isMilked:
        # a.milk()
        # print("Milked")
    # if sheep in a.__class__ and not a.isSheared:
        # a.shear()
        # print("Sheared")
    
for base in animals[3].__class__.__bases__:
    print(base.__name__)
    
print(bird)
print(animals[3].__class__.__bases__)

if bird == animals[3].__class__.__bases__:
    print("pingus")
else:
    print("not pingus")