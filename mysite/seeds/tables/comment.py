from django_seed import Seed
from blog.models import Comment, User, Posts
import random
from faker import Faker
from seeds.utils_seed import SeedExtension


class CommentSeed(SeedExtension):
    order = 4
    value_count = 500
    model = Comment


    def start(self) -> None:

        fake = Faker()
        seeder = Seed.seeder()

        author_id = User.objects.values_list('id', flat=True)
        post_id = Posts.objects.values_list("id", flat=True)
        
        for id in range(1, self.value_count + 1):
            seed = {
                "id": id,
                "content": fake.text(max_nb_chars=150),
                "comment_date": fake.date_time(),
                "author_id": random.choice(author_id),
                "post_id": random.choice(post_id),
            }
            seeder.add_entity(self.model, 1, seed)
        seeder.execute()

