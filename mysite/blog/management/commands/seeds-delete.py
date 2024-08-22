from django.core.management.base import BaseCommand, CommandError
# from seeds.tables.author import AuthorSeed
from seeds.main import Main

class Command(BaseCommand):

    def handle(self, *args, **options):
        Main().delete()
        print("Delete complete!")
        