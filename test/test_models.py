from django.test import TestCase
from shop.models import Category, Product

class TestCategoriesModel(TestCase):
    
    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        # Testing Category model data insertion/types/field attributes
        
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry(self):
        data = self.data1
        self.assertEqual(str(data), 'django')

class TestProductModel(TestCase):
    pass
