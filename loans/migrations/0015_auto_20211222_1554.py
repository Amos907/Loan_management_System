# Generated by Django 3.1.7 on 2021-12-22 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0014_auto_20211222_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='loan_type_id',
        ),
        migrations.AddField(
            model_name='loan',
            name='loan_type_name',
            field=models.CharField(choices=[('P', 'Personal Loan'), ('S', 'Small Business Loan'), ('M', 'Mortgate')], default='P', max_length=2),
        ),
    ]
