# Generated by Django 4.1.1 on 2022-09-15 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_student_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='seats',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='subject',
            name='semester',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='subject',
            name='year',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
