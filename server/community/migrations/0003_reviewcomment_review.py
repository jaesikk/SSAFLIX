# Generated by Django 3.2.3 on 2021-05-21 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_auto_20210521_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewcomment',
            name='review',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='community.review'),
            preserve_default=False,
        ),
    ]