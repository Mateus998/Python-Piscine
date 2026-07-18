from ex0.Creature import Creature
from ex1.Capability import HealCapability
from ex1.Capability import TransformCapability
from abc import ABC, abstractmethod

class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature):
        pass

class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature):
        return True
    
    def act(self, creature: Creature):
        print(creature.attack())

class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature):
        if isinstance(creature, TransformCapability):
            return True
        return False
    
    def act(self, creature: Creature):
        if not self.is_valid(creature):
            raise Exception('Invalid creature type for aggressive strategy')
        elif isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())

class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature):
        if isinstance(creature, HealCapability):
            return True
        return False
    
    def act(self, creature: Creature):
        if not self.is_valid(creature):
            raise Exception('Invalid creature type for defensive strategy')
        elif isinstance(creature, HealCapability):
            print(creature.attack())
            print(creature.heal('self'))