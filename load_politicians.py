"""
Script to load current Congress members from the congress-legislators GitHub dataset
into the politicians table.
"""
import yaml
import requests
from datetime import datetime
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import Base, Politician

# URL to the legislators-current.yaml file from congress-legislators repository
LEGISLATORS_URL = "https://raw.githubusercontent.com/unitedstates/congress-legislators/main/legislators-current.yaml"


def fetch_legislators_data():
    """Fetch the legislators-current.yaml file from GitHub"""
    print(f"Fetching legislators data from {LEGISLATORS_URL}...")
    response = requests.get(LEGISLATORS_URL)
    response.raise_for_status()
    return yaml.safe_load(response.text)


def parse_date(date_str):
    """Parse a date string in YYYY-MM-DD format"""
    if date_str:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    return None


def load_legislators_to_db(legislators_data):
    """Load legislators data into the database"""
    db = SessionLocal()
    
    try:
        count = 0
        for legislator in legislators_data:
            # Extract basic information
            name_data = legislator.get("name", {})
            full_name = f"{name_data.get('first', '')} {name_data.get('last', '')}".strip()
            
            # Get current term (last term in the terms list)
            terms = legislator.get("terms", [])
            if not terms:
                print(f"Skipping {full_name}: no terms data")
                continue
                
            current_term = terms[-1]  # Get the most recent term
            
            # Extract term information
            office_type = current_term.get("type", "").capitalize()  # "rep" -> "Rep", "sen" -> "Sen"
            if office_type == "Rep":
                office_type = "House"
            elif office_type == "Sen":
                office_type = "Senate"
            
            state = current_term.get("state", "")
            party = current_term.get("party", "")
            term_start = parse_date(current_term.get("start"))
            term_end = parse_date(current_term.get("end"))
            
            # Extract external IDs
            ids = legislator.get("id", {})
            govtrack_id = ids.get("govtrack")
            opensecrets_id = ids.get("opensecrets")
            followthemoney_id = ids.get("fec")  # Using FEC ID as a proxy for followthemoney
            
            # Skip if missing required fields
            if not all([full_name, state, office_type, party, term_start, term_end]):
                print(f"Skipping {full_name}: missing required fields")
                continue
            
            # Convert IDs to strings if they exist
            govtrack_id = str(govtrack_id) if govtrack_id else None
            opensecrets_id = str(opensecrets_id) if opensecrets_id else None
            followthemoney_id = str(followthemoney_id) if followthemoney_id else None
            
            # Check if politician already exists (by govtrack_id or name)
            existing = None
            if govtrack_id:
                existing = db.query(Politician).filter(Politician.govtrack_id == govtrack_id).first()
            
            if existing:
                # Update existing record
                existing.name = full_name
                existing.state = state
                existing.office_type = office_type
                existing.party = party
                existing.term_start = term_start
                existing.term_end = term_end
                existing.opensecrets_id = opensecrets_id
                existing.followthemoney_id = followthemoney_id
                print(f"Updated: {full_name} ({state}-{office_type})")
            else:
                # Create new record
                politician = Politician(
                    name=full_name,
                    state=state,
                    office_type=office_type,
                    party=party,
                    term_start=term_start,
                    term_end=term_end,
                    govtrack_id=govtrack_id,
                    opensecrets_id=opensecrets_id,
                    followthemoney_id=followthemoney_id
                )
                db.add(politician)
                print(f"Added: {full_name} ({state}-{office_type})")
            
            count += 1
        
        db.commit()
        print(f"\nSuccessfully loaded {count} legislators into the database.")
        
    except Exception as e:
        db.rollback()
        print(f"Error loading legislators: {e}")
        raise
    finally:
        db.close()


def main():
    """Main function to create tables and load data"""
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    
    print("\nFetching and loading legislators data...")
    legislators_data = fetch_legislators_data()
    
    print(f"Found {len(legislators_data)} legislators in the dataset.\n")
    load_legislators_to_db(legislators_data)


if __name__ == "__main__":
    main()
