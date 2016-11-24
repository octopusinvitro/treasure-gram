from django.test import TestCase
from django.contrib.auth.models import User
from .models import Treasure


class TreasureTestCase(TestCase):


    def setUp(self):
        admin   = User.objects.create(username='admin')
        octopus = User.objects.create(username='octopus')
        Treasure.objects.create(
            user=admin,
            name='Shiny Rock',
            value=20.00,
            material='alien dust',
            location='Mars',
            image='',
            likes=0)

        Treasure.objects.create(
            user=admin,
            name='Sparkly Rock',
            value=50.00,
            material='meteorite',
            location='Moon',
            image='',
            likes=0)

        Treasure.objects.create(
            user=octopus,
            name='Pirate hook',
            value=200.00,
            material='iron',
            location='Underworld',
            image='',
            likes=0)


    def test_treasures_have_an_owner(self):
        """Can find all treasures of an owner"""
        admin   = User.objects.get(username='admin')
        octopus = User.objects.get(username='octopus')
        admin_treasures   = Treasure.objects.filter(user=admin)
        octopus_treasures = Treasure.objects.filter(user=octopus)
        self.assertEqual(admin_treasures.count(), 2)
        self.assertEqual(octopus_treasures.count(), 1)
