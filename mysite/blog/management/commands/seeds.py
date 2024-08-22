from django.core.management.base import BaseCommand, CommandError
from seeds.main import Main

class Command(BaseCommand):

    def handle(self, *args, **options):
        Main().start()
        print("Seeding complete!")
