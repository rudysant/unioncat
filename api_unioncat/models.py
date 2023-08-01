from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=200, blank=False, default='')
    author = models.CharField(max_length=200,blank=False, default='')
    publisher = models.CharField(max_length=200,blank=False, default='')
    publish_year = models.IntegerField()
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Books'