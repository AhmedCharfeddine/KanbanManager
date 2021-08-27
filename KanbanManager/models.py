from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.enums import IntegerChoices
from django.db.models.fields import CharField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.utils.translation import gettext_lazy as _

# Create your models here.

class KanbanBoard(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return f'board {self.id}: "{self.name}"'

""" class KanbanColumn(models.Model):
    name = models.CharField(max_length=30)
    wip = models.IntegerField()
    board = models.ForeignKey(KanbanBoard, on_delete=models.CASCADE) """

class KanbanCard(models.Model):

    class Card_states(models.TextChoices):
        BACKLOG = 'BL', _('Backlog')
        UP_NEXT = 'UN', _('Up next')
        IN_PROGRESS = 'IP', _('In progress')
        ON_HOLD = 'OH', _('On hold')
        DONE = 'DN', _('Done')

    name = models.CharField(max_length=60)
    description = models.TextField()
    pilot = models.CharField(max_length=64)
    estimated = models.IntegerField(default=0, blank=True) # in hours
    attached = models.CharField(max_length=700, blank=True) 
    card_type = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=2, choices=Card_states.choices, default=Card_states.BACKLOG)
    board = models.ForeignKey(KanbanBoard, on_delete=CASCADE)

    def __str__(self):
        return f'card {self.id}: "{self.name}", in board "{self.board.name}"'