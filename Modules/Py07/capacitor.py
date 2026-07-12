import ex1 as t

healFac = t.HealingCreatureFactory()

heal1 = healFac.create_base()
heal2 = healFac.create_evolved()

print('Teating healing creatures')
print(heal1.describe())
print(heal2.describe())
print(heal1.attack())
print(heal2.attack())
print(heal1.heal('other'))
print(heal2.heal('other'))

transFac = t.TransformCreatureFactory()

trans1 = transFac.create_base()
trans2 = transFac.create_evolved()

print('\nTeating transforming creatures')
print(trans1.describe())
print(trans2.describe())
print(trans1.attack())
print(trans2.attack())
print(trans1.transform())
print(trans2.transform())
print(trans1.attack())
print(trans2.attack())
print(trans1.revert())
print(trans2.revert())
