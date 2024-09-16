from django_seed import Seed
from magazine.models import Products, ProductCategory
import random
from faker import Faker


class ProductsSeed:
    value_count = 2
    model = Products
    image_paths = [
        "images/product/product-item/item1.jpg",
        "images/product/product-item/item2.jpg",
        "images/product/product-item/item3.jpg",
        "images/product/product-item/item4.jpg",
        "images/product/product-item/item5.jpg",
        "images/product/product-item/item6.jpg",
        "images/product/product-item/item7.jpg",
        "images/product/product-item/item8.jpg",
        "images/product/product-item/item9.jpg",
        "images/product/product-item/item10.jpg",
        "images/product/product-item/item11.jpg",
        "images/product/product-item/item12.jpg",
    ]


    @staticmethod
    def order():
        return 5

    def __init__(self) -> None:

        fake = Faker()
        seeder = Seed.seeder()

        categories = ProductCategory.objects.all()
        
        for id in range(1, self.value_count + 1):
            seed = {
                "id": id,
                "title": fake.text(max_nb_chars=15),
                "short_description": fake.text(max_nb_chars=100),
                "description": fake.text(max_nb_chars=1000),
                # "main_image_product": random.choice(self.image_paths),
                "count": 0,
                "price": random.uniform(0, 10000),
                "old_price": random.uniform(0, 10000),
                "category": random.choice(categories),
            }
            seeder.add_entity(self.model, 1, seed)
        seeder.execute()

    @staticmethod
    def delete():
        Products.objects.all().delete()
