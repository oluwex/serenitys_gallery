from django.db import models

# Create your models here.

def picture_directory_path(instance, filename):
    if instance.design_type == Design.TWO_D:
        return 'designs/2d/{0}'.format(filename)
    elif instance.design_type == Design.THREE_D:
        return 'designs/3d/{0}'.format(filename)
    return 'designs/general/{0}'.format(filename)


class Design(models.Model):

    TWO_D = '2d'
    THREE_D = '2d'

    design_choices = (
        (TWO_D, '2D'),
        (THREE_D, '3D'),
    )

    name = models.CharField(max_length=30)
    caption = models.TextField()
    design_type = models.CharField(max_length=5, choices=design_choices)
    pic = models.ImageField(upload_to=picture_directory_path)
    # client = models.CharField(max_length=50)
    description = models.TextField()
    time_completed = models.DateField()

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-timestamp']


class Message(models.Model):
    sender_name = models.CharField(max_length=100)
    sender_email = models.EmailField()
    subject = models.CharField(max_length=100)
    content = models.TextField()

    timestamp = models.DateTimeField(auto_now_add=True)
    sender_ip = models.GenericIPAddressField()

    def __str__(self):
        return self.sender_name