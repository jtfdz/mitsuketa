from django.db import models

# Create your models here.

RADIO_CHOICES = ((0, "submit page / manga"),
                 (1, "report a problem"))

class Submission(models.Model):
    id_submission = models.BigAutoField(primary_key=True)
    problem = models.CharField(choices = RADIO_CHOICES, max_length=1)
    manga_name = models.CharField(max_length=40)
    page_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=400)
