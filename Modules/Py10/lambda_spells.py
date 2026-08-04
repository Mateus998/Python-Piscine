
artifacts: list[dict[str, str | int]] = [
    {
        "name": "Silver Ring",
        "power": 30,
        "type": "jewelry",
    },
    {
        "name": "Ancient Sword",
        "power": 85,
        "type": "weapon",
    },
    {
        "name": "Healing Stone",
        "power": 50,
        "type": "crystal",
    },
]

mages: list[dict[str, str | int]] = [
    {
        "name": "Aldric",
        "power": 72,
        "element": "fire",
    },
    {
        "name": "Lyra",
        "power": 91,
        "element": "water",
    },
    {
        "name": "Orin",
        "power": 45,
        "element": "earth",
    },
    {
        "name": "Selene",
        "power": 63,
        "element": "air",
    },
]

spells: list[str] = [
    "Fireball",
    "Healing Light",
    "Ice Shield",
    "Thunder Strike",
    "Wind Barrier",
]

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    result = sorted(artifacts, key=lambda artifact: artifact.get('power'), reverse=True)
    return result

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    result = filter(lambda mage: mage.get('power') >= min_power, mages)
    return result

def spell_transformer(spells: list[str]) -> list[str]:
    result = map(lambda spell: f'* {spell} *' , spells)
    return result

def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda mage: mage.get('power'))
    min_power = min(mages, key=lambda mage: mage.get('power'))
    avg_power = round(sum(map(lambda mage: mage.get('power') , mages))/len(mages), 2)
    return {'max_power': max_power.get('power'), 'min_power': min_power.get('power'), 'avg_power': avg_power}


def main():
    print('NOT SORTED')
    for elem in artifacts:
        print(elem.get('name'))
    print('\nSORTED')
    result = artifact_sorter(artifacts)
    for elem in result:
        print(elem.get('name'))

    print('\nNOT FILTERED')
    for elem in mages:
        print(elem.get('name'))
    print('\nFILTERED')
    result = power_filter(mages, 70)
    for elem in result:
        print(elem.get('name'))

    print('\nNOT TRANSFORMED')
    for elem in spells:
        print(elem)
    print('\nTRANSFORMED')
    result = spell_transformer(spells)
    for elem in result:
        print(elem)

    print(f'\n{mage_stats(mages)}')


if __name__ == '__main__':
    main()
        
