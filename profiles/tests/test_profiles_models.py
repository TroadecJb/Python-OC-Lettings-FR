import pytest


@pytest.mark.django_db
def test_user(mock_user):
    expected_username = "testuser"
    expected_first_name = "firstname"
    expected_last_name = "lastname"
    expected_email = "test@mail.test"
    expected_str = "testuser"

    assert expected_str == str(mock_user)
    assert expected_username == mock_user.username
    assert expected_first_name == mock_user.first_name
    assert expected_last_name == mock_user.last_name
    assert expected_email == mock_user.email


@pytest.mark.django_db
def test_profile(mock_profile, mock_user):
    expecteted_user = mock_user
    expecteted_favorite_city = "fav city"
    expected_str = "testuser"

    assert expected_str == str(mock_profile)
    assert expecteted_user == mock_profile.user
    assert expecteted_favorite_city == mock_profile.favorite_city
