from django.contrib import admin
from .models import User


class UserFeedbackAdmin(admin.ModelAdmin):
    list_display = ["username", "fullname", "is_staff", "is_active", "email"]
    list_filter = ["is_staff", "is_active"]
    date_hierarchy = "date_joined"
    search_fields = ["username", "fullname"]


admin.site.register(User, UserFeedbackAdmin)
