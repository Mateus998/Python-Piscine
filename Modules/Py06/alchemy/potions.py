import elements as ext

from . import elements as int

def healing_potion() -> str:
    return 'Healing potion brewed with ' + int.create_earth() + ' and ' + int.create_air()

def strength_potion() -> str:
    return 'Strength potion brewed with ' + ext.create_fire() + ' and ' + ext.create_water()