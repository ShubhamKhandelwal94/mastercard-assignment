from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Subcategories(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=255)
    subcategory = models.ForeignKey(Subcategories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
