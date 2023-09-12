import pytest
from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_lettings_index_content_OK():
    client = Client()
    path = reverse("index")
    response = client.get(path)
    content = response.content.decode()

    expected_title = "Welcome to Holiday Homes"

    assert expected_title in content
    assert response.status_code == 200
    assertTemplateUsed(response, "index.html")
