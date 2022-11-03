from django.test import TestCase
from ..models import Category, Women
from django.contrib.auth.models import User


class CategogyTestCase(TestCase):
	def test_create(self):
		category = Category.objects.create(title='category')
		expected_category_data = (category.id, 'category')
		self.assertEqual(expected_category_data, (category.id, category.title))

	def test_delete(self):
		category = Category.objects.create(title='category')
		category.delete()
		received_category = Category.objects.filter(title='category')
		self.assertEqual(0, len(received_category))

	def test_delete_double(self):
		category = Category.objects.create(title='category')
		category.delete()
		try:
			category.delete()
		except ValueError:
			return True
			
	def test_not_fund(self):
		received_category = Category.objects.filter(title='no_name')
		self.assertEqual(0, len(received_category))

	def test_read_list(self):
		category_1 = Category.objects.create(title='category_1')
		category_2 = Category.objects.create(title='category_2')
		received_categories = Category.objects.all()
		received_categories_data = []
		for category in received_categories:
			received_categories_data.append((category.id, category.title)) 
		expected_category_data = [(category_1.id, 'category_1'),(category_2.id, 'category_2')]
		self.assertEqual(expected_category_data, received_categories_data)

	def test_read_detail(self):
		category = Category.objects.create(title='category')
		category = Category.objects.get(title='category')
		received_category = (category.id, category.title)
		expected_category_data = (category.id ,'category')
		self.assertEqual(expected_category_data, received_category)

	def test_update(self):
		category = Category.objects.create(title='category')
		category.id = 1000
		category.title = 'updated_category'
		category.save()
		expected_category_data = (1000, 'updated_category')
		self.assertEqual(expected_category_data, (category.id, category.title))


class WomenTestCase(TestCase):
	def test_create(self):
		user = User.objects.create_user(username='test_user', password='1q2w3e4r5tQ')
		women = Women.objects.create(title='women',user_id=user.id)
		expected_women_data = (women.id, 'women', None, user.id)
		received_women_data = (women.id, women.title, women.cat, women.user_id)
		self.assertEqual(expected_women_data, received_women_data)

	def test_delete(self):
		user = User.objects.create_user(username='test_user', password='1q2w3e4r5tQ')
		women = Women.objects.create(title='women', user_id=user.id)
		women.delete()
		received_women = Women.objects.filter(title='women')
		self.assertEqual(0, len(received_women))

	def test_delete_double(self):
		user = User.objects.create_user(username='test_user', password='1q2w3e4r5tQ')
		women = Women.objects.create(title='women', user_id=user.id)
		women.delete()
		try:
			women.delete()
		except ValueError:
			return True

	def test_not_fund(self):
		received_women = Women.objects.filter(title='no_name')
		self.assertEqual(0, len(received_women))

	def test_read_list(self):
		user = User.objects.create_user(username='test_user', password='1q2w3e4r5tQ')
		women_1 = Women.objects.create(title='women_1', user_id=user.id)
		women_2 = Women.objects.create(title='women_2', user_id=user.id)
		received_womens = Women.objects.all()
		received_womens_data = []
		for women in received_womens:
			received_womens_data.append((women.id, women.title, women.cat, women.user_id)) 
		expected_womens_data = [(women_1.id, 'women_1', None, user.id),
								(women_2.id, 'women_2', None, user.id)]
		self.assertEqual(expected_womens_data, received_womens_data)

	def test_read_detail(self):
		user = User.objects.create_user(username='test_user', password='1q2w3e4r5tQ')
		women = Women.objects.create(title='women', user_id=user.id)
		women = Women.objects.get(title='women')
		received_women_data = (women.id, women.title, women.cat, women.user_id)
		expected_women_data = (women.id, 'women', None, user.id)
		self.assertEqual(expected_women_data, received_women_data)

	def test_update(self):
		user_1 = User.objects.create_user(username='user_1', password='1q2w3e4r5tQ')
		user_2 = User.objects.create_user(username='user_2', password='1q2w3e4r5tQ')
		category = Category.objects.create(title='category')
		women = Women.objects.create(title='women', user_id=user_1.id)
		women.id = 1000
		women.title = 'updated_women'
		
		women.user_id = user_2.id
		women.cat = category
		women.save()
		expected_women_data = (1000, 'updated_women', category.id, user_2.id)
		self.assertEqual(expected_women_data, (women.id, women.title, women.cat_id, women.user_id))

'''
Доработать проверку по времени.
Сейчас часовой пояс во время создания объекта модели использует часовой пояс +00:00
xотя в настройках стоит часовой пояс +03:00. 
Учесть это при разработке проектов с несколькими часовыми поясами!!!
'''

'''
тесты для модели User не пишем, так как пользуемся дефолтной и не меняли ee! 
'''