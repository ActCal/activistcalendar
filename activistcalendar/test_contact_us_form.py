"""
This suite tests the contact_us and the contact_submit routes
Tests should use the OutsideContact model.
"""

from django.test import TestCase
from django.test import Client
from activistcalendar.models import OutsideContact


class OutsideContactTestCase(TestCase):
    def setUp(self):

        OutsideContact.objects.create(
            contact_name="David Test",
            contact_email="david314@gmail.com",
            contact_subject="Subject field test",
            contact_message="Hello from the message field"
        )

        OutsideContact.objects.create(
            contact_name="Donald Test",
            contact_email="donald159@gmail.com",
            contact_subject="Subject field test",
            contact_message="Hello from message field"
        )

    def test_form_submitted(self):
        '''POST to /contact_submit route from the contact_us.html template'''
        client = Client()
        response = client.post('/contact_submit/',
            {
                'input_contact_name': 'David Test',
                'input_contact_email': 'david314@gmail.com',
                'input_contact_subject': 'Subject field test',
                'input_contact_message': 'Hello from message field'
            })
        self.assertEquals(response.status_code, 200)
