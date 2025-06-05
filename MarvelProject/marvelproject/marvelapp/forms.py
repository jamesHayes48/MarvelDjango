from django import forms
from .models import ReadingGuide

class ListForm(forms.ModelForm):
    '''Form for users to create a list'''
    title = forms.TextInput(empty_label="Enter name of guide", required=True)

    section = forms.TextInput(empty_label="Enter list of comics using markdown, use []-'for best use'")

    class Meta:
        model = ReadingGuide
        fields = ['title', 'reading_list']