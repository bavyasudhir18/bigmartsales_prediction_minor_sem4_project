import pandas as pd
from django.core.management.base import BaseCommand
from sales.models import TrainData

class Command(BaseCommand):
    help = 'Loads data from train.csv into the database'

    def handle(self, *args, **kwargs):
        df = pd.read_csv('train.csv')
        for _, row in df.iterrows():
            TrainData.objects.create(
                Item_Identifier=row['Item_Identifier'],
                Item_Weight=row.get('Item_Weight', None),
                Item_Fat_Content=row['Item_Fat_Content'],
                Item_Visibility=row['Item_Visibility'],
                Item_Type=row['Item_Type'],
                Item_MRP=row['Item_MRP'],
                Outlet_Identifier=row['Outlet_Identifier'],
                Outlet_Establishment_Year=row['Outlet_Establishment_Year'],
                Outlet_Size=row.get('Outlet_Size', None),
                Outlet_Location_Type=row['Outlet_Location_Type'],
                Outlet_Type=row['Outlet_Type'],
                Item_Outlet_Sales=row['Item_Outlet_Sales']
            )
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from train.csv'))
