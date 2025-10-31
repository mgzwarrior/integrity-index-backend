# Contributing to Integrity Index Backend

Welcome! We're excited that you're interested in contributing to the Integrity Index Backend project. This FastAPI-based service sources and manages all data relevant to the Integrity Index.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git

### Setup Steps

1. **Fork and clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/integrity-index-backend.git
   cd integrity-index-backend
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install pre-commit hooks:**
   ```bash
   pip install pre-commit
   pre-commit install
   ```

4. **Load sample data (optional):**
   ```bash
   python load_politicians.py
   ```

5. **Run the application:**
   ```bash
   uvicorn app.main:app --reload
   ```
   
   The API will be available at `http://localhost:8000`

### Running Tests

Run the test suite using pytest:
```bash
pytest
```

## Coding Standards

We follow industry best practices for Python development. Please review our detailed coding standards in [.github/copilot-instructions.md](.github/copilot-instructions.md), which include:

### Key Guidelines

- **Python Style:** Follow PEP 8 guidelines
- **Type Hints:** Use type annotations for all function signatures
- **Imports:** Group and sort imports (standard library, third-party, local)
- **FastAPI Best Practices:** RESTful endpoints, Pydantic models for validation
- **Database:** Use SQLAlchemy ORM with async operations
- **Testing:** Write unit tests with pytest, aim for 80%+ coverage
- **Security:** Never hard-code credentials, validate all inputs

### Code Quality Tools

We use the following tools to maintain code quality:

- **Ruff:** For linting, formatting, and import sorting
- **pytest:** For running tests
- **pre-commit:** To automatically run checks before commits

All contributions are automatically checked by our CI pipeline when you submit a pull request.

## Development Workflow

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes:**
   - Write clean, well-documented code
   - Add or update tests as needed
   - Follow the coding standards outlined above

3. **Run pre-commit checks:**
   ```bash
   pre-commit run --all-files
   ```

4. **Commit your changes:**
   ```bash
   git add .
   git commit -m "Add: brief description of your changes"
   ```

5. **Push to your fork and submit a pull request:**
   ```bash
   git push origin feature/your-feature-name
   ```

## Pull Request Guidelines

- Provide a clear description of the changes
- Reference any related issues
- Ensure all tests pass
- Make sure pre-commit hooks pass
- Keep changes focused and atomic

## Need Help?

If you have questions or need assistance:

- **GitHub Discussions:** Visit our [GitHub Discussions](https://github.com/mgzwarrior/integrity-index-backend/discussions) to ask questions, share ideas, or get help from the community
- **Issues:** Check existing [issues](https://github.com/mgzwarrior/integrity-index-backend/issues) or create a new one for bugs or feature requests

## Code of Conduct

Please be respectful and constructive in all interactions. We're building a welcoming community where everyone can contribute.

## License

By contributing to this project, you agree that your contributions will be licensed under the same license as the project (see [LICENSE](LICENSE)).

Thank you for contributing to the Integrity Index Backend! 🎉
