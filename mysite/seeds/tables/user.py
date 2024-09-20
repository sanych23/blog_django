from django_seed import Seed
from blog.models import User
import random
from faker import Faker
from authorisation.services.token_generate import TokenGenerator
from seeds.utils_seed import SeedExtension


class UserSeed(SeedExtension):
    order = 1
    model = User
    
    data = [
        {
            'id': 1,
            'username': 'Sasha',
            'email': 'sasha@ya.ru',
            'password': '123',
            'role_id': 1,
        },
        {
            'id': 2,
            'username': 'Pasha',
            'email': 'pasha@ya.ru',
            'password': '123',
            'role_id': 1,
            
        },
        {
            'id': 3,
            'username': 'Masha',
            'email': 'masha@ya.ru',
            'password': '123',
            'role_id': 1,
        },
        {
            'id': 4,
            'username': 'Kasha',
            'email': 'kasha@ya.ru',
            'password': '123',
            'role_id': 1,
        },
        {
            'id': 5,
            'username': 'sansanych',
            'email': 'sansanych@ya.ru',
            'password': '2001',
            'is_staff': True,
            'role_id': 1,
        }
    ]


    def start(self) -> None:

        fake = Faker()
        seeder = Seed.seeder()
        
        for seed in self.data:
            seed['token'] = TokenGenerator.generate(seed['email'], seed['username'])
            seeder.add_entity(self.model, 1, seed)
        seeder.execute()

