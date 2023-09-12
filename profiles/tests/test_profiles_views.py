import pytest
from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_profiles_index_content_OK(mock_profile):
    client = Client()
    path = reverse("profiles_index")
    response = client.get(path)
    content = response.content.decode()

    expected_username = mock_profile.user.username

    assert expected_username in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")


@pytest.mark.django_db
def test_profiles_index_404():
    client = Client()
    response = client.get("proile/")
    content = response.content.decode()

    expected_message = "Page not found"

    assert expected_message in content
    assert response.status_code == 404
    assertTemplateUsed(response, "404.html")


@pytest.mark.django_db
def test_profile_content_OK(mock_profile):
    client = Client()
    path = reverse("profile", kwargs={"username": mock_profile.user.username})
    response = client.get(path)
    content = response.content.decode()

    expected_username = mock_profile.user.username
    expected_first_name = mock_profile.user.first_name
    expected_last_name = mock_profile.user.last_name
    expected_email = mock_profile.user.email
    expected_fav_city = mock_profile.favorite_city

    assert response.status_code == 200
    assert expected_username in content
    assert expected_first_name in content
    assert expected_last_name in content
    assert expected_email in content
    assert expected_fav_city in content
    assertTemplateUsed(response, "profiles/profile.html")


@pytest.mark.django_db
def test_profile_404():
    client = Client()
    path = reverse("profile", kwargs={"username": "doesnotexist"})
    response = client.get(path)
    content = response.content.decode()

    expected_message = "Profile does not exist"

    assert response.status_code == 404
    assert expected_message in content
    assertTemplateUsed(response, "404.html")
