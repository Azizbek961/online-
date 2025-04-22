# from django.test import TestCase
# from django.urls import reverse
# from category.models import Category
#
# class CategoryViewTest(TestCase):
#     def setUp(self):
#         self.category = Category.objects.create(
#             name="Elektronika", slug="elektronika", is_main=True
#         )
#
#     def test_category_list_view_status_code(self):
#         response = self.client.get(reverse('main'))
#         self.assertEqual(response.status_code, 200)
#
#
#     def test_category_list_view_context(self):
#         response = self.client.get(reverse('main'))
#         self.assertIn(self.category, response.context['categories'])
#
#
