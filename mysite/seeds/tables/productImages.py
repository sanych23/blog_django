from django_seed import Seed
from magazine.models import ProductImages, Products
import random
from faker import Faker


class ProductimagesSeed:
    order = 7
    model = ProductImages
    
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


    def start(self) -> None:

        seeder = Seed.seeder()
        id = 0

        for product in Products.objects.all():
            id += 1
            seed = {
                'id': id,
                'image_path': random.choice(self.image_paths),
                'product_id': product.id,
                'main_image': True
            }
            seeder.add_entity(self.model, 1, seed)
        seeder.execute()


    def delete(self):
        self.model.objects.all().delete()