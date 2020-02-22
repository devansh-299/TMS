from django.test import TestCase
from django.contrib.auth.models import User
from transfers.models import UserProfile, PS2TSTransfer, TS2PSTransfer

class TestModels(TestCase):
     

    def test_user_profile(self):

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

        # testing on the basis of field comparision
        self.assertEquals(user_profile.user_type, 1)
        print("User Model tested")

    def test_ps2tstransfer(self):

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

        ps2tstransfer = PS2TSTransfer.objects.create(
            applicant= user_profile,
            supervisor_email= 'test_supervisor@gmail.com',
            hod_email= 'test_hod@gmail.com',
            sub_type= 1,
            cgpa= 9.99,
            thesis_locale= 1,
            thesis_subject= 'test_subject',
            name_of_org= 'test_name_of_org',
            expected_deliverables= 'test_expected_deliverables',
            is_supervisor_approved= True,
            is_hod_approved= False )

        # testing on the basis of field comparision
        self.assertEquals(ps2tstransfer.thesis_locale, 1)

    def test_ts2pstransfer(self):

        user = User.objects.create(
            username='tester_username3',
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

        ts2pstransfer = TS2PSTransfer.objects.create(
            applicant= user_profile,
            hod_email= 'test_hod@gmail.com',
            sub_type= 1,
            cgpa= 9.99,
            reason_for_transfer= 'test_reason',
            name_of_org= 'test_name_of_org',
            is_hod_approved= True )

        # testing on the basis of field comparision
        self.assertEquals(ts2pstransfer.cgpa, 9.99)

    




        
