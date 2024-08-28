from django_seed import Seed
from blog.models import CategoryPost
from faker import Faker


class CategorySeed:
    model = CategoryPost
    data = [
        {
            "id": 1,
            "title_ru": "Красота",
            "title_en": "Beauty",
            "description_ru": "Описание категории Красота",
            "description_en": "Description category Beauty",
        },
        {
            "id": 2,
            "title_ru": "Автомобили",
            "title_en": "Auto",
            "description_ru": "Описание категории Автомобили",
            "description_en": "Description category Auto",
        },
        {
            "id": 3,
            "title_ru": "Спорт",
            "title_en": "Sport",
            "description_ru": "Описание категории Спорт",
            "description_en": "Description category Sport",
        },
        {
            "id": 4,
            "title_ru": "Музыка",
            "title_en": "Music",
            "description_ru": "Описание категории Музыка",
            "description_en": "Description Category Music",
        },
    ]

    @staticmethod
    def order():
        return 2

    def __init__(self) -> None:
        seeder = Seed.seeder()
        for seed in self.data:
            seeder.add_entity(self.model, 1, seed)
        seeder.execute()


    @staticmethod
    def delete():
        CategoryPost.objects.all().delete()
