from django.test import TestCase
from django.test import TestCase, Client
from django.urls import reverse
from .models import Recipe, Category
# Create your tests here.
class RecipeViewsTestCase(TestCase):
    def setUp(self):
        # Перед кожним тестом створюємо тестові дані
        self.client = Client()
        self.category = Category.objects.create(name='Test Category')
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            description='Test Description',
            instructions='Test Instructions',
            ingredients='Test Ingredients',
            category=self.category
        )

    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertIn(self.recipe, response.context['recipes'])

    def test_category_detail_view(self):
        url = reverse('category_detail', args=[self.category.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_detail.html')
        self.assertEqual(self.category, response.context['category'])
        self.assertIn(self.recipe, response.context['recipes'])
