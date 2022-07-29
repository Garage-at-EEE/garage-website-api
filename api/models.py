from xmlrpc.client import boolean
from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
# Create your models here.

#Google drive backend setup. Refer to https://django-googledrive-storage.readthedocs.io/en/latest/
from gdstorage.storage import GoogleDriveStorage
gd_storage = GoogleDriveStorage()
#All file & image fields will accept the property " storage=gd_storage " & that automatically connects to Google Drive 

class Ambassador(models.Model):
    """Model representing an Ambassador"""
    name = models.CharField(max_length=200, help_text='Enter name of Ambassador')
    desc = models.CharField(max_length=200, help_text='Enter description of Ambassador')
    displayImage = models.ImageField(upload_to = 'AmbassadorImage/', storage=gd_storage, max_length=100, verbose_name = "Ambassador Image", default = None)
    def __str__(self):
        """String for representing the Model object."""
        return self.name
class AmbassadorImage(models.Model):
    Ambassador = models.ForeignKey(Ambassador, default=None, on_delete=models.CASCADE, related_name="contentImages")
    image = models.ImageField(upload_to='images/', storage=gd_storage)
    def __str__(self):
        """String for representing the Model object."""
        return self.image.name


class Event(models.Model):
    name = models.CharField(max_length=200, help_text='Enter name of Event')
    date = models.DateField()
    desc = models.CharField(max_length=200, help_text='Enter description of Event')
    article = models.TextField(default = None)
    isFlagshipEvent = models.BooleanField(default = False)
    displayImage = models.ImageField(upload_to = 'Event Image/', storage=gd_storage, max_length=100, verbose_name = "Event Image", default = None)
    contentVideo = models.FileField(upload_to='Event Videos/', storage=gd_storage, null=True,
                    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    link = models.URLField(default=None)
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    # def get_absolute_url(self):
    #     """Returns the URL to access a particular instance of the model."""
    #     return reverse('model-detail-view', args=[str(self.id)])
class EventImage(models.Model):
    Event = models.ForeignKey(Event, default=None, on_delete=models.CASCADE, related_name="contentImages")
    image = models.ImageField(upload_to='images/', storage=gd_storage)
    def __str__(self):
        """String for representing the Model object."""
        return self.image.name

class Project(models.Model):
    name = models.CharField(max_length=200, help_text='Enter name of Project')
    desc = models.CharField(max_length=200, help_text='Enter description of Project')
    article = models.TextField(default = None)
    displayImage = models.ImageField(upload_to = 'Project Image/', storage=gd_storage, max_length=100, verbose_name = "Project Image", default = None)
    contentVideo = models.FileField(upload_to='Project Videos/', storage=gd_storage, null=True,
                    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    link = models.URLField(default=None)
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    # def get_absolute_url(self):
    #     """Returns the URL to access a particular instance of the model."""
    #     return reverse('model-detail-view', args=[str(self.id)])
class ProjectImage(models.Model):
    Event = models.ForeignKey(Project, default=None, on_delete=models.CASCADE, related_name="contentImages")
    image = models.ImageField(upload_to='images/', storage=gd_storage)
    def __str__(self):
        """String for representing the Model object."""
        return self.image.name

class InnovatorRegistration(models.Model):
    regIsOpen = models.BooleanField()
    regLink = models.TextField(default = None)

    def save(self, *args, **kwargs):
        if not self.pk and InnovatorRegistration.objects.exists():
        # if you'll not check for self.pk 
        # then error will also raised in update of exists model
            raise ValidationError('There is can be only one InnovatorRegistration instance')
        return super(InnovatorRegistration, self).save(*args, **kwargs)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.regLink