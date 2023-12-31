from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class JWTAuthenticationTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user('Whoami')
        cls.user.set_password('12345')
        cls.user.save()
        cls.token_url = reverse('token')

    def test_authentication(self):
        response = self.client.post(self.token_url, data={'username': 'Whoami',
                                                          'password': '12345'},
                                    )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'access')

    def test_bad_credentials_authentication(self):
        response = self.client.post(self.token_url, data={'username': 'Whoami',
                                                          'password': '123456'})
        self.assertEqual(response.status_code, 401)


class AuthCRUDTestCase(APITestCase):
    fixtures = ['initial_data.json']

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user('Whoami')
        cls.user.set_password('12345')
        cls.user.save()
        cls.token_url = reverse('token')
        cls.employee_list_url = reverse('employee-list')
        cls.employee_url = reverse('employee-retrieve', kwargs={'pk': 1})
        cls.headers = dict()

    def setUp(self):
        response_data = self.client.post(self.token_url, data={'username': 'Whoami',
                                                               'password': '12345'}).json()
        self.headers['Authorization'] = f'Bearer {response_data["access"]}'

    def test_retrieve_employee(self):
        response = self.client.get(self.employee_url, headers=self.headers)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Project Manager')

    def test_create_employee(self):
        data = {'name': 'Test',
                'surname': 'Employee',
                'job_title': 'Test Job Title',
                'chiefs': [1, ]}
        response = self.client.post(self.employee_list_url,
                                    headers=self.headers,
                                    data=data)
        self.assertEqual(response.status_code, 201)
        self.assertContains(response, 'Test', status_code=201)

    def test_delete_employee(self):
        response = self.client.delete(self.employee_url, headers=self.headers)
        self.assertEqual(response.status_code, 204)

    def test_update_employee(self):
        data = {'name': 'TestUpdate'}
        response = self.client.patch(self.employee_url, data=data, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'TestUpdate')


