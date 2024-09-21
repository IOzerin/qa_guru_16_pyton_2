import pytest


@pytest.fixture
def login_page(browser_for_fixtures):
    print("Логин пэйдж!")
    pass


@pytest.fixture
def user():
    print("Юзер!")
    return "username", "password"


def test_login(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"


def test_logout(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"
