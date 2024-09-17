from django_seed import Seed
from blog.models import CategoryPost
from faker import Faker
from seeds.utils_seed import SeedExtension


class CategorySeed(SeedExtension):
    order = 2
    model = CategoryPost
    data = [
        {
            "id": 1,
            "title": "Красота",
            "description": "Описание категории Красота",
        },
        {
            "id": 2,
            "title": "Автомобили",
            "description": "Описание категории Автомобили",
        },
        {
            "id": 3,
            "title": "Спорт",
            "description": "Описание категории Спорт",
        },
        {
            "id": 4,
            "title": "Музыка",
            "description": "Описание категории Музыка",
        },
    ]


    def start(self) -> None:
        seeder = Seed.seeder()
        for seed in self.data:
            seeder.add_entity(self.model, 1, seed)
        seeder.execute()
