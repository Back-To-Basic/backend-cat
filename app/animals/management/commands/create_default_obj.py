from pathlib import PurePath

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.images import ImageFile
from django.core.management.base import BaseCommand

from animals.models import Animal, AnimalImage

User = get_user_model()
TEST_DIR = PurePath(settings.MEDIA_ROOT, 'test')


class Command(BaseCommand):
    help = 'Create test objects'

    def handle(self, *args, **options):
        file_names = ['cat_1.jpeg', 'cat_2.jpg', 'cat_3.jpg', 'cat_4.jpg', 'cat_5.jpg']
        cat, _ = Animal.objects.get_or_create(name='고양이')
        User.objects.create_superuser(username='admin', password='1234')
        for name in file_names:
            print(f'{TEST_DIR}/{name}')
            with open(f'{TEST_DIR}/{name}', 'rb') as f:
                AnimalImage.objects.create(image=ImageFile(f, name=name), animal=cat)
        self.stdout.write(self.style.SUCCESS('Success created test objects'))
