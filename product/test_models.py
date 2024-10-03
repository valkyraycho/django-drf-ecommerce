import pytest
from factory.django import DjangoModelFactory

from .factories import BrandFactory, CategoryFactory, ProductFactory
from .models import Product


@pytest.mark.django_db
@pytest.mark.parametrize(
    ("factory", "name"),
    [
        (CategoryFactory, "test_category"),
        (BrandFactory, "test_brand"),
        (ProductFactory, "test_product"),
    ],
)
def test_str_method(
    factory: type[DjangoModelFactory],
    name: str,
    brand_factory: type[BrandFactory],
) -> None:
    if factory == ProductFactory:
        brand = brand_factory(name="product_brand")
        created_model: Product = factory(name=name, brand=brand)
        assert created_model.brand.__str__() == "product_brand"
        assert created_model.is_digital
    else:
        created_model = factory(name=name)

    assert created_model.__str__() == name
