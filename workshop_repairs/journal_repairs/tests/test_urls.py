from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import Client, TestCase

from ..models import (AddressOperation, Customer, Engine, EngineNumber,
                      EngineNumberRepair, Repair, RepairType, Еquipment)

User = get_user_model()


class JournalRepairUrlTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='admin')
        cls.engine = Engine.objects.create(
            title='KTTA-19',
            cylinders=6,
        )
        cls.equipment = Еquipment.objects.create(
            title='Белаз',
            name_equipment='Белаз 7555'
        )
        cls.customer = Customer.objects.create(
            name='Сурхур компани'
        )
        cls.address = AddressOperation.objects.create(
            address='Липецк СТАГДОК'
        )
        cls.repair_type = RepairType.objects.create(
            title='Капитальный ремонт'
        )
        cls.engine_number = EngineNumber.objects.create(
            engine_number='66666666',
            engine=cls.engine,
            equipment=cls.equipment,
            customer=cls.customer,
            address=cls.address,
            start_date='2022-02-15'
        )
        cls.repair = Repair.objects.create(
            repair_number='001',
            customer=cls.customer,
            repair_type=cls.repair_type,
            address=cls.address,
            author=cls.user,
            description='КР',
        )
        cls.engine_number_repair = EngineNumberRepair.objects.create(
            engine_number=cls.engine_number,
            repair=cls.repair
        )

    def setUp(self):
        self.guest_client = Client()
        self.admin = User.objects.get(username='admin')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.admin)
        self.journal_repair_page = '/repair/'
        self.repair_create_page = '/repair_create/'
        self.esn_create_page = '/esn_create/'
        self.esn_add_page = '/esn_add/'
        self.hours_add_page = '/hours_add/'
        self.repair_detail_page = f'/repair/{self.repair.id}/'
        self.add_comment_page = f'/repair/{self.repair.id}/comment/'
        self.repair_edit_page = f'/repair/{self.repair.id}/edit/'
        self.esn_edit_page = (f'/esn/{self.engine_number.id}/'
                              f'edit/{self.repair.id}/')
        self.esn_repairs_page = f'/esn/{self.engine_number.slug}/'

    def test_pages_journal_to_all_users(self):
        urls_name = {
            self.journal_repair_page: HTTPStatus.FOUND,
            self.repair_create_page: HTTPStatus.FOUND,
            self.esn_create_page: HTTPStatus.FOUND,
            self.esn_add_page: HTTPStatus.FOUND,
            self.hours_add_page: HTTPStatus.FOUND,
            self.repair_detail_page: HTTPStatus.FOUND,
            self.add_comment_page: HTTPStatus.FOUND,
            self.repair_edit_page: HTTPStatus.FOUND,
            self.esn_edit_page: HTTPStatus.FOUND,
            self.esn_repairs_page: HTTPStatus.FOUND,
        }
        for address, code in urls_name.items():
            with self.subTest(address=address):
                response = self.guest_client.get(address)
                self.assertEqual(response.status_code, code)

    def test_pages_journal_to_authorized_client(self):
        urls_name = {
            self.journal_repair_page: HTTPStatus.OK,
            self.repair_create_page: HTTPStatus.OK,
            self.esn_create_page: HTTPStatus.OK,
            self.esn_add_page: HTTPStatus.OK,
            self.hours_add_page: HTTPStatus.OK,
            self.repair_detail_page: HTTPStatus.OK,
            self.add_comment_page: HTTPStatus.FOUND,
            self.repair_edit_page: HTTPStatus.OK,
            self.esn_edit_page: HTTPStatus.OK,
            self.esn_repairs_page: HTTPStatus.OK,
        }
        for address, code in urls_name.items():
            with self.subTest(address=address):
                response = self.authorized_client.get(address)
                self.assertEqual(response.status_code, code)

    def test_correct_template_to_authorized_client(self):
        templates_name = {
            self.journal_repair_page: 'repairs/journal_repairs.html',
            self.repair_create_page: 'repairs/create_record.html',
            self.esn_create_page: 'repairs/create_record.html',
            self.esn_add_page: 'repairs/create_record.html',
            self.hours_add_page: 'repairs/create_record.html',
            self.repair_detail_page: 'repairs/repair_detail.html',
            self.repair_edit_page: 'repairs/create_record.html',
            self.esn_edit_page: 'repairs/create_record.html',
            self.esn_repairs_page: 'repairs/journal_repairs.html',
        }
        for address, name in templates_name.items():
            with self.subTest(address=address):
                response = self.authorized_client.get(address)
                self.assertTemplateUsed(response, name)
