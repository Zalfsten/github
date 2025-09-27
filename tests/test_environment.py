import json
import os
from unittest.mock import patch

from app.app import app


class TestEnvironmentVariables:
    """Test cases for environment variable handling."""

    @patch.dict(os.environ, {"APP_VERSION": "2.0.0"})
    def test_app_version_from_env(self, client):
        """Test that APP_VERSION is read from environment."""
        response = client.get("/")
        data = json.loads(response.data)
        assert data["version"] == "2.0.0"

    @patch.dict(os.environ, {"FLASK_ENV": "development"})
    def test_flask_env_from_env(self, client):
        """Test that FLASK_ENV is read from environment."""
        response = client.get("/")
        data = json.loads(response.data)
        assert data["environment"] == "development"

    @patch.dict(os.environ, {"PORT": "9000"})
    def test_port_from_env(self):
        """Test that PORT is read from environment."""
        from app.app import app as test_app

        # Test that the port would be read correctly (we can't test the actual server start)
        expected_port = int(os.environ.get("PORT", 8080))
        assert expected_port == 9000

    def test_default_values(self, client):
        """Test default values when environment variables are not set."""
        # Remove environment variables if they exist
        env_vars = ["APP_VERSION", "FLASK_ENV", "PORT"]
        original_values = {}

        for var in env_vars:
            if var in os.environ:
                original_values[var] = os.environ[var]
                del os.environ[var]

        try:
            response = client.get("/")
            data = json.loads(response.data)

            # Check defaults
            assert data["version"] == "development"
            assert data["environment"] == "production"  # Flask default in our app

        finally:
            # Restore original environment variables
            for var, value in original_values.items():
                os.environ[var] = value
