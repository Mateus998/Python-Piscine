import ex2 as f
import ex0 as g
import ex1 as h
from ex1.Factory import CreatureFactory
from ex2.strategy import BattleStrategy
from itertools import combinations

def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    fighters = [(factory.create_base(), strategy) for factory, strategy in opponents]

    for (c_a, s_a), (c_b, s_b) in combinations(fighters, 2):
        print('# Battle #')
        print(c_a.describe())
        print(' VS ')
        print(c_b.describe())
        print('Fight!!!\n')

        try:
            s_a.act(c_a)
            s_b.act(c_b)
        except Exception as err:
            print(err)
            return
        print()

flameFac = g.FlameFactory()
aquaFac = g.AquaFactory()
transFac = h.TransformCreatureFactory()
healFac = h.HealingCreatureFactory()

agro = f.AggressiveStrategy()
deff = f.DefensiveStrategy()
norm = f.NormalStrategy()

tornament1: list[tuple[CreatureFactory, BattleStrategy]] = [(flameFac, norm), (transFac, agro), (healFac, deff)]
tornament2: list[tuple[CreatureFactory, BattleStrategy]] = [(aquaFac, norm), (transFac, agro), (healFac, agro)]

print('* Tournament 1 *')
battle(tornament1)

print('* Tournament 2 *')
battle(tornament2)