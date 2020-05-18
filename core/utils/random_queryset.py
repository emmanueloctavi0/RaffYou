
# Django
from django.db.models import Max
import random


def random_pk(model):
    """Get a random id from model"""
    max_id = model.objects.all().aggregate(max_id=Max("id"))['max_id']
    while max_id:
        pk = random.randint(1, max_id)
        try:
            return model.objects.values('id').get(pk=pk)['id']
        except model.DoesNotExist:
            pass


def random_pk_list(model, length):
    """Get a random pk list"""
    pk_list = []
    for _ in range(length):
        pk_list.append(random_pk(model))

    return pk_list
