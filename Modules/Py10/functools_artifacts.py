from functools import reduce, partial, lru_cache, singledispatch
from collections.abc import Callable
import operator
from typing import Any

def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatcher(value: Any) -> str:
        return 'Unknown spell'

    @dispatcher.register(int)
    def _(value):
        return f'Deals {value} damage'
    @dispatcher.register(str)
    def _(value):
        return f'Enchants a {value} item'
    @dispatcher.register(list)
    def _(value):
        return f'Casts: {value}'
    return dispatcher

@lru_cache(maxsize=None)
def memoized_fibonacci(power: int) -> int:
    if power < 2:
        return power
    return memoized_fibonacci(power - 1) + memoized_fibonacci(power - 2)

def enchantment(power: int, element: str, target: str) -> str:
    return f'Enchant {target} with {power} power {element}'

def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    enchantments = {
        'fire': partial(base_enchantment, power=50, element='fire'),
        'dark': partial(base_enchantment, element='dark', power=50),
        'light': partial(base_enchantment, element='light', power=50) 
    }
    return enchantments

op = {
    'add': operator.add,
    'multiply': operator.mul,
    'max': max,
    'min': min
}

def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    
    opr = op.get(operation, None)
    if not opr:
        raise ValueError('Operation unknown: add, multiply, max and min')

    return reduce(opr, spells)


def main() -> None:
    print('SPELL REDUCER')
    spells = [1, 2, 3, 4, 5]
    print(f'add: {spell_reducer(spells, 'add')}')
    print(f'multiply: {spell_reducer(spells, 'multiply')}')
    print(f'max: {spell_reducer(spells, 'max')}')
    print(f'min: {spell_reducer(spells, 'min')}')
    try:
        print(f'unknown: {spell_reducer(spells, 'unknown')}')
    except ValueError as error:
        print(error)

    print('\nPARTIAL ENCHANTER')
    enchantments = partial_enchanter(enchantment)
    print(enchantments.get('fire')(target='minion'))
    print(enchantments.get('dark')(target='minion'))
    print(enchantments.get('light')(target='minion'))

    print('\nMEMOIZED FIBONACCI')
    memoized_fibonacci(10)
    print(memoized_fibonacci.cache_info())
    
    print('\nSPELL DISPACHER')
    disp = spell_dispatcher()
    print(disp(10))
    print(disp('Sword'))
    print(disp(['fire ball', 'poison cloud', 'water jat']))


if __name__ == '__main__':
    main()
