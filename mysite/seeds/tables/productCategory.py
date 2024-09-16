from django_seed import Seed
from magazine.models import ProductCategory
import random
from faker import Faker


class ProductcategorySeed:
    # value_count = 
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


    @staticmethod
    def order():
        return 4

    def __init__(self) -> None:

        fake = Faker()
        seeder = Seed.seeder()

        # categories_id = ProductCategory.objects.values_list('id', flat=True)
        # categorie_id = CategoryPost.objects.values_list('id', flat=True)
        # author_id = User.objects.values_list('id', flat=True)
        
        for seed in self.data:
            # seed = {
                # "id": id,
                # "title": fake.text(max_nb_chars=15),
                # "short_description": fake.text(max_nb_chars=100),
                # "description": fake.text(max_nb_chars=1000),
                # "main_image_product": random.choice(self.image_paths),
                # "count": 0,
                # "price": random.uniform(0, 1000000),
                # "old_price": random.uniform(0, 1000000),
                # "category": random.choice(categories_id),
                # "id": id,
                # "title": fake.text(max_nb_chars=30), # random.choice(self.titles)
                # "content": fake.text(max_nb_chars=1000),
                # "post_date": fake.date_this_year(),
                # "image_path": random.choice(self.image_paths),
                # "category_id": random.choice(categorie_id),
                # "author_id": random.choice(author_id),
                # "view_count": 0,
            # }
            seeder.add_entity(self.model, 1, seed)
        seeder.execute()

    @staticmethod
    def delete():
        ProductCategory.objects.all().delete()
