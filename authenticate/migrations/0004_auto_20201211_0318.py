# Generated by Django 3.1.2 on 2020-12-10 21:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0003_auto_20201211_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='cv_file_tsync_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
