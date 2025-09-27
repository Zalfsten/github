# Tests

This directory contains all test files for the dummy Python application.

## Test Types

### Unit Tests (pytest)
- `test_app.py` - Flask application unit tests
- `test_environment.py` - Environment variable tests
- `conftest.py` - pytest fixtures and configuration

**Run with:**
```bash
uv run pytest
uv run pytest -v                    # verbose
uv run pytest --cov=app            # with coverage
```

### Container Structure Tests
- `container-structure-test.yaml` - Docker image validation tests

**Run with:**
```bash
# First build the image
docker build -t dummy-python-app .

# Download container-structure-test binary (if not already available)
curl -LO https://storage.googleapis.com/container-structure-test/latest/container-structure-test-linux-amd64
chmod +x container-structure-test-linux-amd64

# Run container structure tests
./container-structure-test-linux-amd64 test --image dummy-python-app --config tests/container-structure-test.yaml
```

## Test Coverage

- **Unit Tests**: Flask endpoints, environment handling, error cases
- **Container Tests**: File structure, permissions, security, functionality
- **Integration**: App imports, Python version, package installation

All tests validate both development and production environments.
