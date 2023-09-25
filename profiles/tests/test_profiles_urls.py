import pytest
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse, resolve


@pytest.mark.django_db
def test_profiles_index_url_OK():
    client = Client()
    path = reverse("profiles_index")
    response = client.get(path)
    assert path == "/profiles/"
    assert response.status_code == 200
    assert resolve(path).view_name == "profiles_index"
    assertTemplateUsed(response, "profiles/index.html")


@pytest.mark.django_db
def test_profiles_index_url_TYPO_ERROR():
    client = Client()
    response = client.get("pofiles/")

    assert response.status_code == 404
    assertTemplateUsed(response, "404.html")


@pytest.mark.django_db
def test_profile_url_OK(mock_profile):
    client = Client()
    path = reverse("profile", kwargs={"username": mock_profile.user})
    response = client.get(path)

    assert response.status_code == 200
    assert path == f"/profiles/{mock_profile.user.username}/"
    assert resolve(path).view_name == "profile"


@pytest.mark.django_db
def test_profile_url_TYPO_ERROR(mock_profile):
    client = Client()
    response = client.get(f"pofil/{mock_profile.user}")

    assert response.status_code == 404
    assertTemplateUsed(response, "404.html")


@pytest.mark.django_db
def test_profile_url_NOT_FOUND():
    client = Client()
    response = client.get("profile/doesnotexist")

    assert response.status_code == 404
    assertTemplateUsed(response, "404.html")
