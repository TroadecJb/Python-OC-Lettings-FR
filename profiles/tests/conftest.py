import pytest
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.fixture(scope="function")
def mock_user():
    user = User.objects.create(
        username="testuser",
        first_name="firstname",
        last_name="lastname",
        email="test@mail.test",
    )
    return user


@pytest.fixture(scope="function")
def mock_profile(mock_user):
    profile = Profile.objects.create(
        user=mock_user,
        favorite_city="fav city",
    )
    return profile
