from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin


# Register your models here.


class DocumentAdmin(admin.ModelAdmin):
    list_display: ["id", "deleted_at", "create_by"]
    search_fields: ["text"]
    readonly_fields = ["timestamp"]


admin.site.register(models.Documents, DocumentAdmin)

