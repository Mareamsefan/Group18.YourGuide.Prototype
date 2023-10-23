import pytest
from Gruppe_18.src.main.modell.Account import Account
from Gruppe_18.src.main.modell.Tour import Tour

@pytest.fixture
def tour():
    return Tour(
        "A tour through italy",
        "Italy",
        4,
        255,
        "https://www.hdwallpaper.nu/wp-content/uploads/2015/05/colosseum-1436103.jpg",
        "English",
        20,
    )

@pytest.fixture
def account():
    return Account(
        "username",
        "password",
        12345678,
        "user_@gmail.com"
    )

def test_if_account_can_Register_to_tour(account, tour):
    account.register_to_tour(tour)
    assert account.registered_tours == [tour]