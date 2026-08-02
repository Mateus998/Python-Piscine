from pydantic import BaseModel, Field, ValidationError, model_validator, field_validator
from datetime import datetime
from enum import Enum, auto
from typing import Self

class ContactType(Enum):
    radio=auto()
    visual=auto()
    physical=auto()
    telepathic=auto()

class AlienContact(BaseModel):
    contact_id: str=Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str=Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float=Field(ge=0.0, le=10.0)
    duration_minutes: int=Field(ge=1, le=1440)
    witness_count: int=Field(ge=1, le=100)
    message_received: str | None=Field(default=None, max_length=500)
    is_verified: bool=False

    @model_validator(mode='after')
    def physical_check(self)->Self:
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError('Physical contacts must be validated')
        return self

    @model_validator(mode='after')
    def telepathic_check(self)->Self:
        if self.contact_type == ContactType.telepathic and self.witness_count < 3:
            raise ValueError('Telepathic contact requires at least 3 witnesses')
        return self

    @model_validator(mode='after')
    def strong_check(self)->Self:
        if self.signal_strength > 7 and not self.message_received:
            raise ValueError('Strong signals should include received messages')
        return self

    @field_validator('contact_id')
    @classmethod
    def id_check(cls, value: str)->str:
        value = value.strip()
        if not value.startswith('AC'):
            raise ValueError('Contact id must strt with \'AC\'')
        return value         


def main():
    contact = AlienContact(
        contact_id='AC_Bilu',
        timestamp=datetime.now(),
        location='Varginha, Brasil',
        contact_type=ContactType.physical,
        signal_strength=8,
        duration_minutes=2,
        witness_count=1,
        message_received='Busquem conhecimento',
        is_verified=True
    )

    print(f'\nID: {contact.contact_id}')
    print(f'Timestamp: {contact.timestamp.strftime('%d/%m/%Y %H:%M')}')
    print(f'Location: {contact.location}')
    print(f'Type: {contact.contact_type}')
    print(f'Strength: {contact.signal_strength}')
    print(f'Duration: {contact.duration_minutes}')
    print(f'Witnesses: {contact.witness_count}')
    print(f'Message: {contact.message_received}')
    print(f'Verified: {'Yes' if contact.is_verified else 'No'}\n')

    try:
        contact = AlienContact(
            contact_id='_Bilu_',
            timestamp=datetime.now(),
            location='Varginha, Brasil',
            contact_type=ContactType.telepathic,
            signal_strength=8,
            duration_minutes=2,
            witness_count=1,
            message_received='Busquem conhecimento',
            is_verified=True
        )
    except ValidationError as error:
        print(f'{error.error_count()} {error.title} errors detected:')
        for item in error.errors():
            field = item['loc'][0]
            info = item['msg']
            print(f'{field}: {info}')


if __name__ == '__main__':
    main()