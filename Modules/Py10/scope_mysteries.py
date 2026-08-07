from collections.abc import Callable, Hashable
from typing import Any

def memory_vault() -> dict[str, Callable]:
    memory: dict[Hashable, Any] = {}
    def store(key: Hashable, value: Any) -> None:
        memory[key] = value
    def recall(key: Hashable) -> Any:
        return memory.get(key, 'Memory not found')
    return {'store': store, 'recall': recall}

def enchantment_factory(enchantment_type: str) -> Callable:
    def apply_enchantment(item_name: str) -> str:
        return f'{enchantment_type} {item_name}'
    return apply_enchantment

def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power
    def increase_power(amount: int) -> int:
        nonlocal total_power
        total_power += amount
        return total_power
    return increase_power

def mage_counter() -> Callable:
    state = 0
    def state_count() -> int:
        nonlocal state
        state += 1
        return state
    return state_count


def main() -> None:
    count1 = mage_counter()
    count2 = mage_counter()

    print('COUNT 1')
    for _ in range(5):
        print(count1())

    print('\nCOUNT 2')
    for _ in range(10):
        print(count2())

    power = spell_accumulator(5)
    print('\nINCREASING POWER: 5')
    print(f'+2 {power(2)}')
    print(f'+5 {power(5)}')
    print(f'+16 {power(16)}')

    flamer = enchantment_factory('flaming')
    darker = enchantment_factory('dark')
    print('\nENCHANTMENT FACTORY')
    print(flamer('sword'))
    print(darker('armor'))

    print('\nMEMORY VAULT')
    memory = memory_vault()
    memory.get('store')('item1', 'thing')
    print(memory.get('recall')('item1'))
    print(memory.get('recall')('item2'))

if __name__ == '__main__':
    main()