# from django.test import SimpleTestCase
# from django.urls import reverse, resolve
# from django.conf import settings
# from django.urls.exceptions import NoReverseMatch
#
# from main import views as main_views
#
# class TestUrls(SimpleTestCase):
#
#     def test_main_url_resolves(self):
#         resolver = resolve('/')
#         self.assertEqual(resolver.func, main_views.main)
#
#     def test_contact_url_resolves(self):
#         resolver = resolve('/contact')
#         self.assertEqual(resolver.func, main_views.contact)
#
#     def test_post_add_url_resolves(self):
#         resolver = resolve('/post_add/')
#         self.assertEqual(resolver.func, main_views.post_add)
#
#     def test_media_url_is_configured(self):
#         self.assertTrue(settings.MEDIA_URL)
#         self.assertTrue(settings.MEDIA_ROOT)
#
#     def test_admin_url(self):
#         try:
#             url = reverse('admin:index')
#         except NoReverseMatch:
#             self.fail("Admin index URL not found!")
