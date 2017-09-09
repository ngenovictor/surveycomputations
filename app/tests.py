from django.test import TestCase as DjangoTestCase
from django.test import Client
from django.urls import reverse
from django.core import mail



class ViewTestCase(DjangoTestCase):
    """
    Define test cases for the Views in the app
    """
    def setUp(self):
        """
        define test client and other test variables
        """
        self.client = Client()

    def test_that_root_url_returns_home_page(self):
        response = self.client.get(
            reverse("home")
        )
        self.assertEqual(response.status_code, 200)

    # def test_that_give_error_on_submission_of_empty_fields(self):
    #     response = self.client.get(
    #         reverse("give_feedback"),
    #         {"name": "Victor", "message": "Love it"}
    #     )
    #     self.assertEqual(response.status_code, 503)


class EmailTestCase(DjangoTestCase):

    def test_app_can_send_mail(self):
        # Send message.
        mail.send_mail(
            'Subject here', 'Here is the message.',
            'from@example.com', ['to@example.com'],
            fail_silently=False,
        )
        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual("one", "two")

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, 'Subject here')
