    from django.test import TestCase, Client, SimpleTestCase
    from django.contrib.auth.models import User
    from django.urls import reverse
    import json


    class TestViews(TestCase):

        def test_login(self):

            c = Client()
            response = c.post('/TMS/login/', {'username': 'tester', 
            'password': 'password'})
            self.assertEquals(response.status_code, 200)
            print("Login Tested")
            
        def test_student_dashboard(self):

            user = User.objects.create_superuser(
                username="tester",
                password="password")

            c = Client()
            c.force_login(user)
            response = c.get('/TMS/student/dashboard/')

            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'transfers/student_dashboard.html')

        def test_ps2ts_application(self):

            user = User.objects.create_superuser(
                username="tester",
                password="password")

            c = Client()
            c.force_login(user)
            response = c.get('/TMS/student/PS2TS/')

            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'transfers/PS2TS.html')

        def test_ts2ps_application(self):
            user = User.objects.create_superuser(
                username="tester",
                password="password")
                
            c = Client()
            c.force_login(user)
            response = c.get('/TMS/student/TS2PS/')

            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'transfers/TS2PS.html')
            print("Student Views Tested")

        def test_hod_home(self):

            user = User.objects.create_superuser(
                username="tester",
                password="password")

            c = Client()
            c.force_login(user)
            response = c.get('/TMS/hod/home/')

            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'transfers/common.html')
            print("HOD View Tested")

        def test_supervisor_home(self):

            user = User.objects.create_superuser(
                username="tester",
                password="password")

            c = Client()
            c.force_login(user)
            response = c.get('/TMS/supervisor/home/')

            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'transfers/common.html')
            print("Supervisor View Tested")

        

        

        