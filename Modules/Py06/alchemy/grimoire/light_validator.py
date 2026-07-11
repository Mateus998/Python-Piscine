
def validate_ingredients(ingredients: str) -> str:
    from . import light_spellbook as ls
    spells = ls.light_spell_allowed_ingredients()
    for s in spells:
        if s in ingredients:
            return ingredients + ' - VALID'
    return ingredients + ' - INVALID'