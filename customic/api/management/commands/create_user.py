from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates admin user"

    def handle(self, *args, **kwargs):
        # get or create superuser
        user = User.objects.filter(username="admin").first()
        if not user:
            user = User.objects.create_superuser(username="admin", password="test")
