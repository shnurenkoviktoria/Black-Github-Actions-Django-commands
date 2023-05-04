import random

from django.core.management.base import BaseCommand
from faker import Faker
from polls.models import Teacher

fake = Faker()


class Command(BaseCommand):
    help = "Generate random teachers"

    def add_arguments(self, parser):
        parser.add_argument(
            "--count", type=int, default=100, help="Number of teachers to generate"
        )

    def handle(self, *args, **options):
        count = options["count"]
        for i in range(count):
            name = fake.name()
            age = fake.random_int(min=22, max=80)
            subject = random.choice(["Math", "English", "Science"])
            Teacher.objects.create(name=name, age=age, subject=subject)
        self.stdout.write(
            self.style.SUCCESS(f"Successfully generated {count} teachers.")
        )
