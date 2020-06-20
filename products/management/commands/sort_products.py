
# Django
from django.core.management.base import BaseCommand, CommandError

# Models
from products.models import Product

# Utilities
from random import randint


class Command(BaseCommand):
    help = 'Sort Random products'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Sort random products'))

        products = Product.objects.filter(is_active=True)
        for product in products:
            product.order = randint(1, 1000)
            product.save()
        self.stdout.write(self.style.SUCCESS('Sort random products. SUCCESS!'))
