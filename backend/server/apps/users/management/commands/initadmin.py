
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from server.keys import Superuser

User = get_user_model()


class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            username = Superuser.USERNAME
            email = Superuser.EMAIL
            password = Superuser.PASSWORD
            print('Creating account for %s (%s)' % (username, email))
            admin = User.objects.create_superuser(
                email=email, username=username, password=password)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
            print('User alrerady exists in DB.')
