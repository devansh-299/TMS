from django.test import TestCase
from django.contrib.auth.models import User
from transfers.models import UserProfile
from transfers.forms import PS2TSTransferForm, TS2PSTransferForm, PSDForm


class TestForms(TestCase):


    def test_ts2ps(self):

        user = User.objects.create(
            username='tester_username1',
            first_name='tester')
        user.set_password('password')
        user.save()

        UserProfile.objects.filter(
            user=user).update(
            campus=1,
            contact=1231231231,
            user_type=1
        )

        user_profile = UserProfile.objects.get(user=user)


        form = TS2PSTransferForm(data={
            'applicant': user_profile,
            'hod_email': 'test_hod@gmail.com',
            'sub_type': 1,
            'cgpa': 9.99,
            'reason_for_transfer': 'test_reason',
            'name_of_org': 'test_name_of_org'
        })
        print(form.errors)
        self.assertTrue(form.is_valid())


    def test_ps2ts(self):

        user = User.objects.create(
            username='tester_username2',
            first_name='tester')
        user.set_password('password')
        user.save()

        UserProfile.objects.filter(
            user=user).update(
            campus=1,
            contact=1231231231,
            user_type=1
        )

        user_profile = UserProfile.objects.get(user=user)


        form = PS2TSTransferForm(data={
            'applicant': user_profile,
            'supervisor_email': 'test_supervisor@gmail.com',
            'hod_email': 'test_hod@gmail.com',
            'sub_type': 1,
            'cgpa': 9.99,
            'thesis_locale': 1,
            'thesis_subject':'test_subject',
            'name_of_org': 'test_name_of_org',
            'expected_deliverables': 'test_deliverables'
        })
        print(form.errors)
        self.assertTrue(form.is_valid())