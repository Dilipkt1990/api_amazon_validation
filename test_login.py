import pytest


@pytest.fixture(scope="module")
def preWork():
   print("browser set up")

def test_initialCheck(preWork):
   print("this is my first check")

def test_initialCheck(preWork):
       print("this is my second check")
