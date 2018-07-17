import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

from users_app.models import User
from faker import Faker

fakergen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_name = fakergen.first_name()
        fake_last_name = fakergen.last_name()
        fake_email = fakergen.email()

        fake_user = User.objects.get_or_create(name=fake_name, last_name=fake_last_name, email=fake_email)

if __name__ == '__main__':
    print("populating script!")
    populate(20)
