from django_seed import Seed
from magazine.models import TagProduct
from faker import Faker


class TagsSeed:
    model = TagProduct
    
    data = [
        {
            'id': 1,
            'title': 'accesories',
            'description': 'test',
        },
        {
            'id': 2,
            'title': 'car',
            'description': 'test',
        },
        {
            'id': 3,
            'title': 'autoparts',
            'description': 'test',
        },
        {
            'id': 4,
            'title': 'furniture',
            'description': 'test',
        },
    ]


    @staticmethod
    def order():
        return 5

    def __init__(self) -> None:

        fake = Faker()
        seeder = Seed.seeder()
        
        for seed in self.data:
            seeder.add_entity(self.model, 1, seed)
        seeder.execute()

    @staticmethod
    def delete():
        TagProduct.objects.all().delete()
        