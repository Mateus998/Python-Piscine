from pydantic import BaseModel, Field, ValidationError
from datetime import datetime

class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def main():
    station = SpaceStation(
        station_id='ISS_01',
        name='MathStation',
        crew_size=10,
        power_level=75.5,
        oxygen_level=90.7,
        last_maintenance=datetime(2026, 7, 30, 19, 26, 0),
        is_operational=True,
        notes='my first station'
    )

    print(f'\nID: {station.station_id}')
    print(f'Name: {station.name}')
    print(f'Crew size: {station.crew_size}')
    print(f'Power level: {station.power_level}')
    print(f'Oxygen level: {station.oxygen_level}')
    print(f'Last maintenance: {station.last_maintenance.strftime('%d/%m/%Y %H:%M')}')
    print(f'Operational: {'On' if station.is_operational else 'Off'}')
    print(f'Notes: {station.notes}\n')

    try:
        station = SpaceStation(
            station_id = 'ISS_01',
            name = None,
            crew_size = 'three',
            power_level = 75.5,
            oxygen_level = 100.01,
            last_maintenance = datetime(2026, 7, 30, 19, 26, 0),
            is_operational = True,
            notes = 'my first station'
        )
    except ValidationError as error:
        print(f'{error.error_count()} {error.title} errors detected:')
        for item in error.errors():
            field = item['loc'][0]
            info = item['msg']
            print(f'{field}: {info}')

if __name__ == '__main__':
    main()