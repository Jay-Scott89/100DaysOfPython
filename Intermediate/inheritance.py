# Class inheritance is the passing on of atributes and behaviours

class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    # Take an existing class and add it to a new class
    def __init__(self):
        super().__init__()

    # Use other behviours and modify them
    def breathe(self):
        super().breathe()
        print("underwater")

    def swim(self):
        print("Moving in water")

nemo = Fish()
nemo.swim()
nemo.breathe()