import csv
import os
from django.core.management.base import BaseCommand
from beer_styles.models import BeerStyle
from django.conf import settings

class Command(BaseCommand):
    help = 'Import beer styles from CSV file'

    def handle(self, *args, **options):
        file_path = os.path.join(settings.BASE_DIR, 'data', 'translated_data.csv')
        
        if not os.path.exists(file_path):
            self.stderr.write(f"File not found: {file_path}")
            return

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            BeerStyle.objects.all().delete()

            count = 0
            errors = 0

            for row in reader:
                try:
                    # Funkce pro bezpečný převod na číslo
                    def convert_decimal(value):
                        if value is None or value.strip() == "":
                            return None
                        value = value.replace(',', '.').strip()  # Nahradí čárku tečkou
                        return float(value)

                    BeerStyle.objects.create(
                        name=row['name'].strip(),
                        number=row['number'].strip(),
                        category=row['category'].strip(),
                        categorynumber=row['categorynumber'].strip(),
                        overallimpression=row['overallimpression'].strip(),
                        aroma=row['aroma'].strip(),
                        appearance=row['appearance'].strip(),
                        flavor=row['flavor'].strip(),
                        mouthfeel=row['mouthfeel'].strip(),
                        comments=row['comments'].strip(),
                        history=row['history'].strip(),
                        characteristicingredients=row['characteristicingredients'].strip(),
                        stylecomparison=row['stylecomparison'].strip(),
                        ibumin=convert_decimal(row['ibumin']),
                        ibumax=convert_decimal(row['ibumax']),
                        ogmin=convert_decimal(row['ogmin']),
                        ogmax=convert_decimal(row['ogmax']),
                        fgmin=convert_decimal(row['fgmin']),
                        fgmax=convert_decimal(row['fgmax']),
                        abvmin=convert_decimal(row['abvmin']),
                        abvmax=convert_decimal(row['abvmax']),
                        srmmin=convert_decimal(row['srmmin']),
                        srmmax=convert_decimal(row['srmmax']),
                        commercialexamples=row['commercialexamples'].strip(),
                        tags=row['tags'].strip(),
                        entryinstructions=row['entryinstructions'].strip(),
                        currentlydefinedtypes=row['currentlydefinedtypes'].strip(),
                        strengthclassifications=row['strengthclassifications'].strip(),
                        overallimpression_cz=row['overallimpression_cz'].strip(),
                        aroma_cz=row['aroma_cz'].strip(),
                        appearance_cz=row['appearance_cz'].strip(),
                        flavor_cz=row['flavor_cz'].strip(),
                        mouthfeel_cz=row['mouthfeel_cz'].strip(),
                        comments_cz=row['comments_cz'].strip(),
                        history_cz=row['history_cz'].strip(),
                        characteristicingredients_cz=row['characteristicingredients_cz'].strip(),
                        stylecomparison_cz=row['stylecomparison_cz'].strip(),
                        tags_cz=row['tags_cz'].strip(),                        
                        
                    )
                    count += 1
                except ValueError as e:
                    errors += 1
                    self.stderr.write(f"Error on row {count + errors}: {e} ")

        self.stdout.write(self.style.SUCCESS(f"Successfully imported {count} beer styles with {errors} errors"))
