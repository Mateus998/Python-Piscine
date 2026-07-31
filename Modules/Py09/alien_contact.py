from pydantic import BaseModel, Field, ValidationError, model_validator, field_validator
from datetime import datetime
from enum import Enum, auto

class ContactType(Enum):
    radio=auto(),
    visual=auto(),
    physical=auto(),
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
    # regra que relaciona varios campos
    @field_validator(mode='after')
    # regra que relaciona apenas um campo
                     