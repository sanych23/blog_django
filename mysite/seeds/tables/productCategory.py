from django_seed import Seed
from magazine.models import ProductCategory
import random
from faker import Faker


class ProductcategorySeed:
    order = 4
    model = ProductCategory
    
    data = [
        {
            "id": 1,
            "title": "Смартфоны",
            "description": "Описание категории Смартфоны",
        },
        {
            "id": 2,
            "title": "Ноутбуки",
            "description": "Описание категории Ноутбуки",
        },
        {
            "id": 3,
            "title": "Аксессуары",
            "description": "Описание категории Аксессуары",
        },
        {
            "id": 4,
            "title": "Одежда",
            "description": "Описание категории Одежда",
        },
        {
            "id": 5,
            "title": "Автомобили",
            "description": "Описание категории Автомобили",
        }
    ]


    def start(self) -> None:
        seeder = Seed.seeder()
        
        for seed in self.data:
            seeder.add_entity(self.model, 1, seed)
        seeder.execute()


    def delete(self):
        self.model.objects.all().delete()
