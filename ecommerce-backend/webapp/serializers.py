from rest_framework import serializers
from . models import Categories, Products, Subcategories


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = "__all__"


class SubcategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subcategories
        fields = "__all__"


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = "__all__"
