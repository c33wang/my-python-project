"""
Simple tests for network utilities - CI/CD demo
"""
import pytest
from src.network_utils import validate_ip_address, calculate_bandwidth_mbps, format_test_result


def test_valid_ip_addresses():
    """Test that valid IP addresses are accepted"""
    assert validate_ip_address("192.168.1.1") is True
    assert validate_ip_address("10.0.0.1") is True
    assert validate_ip_address("127.0.0.1") is True

def test_invalid_ip_addresses():
    """Test that invalid IP addresses are rejected"""
    assert validate_ip_address("256.1.1.1") is False
    assert validate_ip_address("192.168.1") is False
    assert validate_ip_address("not.an.ip.address") is False
    assert validate_ip_address("") is False

def test_bandwidth_calculation():
    """Test bandwidth calculation"""
    # 1 MB in 1 second = 8 Mbps
    assert calculate_bandwidth_mbps(1_000_000, 1) == 8.0
    # 10 MB in 2 seconds = 40 Mbps
    assert calculate_bandwidth_mbps(10_000_000, 2) == 40.0

def test_bandwidth_zero_time():
    """Test bandwidth calculation with zero time raises error"""
    with pytest.raises(ValueError, match="Time must be positive"):
        calculate_bandwidth_mbps(1000, 0)

def test_format_results():
    """Test result formatting"""
    result = format_test_result(100.5, 10)
    assert result == "Bandwidth: 100.5 Mbps (tested for 10s)"

@pytest.mark.parametrize("ip,expected", [
    ("192.168.1.1", True),
    ("10.0.0.1", True),
    ("256.1.1.1", False),
    ("192.168.1", False),
])
def test_ip_validation_parametrized(ip, expected):
    """Test IP validation with multiple cases"""
    assert validate_ip_address(ip) == expected