from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import Client, TestCase

User = get_user_model()


class AboutUrlTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='admin')
    
    def setUp(self):
        self.guest_client = Client()
        self.admin = User.objects.get(username='admin')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.admin)
        self.main_page = '/'
        self.login_page = '/auth/login/'
        self.password_reset_page = '/auth/password_reset_admin/'
        self.password_change_page = '/auth/password_change/'


    def test_pages_about_to_all_users(self):
        urls_name = {
            self.main_page: HTTPStatus.OK,
            self.login_page: HTTPStatus.OK,
            self.password_reset_page: HTTPStatus.OK,
            self.password_change_page: HTTPStatus.FOUND,
        }
        for address, code in urls_name.items():
            with self.subTest(address=address):
                response = self.guest_client.get(address)
                self.assertEqual(response.status_code, code)

    def test_pages_about_to_authorized_users(self):
        urls_name = {
            self.main_page: HTTPStatus.OK,
            self.login_page: HTTPStatus.OK,
            self.password_reset_page: HTTPStatus.OK,
            self.password_change_page: HTTPStatus.OK,
        }
        for address, code in urls_name.items():
            with self.subTest(address=address):
                response = self.authorized_client.get(address)
                self.assertEqual(response.status_code, code)

    def test_correct_template_to_all_users(self):
        templates_name = {
            self.main_page: 'about/index.html',
            self.login_page: 'users/login.html',
            self.password_reset_page: 'users/password_reset_to_admin.html',
        }
        for address, name in templates_name.items():
            with self.subTest(address=address):
                response = self.guest_client.get(address)
                self.assertTemplateUsed(response, name)

    def test_correct_template_to_authorized_users(self):
        templates_name = {
            self.main_page: 'about/index.html',
            self.login_page: 'users/login.html',
            self.password_reset_page: 'users/password_reset_to_admin.html',
            self.password_change_page: 'users/password_change_form.html',
        }
        for address, name in templates_name.items():
            with self.subTest(address=address):
                response = self.authorized_client.get(address)
                self.assertTemplateUsed(response, name)
