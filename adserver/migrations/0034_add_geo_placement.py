# Generated by Django 2.2.13 on 2020-09-30 20:33
import django.db.models.deletion
import django_countries.fields
import django_extensions.db.fields
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('adserver', '0033_add_keyword_placement_impressions'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='placementimpression',
            options={'ordering': ('-date',)},
        ),
        migrations.AddField(
            model_name='publisher',
            name='record_geos',
            field=models.BooleanField(default=False, help_text='Record geo impressions for this publisher'),
        ),
        migrations.CreateModel(
            name='GeoImpression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('date', models.DateField(verbose_name='Date')),
                ('offers', models.PositiveIntegerField(default=0, help_text='The number of times an ad was proposed by the ad server. The client may not load the ad (a view) for a variety of reasons ', verbose_name='Offers')),
                ('views', models.PositiveIntegerField(default=0, help_text='Number of times the ad was legitimately viewed', verbose_name='Views')),
                ('clicks', models.PositiveIntegerField(default=0, help_text='Number of times the ad was legitimately clicked', verbose_name='Clicks')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('advertisement', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='geo_impressions', to='adserver.Advertisement')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='geo_impressions', to='adserver.Publisher')),
            ],
            options={
                'ordering': ('-date',),
                'unique_together': {('publisher', 'advertisement', 'date', 'country')},
            },
        ),
    ]