# Generated by Django 4.1.1 on 2022-10-07 14:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0009_subject_capacity_remove_subject_seats_subject_seats'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.PROTECT, related_name='User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
