from . import Creature as c
from abc import ABC, abstractmethod

class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> c.Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> c.Creature:
        pass

class FlameFactory(CreatureFactory):
    def create_base(self) -> c.Creature:
        return c.Flameling()
    
    def create_evolved(self) -> c.Creature:
        return c.Pyrodon()
    
class AquaFactory(CreatureFactory):
    def create_base(self) -> c.Creature:
        return c.Aquahub()
    
    def create_evolved(self) -> c.Creature:
        return c.Torragon()
