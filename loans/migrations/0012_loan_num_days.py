# Generated by Django 3.1.7 on 2021-12-22 12:04

import computed_property.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0011_auto_20211222_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='num_days',
            field=computed_property.fields.ComputedTextField(compute_from='calc_dueDate', default=0, editable=False),
        ),
    ]
