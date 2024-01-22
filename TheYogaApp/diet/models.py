from django.db import models


class Diet(models.Model):
    problem = models.CharField(max_length=20)
    tips = models.TextField()

    def __str__(self):
        return self.problem

    def tips_list(self):
        return self.tips.split('\n')
