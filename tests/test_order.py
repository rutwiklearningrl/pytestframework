import pytest

@pytest.mark.order(2)
def test_login():
    print("Login")

@pytest.mark.order(1)
def test_add_to_cart():
    print("Add item")

@pytest.mark.order(3)
def test_logout():
    print("Logout")
