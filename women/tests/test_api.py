from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse_lazy
from ..models import Women
from django.contrib.auth.models import User
from ..serializers import WomenSerializer


class WomenAPITestCase(APITestCase):
	def test_get_list(self):
		user = User.objects.create_user(
			username='test_user', password='1q2w3e4r5tQ')
		women_1 = Women.objects.create(title='women_1', user_id=1)
		women_2 = Women.objects.create(title='women_2', user_id=1)
		url = reverse_lazy('women_list')
		response = self.client.get(url)
		self.assertEqual(status.HTTP_200_OK, response.status_code)
		serializer_data = WomenSerializer([women_1, women_2], many=True).data
		self.assertEqual(serializer_data, response.data)

class WomenTestCase(TestCase):
	def test_create(self):
		user = User.objects.create_user(
			username='test_user', password='1q2w3e4r5tQ')
		women = Women.objects.create(title='women',user_id=user.id)
		expected_women_data = (1, 'women', None, user.id)
		self.assertEqual(expected_women_data, (women.id, women.title, women.cat, women.user_id))
