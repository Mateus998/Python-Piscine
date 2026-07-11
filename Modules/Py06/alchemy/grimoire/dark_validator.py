from .dark_spellbook import dark_spell_allowed_ingredients as dv

def validate_ingredients(ingredients: str) -> str:
    spells = dv()
    for s in spells:
        if s in ingredients:
            return ingredients + ' - VALID'
    return ingredients + ' - INVALID'