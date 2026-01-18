import pytest

@pytest.fixture
def login():
    print("Login done")

@pytest.mark.usefixtures("login")
def test_dashboard():
    assert True

@pytest.mark.smoke
def test_TC01():
    print("Testing TC01")

@pytest.mark.sanity
def test_TC02():
    print("Testing TC02")

@pytest.mark.smoke
@pytest.mark.sanity
def test_TC03():
    print("Testing TC03")


@pytest.mark.xyz
def test_TC04():
    print("Testing TC04")
