from django.test import TestCase
from django.urls import reverse
from .models import Officer
from .forms import OfficerForm


class OfficerModelTest(TestCase):

    def test_officer_str(self):
        officer = Officer.objects.create(
            name='John Doe',
            sex='male',
            rank='Constable',
            badge_number=123456,
            area='Patrol',
            date_of_birth='1990-01-01',
            phone_number='123-456-7890',
            email='john@example.com',
            address='123 Main St',
            city='Metropolis',
            state='State',
            nationality='Nigerian',
            duty_status='On Duty',
        )
        self.assertEqual(str(officer), 'Constable John Doe')


class OfficerFormTest(TestCase):

    def test_officer_form_valid(self):
        form = OfficerForm(data={
            'name': 'Jane Doe',
            'sex': 'female',
            'rank': 'Sergeant',
            'badge_number': 654321,
            'area': 'Traffic',
            'date_of_birth': '1995-01-01',
            'phone_number': '987-654-3210',
            'email': 'jane@example.com',
            'address': '456 Elm St',
            'city': 'Metropolis',
            'state': 'State',
            'nationality': 'Nigerian',
            'duty_status': 'Off Duty',
        })
        self.assertTrue(form.is_valid())

    def test_officer_form_invalid(self):
        form = OfficerForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('badge_number', form.errors)
        self.assertIn('email', form.errors)


class OfficerViewsTest(TestCase):

    def test_officer_list_view(self):
        response = self.client.get(reverse('officer_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'officer_list.html')

    def test_officer_create_view(self):
        response = self.client.get(reverse('officer_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'officer_form.html')

    def test_officer_create_post(self):
        data = {
            'name': 'Test Officer',
            'sex': 'male',
            'rank': 'Constable',
            'badge_number': 987654,
            'area': 'Investigation',
            'date_of_birth': '1985-01-01',
            'phone_number': '555-555-5555',
            'email': 'test@example.com',
            'address': '789 Oak St',
            'city': 'Metropolis',
            'state': 'State',
            'nationality': 'Nigerian',
            'duty_status': 'On Duty',
        }
        response = self.client.post(reverse('officer_create'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Officer.objects.count(), 1)

    def test_officer_update_view(self):
        officer = Officer.objects.create(
            name='Test Officer',
            sex='male',
            rank='Constable',
            badge_number=987654,
            area='Investigation',
            date_of_birth='1985-01-01',
            phone_number='555-555-5555',
            email='test@example.com',
            address='789 Oak St',
            city='Metropolis',
            state='State',
            nationality='Nigerian',
            duty_status='On Duty',
        )
        response = self.client.get(reverse('officer_update', args=[officer.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'officer_form.html')

    def test_officer_delete_view(self):
        officer = Officer.objects.create(
            name='Test Officer',
            sex='male',
            rank='Constable',
            badge_number=987654,
            area='Investigation',
            date_of_birth='1985-01-01',
            phone_number='555-555-5555',
            email='test@example.com',
            address='789 Oak St',
            city='Metropolis',
            state='State',
            nationality='Nigerian',
            duty_status='On Duty',
        )
        response = self.client.get(reverse('officer_delete', args=[officer.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'officer_delete.html')
