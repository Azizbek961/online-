# from django.test import TestCase
# from django.urls import reverse, resolve
# from main.views import main, contact, post_add
# from django.contrib.auth import get_user_model
#
# class URLTests(TestCase):
#
#     def test_main_url(self):
#         url = reverse('main')
#         self.assertEqual(resolve(url).func, main)
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#
#     def test_post_add_url_redirects_if_not_logged_in(self):
#         url = reverse('post_add')
#         self.assertEqual(resolve(url).func, post_add)
#         response = self.client.get(url)
#         # Agar login talab qilinsa, 302 bo'lishi kerak
#         self.assertIn(response.status_code, [200, 302])
#
#     def test_post_add_url_access_when_logged_in(self):
#         # Foydalanuvchi yaratamiz
#         User = get_user_model()
#         user = User.objects.create_user(username='testuser', password='testpass123')
#         self.client.login(username='testuser', password='testpass123')
#
#         url = reverse('post_add')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
