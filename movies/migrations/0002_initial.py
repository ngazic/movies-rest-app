# Generated by Django 3.2.6 on 2021-08-13 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='movie',
            name='platform',
            field=models.ForeignKey(db_column='platform', on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='movies.streamplatform'),
        ),
    ]
