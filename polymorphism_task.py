class Bird:
    def sound(self):
        print("bird make a sound")
        
class Parrot(Bird):
    def sound(self):
        print("bird make a hello")

class Sapprow(Bird):
    def sound(self):
        print("sapprow chirps")

def make_sound(bird):
    bird.sound()

parrot = Parrot()
sapprow =  Sapprow()

make_sound(parrot)
make_sound(sapprow)


