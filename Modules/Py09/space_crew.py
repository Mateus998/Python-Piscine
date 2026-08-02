from pydantic import ValidationError, Field, model_validator, BaseModel
from typing import Self
from enum import Enum, auto
from datetime import datetime

class Rank(Enum):
    cadet=auto()
    officer=auto()
    lieutenant=auto()
    captain=auto()
    commander=auto()

class CrewModel(BaseModel):
    member_id: str=Field(min_length=3, max_length=10)
    name: str=Field(min_length=2, max_length=50)
    rank: Rank
    age: int=Field(ge=18, le=80)
    specialization: str=Field(min_length=3, max_length=30)
    years_experience: int=Field(ge=0, le=50)
    is_active: bool=True

class SpaceMission(BaseModel):
    mission_id: str=Field(min_length=5, max_length=15)
    mission_name: str=Field(min_length=3, max_length=100)
    destination: str=Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int=Field(ge=1, le=3650)
    crew: list[CrewModel]=Field(min_length=1, max_length=12)
    mission_status: str='planned'
    budget_millions: float=Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def id_validation(self)->Self:
        if not self.mission_id.startswith('M'):
            raise ValueError('Mission ID must start with \'M\'')
        return self

    @model_validator(mode='after')
    def crew_validation(self)->Self:
        has_leader: bool=False
        for member in self.crew:
            if member.rank in [Rank.captain, Rank.commander]:
                has_leader=True
            if not member.is_active:
                raise ValueError('All crew members must be active')

        if not has_leader:
            raise ValueError('Crew must have at leat one Commander or Captain')
        return self

    @model_validator(mode='after')
    def mission_validation(self)->Self:
        if self.duration_days > 365:
            experience: int=0
            for member in self.crew:
                if member.years_experience >= 5:
                    experience += 1
            if experience < len(self.crew) / 2:
                raise ValueError('Long missions need 50 percent experienced crew')
        return self


def main()->None:
    crew_member1=CrewModel(
        member_id='001',
        name='member1',
        rank=Rank.cadet,
        age=32,
        specialization='Csientist',
        years_experience=6,
        is_active=True
    )
    crew_member2=CrewModel(
        member_id='002',
        name='member2',
        rank=Rank.captain,
        age=35,
        specialization='Pilot',
        years_experience=7,
        is_active=True
    )
    crew_member3=CrewModel(
        member_id='003',
        name='member3',
        rank=Rank.lieutenant,
        age=40,
        specialization='Engeneer',
        years_experience=9,
        is_active=True
    )
    crew_member4=CrewModel(
        member_id='004',
        name='member4',
        rank=Rank.officer,
        age=25,
        specialization='Medic',
        years_experience=3,
        is_active=True
    )

    mission=SpaceMission(
        mission_id='M001234',
        mission_name='first mission to mars',
        destination='plannet mars',
        launch_date=datetime.now(),
        duration_days=800,
        crew=[crew_member1, crew_member2, crew_member3],
        mission_status='planned',
        budget_millions=15.34
    )

    print(f'\nID: {mission.mission_id}')
    print(f'Name: {mission.mission_name}')
    print(f'Destination: {mission.destination}')
    print(f'Duration: {mission.duration_days}')
    print(f'Duration: {mission.launch_date.strftime('%d/%m/%Y %H:%M')}')
    print(f'Crew: {mission.crew}')
    print(f'Budget: {mission.budget_millions}')
    print(f'Status: {mission.mission_status}\n')

    try:
        mission=SpaceMission(
            mission_id='M001234',
            mission_name='first mission to mars',
            destination='plannet mars',
            launch_date=datetime.now(),
            duration_days=1204,
            crew=[crew_member1, crew_member4, crew_member3],
            mission_status='planned',
            budget_millions=15.34
        )
    except ValidationError as error:
        print(error)
        

if __name__ == '__main__':
    main()