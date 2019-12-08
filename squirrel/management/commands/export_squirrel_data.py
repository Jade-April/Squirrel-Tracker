from django.core.management.base import BaseCommand
from squirrel.models import Squirrel
import csv

class Command(BaseCommand):
    help=("output model into  CSV file")

    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self,*args,**options):
        path=options['csv_file']
        meta=Squirrel._meta
        field_names=[field.name for field in meta.fields]
        with open(path, 'w') as csvfile:
            writer=csv.writer(csvfile)
            writer.writerow(field_names)
            for obj in Squirrel.objects.all():
                row=writer.writerow([getattr(obj, field) for field in field_names])
