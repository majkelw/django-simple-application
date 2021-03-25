from django.core.management import BaseCommand
from app.models import Hunting, HuntingDetails


class Command(BaseCommand):
    def handle(self, *args, **options):
        list_cats = []
        cat_preys = []
        for hunting in Hunting.objects.all():
            list_cats.append(hunting.cat.name)

        for cat in list_cats:
            counter = 0
            for hunting_details in HuntingDetails.objects.all():
                if cat == hunting_details.cat.name:
                    counter += 1
            cat_preys.append([cat, counter])

        print(cat_preys)
        f = open("file.csv", "w")
        f.write(cat_preys.__str__())
        f.close()
