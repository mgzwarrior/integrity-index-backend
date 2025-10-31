# Copilot Instructions

This project is a Python backend service for the Integrity Index, built with FastAPI and using PostgreSQL for data storage.

## Technology Stack
- **Framework**: FastAPI
- **Database**: PostgreSQL (using SQLAlchemy ORM and asyncpg)
- **Python Version**: 3.9+
- **Package Management**: pip with requirements.txt

## Coding Standards

### Python Style
- Follow PEP 8 style guidelines
- Use snake_case for variables, functions, and module names
- Use PascalCase for class names
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 88 characters (Black formatter standard)

### Type Hints
- Use type hints for all function signatures
- Use Python 3.x type annotations (e.g., `list[str]` instead of `List[str]` when Python 3.9+)
- Import types from `typing` module when necessary

### Imports
- Group imports in the following order:
  1. Standard library imports
  2. Related third-party imports
  3. Local application imports
- Use absolute imports for clarity
- Sort imports alphabetically within each group

## FastAPI Best Practices

### API Endpoints
- Use appropriate HTTP methods (GET, POST, PUT, PATCH, DELETE)
- Follow RESTful conventions for endpoint naming
- Use plural nouns for resource collections (e.g., `/users`, `/items`)
- Use path parameters for resource IDs (e.g., `/users/{user_id}`)
- Use query parameters for filtering and pagination

### Request/Response Models
- Define Pydantic models in `schemas.py` for request and response validation
- Use descriptive model names (e.g., `UserCreate`, `UserResponse`, `UserUpdate`)
- Add examples and descriptions to schema fields for API documentation

### Error Handling
- Use FastAPI's HTTPException for error responses
- Return appropriate HTTP status codes
- Provide clear error messages in responses

## Database Standards

### SQLAlchemy Models
- Define database models in `models.py`
- Use declarative base classes
- Define relationships explicitly
- Add appropriate indexes for frequently queried fields

### Database Operations
- Use async database operations with asyncpg
- Handle database sessions properly using dependency injection
- Use transactions for operations that modify multiple tables
- Avoid N+1 query problems

### Migrations
- Use Alembic for database migrations when needed
- Always create migration scripts for schema changes
- Test migrations in both upgrade and downgrade directions

## Security Guidelines

### Authentication & Authorization
- Never hard-code credentials or API keys
- Use environment variables for sensitive configuration
- Implement proper authentication middleware when needed
- Validate and sanitize all user inputs

### Data Validation
- Use Pydantic models for request validation
- Validate data types, ranges, and formats
- Escape SQL queries (SQLAlchemy ORM handles this automatically)
- Implement rate limiting for public endpoints when necessary

### Dependencies
- Keep dependencies up to date
- Review security advisories for packages
- Pin dependency versions in requirements.txt

## Testing

### Test Structure
- Write unit tests for all new features
- Use pytest as the testing framework
- Place tests in a `tests/` directory mirroring the `app/` structure
- Name test files with `test_` prefix (e.g., `test_main.py`)

### Test Coverage
- Aim for at least 80% code coverage
- Test happy paths and edge cases
- Test error handling and validation

### Test Best Practices
- Use fixtures for common test setup
- Mock external dependencies
- Use descriptive test function names
- Test one thing per test function

## Environment Configuration

### Environment Variables
- Use python-dotenv for loading environment variables
- Create a `.env.example` file showing required variables (without values)
- Never commit `.env` files to version control
- Document all required environment variables

### Configuration Structure
```python
# Example configuration pattern (Pydantic v2)
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    
    database_url: str
    secret_key: str
```

## Documentation

### Code Comments
- Write docstrings for all public functions and classes
- Use Google-style or NumPy-style docstrings
- Comment complex logic or non-obvious implementations
- Keep comments up to date with code changes

### API Documentation
- FastAPI automatically generates OpenAPI documentation
- Add descriptions to endpoints using docstrings
- Document request/response models thoroughly
- Include examples in Pydantic models

## Logging

### Logging Standards
- Use Python's built-in `logging` module
- Configure logging in the application startup
- Use appropriate log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Include context in log messages (e.g., user_id, request_id)

### Log Messages
```python
import logging

logger = logging.getLogger(__name__)

# Good logging examples
logger.info(f"User {user_id} created successfully")
logger.error(f"Failed to connect to database: {error}")
```

## Performance

### Optimization Guidelines
- Use async/await for I/O-bound operations
- Implement pagination for list endpoints
- Use database indexes appropriately
- Cache frequently accessed data when appropriate
- Monitor query performance and optimize slow queries

## Git Workflow

### Commit Messages
- Use clear, descriptive commit messages
- Start with a verb in imperative mood (e.g., "Add", "Fix", "Update")
- Keep the first line under 50 characters
- Add detailed description if necessary

### Branch Naming
- Use descriptive branch names
- Follow pattern: `feature/description`, `fix/description`, `refactor/description`

## Project-Specific Notes

### Integrity Index Context
- This backend service sources all data relevant to the Integrity Index
- Focus on data integrity and accuracy
- Implement robust error handling for external data sources
- Ensure data validation at all entry points
