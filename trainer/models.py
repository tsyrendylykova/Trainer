from django.conf import settings
from django.db import models
from django.utils import timezone

class Trainer(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return '{},{}'.format(self.name, self.description)



