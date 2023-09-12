import pytest
from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_lettings_index_content_OK(mock_letting):
    client = Client()
    path = reverse("lettings_index")
    response = client.get(path)
    content = response.content.decode()

    expected_title = mock_letting.title

    assert expected_title in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")


@pytest.mark.django_db
def test_lettings_index_404():
    client = Client()
    response = client.get("letin/")
    content = response.content.decode()

    expected_message = "Page not found"

    assert expected_message in content
    assert response.status_code == 404
    assertTemplateUsed(response, "404.html")


@pytest.mark.django_db
def test_letting_content_OK(mock_letting, mock_address):
    client = Client()
    path = reverse("letting", kwargs={"letting_id": 1})
    response = client.get(path)
    content = response.content.decode()
    expected_title = mock_letting.title
    expected_address = f"{mock_address.number} {mock_address.street}"
    expected_address_comp = (
        f"{mock_address.city}, {mock_address.state} {mock_address.zip_code}"
    )
    expected_address_iso = mock_address.country_iso_code

    assert expected_title in content
    assert expected_address in content
    assert expected_address_comp in content
    assert expected_address_iso in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")


@pytest.mark.django_db
def test_letting_404():
    client = Client()
    path = reverse("letting", kwargs={"letting_id": 900})
    response = client.get(path)
    content = response.content.decode()

    expected_message = "Letting not found"

    assert response.status_code == 404
    assert expected_message in content
    assertTemplateUsed(response, "404.html")
