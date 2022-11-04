from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse_lazy
from ..models import Women
from django.contrib.auth.models import User
from ..serializers import WomenSerializer
from rest_framework.test import APIClient


class WomenAPITestCase(APITestCase):
	def test_get_list_owner(self):
		user_1 = User.objects.create_user(username='test_user_1', password='1q2w3e4r5tQ')
		user_2 = User.objects.create_user(username='test_user_2', password='1q2w3e4r5tQ')
		url_token = reverse_lazy('token_obtain_pair')
		client = APIClient()
		response_token = client.post(url_token,
								{'password': '1q2w3e4r5tQ', 'username': 'test_user_1'},
								format='json')
		access_token = response_token.data['access']
		client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)

		women_1 = Women.objects.create(title='women_1', user_id=user_1.id)
		women_2 = Women.objects.create(title='women_2', user_id=user_1.id)
		women_3 = Women.objects.create(title='women_3', user_id=user_2.id)
		url = reverse_lazy('women_list_create')
		response_women = client.get(url, format='json')
		self.assertEqual(status.HTTP_200_OK, response_women.status_code) # проверяем успех запроса
		
		serializer_data = WomenSerializer([women_1, women_2], many=True).data
		self.assertEqual(serializer_data, response_women.data) # сравниваем данные сериализатора и View

		owner_women_data = WomenSerializer(Women.objects.filter(user_id=user_1.id), many=True).data
		# сравниваем данные (IsOwnerOrAdminFilterBackend) и данные View
		self.assertEqual(owner_women_data, response_women.data) 

	def test_get_list_admin(self):
		user_admin = User.objects.create_user(username='test_user_admin',
												password='1q2w3e4r5tQ',
												is_staff=True)
		user = User.objects.create_user(username='test_user', password='1q2w3e4r5tQ')
		url_token = reverse_lazy('token_obtain_pair')
		client = APIClient()
		response_token = client.post(url_token,
								{'password': '1q2w3e4r5tQ', 'username': 'test_user_admin'},
								format='json')
		access_token = response_token.data['access']
		client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
		
		women_1 = Women.objects.create(title='women_1', user_id=user_admin.id)
		women_2 = Women.objects.create(title='women_2', user_id=user_admin.id)
		women_3 = Women.objects.create(title='women_3', user_id=user.id)
		url = reverse_lazy('women_list_create')
		response_women = client.get(url, format='json')
		self.assertEqual(status.HTTP_200_OK, response_women.status_code) # проверяем успех запроса

		serializer_data = WomenSerializer([women_1, women_2, women_3], many=True).data
		self.assertEqual(serializer_data, response_women.data) # сравниваем данные сериализатора и View

		owner_women_data = WomenSerializer( Women.objects.all(), many=True).data
		# сравниваем данные (IsOwnerOrAdminFilterBackend) и данные View
		self.assertEqual(owner_women_data, response_women.data) 

	def test_get_list_unknown(self):
		url = reverse_lazy('women_list_create')
		response = self.client.get(url)
		self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code) # проверяем успех запроса

	def test_create_unknown(self):
		url_women = reverse_lazy('women_list_create')
		women_data =  {'title': 'women', 'content': 'content'}
		response = self.client.post(url_women, women_data, format='json')
		self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

	def test_create(self):
		client = APIClient()
		user = User.objects.create_user(username='test_user', password='1q2w3e4r5tQ', is_active=True)
		url_token = reverse_lazy('token_obtain_pair')
		url_women = reverse_lazy('women_list_create')
		women_data =  {'title': 'women', 'content': 'content'}
		serializer_data = WomenSerializer(women_data).data
		response_token = client.post(url_token,
									{'password': '1q2w3e4r5tQ', 'username': 'test_user'},
									format='json')
		access_token = response_token.data['access']
		client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
		response_women = client.post(url_women, women_data, format='json')
		self.assertEqual(status.HTTP_201_CREATED, response_women.status_code)
		response_women.data.pop('time_create')
		response_women.data.pop('time_update')
		response_women.data.pop('id')
		self.assertEqual(serializer_data, response_women.data)

	def test_get_detail_1(self): # для url women_detail_update
		user = User.objects.create_user(username='test_user', password='1q2w3e4r5tQ')
		women = Women.objects.create(title='women', user_id=user.id)
		url = reverse_lazy('women_detail_update', kwargs={'pk':women.id})
		response = self.client.get(url)
		self.assertEqual(status.HTTP_200_OK, response.status_code) # Проверяем успех запроса
		serializer_data = WomenSerializer(women).data
		self.assertEqual(serializer_data, response.data) # сравниваем данные сериалайзера и View

	def test_put_update_unknown(self):
		user = User.objects.create_user(username='test_user', password='1q2w3e4r5tQ')
		women = Women.objects.create(title='women', user_id=user.id)
		url_women = reverse_lazy('women_detail_update', kwargs={'pk': women.id})
		women_data_update =  {'title': 'update_women', 'content': 'update_content'}
		response = self.client.put(url_women, women_data_update, format='json')
		self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

	def test_put_update(self):
		user = User.objects.create_user(username='test_user', password='1q2w3e4r5tQ', is_active=True)
		url_token = reverse_lazy('token_obtain_pair')
		client = APIClient()
		response_token = client.post(url_token,
								{'password': '1q2w3e4r5tQ', 'username': 'test_user'},
								format='json')
		access_token = response_token.data['access']
		client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
		women = Women.objects.create(title='women', user_id=user.id)
		url_women = reverse_lazy('women_detail_update', kwargs={'pk': women.id})
		women_data_update =  {'title': 'update_women', 'content': 'update_content'}
		response_women = client.put(url_women, women_data_update, format='json')
		self.assertEqual((women_data_update['title'], women_data_update['content']),
							(response_women.data['title'], response_women.data['content']))

	def test_patch_update_unknown(self):
		user = User.objects.create_user(username='test_user', password='1q2w3e4r5tQ')
		women = Women.objects.create(title='women', user_id=user.id)
		url_women = reverse_lazy('women_detail_update', kwargs={'pk': women.id})
		women_data_update =  {'content': 'update_content'}
		response = self.client.patch(url_women, women_data_update, format='json')
		self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

	def test_patch_update(self):
		user = User.objects.create_user(username='test_user', password='1q2w3e4r5tQ', is_active=True)
		url_token = reverse_lazy('token_obtain_pair')
		client = APIClient()
		response_token = client.post(url_token,
								{'password': '1q2w3e4r5tQ', 'username': 'test_user'},
								format='json')
		access_token = response_token.data['access']
		client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
		women = Women.objects.create(title='women', user_id=user.id)
		url_women = reverse_lazy('women_detail_update', kwargs={'pk': women.id})
		women_data_update =  {'content': 'update_content'}
		response_women = client.patch(url_women, women_data_update, format='json')
		self.assertEqual(status.HTTP_200_OK, response_women.status_code)
		self.assertEqual((women.title, women_data_update['content']),
							(response_women.data['title'], response_women.data['content']))

	def test_get_detail_2(self): # для url women_detail_delete
		user = User.objects.create_user(username='test_user', password='1q2w3e4r5tQ')
		women = Women.objects.create(title='women', user_id=user.id)
		url = reverse_lazy('women_detail_delete', kwargs={'pk':women.id})
		response = self.client.get(url)
		self.assertEqual(status.HTTP_200_OK, response.status_code) # Проверяем успех запроса
		serializer_data = WomenSerializer(women).data
		self.assertEqual(serializer_data, response.data) # сравниваем данные сериалайзера и View

	def test_delete_unknown(self):
		user = User.objects.create_user(username='test_user', password='1q2w3e4r5tQ')
		women = Women.objects.create(title='women', user_id=user.id)
		url = reverse_lazy('women_detail_delete', kwargs={'pk':women.id})
		response = self.client.delete(url)
		self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code) # Проверяем успех запроса
		
	def test_delete_not_owner(self):
		user_1 = User.objects.create_user(username='test_user_1', password='1q2w3e4r5tQ')
		user_2 = User.objects.create_user(username='test_user_2', password='1q2w3e4r5tQ')
		url_token = reverse_lazy('token_obtain_pair')
		client = APIClient()
		response_token = client.post(url_token,
								{'password': '1q2w3e4r5tQ', 'username': 'test_user_1'},
								format='json')
		access_token = response_token.data['access']
		client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
		women = Women.objects.create(title='women', user_id=user_2.id)
		url = reverse_lazy('women_detail_delete', kwargs={'pk':women.id})
		response_women = client.delete(url)
		self.assertEqual(status.HTTP_403_FORBIDDEN, response_women.status_code) # Проверяем успех запроса

	def test_delete_owner(self):
		user = User.objects.create_user(username='test_user', password='1q2w3e4r5tQ')
		url_token = reverse_lazy('token_obtain_pair')
		client = APIClient()
		response_token = client.post(url_token,
								{'password': '1q2w3e4r5tQ', 'username': 'test_user'},
								format='json')
		access_token = response_token.data['access']
		client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
		women = Women.objects.create(title='women', user_id=user.id)
		url = reverse_lazy('women_detail_delete', kwargs={'pk':women.id})
		response_women = client.delete(url)
		self.assertEqual(status.HTTP_204_NO_CONTENT, response_women.status_code) # Проверяем успех запроса
	
	def test_delete_admin(self):
		user_1 = User.objects.create_user(username='test_user_1', password='1q2w3e4r5tQ', is_staff=True)
		user_2 = User.objects.create_user(username='test_user_2', password='1q2w3e4r5tQ')
		url_token = reverse_lazy('token_obtain_pair')
		client = APIClient()
		response_token = client.post(url_token,
								{'password': '1q2w3e4r5tQ', 'username': 'test_user_1'},
								format='json')
		access_token = response_token.data['access']
		client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
		women = Women.objects.create(title='women', user_id=user_2.id)
		url = reverse_lazy('women_detail_delete', kwargs={'pk':women.id})
		response_women = client.delete(url)
		self.assertEqual(status.HTTP_204_NO_CONTENT, response_women.status_code) # Проверяем успех запроса
