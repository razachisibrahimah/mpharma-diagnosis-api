from django.test import TestCase
from categories.models import Category




class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Category.objects.create(code='A07841', title='Paratyphoid fever')

    def test_code_label(self):
        code = Category.objects.get(id=1)
        label = code._meta.get_field('code').verbose_name
        self.assertEqual(label, 'code')

    def test_title_label(self):
        title=Category.objects.get(id=1)
        label = title._meta.get_field('title').verbose_name
        self.assertEqual(label, 'title')
        

    def test_code_max_length(self):
        code = Category.objects.get(id=1)
        max_length = code._meta.get_field('code').max_length
        self.assertEqual(max_length, 20)

    def test_title_max_length(self):
        title = Category.objects.get(id=1)
        max_length = title._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)    

    def test_object_name_is_code_comma_title(self):
        categories = Category.objects.get(id=1)
        expected_object_name = f'{categories.code}, {categories.title}'
        self.assertEqual(expected_object_name, str(categories))

    def test_fields(self):
        category = Category()
        category.code ="A0232"
        category.title = "fever"
        category.description ="Malaria"
        category.save()
        record = Category.objects.get(pk=category.id)
        self.assertEqual(record,category)   




