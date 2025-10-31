from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List

from app.database import get_db, engine
from app.models import Base, Politician as PoliticianModel
from app.schemas import Politician, PoliticianCreate

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Integrity Index Backend API")


@app.get("/")
def read_root():
    """Root endpoint"""
    return {"message": "Welcome to Integrity Index Backend API"}


@app.get("/politicians", response_model=List[Politician])
def get_politicians(
    skip: int = 0,
    limit: int = 100,
    state: str = None,
    office_type: str = None,
    party: str = None,
    db: Session = Depends(get_db)
):
    """Get list of politicians with optional filters"""
    query = db.query(PoliticianModel)
    
    if state:
        query = query.filter(PoliticianModel.state == state)
    if office_type:
        query = query.filter(PoliticianModel.office_type == office_type)
    if party:
        query = query.filter(PoliticianModel.party == party)
    
    politicians = query.offset(skip).limit(limit).all()
    return politicians


@app.get("/politicians/{politician_id}", response_model=Politician)
def get_politician(politician_id: int, db: Session = Depends(get_db)):
    """Get a specific politician by ID"""
    politician = db.query(PoliticianModel).filter(PoliticianModel.id == politician_id).first()
    if politician is None:
        raise HTTPException(status_code=404, detail="Politician not found")
    return politician


@app.post("/politicians", response_model=Politician)
def create_politician(politician: PoliticianCreate, db: Session = Depends(get_db)):
    """Create a new politician"""
    try:
        db_politician = PoliticianModel(**politician.model_dump())
        db.add(db_politician)
        db.commit()
        db.refresh(db_politician)
        return db_politician
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=f"Database constraint violation: {str(e.orig)}"
        )
