from django.db import models
from django.core import validators

class Task(models.Model):
    """Class for tasks"""
    title = models.CharField('Title of task', max_length=250, validators=[validators.MinLengthValidator(3, message='too small task')])
    delete = models.BooleanField('Delete', default=False)
    complete = models.BooleanField('Complete', default=False)
    datetime = models.DateTimeField('Date and Time', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Task'
        verbose_name_plural='Tasks'
