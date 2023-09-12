import pytest
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse, resolve


@pytest.mark.django_db
def test_oc_lettings_site_index_OK():
    client = Client()
    path = reverse("index")
    response = client.get(path)

    assert path == "/"
    assert response.status_code == 200
    assert resolve(path).view_name == "index"
    assertTemplateUsed(response, "index.html")
