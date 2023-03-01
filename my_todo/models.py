from django.db import models
from django.core import validators


class Task(models.Model):
    """Class for tasks"""
    title = models.CharField('Title of task', max_length=250,
                             validators=[validators.MinLengthValidator(3, message='too small task')])
    complete = models.BooleanField('Complete', default=False)
    created_at = models.DateTimeField('Created time', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
