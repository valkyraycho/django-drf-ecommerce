import pytest
from django.db import models

from .models import Brand, Category, Product


@pytest.mark.django_db
@pytest.mark.parametrize(
    ("model", "name"),
    [(Category, "test_category"), (Brand, "test_brand"), (Product, "test_product")],
)
def test_str_method(model: models.Model, name: str) -> None:
    if model == Product:
        brand = Brand.objects.create(name="product_brand")
        created_model = model.objects.create(name=name, brand=brand)
        assert created_model.brand.__str__() == "product_brand"  # type: ignore
    else:
        created_model = model.objects.create(name=name)
    assert created_model.__str__() == name
