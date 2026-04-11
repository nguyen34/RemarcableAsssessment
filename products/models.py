from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name