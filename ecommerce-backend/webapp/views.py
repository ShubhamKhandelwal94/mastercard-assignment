from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . models import Categories, Products, Subcategories
from . serializers import CategoriesSerializer, ProductsSerializer, SubcategoriesSerializer


class CategoriesList(APIView):

    def get(self, request):

        categories = Categories.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = CategoriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubcategoriesList(APIView):

    def get(self, request):

        if len(request.GET) == 0:
            subcategories = Subcategories.objects.all()
        else:
            category = request.GET["category"]
            if category.isnumeric():
                subcategories = Subcategories.objects.filter(category=category)
            else:
                category = Categories.objects.filter(name=category.title())
                category_serializer = CategoriesSerializer(category, many=True)
                subcategories = Subcategories.objects.filter(category=category_serializer.data[0]["id"])

        subcategory_serializer = SubcategoriesSerializer(subcategories, many=True)
        return Response(subcategory_serializer.data)

    def post(self, request):

        serializer = SubcategoriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductsList(APIView):

    def get(self, request):

        products = Products.objects.all()
        products_serializer = ProductsSerializer(products, many=True)
        for product in products_serializer.data:
            subcategory = Subcategories.objects.filter(id=product["subcategory"])
            subcategory_serializer = SubcategoriesSerializer(subcategory, many=True)
            category = Categories.objects.filter(id=subcategory_serializer.data[0]["category"])
            category_serializer = CategoriesSerializer(category, many=True)
            product["category_name"] = category_serializer.data[0]["name"]
            product["subcategory_name"] = subcategory_serializer.data[0]["name"]
        return Response(products_serializer.data)

    def post(self, request):

        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def getProductsBySubcategory(request):

    if len(request.GET) == 0:
        products = Products.objects.all()
    else:
        subcategory = request.GET["subcategory"]
        if subcategory.isnumeric():
            products = Products.objects.filter(subcategory=subcategory)
        else:
            subcategory = Subcategories.objects.filter(name=subcategory.title())
            subcategory_serializer = SubcategoriesSerializer(subcategory, many=True)
            products = Products.objects.filter(subcategory=subcategory_serializer.data[0]["id"])
    products_serializer = ProductsSerializer(products, many=True)
    return Response(products_serializer.data)

@api_view(["GET"])
def getProductsByCategory(request):

    if len(request.GET) == 0:
        products = Products.objects.all()
    else:
        category = request.GET["category"]
        if category.isnumeric():
            subcategory = Subcategories.objects.filter(category=category)
        else:
            category = Categories.objects.all().filter(name=category.title())
            category_serializer = CategoriesSerializer(category, many=True)
            subcategory = Subcategories.objects.filter(category=category_serializer.data[0]["id"])
        subcategory_serializer = SubcategoriesSerializer(subcategory, many=True)
        subcategory_ids = [subcategory["id"] for subcategory in subcategory_serializer.data]
        products = Products.objects.filter(subcategory__in=subcategory_ids)
    products_serializer = ProductsSerializer(products, many=True)
    return Response(products_serializer.data)