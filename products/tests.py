from django.test import TestCase
from products.models import Product, Category, Tag

# Simple Test Cases to encapsulate product filtering behaviour
class SandwichProductTestCase(TestCase):

    def setUp(self):
        Category.objects.create(name="Food")
        Tag.objects.create(name="Dairy")
        Tag.objects.create(name="Meat")
        Tag.objects.create(name="Vegetables")
        tags = Tag.objects.filter(name__in=["Dairy", "Meat", "Vegetables"])
        category = Category.objects.get(name="Food")
        sandwich = Product.objects.create(name="Sandwich", category=category)
        sandwich.tags.set(tags)
        sandwich.save()
    
    def test_searching_sandwich(self):
        query = Product.objects.filter(name__icontains="sand").first()
        self.assertEqual(query.name, "Sandwich")

    def test_filtering_sandwich(self):
        meat_tag = Tag.objects.get(name="Meat")
        query = Product.objects.filter(tags=meat_tag)
        self.assertEqual(query.count(), 1)
        food_category = Category.objects.get(name="Food")
        query = Product.objects.filter(category=food_category)
        self.assertEqual(query.count(), 1)
