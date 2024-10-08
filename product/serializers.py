from django_stubs_ext.db.models import TypedModelMeta
from rest_framework.serializers import ModelSerializer

from .models import Brand, Category, Product


class CategorySerializer(ModelSerializer[Category]):
    class Meta(TypedModelMeta):
        model = Category
        fields = ("name",)


class BrandSerializer(ModelSerializer[Brand]):
    class Meta(TypedModelMeta):
        model = Brand
        fields = "__all__"


class ProductSerializer(ModelSerializer[Product]):
    brand = BrandSerializer()
    category = CategorySerializer()

    class Meta(TypedModelMeta):
        model = Product
        fields = "__all__"
