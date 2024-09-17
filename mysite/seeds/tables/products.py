from magazine.models import Products, ProductCategory
import random
from faker import Faker
from seeds.utils_seed import SeedExtension


class ProductsSeed(SeedExtension):
    order = 6
    value_count = 10
    model = Products

    categories = ProductCategory.objects.all()
    
    product_tags = {
        'Чехол': [1],
        'M5': [2, 3],
        'Карданный вал': [3],
        'W124': [2, 3],
        'UAZ': [2, 3],
        'Шруз автомобильный': [3],
        'Шкаф': [4],
        'Кресло': [4],
        'Диван': [4],
    }

    real_data = [
        {
            "title": 'Чехол',
            "short_description": "Чехол обычкновенный черный",
            "description": "test",
            "count": 0,
            "price": random.uniform(0, 10000),
            "old_price": random.uniform(0, 10000),
        },
        {
            "title": 'M5',
            "short_description": "Машина спортивная черная",
            "description": "test",
            "count": 0,
            "price": random.uniform(0, 10000),
            "old_price": random.uniform(0, 10000),
        },
        {
            "title": 'Карданный вал',
            "short_description": "Запчасть для автомобиля",
            "description": "test",
            "count": 0,
            "price": random.uniform(0, 10000),
            "old_price": random.uniform(0, 10000),
        },
        {
            "title": 'W124',
            "short_description": "Комфортный немецкий старый автомобиль",
            "description": "test",
            "count": 0,
            "price": random.uniform(0, 10000),
            "old_price": random.uniform(0, 10000),
        },
        {
            "title": 'UAZ',
            "short_description": "Надежная техничка для работы",
            "description": "test",
            "count": 0,
            "price": random.uniform(0, 10000),
            "old_price": random.uniform(0, 10000),
        },
        {
            "title": 'Шруз автомобильный',
            "short_description": "Запчасть для подвески автомобиля",
            "description": "test",
            "count": 0,
            "price": random.uniform(0, 10000),
            "old_price": random.uniform(0, 10000),
        },
        {
            "title": 'Шкаф',
            "short_description": "Просторный шкаф для хранения вещей",
            "description": "test",
            "count": 0,
            "price": random.uniform(0, 10000),
            "old_price": random.uniform(0, 10000),
        },
        {
            "title": 'Кресло',
            "short_description": "Удобное кресло",
            "description": "test",
            "count": 0,
            "price": random.uniform(0, 10000),
            "old_price": random.uniform(0, 10000),
        },
        {
            "title": 'Диван',
            "short_description": "Диван для гостей в голубом цвете",
            "description": "test",
            "count": 0,
            "price": random.uniform(0, 10000),
            "old_price": random.uniform(0, 10000),
        }
    ]


    def start(self) -> None:

        fake = Faker()
        
        for id in range(1, self.value_count + 1):
            seed = {
                "id": id,
                "title": fake.text(max_nb_chars=15),
                "short_description": fake.text(max_nb_chars=100),
                "description": fake.text(max_nb_chars=1000),
                "count": 0,
                "price": random.uniform(0, 10000),
                "old_price": random.uniform(0, 10000),
                "category": random.choice(self.categories),
            }
            obj = self.model(**seed)
            obj.save()

        for seed in self.real_data:
            self.value_count += 1
            seed['id'] = self.value_count
            seed['category'] = random.choice(self.categories)
            obj = self.model(**seed)
            obj.save()
            obj.tags.add(*self.product_tags[seed['title']])

