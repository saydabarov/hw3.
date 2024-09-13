from django.db import models

# Create your models here.

class Team(models.Model):
    photo = models.ImageField(upload_to='team_photos/')  
    name = models.CharField(max_length=255)  
    position = models.CharField(max_length=255)  

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команда"



class Banner(models.Model):
    logo = models.ImageField(upload_to='logos/')  
    banner_photo = models.ImageField(upload_to='banner_photos/')  
    title = models.CharField(max_length=255) 
    description = models.TextField()  
    watermark = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
    
    




