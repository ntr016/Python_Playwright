# tests/conftest.py
import pytest
import os
os.environ["PW_HEADLESS"] = "false"

@pytest.fixture(scope="session")
def base_url():
    return "https://the-internet.herokuapp.com"

