from django_seed import Seed
from blog.models import User
import random
from faker import Faker


class UserSeed:
    model = User
    
    data = [
        {
            'id': 1,
            'username': 'Sasha',
            'email': 'sasha@ya.ru',
            'password': '123',
        },
        {
            'id': 2,
            'username': 'Pasha',
            'email': 'pasha@ya.ru',
            'password': '123',
        },
        {
            'id': 3,
            'username': 'Masha',
            'email': 'masha@ya.ru',
            'password': '123',
        },
        {
            'id': 4,
            'username': 'Kasha',
            'email': 'kasha@ya.ru',
            'password': '123',
        },
        {
            'id': 5,
            'username': 'sansanych',
            'email': 'sansanych@ya.ru',
            'password': '2001',
            'is_staff': True
        }
    ]


    @staticmethod
    def order():
        return 1

    def __init__(self) -> None:

        fake = Faker()
        seeder = Seed.seeder()
        
        for seed in self.data:
            seeder.add_entity(self.model, 1, seed)
        seeder.execute()

    @staticmethod
    def delete():
        User.objects.all().delete()