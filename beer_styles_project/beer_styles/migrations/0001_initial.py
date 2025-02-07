# Generated by Django 5.1.3 on 2024-11-13 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BeerStyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=100)),
                ('categorynumber', models.CharField(max_length=10)),
                ('overallimpression', models.TextField()),
                ('aroma', models.TextField()),
                ('appearance', models.TextField()),
                ('flavor', models.TextField()),
                ('mouthfeel', models.TextField()),
                ('comments', models.TextField()),
                ('history', models.TextField()),
                ('characteristicingredients', models.TextField()),
                ('stylecomparison', models.TextField()),
                ('ibumin', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ibumax', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ogmin', models.DecimalField(decimal_places=4, max_digits=5)),
                ('ogmax', models.DecimalField(decimal_places=4, max_digits=5)),
                ('fgmin', models.DecimalField(decimal_places=4, max_digits=5)),
                ('fgmax', models.DecimalField(decimal_places=4, max_digits=5)),
                ('abvmin', models.DecimalField(decimal_places=2, max_digits=5)),
                ('abvmax', models.DecimalField(decimal_places=2, max_digits=5)),
                ('srmmin', models.DecimalField(decimal_places=2, max_digits=5)),
                ('srmmax', models.DecimalField(decimal_places=2, max_digits=5)),
                ('commercialexamples', models.TextField()),
                ('tags', models.TextField()),
                ('entryinstructions', models.TextField()),
                ('currentlydefinedtypes', models.TextField()),
                ('strengthclassifications', models.TextField()),
                ('overallimpression_cz', models.TextField()),
                ('aroma_cz', models.TextField()),
                ('appearance_cz', models.TextField()),
                ('flavor_cz', models.TextField()),
                ('mouthfeel_cz', models.TextField()),
                ('comments_cz', models.TextField()),
                ('entryinstructions_cz', models.TextField()),
            ],
        ),
    ]
