from django.test import TestCase
from django.urls import reverse

from categories.models import Category

class CategoriesListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 30 categories for pagination tests
        number_of_categories = 30

        for category_id in range(number_of_categories):
            Category.objects.create(
                code=f'A04541 {category_id}',
                title=f'Paratyphoid fever {category_id}',
            )


def test_pagination_is_twenty(self):
    response = self.client.get(reverse('categories'))
    self.assertEqual(response.status_code, 200)
    self.assertTrue('is_paginated' in response.context)
    self.assertTrue(response.context['is_paginated'] == True)
    self.assertTrue(len(response.context['category_list']) == 20) 

    
def test_lists_all_authors(self):
    # Get second page and confirm it has (exactly) remaining 3 items
    response = self.client.get(reverse('authors')+'?page=2')
    self.assertEqual(response.status_code, 200)
    self.assertTrue('is_paginated' in response.context)
    self.assertTrue(response.context['is_paginated'] == True)
    self.assertTrue(len(response.context['category_list']) == 3)           


def test_view_url_accessible_by_name(self):
    response = self.client.get(reverse('categories'))
    self.assertEqual(response.status_code, 200)


