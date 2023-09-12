import pytest
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse, resolve


@pytest.mark.django_db
def test_letting_index_url_OK():
    client = Client()
    path = reverse("lettings_index")
    response = client.get(path)
    assert path == "/lettings/"
    assert response.status_code == 200
    assert resolve(path).view_name == "lettings_index"
    assertTemplateUsed(response, "lettings/index.html")


@pytest.mark.django_db
def test_letting_index_url_TYPO_ERROR():
    client = Client()
    response = client.get("letting/")
    assert response.status_code == 404
    assertTemplateUsed(response, "404.html")


@pytest.mark.django_db
def test_letting_url_OK(mock_letting):
    client = Client()
    path = reverse("letting", kwargs={"letting_id": mock_letting.id})
    response = client.get(path)
    assert path == f"/lettings/{mock_letting.id}/"
    assert response.status_code == 200
    assert resolve(path).view_name == "letting"


@pytest.mark.django_db
def test_letting_url_TYPO_ERROR(mock_letting):
    client = Client()
    response = client.get(f"letting/{mock_letting.id}/")
    assert response.status_code == 404
    assertTemplateUsed(response, "404.html")


@pytest.mark.django_db
def test_letting_url_NOT_FOUND():
    client = Client()
    path = reverse("letting", kwargs={"letting_id": 900})
    response = client.get(path)
    assert path == f"/lettings/900/"
    assert response.status_code == 404
    assert resolve(path).view_name == "letting"
