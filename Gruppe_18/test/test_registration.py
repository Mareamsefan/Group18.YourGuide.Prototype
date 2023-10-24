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
        2,
    )


@pytest.fixture
def account():
    return Account(
        "username",
        "password",
        12345678,
        "user_@gmail.com"
    )


def test_if_account_can_register_to_tour_that_is_not_fully_booked(account, tour):
    account.register_to_tour(tour)
    assert account.registered_tours == [tour]


def test_if_account_can_not_register_to_fully_booked_tour(account, tour):
    tour.max_travelers = 1
    account.register_to_tour(tour)
    another_account = Account("username", "password", 2435, "user_@gmail.com")
    assert another_account.register_to_tour(tour) == "you can't register to this tour"
    assert another_account.registered_tours == []


def test_if_account_can_not_register_to_same_tour_twice(account, tour):
    account.register_to_tour(tour)
    assert account.register_to_tour(tour) == "you can't register to this tour"
    assert account.registered_tours == [tour]


def test_if_number_of_booked_changes_after_registration(account, tour):
    account.register_to_tour(tour)
    assert tour.booked == 1
