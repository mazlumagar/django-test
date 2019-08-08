from django.test import TestCase

from .models import Model1


class TestModel(TestCase):
    def test_model1(self):
        model1 = Model1.objects.create(name="selam")
        self.assertEqual(str(model1), "selam")
