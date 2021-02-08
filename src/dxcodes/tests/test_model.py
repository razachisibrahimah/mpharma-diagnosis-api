from django.test import TestCase
from dxcodes.models import Dxcode
from categories.models import Category


class DxcodeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = Category(code='A023021', title='Paratyphoid fever')
        category.save()

        # Set up non-modified objects used by all test methods
        Dxcode.objects.create(category= category, diagnosis_code='0', full_code='A0101',abbreviated_description='Typhoid fever, unspecified',category_title='Typhoid fever')

    def test_code_label(self):
        diagnosis_code = Dxcode.objects.get(id=1)
        label = diagnosis_code._meta.get_field('diagnosis_code').verbose_name
        self.assertEqual(label, 'diagnosis code')

    def test_full_code_label(self):
        full_code=Dxcode.objects.get(id=1)
        label = full_code._meta.get_field('full_code').verbose_name
        self.assertEqual(label, 'full code')
        

    def test_diagnosis_code_max_length(self):
        diagnosis_code = Dxcode.objects.get(id=1)
        max_length = diagnosis_code._meta.get_field('diagnosis_code').max_length
        self.assertEqual(max_length, 20)

    def test_full_code_max_length(self):
        full_code = Dxcode.objects.get(id=1)
        max_length = full_code._meta.get_field('full_code').max_length
        self.assertEqual(max_length, 20) 
   
    def test_abbreviated_description_max_length(self):
        abbreviated_description = Dxcode.objects.get(id=1)
        max_length = abbreviated_description._meta.get_field('abbreviated_description').max_length
        self.assertEqual(max_length, 150)

    def test_full_description_max_length(self):
        full_description = Dxcode.objects.get(id=1)
        max_length = full_description._meta.get_field('full_description').max_length
        self.assertEqual(max_length, 200) 

    def test_category_title_max_length(self):
        category_title = Dxcode.objects.get(id=1)
        max_length = category_title._meta.get_field('category_title').max_length
        self.assertEqual(max_length, 100) 
  


  



