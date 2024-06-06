from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import CriminalRecord, LogIn
from officers.models import Officer
from cases.models import CriminalCase
from .forms import CriminalForm, LogInForm


class CriminalRecordModelTest(TestCase):

    def setUp(self):
        self.officer = Officer.objects.create(name='Jane Doe')
        self.criminal_case = CriminalCase.objects.create(
            case_number='CR123456',
            event_date=timezone.now(),
            location_of_crime='123 Crime St',
            case_description='Test case description',
            witnesses='Witness A',
            known_suspects='Suspect A',
            arrested_suspects='Suspect B',
            case_status='active',
            case_officer=self.officer,
        )
        self.criminal_record = CriminalRecord.objects.create(
            first_name='John',
            middle_name='Doe',
            surname='Smith',
            date_of_birth='1990-01-01',
            tribe='Yoruba',
            religion='Christianity',
            marital_status='Single',
            height_in_meters=1.75,
            weight_in_kg=70,
            gender='male',
            nin='NIN123456789',
            address='456 Criminal St',
            associated_cases=self.criminal_case,
            contact_info='123-456-7890',
            distinctive_features='Scar on left cheek',
            next_of_kin='Jane Smith',
            known_aliases='Johnny',
            associates='Jane Doe',
            arresting_officer=self.officer,
        )

    def test_criminal_record_str(self):
        expected_string = f"Case Number: {self.criminal_record.case_number}, Name: John Doe Smith, Arresting Officer: {self.officer}, Date: 1990-01-01, Yoruba, Christianity, Single, 1.75, 70.0"
        self.assertEqual(str(self.criminal_record), expected_string)

    def test_generate_case_number(self):
        case_number = self.criminal_record.case_number
        self.assertEqual(len(case_number), 8)
        self.assertTrue(case_number[:2].isalpha())
        self.assertTrue(case_number[2:].isdigit())


class LogInModelTest(TestCase):

    def setUp(self):
        self.login = LogIn.objects.create(username='testuser', password='password123')

    def test_login_str(self):
        self.assertEqual(str(self.login), 'testuser, password123')


class CriminalFormTest(TestCase):

    def setUp(self):
        self.officer = Officer.objects.create(name='Jane Doe')
        self.criminal_case = CriminalCase.objects.create(
            case_number='CR123456',
            event_date=timezone.now(),
            location_of_crime='123 Crime St',
            case_description='Test case description',
            witnesses='Witness A',
            known_suspects='Suspect A',
            arrested_suspects='Suspect B',
            case_status='active',
            case_officer=self.officer,
        )

    def test_criminal_form_valid(self):
        form = CriminalForm(data={
            'first_name': 'John',
            'middle_name': 'Doe',
            'surname': 'Smith',
            'date_of_birth': '1990-01-01',
            'tribe': 'Yoruba',
            'religion': 'Christianity',
            'marital_status': 'Single',
            'height_in_meters': 1.75,
            'weight_in_kg': 70,
            'gender': 'male',
            'nin': 'NIN123456789',
            'address': '456 Criminal St',
            'associated_cases': self.criminal_case.id,
            'contact_info': '123-456-7890',
            'distinctive_features': 'Scar on left cheek',
            'next_of_kin': 'Jane Smith',
            'known_aliases': 'Johnny',
            'associates': 'Jane Doe',
            'arresting_officer': self.officer.id,
            'case_number': 'AB123456',
            'is_incarcerated': True,
            'is_wanted': False,
        })
        self.assertTrue(form.is_valid())

    def test_criminal_form_invalid(self):
        form = CriminalForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)
        self.assertIn('surname', form.errors)
        self.assertIn('date_of_birth', form.errors)
        self.assertIn('nin', form.errors)


class LogInFormTest(TestCase):

    def test_login_form_valid(self):
        form = LogInForm(data={
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertTrue(form.is_valid())

    def test_login_form_invalid(self):
        form = LogInForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('password', form.errors)


class CriminalViewsTest(TestCase):

    def setUp(self):
        self.officer = Officer.objects.create(name='Jane Doe')
        self.criminal_case = CriminalCase.objects.create(
            case_number='CR123456',
            event_date=timezone.now(),
            location_of_crime='123 Crime St',
            case_description='Test case description',
            witnesses='Witness A',
            known_suspects='Suspect A',
            arrested_suspects='Suspect B',
            case_status='active',
            case_officer=self.officer,
        )
        self.criminal_record = CriminalRecord.objects.create(
            first_name='John',
            middle_name='Doe',
            surname='Smith',
            date_of_birth='1990-01-01',
            tribe='Yoruba',
            religion='Christianity',
            marital_status='Single',
            height_in_meters=1.75,
            weight_in_kg=70,
            gender='male',
            nin='NIN123456789',
            address='456 Criminal St',
            associated_cases=self.criminal_case,
            contact_info='123-456-7890',
            distinctive_features='Scar on left cheek',
            next_of_kin='Jane Smith',
            known_aliases='Johnny',
            associates='Jane Doe',
            arresting_officer=self.officer,
        )

    def test_criminal_list_view(self):
        response = self.client.get(reverse('criminal_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'criminal_list.html')
        self.assertContains(response, self.criminal_record.first_name)

    def test_criminal_create_view(self):
        response = self.client.get(reverse('criminal_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'criminal_form.html')

    def test_criminal_create_post(self):
        data = {
            'first_name': 'Jane',
            'middle_name': 'Doe',
            'surname': 'Smith',
            'date_of_birth': '1992-02-02',
            'tribe': 'Igbo',
            'religion': 'Islam',
            'marital_status': 'Married',
            'height_in_meters': 1.65,
            'weight_in_kg': 60,
            'gender': 'female',
            'nin': 'NIN987654321',
            'address': '789 Crime St',
            'associated_cases': self.criminal_case.id,
            'contact_info': '987-654-3210',
            'distinctive_features': 'Tattoo on right arm',
            'next_of_kin': 'John Doe',
            'known_aliases': 'Janie',
            'associates': 'John Doe',
            'arresting_officer': self.officer.id,
            'case_number': 'XY654321',
            'is_incarcerated': True,
            'is_wanted': False,
        }
        response = self.client.post(reverse('criminal_create'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(CriminalRecord.objects.count(), 2)

    def test_criminal_update_view(self):
        response = self.client.get(reverse('criminal_update', args=[self.criminal_record.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'criminal_form.html')

    def test_criminal_update_post(self):
        data = {
            'first_name': 'John',
            'middle_name': 'Doe',
            'surname': 'Smith',
            'date_of_birth': '1990-01-01',
            'tribe': 'Yoruba',
            'religion': 'Christianity',
            'marital_status': 'Single',
            'height_in_meters': 1.75,
            'weight_in_kg': 70,
            'gender': 'male',
            'nin': 'NIN123456789',
            'address': '456 Criminal St',
            'associated_cases': self.criminal_case.id,
            'contact_info': '123-456-7890',
            'distinctive_features': 'Scar on left cheek',
            'next_of_kin': 'Jane Smith',
            'known_aliases': 'Johnny',
            'associates': 'Jane Doe',
            'arresting_officer': self.officer.id,
            'case_number': 'AB123456',
            'is_incarcerated': True,
            'is_wanted': False,
        }