from django_seed import Seed
from blog.models import Posts, CategoryPost, User
import random
from faker import Faker


class PostSeed:
    value_count = 100
    model = Posts
    image_paths = [
        "images/blog/blog-md/blog/pic1.jpg",
        "images/blog/blog-md/blog/pic2.jpg",
        "images/blog/blog-md/blog/pic3.jpg",
        "images/blog/blog-md/blog/pic4.jpg",
        "images/blog/blog-md/blog/pic5.jpg",
        "images/blog/blog-md/blog/pic6.jpg",
        "images/blog/blog-md/blog/pic7.jpg",
    ]

    titles = [
        "House & Life Update…",
        "5 Tips for Making Your House Look Awesome",
        "Crafts for Kids",
        "Packing to Orlando",
        "Love in Las Vegas",
        "Absolutely Romance",
    ]


    @staticmethod
    def order():
        return 3

    def __init__(self) -> None:

        fake = Faker()
        seeder = Seed.seeder()

        categorie_id = CategoryPost.objects.values_list('id', flat=True)
        author_id = User.objects.values_list('id', flat=True)
        
        for id in range(1, self.value_count + 1):
            seed = {
                "id": id,
                "title": fake.text(max_nb_chars=30), # random.choice(self.titles)
                "content": fake.text(max_nb_chars=1000),
                "post_date": fake.date_this_year(),
                "image_path": random.choice(self.image_paths),
                "category_id": random.choice(categorie_id),
                "author_id": random.choice(author_id),
                "view_count": 0,
            }
            seeder.add_entity(self.model, 1, seed)
        seeder.execute()

    @staticmethod
    def delete():
        Posts.objects.all().delete()
