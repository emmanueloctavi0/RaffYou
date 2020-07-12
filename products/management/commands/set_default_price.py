
# Django
from django.core.management.base import BaseCommand

# Models
from products.models import Product


class Command(BaseCommand):
    help = 'Set default price to products'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Reading products...'))

        products = Product.objects.all()
        for product in products:
            product.price_default = product.productprice_set.first().price
            product.save()

        self.stdout.write(self.style.SUCCESS('Setted default price to products'))
