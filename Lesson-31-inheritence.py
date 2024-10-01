class Laptop:
    def parts(self):
        print('keyboard, display, motherboard')

my_laptop = Laptop()
my_laptop.parts()

class Desktop(Laptop):
    def weight(self):
        print('Desktop are have weight')
    
my_desktop = Desktop()
my_desktop.parts()
my_desktop.weight()

