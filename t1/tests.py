from django.test import TestCase

from .models import Model1, Model2


class TestModel(TestCase):
    def test_model1(self):
        model1 = Model1.objects.create(name="selam")
        self.assertEqual(str(model1), "selam")

    def test_model1(self):
        model2 = Model2.objects.create(name="test")
        self.assertEqual(str(model2), "test")

