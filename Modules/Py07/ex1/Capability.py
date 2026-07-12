from abc import ABC, abstractmethod
from ex0.Creature import Creature

class HealCapability(ABC):

    @abstractmethod
    def heal(self, target: str) -> str:
        pass

class TransformCapability(ABC):
    def __init__(self) -> None:
        self.transformed = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass

class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        self.name = 'Sproutling'
        self.type = 'Heal'

    def heal(self, target: str):
        return 'Healing rain on ' + target

    def attack(self):
        return self.name + ' uses ' + self.heal('enemy')
    
class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        self.name = 'Bloomelle'
        self.type = 'Heal'

    def heal(self, target: str):
        return 'Healing light on ' + target

    def attack(self):
        return self.name + ' uses ' + self.heal('enemy')
    
class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        self.name = 'Shiftling'
        self.type = 'Trans'
        self.transformed = False

    def transform(self) -> str:
        if not self.transformed:
            self.transformed = True
            return self.name + ' transformed'
        return ''
    
    def revert(self) -> str:
        if self.transformed:
            self.transformed = False
            return self.name + ' revert'
        return ''

    def attack(self):
        attack: str = ''
        if self.transformed:
            attack = 'transtack'
        else:
            attack = 'revtack'
        return self.name + ' uses ' + attack
    
class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        self.name = 'Morphagon'
        self.type = 'Trans'
        self.transformed = False

    def transform(self) -> str:
        if not self.transformed:
            self.transformed = True
            return self.name + ' transformed'
        return ''
    
    def revert(self) -> str:
        if self.transformed:
            self.transformed = False
            return self.name + ' revert'
        return ''

    def attack(self):
        attack: str = ''
        if self.transformed:
            attack = 'transtack'
        else:
            attack = 'revtack'
        return self.name + ' uses ' + attack