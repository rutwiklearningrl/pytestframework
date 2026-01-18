import pytest

@pytest.mark.dependency()
def test_create_user():
    assert 2==3

@pytest.mark.dependency(depends=["test_create_user"])
def test_delete_user():
    print("test_delete_user")
