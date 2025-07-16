from django.db import models
from django.contrib.auth import get_user_model

from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

User = get_user_model()

# Create your models here.
class ReadingGuide(models.Model):
    '''
    Hold values for a user's comic reading guide in markdown,
    (ideally)

    Fields:
    
    '''
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    reading_list = MarkdownxField()

    def formatted_markdown(self):
        return markdownify(self.reading_list)
    
    def __str__(self):
        return self.title
