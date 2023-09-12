import pytest
from lettings.models import Letting, Address


@pytest.fixture(scope="function")
def mock_address():
    address = Address.objects.create(
        number=3,
        street="the street",
        city="the city",
        state="the state",
        zip_code=1234,
        country_iso_code="USA",
    )
    return address


@pytest.fixture(scope="function")
def mock_letting(mock_address):
    letting = Letting.objects.create(
        title="test_letting",
        address=mock_address,
    )

    return letting
