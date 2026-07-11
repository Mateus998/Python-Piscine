import alchemy.grimoire as g

spell = 'Fantasy'
ingredients = 'earth, wind and fire'

try:
    print(g.dark_spell_record(spell, ingredients))
except Exception as err:
    print(err)