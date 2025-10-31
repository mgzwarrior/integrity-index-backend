# integrity-index-backend
A backend Python service to source all data relevant to the Integrity Index.

## Features

- **Politician Data Management**: SQLAlchemy models and Pydantic schemas for storing politician information
- **Congress Data Loader**: Script to automatically fetch and load current Congress members from the official congress-legislators dataset
- **FastAPI REST API**: RESTful endpoints for querying politician data with filtering capabilities

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Load current Congress members into the database:
```bash
python load_politicians.py
```

This will:
- Fetch the latest legislators-current.yaml from the [congress-legislators repository](https://github.com/unitedstates/congress-legislators)
- Create the database tables
- Load all current members of Congress (House and Senate)

## Running the API

Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

- `GET /` - Root endpoint
- `GET /politicians` - Get list of politicians with optional filters:
  - `?state=CA` - Filter by state
  - `?office_type=House` or `?office_type=Senate` - Filter by office type
  - `?party=Democrat` or `?party=Republican` - Filter by party
  - `?limit=50&skip=0` - Pagination
- `GET /politicians/{id}` - Get specific politician by ID
- `POST /politicians` - Create a new politician

## Data Model

The Politician model includes:
- **name**: Full name of the politician
- **state**: Two-letter state code
- **office_type**: "House" or "Senate"
- **party**: Political party affiliation
- **term_start**: Start date of current term
- **term_end**: End date of current term
- **govtrack_id**: GovTrack.us identifier (optional)
- **opensecrets_id**: OpenSecrets.org identifier (optional)
- **followthemoney_id**: FollowTheMoney.org identifier (optional)

## Database

By default, the application uses SQLite (stored in `integrity_index.db`). You can configure a different database by setting the `DATABASE_URL` environment variable:

```bash
export DATABASE_URL="postgresql://user:password@localhost/integrity_index"
```
