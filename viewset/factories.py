import factory
from .models import *
from faker import Faker
from factory.django import DjangoModelFactory

fake = Faker()

class ProductFactory(DjangoModelFactory):
    class Meta:
        model = product

    name = factory.LazyAttribute(lambda _:fake.word())
    price = factory.LazyAttribute(lambda _:fake.pydecimal(right_digits=3, max_value=9999, min_value=0))
    rating = factory.LazyAttribute(lambda _:fake.pyfloat(right_digits=1, positive=True, max_value=5))    