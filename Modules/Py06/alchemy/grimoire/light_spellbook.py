
def  light_spell_allowed_ingredients() -> list[str]:
    return ['earth', 'air', 'fire', 'water']

def light_spell_record(spell_name: str, ingredients: str) -> str:
    from . import light_validator as lv
    validation = lv.validate_ingredients(ingredients)
    if 'VALID' in validation:
        return 'Spell recorded: ' + spell_name + \
            ' (' + validation + ')'
    return 'Spell rejected: ' + spell_name + \
            ' (' + validation + ')'

