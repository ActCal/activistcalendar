"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
from activistcalendar.models import Profile

class ProfileTestCase(TestCase):
    def setUp(self):
        Profile.objects.create(
            username="david",
            user_full_name="David Test",
            user_email="david314@gmail.com",
            phone_number="+5934382319",
            website="http://www.foo.org/",
            personal_message="Hello",
        )
        Profile.objects.create(
            username="donald",
            user_full_name="Donald Test",
            user_email="donald159@gmail.com",
            phone_number="+5933141065",
            website="http://www.bar.org/",
            personal_message="Aloha",
        )


    def test_profile_exists(self):
        david = Profile.objects.get(user_email="david314@gmail.com")
        self.assertEqual(david.user_full_name, "David Test")
        self.assertEqual(david.user_email, "david314@gmail.com")
        self.assertEqual(david.phone_number, "+5934382319")
        self.assertEqual(david.website, "http://www.foo.org/")
        self.assertEqual(david.phone_number, "+5934382319")
        self.assertEqual(david.website, "http://www.foo.org/")
        self.assertEqual(david.personal_message, "Hello")

    def test_profile_deletes(self):
        donald = Profile.objects.get(user_email="donald159@gmail.com")
        donald.delete()
        donald = None
        try:
            donald2 = Profile.objects.get(user_email="donald159@gmail.com")
        except (ObjectDoesNotExist):
            donald2 = None
        self.assertEqual(donald2, None)

    def test_profile_updates(self):
        david = Profile.objects.get(user_email="david314@gmail.com")
        self.assertEqual(david.user_full_name, "David Test")
        self.assertEqual(david.user_email, "david314@gmail.com")
        self.assertEqual(david.phone_number, "+5934382319")
        self.assertEqual(david.website, "http://www.foo.org/")
        self.assertEqual(david.phone_number, "+5934382319")
        self.assertEqual(david.website, "http://www.foo.org/")
        self.assertEqual(david.personal_message, "Hello")
        david.user_full_name = "David Tester"
        self.assertEqual(david.user_full_name, "David Tester")
