from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date


class PoliticianBase(BaseModel):
    """Base Politician schema with common attributes"""

    name: str
    state: str
    office_type: str  # "House" or "Senate"
    party: str
    term_start: date
    term_end: date
    govtrack_id: Optional[str] = None
    opensecrets_id: Optional[str] = None
    followthemoney_id: Optional[str] = None


class PoliticianCreate(PoliticianBase):
    """Schema for creating a new Politician"""

    pass


class Politician(PoliticianBase):
    """Schema for reading a Politician from the database"""

    id: int

    model_config = ConfigDict(from_attributes=True)
