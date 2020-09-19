from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext
from django.conf import settings

# Create your models here.
class Documents(models.Model):
    create_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="create_by",
        help_text="Created by documents name",
    )
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    deleted_at = models.DateTimeField(_("deleted at"), null=True, blank=True)
    file = models.FileField(null=True, blank=True, upload_to="File/Legal/")
    text = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        self.create_by = self.request.user
