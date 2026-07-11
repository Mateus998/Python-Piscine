from .dark_validator import validate_ingredients as vi

def  dark_spell_allowed_ingredients() -> list[str]:
    return ['bats', 'frogs', 'arsenic', 'eyeball']

def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validation = vi(ingredients)
    if 'VALID' in validation:
        return 'Spell recorded: ' + spell_name + \
            ' (' + validation + ')'
    return 'Spell rejected: ' + spell_name + \
            ' (' + validation + ')'

