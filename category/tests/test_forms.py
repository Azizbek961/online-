# from django.test import TestCase
# from category.forms import RegionForm
#
# class RegionFormTest(TestCase):
#
#     def test_region_form_valid_data(self):
#         form_data = {
#             'name': 'Andijon',
#             'sorting': 1
#         }
#         form = RegionForm(data=form_data)
#         self.assertTrue(form.is_valid())
#         region = form.save()
#         self.assertEqual(region.name, 'Andijon')
#         self.assertEqual(region.sorting, 1)
#
#     def test_region_form_missing_name(self):
#         form_data = {
#             'name': '',  # Ism bo‘sh
#             'sorting': 2
#         }
#         form = RegionForm(data=form_data)
#         self.assertFalse(form.is_valid())
#         self.assertIn('name', form.errors)
#
#     def test_region_form_invalid_sorting(self):
#         form_data = {
#             'name': 'Samarqand',
#             'sorting': 'not_a_number'
#         }
#         form = RegionForm(data=form_data)
#         self.assertFalse(form.is_valid())
#         self.assertIn('sorting', form.errors)
