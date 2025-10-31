from sqlalchemy import Column, Integer, String, Date
from app.database import Base


class Politician(Base):
    __tablename__ = "politicians"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    state = Column(String, nullable=False, index=True)
    office_type = Column(String, nullable=False)  # "House" or "Senate"
    party = Column(String, nullable=False)
    term_start = Column(Date, nullable=False)
    term_end = Column(Date, nullable=False)

    # Optional external IDs
    govtrack_id = Column(String(50), nullable=True, unique=True, index=True)
    opensecrets_id = Column(String(50), nullable=True, unique=True, index=True)
    followthemoney_id = Column(String(100), nullable=True, unique=True, index=True)

    def __repr__(self):
        return f"<Politician(name='{self.name}', state='{self.state}', office_type='{self.office_type}')>"
