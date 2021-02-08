from django.test import TestCase
from categories.models import Category

class TestModels(TestCase):
    def test_fields(self):
        category = Category()
        category.code ="A0232"
        category.title = "fever"
        category.description ="Malaria"
        category.save()
        record = Category.objects.get(pk=category.id)
        self.assertEqual(record,category)

    def test_model_str(self):

            # code = Category.objects.create(code="A04")
        title = Category.objects.create(title="fever")
        self.assertEqual(str(title),"fever")


 