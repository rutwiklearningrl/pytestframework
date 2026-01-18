import pytest

@pytest.mark.parametrize("username, password", [
    ("admin", "admin123"),
    ("user", "user123"),
    ("admin123", "xyz"),
    ("user123", "pqr")
])

def test_login(username, password):
    print(username, password)



@pytest.mark.parametrize("fname, lname,company", [
    ("rahul", "gandhi","Congress"),
    ("Narendra", "Modi","BJP")

])

def test_user(fname, lname,company):
    print(fname, lname,company)

