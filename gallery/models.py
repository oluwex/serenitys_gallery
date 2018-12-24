from django.db import models

from choices.models import DesignType

# Create your models here.

def picture_directory_path(instance, filename):
    if instance.design_type.name.lower() == '2d':
        return 'designs/2d/{0}'.format(filename)
    elif instance.design_type.name.lower() == '3d':
        return 'designs/3d/{0}'.format(filename)
    return 'designs/general/{0}'.format(filename)


class Design(models.Model):
    name = models.CharField(max_length=30)
    caption = models.TextField()
    design_type = models.ForeignKey(DesignType, on_delete=models.SET_NULL, null=True)
    pic = models.ImageField(upload_to=picture_directory_path)

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name