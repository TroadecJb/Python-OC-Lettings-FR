import pytest


@pytest.mark.django_db
def test_letting(mock_letting, mock_address):
    expected_str = "test_letting"
    expected_address = str(mock_address)

    assert expected_str == str(mock_letting)
    assert expected_address == str(mock_letting.address)


@pytest.mark.django_db
def test_address(mock_address):
    expected_str = "3 the street"
    expected_number = 3
    expected_street = "the street"
    expected_city = "the city"
    expected_state = "the state"
    expected_zip_code = 1234
    expected_country_iso_code = "USA"

    assert expected_str == str(mock_address)
    assert expected_number == mock_address.number
    assert expected_street == mock_address.street
    assert expected_city == mock_address.city
    assert expected_state == mock_address.state
    assert expected_zip_code == mock_address.zip_code
    assert expected_country_iso_code == mock_address.country_iso_code
