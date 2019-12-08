from django.core.management.base import BaseCommand,CommandError
from squirrel.models import Squirrel
import pandas as pd
from django.utils import timezone
import datetime

class Command(BaseCommand):
    help=("input CSV file into model")
    def add_arguments(self, parser): 
        parser.add_argument('csv_file')

    def handle(self,*args,**options):
        path_file=options['csv_file']
        df=pd.read_csv(path_file)
        for i in range(len(df)):
            date=datetime.datetime.strptime(str(df.iloc[i,5]),'%m%d%Y')
            year=date.year
            month=date.month
            day=date.day
            try:
                s=Squirrel(
                        Latitude=df.iloc[i,1],
                        Longitude=df.iloc[i,0],
                        Unique_Squirrel_ID=df.iloc[i,2],
                        Shift=df.iloc[i,4],
                        Date=timezone.datetime(year,month,day),
                        Age=df.iloc[i,7],
                        Primary_Fur_Color=df.iloc[i,8],
                        Location=df.iloc[i,12],
                        Specific_Location=df.iloc[i,14],
                        Running=df.iloc[i,15],
                        Chasing=df.iloc[i,16],
                        Climbing=df.iloc[i,17],
                        Eating=df.iloc[i,18],
                        Foraging=df.iloc[i,19],
                        Other_Activities=df.iloc[i,20],
                        Kuks=df.iloc[i,21],
                        Quaas=df.iloc[i,22],
                        Moans=df.iloc[i,23],
                        Tail_flags=df.iloc[i,24],
                        Tail_twitches=df.iloc[i,25],
                        Approaches=df.iloc[i,26],
                        Indifferent=df.iloc[i,27],
                        Runs_from=df.iloc[i,28],
                        )
                s.save()
            except:
                pass
