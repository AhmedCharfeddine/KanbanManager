# Generated by Django 3.1.4 on 2021-08-26 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KanbanManager', '0007_auto_20210826_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kanbancard',
            name='attached',
            field=models.CharField(blank=True, max_length=700),
        ),
        migrations.AlterField(
            model_name='kanbancard',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
