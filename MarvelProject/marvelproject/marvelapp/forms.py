from django import forms
from .models import ReadingGuide

from martor.fields import MartorFormField

class ListForm(forms.ModelForm):
    '''Form for users to create a list'''
    reading_list = MartorFormField()

    class Meta:
        model = ReadingGuide
        fields = ['title', 'reading_list']