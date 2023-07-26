import json

from django.contrib.auth.models import User
from django.test import TestCase

from employee_records.models import Employee


# Create your tests here.


class AuthCRUDTestCase(TestCase):
    fixtures = ['initial_data.json']

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user('Whoami')
        cls.password = '12345'
        cls.user.set_password(cls.password)
        cls.user.save()

    def test_list_employees(self):
        token_response = self.client.post('/api/token/',
                                          data={'username': self.user.username, 'password': self.password})
        token = token_response.data['access']
        headers = {'Authorization': f'Bearer {token}'}
        response = self.client.get('/api/employee_records/', headers=headers)

        self.assertEqual(response.status_code, 200)

    def test_retrieve_employee(self):
        token_response = self.client.post('/api/token/',
                                          data={'username': self.user.username, 'password': self.password})
        token = token_response.data['access']
        headers = {'Authorization': f'Bearer {token}'}
        response = self.client.get('/api/employee_records/1/', headers=headers)

        self.assertEqual(response.status_code, 200)

    def test_create_employee(self):
        token_response = self.client.post('/api/token/',
                                          data={'username': self.user.username, 'password': self.password})
        token = token_response.data['access']
        headers = {'Authorization': f'Bearer {token}'}
        data = {'name': 'who', 'surname': 'ami', 'job_title': 'Jun Dev', 'chiefs': [1, 2, 3, 4]}
        response = self.client.post('/api/employee_records/', headers=headers, data=data)

        self.assertEqual(response.status_code, 201)

    def test_update_employee(self):
        token_response = self.client.post('/api/token/',
                                          data={'username': self.user.username, 'password': self.password})
        token = token_response.data['access']
        headers = {'Authorization': f'Bearer {token}'}
        data = {'name': 'who', 'surname': 'ami'}
        response = self.client.patch('/api/employee_records/1/', content_type='application/json', data=data,
                                     headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_delete_employee(self):
        token_response = self.client.post('/api/token/',
                                          data={'username': self.user.username, 'password': self.password})
        token = token_response.data['access']
        headers = {'Authorization': f'Bearer {token}'}
        response = self.client.delete('/api/employee_records/1/', headers=headers)

        self.assertEqual(response.status_code, 204)


class NoAuthCRUDTestCase(TestCase):
    def test_list_employees(self):
        response = self.client.get('/api/employee_records/')
        self.assertEqual(response.status_code, 401)

    def test_retrieve_employee(self):
        response = self.client.get('/api/employee_records/1/')
        self.assertEqual(response.status_code, 401)

    def test_create_employee(self):
        data = {'name': 'who', 'surname': 'ami', 'job_title': 'Jun Dev', 'chiefs': [1, 2, 3, 4]}
        response = self.client.post('/api/employee_records/', data=data)

        self.assertEqual(response.status_code, 401)

    def test_update_employee(self):
        data = {'name': 'who', 'surname': 'ami'}
        response = self.client.patch('/api/employee_records/1/', content_type='application/json', data=data)
        self.assertEqual(response.status_code, 401)

    def test_delete_employee(self):
        response = self.client.delete('/api/employee_records/1/')
        self.assertEqual(response.status_code, 401)
