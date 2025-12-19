class Dog:
    def __init__(self,cachorro):
        self.cachorro = cachorro

    def bark(self):
        return f'{self.cachorro} uauauauauauauau'
    
catioro = Dog('rex')

print(catioro.bark())