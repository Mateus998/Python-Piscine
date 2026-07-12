import ex0 as f

print('Testing Flame Factory')
flameFac = f.FlameFactory()

flame1 = flameFac.create_base()
flame2 = flameFac.create_evolved()

print(flame1.describe())
print(flame1.attack())
print(flame2.describe())
print(flame2.attack())

print('\nTesting Aqua Factory')
aquaFac = f.AquaFactory()

aqua1 = aquaFac.create_base()
aqua2 = aquaFac.create_evolved()

print(aqua1.describe())
print(aqua1.attack())
print(aqua2.describe())
print(aqua2.attack())

print('\nTesting battle')
print(flame1.describe())
print(' vs')
print(aqua1.describe())
print(' fight!')
print(flame1.attack())
print(aqua1.attack())