from ex0.Factory import CreatureFactory
from .Capability import Sproutling
from .Capability import Bloomelle
from .Capability import Shiftling
from .Capability import Morphagon

class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return Sproutling()
    
    def create_evolved(self) -> Bloomelle:
        return Bloomelle()
    
class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling()
    
    def create_evolved(self) -> Morphagon:
        return Morphagon()