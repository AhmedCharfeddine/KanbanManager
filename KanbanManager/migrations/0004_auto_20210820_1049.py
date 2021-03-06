# Generated by Django 3.1.4 on 2021-08-20 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KanbanManager', '0003_kanbanboard_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kanbancard',
            name='column',
        ),
        migrations.AddField(
            model_name='kanbancard',
            name='attached',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kanbancard',
            name='card_type',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kanbancard',
            name='estimated',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kanbancard',
            name='pilot',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kanbancard',
            name='state',
            field=models.CharField(choices=[('BL', 'Backlog'), ('UN', 'Up next'), ('IP', 'In progress'), ('OH', 'On hold'), ('DN', 'Done')], default='BL', max_length=2),
        ),
        migrations.DeleteModel(
            name='KanbanColumn',
        ),
    ]
