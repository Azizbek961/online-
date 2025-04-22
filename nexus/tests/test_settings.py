# from django.test import TestCase
# from django.conf import settings
# from pathlib import Path
#
# class SettingsTestCase(TestCase):
#
#
#     def test_secret_key_exists(self):
#         self.assertIsInstance(settings.SECRET_KEY, str)
#         self.assertTrue(len(settings.SECRET_KEY) > 10)
#
#     def test_allowed_hosts(self):
#         self.assertIsInstance(settings.ALLOWED_HOSTS, list)
#
#     def test_installed_apps(self):
#         required_apps = ['main', 'category', 'user', 'product', 'blog']
#         for app in required_apps:
#             self.assertIn(app, settings.INSTALLED_APPS)
#
#     def test_templates_dir_exists(self):
#         expected_dir = settings.BASE_DIR / 'templates'
#         self.assertIn(expected_dir, settings.TEMPLATES[0]['DIRS'])
#         self.assertTrue(expected_dir.exists())
#
#     def test_staticfiles_dirs(self):
#         expected_static_dir = settings.BASE_DIR / 'static'
#         self.assertIn(expected_static_dir, settings.STATICFILES_DIRS)
#         self.assertTrue(expected_static_dir.exists())
#
#     def test_template_context_processors(self):
#         context_processors = settings.TEMPLATES[0]['OPTIONS']['context_processors']
#         self.assertIn('user.context_processors.use_context', context_processors)
#
#     def test_auth_password_validators(self):
#         validators = settings.AUTH_PASSWORD_VALIDATORS
#         self.assertGreaterEqual(len(validators), 4)
#         names = [v['NAME'] for v in validators]
#         self.assertIn('django.contrib.auth.password_validation.MinimumLengthValidator', names)
