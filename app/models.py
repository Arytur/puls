from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta(object):
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(null=True, blank=True)
    products = models.ManyToManyField(Product, through='ProductInShop')

    def __str__(self):
        return self.name


class ProductInShop(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    url = models.URLField()
    added = models.DateField(auto_now_add=True)


class PriceHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.date}:\t{self.price}"
