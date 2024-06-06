from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import CrimeType, CrimeSubcategory, CriminalCase
from officers.models import Officer
from .forms import CriminalCaseForm

class CrimeTypeModelTest(TestCase):

    def setUp(self):
        self.crime_type = CrimeType.objects.create(name='Theft')

    def test_crime_type_str(self):
        self.assertEqual(str(self.crime_type), 'Theft')


class CrimeSubcategoryModelTest(TestCase):

    def setUp(self):
        self.crime_type = CrimeType.objects.create(name='Theft')
        self.crime_subcategory = CrimeSubcategory.objects.create(crime_type=self.crime_type, name='Shoplifting')

    def test_crime_subcategory_str(self):
        self.assertEqual(str(self.crime_subcategory), 'Shoplifting')


class CriminalCaseModelTest(TestCase):

    def setUp(self):
        self.crime_type = CrimeType.objects.create(name='Theft')
        self.crime_subcategory = CrimeSubcategory.objects.create(crime_type=self.crime_type, name='Shoplifting')
        self.officer = Officer.objects.create(name='John Doe')
        self.criminal_case = CriminalCase.objects.create(
            event_date=timezone.now(),
            crime_type=self.crime_type,
            crime_subcategory=self.crime_subcategory,
            location_of_crime='123 Street',
            case_description='Description of the case',
            witnesses='Witness A, Witness B',
            known_suspects='Suspect A',
            arrested_suspects='Suspect B',
            case_status='active',
            case_officer=self.officer
        )

    def test_criminal_case_str(self):
        self.assertEqual(str(self.criminal_case), self.criminal_case.case_number)

    def test_case_number_generation(self):
        self.assertIsNotNone(self.criminal_case.case_number)
        self.assertEqual(len(self.criminal_case.case_number), 12)

    def test_case_status_choices(self):
        self.criminal_case.case_status = 'in_progress'
        self.criminal_case.save()
        self.assertEqual(self.criminal_case.case_status, 'in_progress')

        self.criminal_case.case_status = 'closed'
        self.criminal_case.save()
        self.assertEqual(self.criminal_case.case_status, 'closed')


class CriminalCaseViewTests(TestCase):

    def setUp(self):
        self.crime_type = CrimeType.objects.create(name='Theft')
        self.crime_subcategory = CrimeSubcategory.objects.create(crime_type=self.crime_type, name='Shoplifting')
        self.officer = Officer.objects.create(name='John Doe')
        self.criminal_case = CriminalCase.objects.create(
            event_date=timezone.now(),
            crime_type=self.crime_type,
            crime_subcategory=self.crime_subcategory,
            location_of_crime='123 Street',
            case_description='Description of the case',
            witnesses='Witness A, Witness B',
            known_suspects='Suspect A',
            arrested_suspects='Suspect B',
            case_status='active',
            case_officer=self.officer
        )

    def test_case_list_view(self):
        response = self.client.get(reverse('case_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'case_list.html')
        self.assertContains(response, self.criminal_case.case_number)

    def test_case_create_view(self):
        response = self.client.get(reverse('case_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'case_form.html')

    def test_case_create_post(self):
        data = {
            'event_date': '2024-05-30',
            'crime_type': self.crime_type.id,
            'crime_subcategory': self.crime_subcategory.id,
            'location_of_crime': '456 Street',
            'case_description': 'New case description',
            'witnesses': 'Witness X, Witness Y',
            'known_suspects': 'Suspect X',
            'arrested_suspects': 'Suspect Y',
            'case_status': 'in_progress',
            'case_officer': self.officer.id,
        }
        response = self.client.post(reverse('case_create'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(CriminalCase.objects.count(), 2)

    def test_case_update_view(self):
        response = self.client.get(reverse('case_update', args=[self.criminal_case.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'case_form.html')

    def test_case_update_post(self):
        data = {
            'event_date': '2024-05-30',
            'crime_type': self.crime_type.id,
            'crime_subcategory': self.crime_subcategory.id,
            'location_of_crime': '456 Street',
            'case_description': 'Updated case description',
            'witnesses': 'Witness X, Witness Y',
            'known_suspects': 'Suspect X',
            'arrested_suspects': 'Suspect Y',
            'case_status': 'closed',
            'case_officer': self.officer.id,
        }
        response = self.client.post(reverse('case_update', args=[self.criminal_case.pk]), data)
        self.assertEqual(response.status_code, 302)
        self.criminal_case.refresh_from_db()
        self.assertEqual(self.criminal_case.case_description, 'Updated case description')

    def test_case_delete_view(self):
        response = self.client.get(reverse('case_delete', args=[self.criminal_case.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'case_delete.html')

    def test_case_delete_post(self):
        response = self.client.post(reverse('case_delete', args=[self.criminal_case.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(CriminalCase.objects.count(), 0)


class CriminalCaseFormTests(TestCase):

    def setUp(self):
        self.crime_type = CrimeType.objects.create(name='Theft')
        self.crime_subcategory = CrimeSubcategory.objects.create(crime_type=self.crime_type, name='Shoplifting')
        self.officer = Officer.objects.create(name='John Doe')

    def test_form_valid_data(self):
        form = CriminalCaseForm(data={
            'event_date': '2024-05-30',
            'crime_type': self.crime_type.id,
            'crime_subcategory': self.crime_subcategory.id,
            'location_of_crime': '123 Street',
            'case_description': 'Case description',
            'witnesses': 'Witness A, Witness B',
            'known_suspects': 'Suspect A',
            'arrested_suspects': 'Suspect B',
            'case_status': 'active',
            'case_officer': self.officer.id,
        })
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form = CriminalCaseForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('event_date', form.errors)
        self.assertIn('crime_type', form.errors)
        self.assertIn('location_of_crime', form.errors)

    def test_form_subcategory_queryset(self):
        form = CriminalCaseForm(data={'crime_type': self.crime_type.id})
        self.assertQuerysetEqual(
            form.fields['crime_subcategory'].queryset,
            CrimeSubcategory.objects.filter(crime_type=self.crime_type).order_by('name')
        )
