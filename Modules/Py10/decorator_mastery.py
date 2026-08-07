from functools import wraps
from collections.abc import Callable
from time import perf_counter, sleep
from functools_artifacts import memoized_fibonacci
from random import randint
from inspect import signature


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__)
        start = perf_counter()
        result = func(*args, **kwargs)
        sleep(2.46)
        print(f'func time: {(perf_counter() - start): .3f}')
        return result
    return wrapper

def power_validator(min_power: int) -> Callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            bound = signature(func).bind(*args, **kwargs)
            try:
                power = bound.arguments['power']
            except ValueError:
                power = args[0]
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator

def retry_spell(max_attempts: int) -> Callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except ValueError:
                    print(f"Spell failed, retrying... ({attempt + 1}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator

@retry_spell(5)
def unstable_operation(number: int) -> int:
    if number < 10:
        raise ValueError("Number too small")

    return 0

class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and name.replace(' ', '').isalpha()

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with <{power}> power"

def main() -> None:
    print('SPELL TIMER')
    fibo = spell_timer(memoized_fibonacci)
    print(fibo(10))

    print('\nPOWER VALIDATOR')
    decorator = power_validator(6)
    fibo = decorator(memoized_fibonacci)
    print(fibo(10))
    print(fibo(5))

    print('\nRETRY SPELL')
    print(unstable_operation(randint(8, 12)))

    print('\nMAGE GUILD')
    name = 'leon321'
    print(f'name: {name} validation is: {MageGuild.validate_mage_name(name)}')
    name = 'leon'
    print(f'name: {name} validation is: {MageGuild.validate_mage_name(name)}')
    obj = MageGuild()
    power = 8
    print(f'Try casting a {power} power spell')
    print(obj.cast_spell('fire ball', power))
    power = 12
    print(f'Try casting a {power} power spell')
    print(obj.cast_spell('fire ball', power))

if __name__ == '__main__':
    main()