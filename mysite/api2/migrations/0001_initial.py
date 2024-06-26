# Generated by Django 5.0.6 on 2024-05-20 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.BigIntegerField()),
                ('DVC_Code', models.TextField()),
                ('Company_Name', models.TextField()),
                ('Business_Nature', models.TextField()),
                ('Business_Sector', models.TextField()),
                ('Business_Industry', models.TextField()),
                ('Listed', models.TextField()),
                ('Legal_Status', models.TextField()),
                ('User_Key', models.TextField()),
                ('User_Name', models.TextField()),
                ('Firm_Key', models.TextField()),
                ('Firm_Name', models.TextField()),
                ('Service_Category', models.TextField()),
                ('Service_Name', models.TextField()),
                ('Document_Date', models.TextField()),
                ('Document', models.TextField()),
                ('Reference_Law', models.TextField()),
                ('DVC_Date', models.DateTimeField()),
                ('Month', models.IntegerField()),
                ('Day', models.IntegerField()),
                ('Year', models.IntegerField()),
            ],
            options={
                'db_table': 'todatabase',
            },
        ),
    ]
