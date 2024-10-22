import click
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'My custom Click-based command'

    def add_arguments(self, parser):
        # Django will recognize the --name argument
        parser.add_argument('--name', type=str, help='Name to greet')

    def handle(self, *args, **options):
        # Get the --name option from the options passed by Django
        name = options.get('name', 'World')

        click.echo(f'Hello, {name}!')

