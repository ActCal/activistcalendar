"""
This suite tests the contact_us route, covering the OutsideContact model.
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
        client = Client()
        response = client.post('/contact_submit/',
                               {
                                    'input_contact_name': 'David Test',
                                    'input_contact_email': 'david314@gmail.com',
                                    'input_contact_subject': 'Subject field test',
                                    'input_contact_message': 'Hello from message field'
                               })
        self.assertEquals(response.status_code, 200)

        # # Alternatively, using the OutsideContact model
        # client = Client()
        # david = OutsideContact.objects.get(contact_name="David Test")
        # response = client.post('/contact_submit/', david)
        # self.assertEquals(response.status_code, 201)

    # def test_form_is_filled(self):
    #     '''Form fields contain outside contact data'''
    #     david = OutsideContact.objects.get(contact_name="David Test")
    #     self.assertEqual(david.contact_id, "1")
    #     self.assertEqual(david.contact_name, "David Test")
    #     self.assertEqual(david.contact_email, "david314@gmail.com")
    #     self.assertEqual(david.contact_subject, "Subject field test")
    #     self.assertEqual(david.contact_message, "Hello from the message field")

    # def test_form_submit(self):
    #     '''Form is submitted successfully'''
    #     def test_form(self):
    #         form = MyForm()
    #         self.assertTrue(form)
    #         self.assertTrue(form.is_valid())

    # def tearDown(self):
    #     pass
