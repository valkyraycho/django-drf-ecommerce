import pytest
from factory.django import DjangoModelFactory
from rest_framework.test import APIClient

from .factories import BrandFactory, CategoryFactory, ProductFactory


@pytest.mark.django_db
@pytest.mark.parametrize(
    ("endpoint", "factory"),
    [
        ("category", CategoryFactory),
        ("brand", BrandFactory),
        ("product", ProductFactory),
    ],
)
def test_endpoints(
    endpoint: str, factory: type[DjangoModelFactory], api_client: APIClient
) -> None:
    factory.create_batch(3)
    api_endpoint = f"/api/{endpoint}/"

    response = api_client.get(path=api_endpoint)
    assert response.status_code == 200
    assert len(response.json()) == 3
