
# Django
from django.core.management.base import BaseCommand, CommandError

# Models
from products.models import Product, Provider

# Utilities
from random import randint


class Command(BaseCommand):
    help = 'Sort Random products and providers'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Sort random products'))

        products = Product.objects.all()
        for product in products:
            product.order = randint(1, 1000)
            product.save()
        self.stdout.write(self.style.SUCCESS('Sort random products. SUCCESS!'))

        self.stdout.write(self.style.SUCCESS('Sort random providers'))
        providers = Provider.objects.all()
        for provider in providers:
            provider.order = randint(1, 1000)
            provider.save()
        self.stdout.write(self.style.SUCCESS('Sort random providers. SUCCESS!'))
