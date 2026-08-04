from collections.abc import Callable

def freeze(target: str, power: int) -> str:
    return f"Freeze immobilizes {target} with {power} power"


def tsunami(target: str, power: int) -> str:
    return f"Tsunami strikes {target} with {power} power"


def earthquake(target: str, power: int) -> str:
    return f"Earthquake shakes {target} with {power} power"


def shield(target: str, power: int) -> str:
    return f"Shield protects {target} with {power} power"

def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combination(target: str, power: int) -> tuple[str, str]:
        result1 = spell1(target, power)
        result2 = spell2(target, power)
        return result1, result2
    return combination

def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplification(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplification

def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cast(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return cast
    
def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence

def condition(target: str, power: int) -> bool:
    if target is 'boss' and power > 10:
        return True
    return False

def main() -> None:
    print('SPELL COMBINER:')
    combo = spell_combiner(tsunami, freeze)
    print(combo('you', 15), end='\n\n')

    print('POWER AMPLIFIER')
    dome = power_amplifier(shield, 3)
    print(dome('me', 7), end='\n\n')

    print('CONDITIONAL CASTER')
    maybe = conditional_caster(condition, earthquake)
    print(maybe('boss', 9))
    print(maybe('boss', 16), end='\n\n')

    print('SPELL SEQUENCE')
    sequence = spell_sequence([tsunami, freeze, earthquake, shield])
    print(sequence('boss', 16), end='\n\n')

if __name__ == '__main__':
    main()