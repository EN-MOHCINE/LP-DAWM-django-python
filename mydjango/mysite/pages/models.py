from django.db import models

# Create your models here.

class Page(models.Model) :
    title = models.CharField(max_length=60)
    permalink = models.CharField(max_length=12 ,unique=True)
    updated_at = models.DateTimeField(verbose_name="Last updated ")
    bodytext =models.TextField('Page Content' ,blank=True)




def __str__(self):
    return self.title
    