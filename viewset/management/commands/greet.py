import click
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Greet a user by name and age"
    
    def add_arguments(self, parser):
        parser.add_argument('--name',type=str,default= 'stranger', help = 'Name of the person to greet')
        parser.add_argument('--age',type=int,default=3,help='Age of the person') 

    def handle(self, *args, **options):
        name = options['name']
        age = options['age']
        if age > 0:
            click.echo(f'Hello {name}! I am {age} years old.')
        else:
            click.echo(f'Hello {name}!')    

             
