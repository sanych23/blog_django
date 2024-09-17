from django_seed import Seed
from blog.models import Role
from faker import Faker
from seeds.utils_seed import SeedExtension


class RoleSeed(SeedExtension):
    order = 0
    model = Role
    
    data = [
        {
            'id': 1,
            'title': 'Пользователь',
            'hidden_role': False,
        },
        {
            'id': 2,
            'title': 'Продавец',
            'hidden_role': False,
        },
        {
            'id': 3,
            'title': 'Редактор',
            'hidden_role': True,
        },
        {
            'id': 4,
            'title': 'Администратор',
            'hidden_role': True,
        },
        {
            'id': 5,
            'title': 'Супер администратор',
            'hidden_role': True,
        },
    ]


    def start(self) -> None:

        fake = Faker()
        seeder = Seed.seeder()
        
        for seed in self.data:
            seeder.add_entity(self.model, 1, seed)
        seeder.execute()

        