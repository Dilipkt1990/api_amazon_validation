# Copilot Instructions - Python Demo Project

## Project Overview
This is a minimal Python testing project using pytest. It contains test cases in files matching the pattern `*test.py`.

## Architecture & Key Components
- **Test Files**: Named with `*test.py` pattern (e.g., `test_main.py`)
- **Framework**: Pytest for test execution, though VS Code is configured for unittest discovery
- **Testing Convention**: Test functions prefixed with `test_` are automatically discovered and executed

## Critical Setup & Workflows

### Running Tests
```bash
pytest
# or
python -m pytest
```

### Test Discovery
- Pattern: `*test.py` files are automatically discovered
- Each test function must be prefixed with `test_` to be recognized

## Project-Specific Conventions

### Configuration Mismatch (Important)
The `.vscode/settings.json` currently has:
- `python.testing.unittestEnabled: true`
- `python.testing.pytestEnabled: false`

However, the codebase uses **pytest** (imports pytest in test files). This creates a discrepancy. When adding new tests, use pytest conventions, and consider aligning VS Code settings if necessary.

### Test File Structure
```python
import pytest

def test_feature_name():
    print("test description")
    # assertions here
```

## Known Issues & Patterns
1. **Duplicate Function Names**: Watch for functions with identical names in the same file - the last definition shadows earlier ones (see `test_second()` in `test_main.py`)
2. **Import Style**: Use `import pytest` at the top of test files
3. **Test Naming**: Function names must start with `test_` for discovery

## Integration Points
- **VS Code Integration**: Uses Python testing extension with unittest/pytest
- **Test Output**: Print statements in tests appear in the test output panel

## Agent Guidance
- Run tests frequently to validate changes: `pytest`
- When adding tests, follow the `test_*` naming convention
- Ensure no duplicate function names in test files
- Keep each test function focused and isolated
