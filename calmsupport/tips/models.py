from django.db import models
from django.core.exceptions import ValidationError
import os
from encryption import encrypts
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

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

def upload_image(instance, filename):
    ext = filename.split(".")[-1]
    return "image/{}.{}".format(uuid4().hex, ext)

def validate_video_extension(value):
    ext = os.path.splitext(value.name)[1]  
    valid_extensions = ['.mp4', '.avi', '.flv', '.wmv', '.mov']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

def validate_audio_extension(value):
    ext = os.path.splitext(value.name)[1]  
    valid_extensions = ['.ogg', '.mp3', '.mp4', '.wav', '.aac','.mpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
        

class Uploads(models.Model):
    title = models.CharField(
        max_length=50, choices=CHOICES, null=False, default="Cyber Attack"
    )
    description = models.TextField()
    video = models.FileField(upload_to='videos/',validators=[validate_video_extension])
    audio  = models.FileField(upload_to='audios/',validators=[validate_audio_extension])
    # image = models.ImageField(upload_to='images/')
    image = models.ImageField(upload_to=upload_image)
    location = models.CharField(max_length=100)
    event_date = models.DateTimeField()

    def save(self):
        # self.save()
        if self.description:
        #    self.description = encrypts.encryptText(self.description)
           print(self.description)
        if self.location:
        #    self.location = encrypts.encryptText(self.location)       
           print(self.location)
        print("inside save func")
        
        return self.save()

    
    class Meta:
        verbose_name = 'Upload'
        verbose_name_plural = 'Uploads'

    def _str_(self):
        return self.title

    @property
    def get_absolute_image_url(self):
        return "{0}{1}".format(settings.MEDIA_URL, self.image.url)
    
    # def documents(self):
    #     path = os.path.join(Settings.BASEDIR,“media”)
    #     path = path + self.get_absolute_image_url
    #     return encrypt

@receiver(post_save,sender=Uploads)
def encrypt_image(sender, *args, **kwargs):
    print('post save callback')
    # file = instance.audio.path
    print(sender.get_absolute_image_url)
    path = settings.MEDIA_ROOT
    path = path + sender.get_absolute_image_url
    print(path)
    return encryptImage(path)
    # encrypts.encryptImage(sender.image, *args, **kwargs)