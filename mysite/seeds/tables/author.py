from django_seed import Seed
from blog.models import Author
from faker import Faker


class AuthorSeed:
    value_count = 100
    model = Author

    @staticmethod
    def order():
        return 1

    def __init__(self) -> None:

        fake = Faker()
        seeder = Seed.seeder()
        
        for id in range(1, self.value_count + 1):
            seed = {
                "id": id,
                "name": fake.name(),
            }
            seeder.add_entity(self.model, 1, seed)
        seeder.execute()
        

    @staticmethod
    def delete():
        Author.objects.all().delete()
