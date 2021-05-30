from django.db import models
from django.utils import timezone
from django.urls import reverse


class Books(models.Model):
    name = models.CharField(max_length=100)
    auther = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    publish_date = models.DateTimeField(default=timezone.now)
    summary =models.TextField(max_length=500,blank=True)
    price = models.IntegerField(blank=True , default=0)
    photo = models.FileField(upload_to='Book/%Y/%m/%d/', blank = True)    

    def __str__(self):
    		return self.name
    
    def get_absolute_url(self):
    		return reverse('Book:book_detail', args=[self.id, self.name])
