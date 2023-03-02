import sys
import pytest
sys.path.append('C:\\Users\\AnJain\\Desktop\\Voting System\\src')
from main import Voter

@pytest.fixture()
def setup():
    v = Voter("Anmol","98765432102")
    return v

def test_voterName(setup):
    assert setup.name == "Anmol"

def test_uidIsEmpty(setup):
    assert setup.unique_id != ""