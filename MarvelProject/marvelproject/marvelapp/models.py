from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class ReadingGuide():
    '''
    Hold values for a user's comic reading guide in markdown,
    (ideally)

    Fields:
    
    '''
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    reading_list = models.TextField()
