from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext
from django.conf import settings

# Create your models here.
class Documents(models.Model):

    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(_("deleted at"), null=True, blank=True)
    file = models.FileField(null=True, blank=True, upload_to="File/Legal/")
    text = models.TextField(blank=True)


    @property
    def text_file(self):
        filename = self.file.name
        ext = filename.split('.')[-1]
        if ext == "txt":
            with open(self.file, 'r') as file:
                return file.read().replace('\n', '')
        else:
            pass

