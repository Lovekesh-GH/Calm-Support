from django.db import models
from django.core.exceptions import ValidationError
import os

# Create your models here.
CHOICES = (
    ("Ambush", "Ambush"),
    ("Bombing", "Bombing"),
    ("Sucide Bombing", "Sucide Bombing"),
    ("Active Shooter", "Active Shooter"),
    ("Explosion", "Explosion"),
    ("Cyberattack", "Cyberattack"),
    ("Biological Attack", "Biological Attack"),
    ("Chemical Attack", "Chemical Attack"),
    ("Kidnapping", "Kidnapping"),
    ("Storming", "Stroming"),
    ("Radiological Attack", "Radiological Attack"),
    ("Other", "Other"),
)

def validate_video_extension(value):
    ext = os.path.splitext(value.name)[1]  
    valid_extensions = ['.mp4', '.avi', '.flv', '.wmv', '.mov']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

def validate_audio_extension(value):
    ext = os.path.splitext(value.name)[1]  
    valid_extensions = ['.ogg', '.mp3', '.mp4', '.wav', '.aac']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
        

class Uploads(models.Model):
    title = models.CharField(
        max_length=50, choices=CHOICES, null=False, default="Cyber Attack"
    )
    description = models.TextField()
    video = models.FileField(upload_to='videos/',validators=[validate_video_extension])
    audio  = models.FileField(upload_to='audio/',validators=[validate_audio_extension])
    image = models.ImageField(upload_to='images/')
    location = models.CharField(max_length=100)
    event_date = models.DateTimeField()
    
    class Meta:
        verbose_name = 'Upload'
        verbose_name_plural = 'Uploads'


    def _str_(self):
        return self.title