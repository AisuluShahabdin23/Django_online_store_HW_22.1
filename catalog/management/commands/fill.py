import json
from django.core.management import BaseCommand
#from django.db import connection
from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Cleaning table Category
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Clearing autoincrement for pk filed table Category
#        with connection.cursor() as cursor:
#            cursor.execute("ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1")

        # Fill file
        category_list = [
            {"pk": 1, 'name': 'Vegetables', 'description': 'Local Vegetables'},
            {"pk": 2, 'name': 'Fruits', 'description': 'Local Fruits'},
            {"pk": 3, 'name': 'Products for babies', 'description': 'Products for children age up to 3 y.o '},
            {"pk": 4, 'name': 'Meat', 'description': 'Beef, chicken, fish, turkey'},
            {"pk": 5, 'name': 'Bakery', 'description': 'buns, pies, donuts and so on'}
        ]
        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Category(**category_item))

        Category.objects.bulk_create(category_for_create)

        category1 = Category.objects.get(pk=1)
        category2 = Category.objects.get(pk=2)
        category3 = Category.objects.get(pk=3)
        category4 = Category.objects.get(pk=4)
        category5 = Category.objects.get(pk=5)

        product_list = [
            {"pk": 1, 'name': 'Брокколи',
             'description': 'Овощное растение из семейства капустных', 'photo': "products/Brokkoli.jpg",
             'category': category1, 'price': 1200, 'creation_date': "2023-10-29T11:51:45Z",
             'changing_date': '2023-10-29T11:51:50Z'},

            {"pk": 2, 'name': 'Яблоко', 'description': 'Плод яблони шарообразной формы', 'photo': "products/Yabloko.jpg",
             'category': category2, 'price': 700, 'creation_date': "2023-10-29T11:53:56Z",
             'changing_date': '2023-10-29T11:53:58Z'},

            {"pk": 3, 'name': 'Печенье Бонди',
             'description': 'Полезное и мягкое печенье для самых маленьких. Для детей с 6 месяцев.',
             'photo': "products/Bondi.png", 'category': category3, 'price': 550, 'creation_date': "2023-10-29T12:08:17Z",
             'changing_date': '2023-10-29T12:08:19Z'},

            {"pk": 4, 'name': 'Говядина', 'description': 'Употребляемое в пищу мясо крупного рогатого скота',
             'photo': "products/Myaso.jpeg",
             'category': category4, 'price': 3000, 'creation_date': "2023-10-29T13:14:11Z",
             'changing_date': '2023-10-29T13:14:13Z'}
        ]

        product_for_create = []

        for product_item in product_list:
            product_for_create.append(Product(**product_item))

        Product.objects.bulk_create(product_for_create)
