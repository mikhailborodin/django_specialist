from django.test import TestCase, Client
from datetime import datetime
from .models import Question


class QuestionTestCase(TestCase):
    fixtures = ['main.json']

    def setUp(self):
        self.client = Client()
        self.objects = (Question.objects.first(), Question.objects.last())

    def test_question_get_text(self):
        for question in self.objects:
            self.assertEqual(question.get_text(), question.question_text)

    def test_get_absolute_url(self):
        for question in self.objects:
            response = self.client.get(question.get_absolute_url())
            self.assertContains(response, '<title>Title</title>')
