from django.db import models

def get_image_upload_path(instance, filename):
    return f'static/slides/images/{filename}'

def get_audio_upload_path(instance, filename):
    return f'static/slides/audio/{filename}'

class Slide(models.Model):
    image = models.ImageField(upload_to=get_image_upload_path)
    audio = models.FileField(upload_to=get_audio_upload_path)
    french_text = models.TextField()
    english_text = models.TextField()

    def __str__(self):
        return f"Slide {self.id}"

