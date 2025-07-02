from django import forms
from .models import ReadingGuide

from markdownx.fields import MarkdownxFormField

class ListForm(forms.ModelForm):
    '''Form for users to create a list'''
    reading_list = MarkdownxFormField()

    class Meta:
        model = ReadingGuide
        fields = ['title', 'reading_list']