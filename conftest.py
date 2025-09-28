"""
pytest configuration for CI/CD demo
"""
import pytest


@pytest.fixture
def sample_test_data():
    """Simple test data fixture"""
    return {
        "valid_ips": ["192.168.1.1", "10.0.0.1", "127.0.0.1"],
        "invalid_ips": ["256.1.1.1", "192.168.1", "not.an.ip"],
        "bandwidth_tests": [
            {"bytes": 1_000_000, "seconds": 1, "expected_mbps": 8.0},
            {"bytes": 5_000_000, "seconds": 2, "expected_mbps": 20.0}
        ]
    }


@pytest.fixture
def sample_numbers():
    """Fixture that provides sample number lists for testing"""
    return {
        'positive': [1, 2, 3, 4, 5],
        'negative': [-5, -3, -1],
        'mixed': [-2, 0, 3, -1, 4],
        'single': [42],
        'empty': []
    }


@pytest.fixture(scope="session")
def test_data():
    """Session-scoped fixture for test data that's expensive to create"""
    return {
        'large_numbers': list(range(1000, 2000)),
        'test_strings': ['hello', 'world', 'pytest', 'testing'],
        'edge_cases': [0, -1, 1, float('inf'), -float('inf')]
    }


# Pytest configuration
def pytest_configure(config):
    """Configure pytest with custom markers"""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests"
    )
    config.addinivalue_line(
        "markers", "unit: marks tests as unit tests"
    )


# Custom pytest hooks
def pytest_collection_modifyitems(config, items):
    """Automatically mark tests based on their names"""
    for item in items:
        # Mark slow tests
        if "slow" in item.nodeid:
            item.add_marker(pytest.mark.slow)
        
        # Mark integration tests
        if "integration" in item.nodeid or "test_calculator" in item.nodeid:
            item.add_marker(pytest.mark.integration)
        else:
            item.add_marker(pytest.mark.unit)