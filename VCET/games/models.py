from django.db import models

# Create your models here.

class Slide(models.Model):
    image = models.ImageField(upload_to='slides/')
    audio = models.FileField(upload_to='audio/')
    french_text = models.TextField()
    english_text = models.TextField()

    def __str__(self):
        return f"Slide {self.id}"
