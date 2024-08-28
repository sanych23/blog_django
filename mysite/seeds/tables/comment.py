from django_seed import Seed
from blog.models import Comment, Author, Posts
import random
from faker import Faker


class CommentSeed:
    value_count = 2000
    model = Comment


    @staticmethod
    def order():
        return 4

    def __init__(self) -> None:

        fake_en = Faker('en')
        fake_ru = Faker('ru')

        seeder = Seed.seeder()

        author_id = Author.objects.values_list('id', flat=True)
        post_id = Posts.objects.values_list("id", flat=True)
        
        for id in range(1, self.value_count + 1):
            seed = {
                "id": id,
                "content": fake_ru.text(max_nb_chars=150),
                "content_ru": fake_ru.text(max_nb_chars=150),
                "content_en": fake_en.text(max_nb_chars=150),
                "comment_date": fake_ru.date_time(),
                "author_id": random.choice(author_id),
                "post_id": random.choice(post_id),
            }
            seeder.add_entity(self.model, 1, seed)
        seeder.execute()


    @staticmethod
    def delete():
        Comment.objects.all().delete()
