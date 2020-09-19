from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext
from django.conf import settings
# Create your models here.
class Documents(models.Model):
    create_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="create_by", help_text="Creater o"
    )