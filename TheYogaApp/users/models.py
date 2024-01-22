from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    f_name = models.CharField(max_length=256)
    l_name = models.CharField(max_length=256)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    dob = models.DateField()
    gender = models.CharField(max_length=10, default='none')
    picture = models.ImageField(upload_to="profile_pics", null=True, blank=True)
    medical_conditions = models.ManyToManyField("problems.Problems")
    diet = models.ManyToManyField("diet.Diet")
    exercise_frequency = models.CharField(max_length=1, default='0')
