# from django.test import TestCase
# from main.forms import LoginForm, ProductForm
# from product.models import Product, Category  # Kategoriya mavjud deb olamiz
# from django.contrib.auth import get_user_model
#
#
# class LoginFormTest(TestCase):
#     def test_login_form_valid_data(self):
#         form = LoginForm(data={'login': 'testuser', 'password': 'testpass123'})
#         self.assertTrue(form.is_valid())
#
#     def test_login_form_missing_data(self):
#         form = LoginForm(data={})
#         self.assertFalse(form.is_valid())
#         self.assertIn('login', form.errors)
#         self.assertIn('password', form.errors)
#
#
# class ProductFormTest(TestCase):
#     def setUp(self):
#         self.category = Category.objects.create(name='Test Category')
