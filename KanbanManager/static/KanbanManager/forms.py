from django import forms
from django.forms.widgets import Textarea

class cardForm(forms.Form):
    name = forms.CharField(label="name", max_length=30)
    description = forms.CharField(widget=Textarea, required=False)
    pilot = forms.CharField(label="pilot", max_length=64)
    estimated = forms.IntegerField(required=False, label="estimated time (in hours)") # in hours
    attached = forms.CharField(label="link to attached files", max_length=300, required=False) 
    card_type = forms.CharField(label="card type", max_length=30, required=False)