# CI/CD Demo with AWS CodePipeline

Simple demonstration of CI/CD pipeline using pytest and AWS CodePipeline.

## Project Structure

```
├── src/
│   └── network_utils.py    # Simple network utility functions
├── tests/
│   └── test_network.py     # Basic tests
├── conftest.py            # Pytest configuration
├── pytest.ini            # Pytest settings
├── requirements.txt       # Just pytest
├── pipeline.yaml         # AWS CI/CD pipeline
└── README.md             # This file
```

## What This Demonstrates

- **Automated testing** on every GitHub commit
- **AWS CodePipeline** integration with GitHub
- **CodeBuild** running pytest automatically
- **Basic Python testing** with pytest

## Functions Tested

Simple network utilities:
- IP address validation
- Bandwidth calculation (for future iperf integration)
- Test result formatting

## Running Tests Locally

```bash
pip install -r requirements.txt
pytest
```

## CI/CD Pipeline

The pipeline automatically:
1. **Triggers** on GitHub push to main branch
2. **Pulls** code from GitHub
3. **Installs** pytest
4. **Runs** all tests
5. **Reports** results in AWS CodeBuild

## Key Files

- `pipeline.yaml` - CloudFormation template for CI/CD
- `tests/test_network.py` - Simple test cases
- `src/network_utils.py` - Functions being tested

Perfect for demonstrating CI/CD concepts without complexity!