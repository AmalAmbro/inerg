import pandas as pd

from django.core.management import BaseCommand

from core.models import Well


def handle_well(well, data):
    try:
        oil = data['OIL']
        gas = data['GAS']
        brine = data['BRINE']
        instance = Well.objects.get(well=well)

        print("Data already exists")
        print(f"Existing data: oil - {instance.oil}, gas - {instance.gas}, brine - {instance.brine}")
        print(f"Current data: oil - {oil}, gas - {gas}, brine - {brine}")

        update = input("Update with current one ? (y/N): ")
        if update == "y" or update == "Y":
            instance.oil = oil
            instance.gas = gas
            instance.brine = brine
            instance.save()

            print(f"Updated api well number: {instance.well}, with current data.")
    except Well.DoesNotExist:
        instance = Well.objects.create(
            well=well,
            oil=oil,
            gas=gas,
            brine=brine,
        )
        print(f"Data Created for api well number: f{instance.well}")
    
    except Exception as e:
        print("Error occured")
        print(e.args)
        

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        file_path = options['file_path']
        print(f"\nReading data from {file_path}")

        try:
            df = pd.read_excel(file_path)
            columns = ['API WELL  NUMBER', 'OIL', 'GAS', 'BRINE']
            df_filtered = df[columns]
            df_group_by = df_filtered.groupby('API WELL  NUMBER').sum()

            for well, row in df_group_by.iterrows():
                handle_well(well, row)

            print("Data Loading Completed")

        except Exception as e:
            print("Error Occured")
            print(e.args[0])
