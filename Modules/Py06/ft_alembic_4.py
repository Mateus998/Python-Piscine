import alchemy

print(alchemy.create_air())
try:
    print(alchemy.create_earth())
except Exception as err:
    print(err)