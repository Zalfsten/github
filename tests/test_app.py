import json

import pytest

from app.app import app


class TestApp:
    """Test cases for the main Flask application."""

    def test_hello_endpoint(self, client):
        """Test the main hello endpoint."""
        response = client.get("/")
        assert response.status_code == 200

        data = json.loads(response.data)
        assert data["message"] == "Hello World from Dummy Python App!"
        assert data["python_version"] == "3.13"
        assert data["package_manager"] == "uv"
        assert "timestamp" in data
        assert "version" in data

    def test_health_endpoint(self, client):
        """Test the health check endpoint."""
        response = client.get("/health")
        assert response.status_code == 200

        data = json.loads(response.data)
        assert data["status"] == "healthy"
        assert data["service"] == "dummy-python-app"

    def test_info_endpoint(self, client):
        """Test the info endpoint."""
        response = client.get("/info")
        assert response.status_code == 200

        data = json.loads(response.data)
        assert data["name"] == "Dummy Python Application"
        assert data["port"] == 8080
        assert data["package_manager"] == "uv"
        assert isinstance(data["endpoints"], list)
        assert "/" in data["endpoints"]
        assert "/health" in data["endpoints"]
        assert "/info" in data["endpoints"]

    def test_nonexistent_endpoint(self, client):
        """Test that nonexistent endpoints return 404."""
        response = client.get("/nonexistent")
        assert response.status_code == 404

    def test_content_type_json(self, client):
        """Test that responses are JSON."""
        endpoints = ["/", "/health", "/info"]

        for endpoint in endpoints:
            response = client.get(endpoint)
            assert "application/json" in response.content_type

    def test_app_configuration(self, app_context):
        """Test app configuration in testing mode."""
        assert app_context.config["TESTING"] is True
