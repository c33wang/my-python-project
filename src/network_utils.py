"""
Simple network utility functions for CI/CD demo
"""

def validate_ip_address(ip):
    """Basic IP address validation"""
    if not ip:
        return False
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    try:
        return all(0 <= int(part) <= 255 for part in parts)
    except ValueError:
        return False

def calculate_bandwidth_mbps(bytes_transferred, seconds):
    """Calculate bandwidth in Mbps"""
    if seconds <= 0:
        raise ValueError("Time must be positive")
    bits = bytes_transferred * 8
    mbps = bits / (seconds * 1_000_000)
    return round(mbps, 2)

def format_test_result(bandwidth_mbps, test_duration):
    """Format network test results"""
    return f"Bandwidth: {bandwidth_mbps} Mbps (tested for {test_duration}s)"