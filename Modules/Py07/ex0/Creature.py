from abc import ABC, abstractmethod

class Creature(ABC):
    def __init__(self) -> None:
        self.name: str = ''
        self.type: str = ''
    
    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return self.name + ' is a ' + \
            self.type + 'type Creature'

class Flameling(Creature):
    def __init__(self) -> None:
        self.name = 'Flameling'
        self.type = 'Fire'

    def attack(self):
        return 'Flameling uses Ember!'
    
class Pyrodon(Creature):
    def __init__(self) -> None:
        self.name = 'Pyrodon'
        self.type = 'Fire'

    def attack(self):
        return 'Pyrodon uses Ember!'
    
class Aquahub(Creature):
    def __init__(self) -> None:
        self.name = 'Aquahub'
        self.type = 'Water'

    def attack(self):
        return 'Aquahub uses Water Gun!'
    
class Torragon(Creature):
    def __init__(self) -> None:
        self.name = 'Torragan'
        self.type = 'Water'

    def attack(self):
        return 'Torragon uses Water Gun!'