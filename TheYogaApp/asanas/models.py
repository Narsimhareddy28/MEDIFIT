from django.db import models


class Asana(models.Model):
    name = models.CharField(max_length=256)
    duration = models.TimeField(default='00:00')
    image = models.CharField(max_length=256, default='')
    problems = models.ManyToManyField("problems.Problems")

    def __str__(self):
        return self.name
