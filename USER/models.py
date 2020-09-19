from django.db import models
import uuid
import os
from django.urls import reverse
from django.db.models.signals import post_save
from datetime import datetime
from django.dispatch import receiver
from datetime import datetime
from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string
from oauth2_provider.models import AccessToken
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

from oauth2_provider.models import AbstractAccessToken

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        user = self.model(
            email=self.normalize_email(email), username=username.lower(), **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


def image_file_path(instance, filename):
    _datetime = datetime.now()
    datetime_str = _datetime.strftime("%Y-%m-%d")
    return "Photo/{0}/{1}/{2}/RET-ZURICHTEAM/".format(
        instance.username, datetime_str, filename
    )


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    fullname = models.CharField(max_length=60, blank=True)
    phone_number = models.CharField(max_length=60, blank=True)
    website = models.CharField(max_length=240, blank=True)
    private_account = models.BooleanField(default=False)
    is_verify = models.BooleanField(default=False)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to=image_file_path, default="avatar.png")
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="user_followers",
        blank=True,
        symmetrical=False,
    )
    following = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="user_following",
        blank=True,
        symmetrical=False,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=255, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def number_of_followers(self):
        if self.followers.count():
            return self.followers.count()
        else:
            return 0

    def number_of_following(self):
        if self.following.count():
            return self.following.count()
        else:
            return 0

    def __str__(self):
        return self.username

    # Once you will register you will get confirmation email  on registration email!
    def send_confirmation_email(self):
        confirm_url = reverse("users_confirm", args=[self.token])
        ctx = {"user": self.username, "confirm_url": confirm_url}
        tpl = "user/registration_email.html"
        html_message = render_to_string(tpl, ctx)
        send_mail(
            subject="Registration confirmation email",
            message="",
            html_message=html_message,
            from_email="RET-ZURICHTEAM <noreply@ret-zurichteam.com>",
            recipient_list=[self.email],
        )

    # Welcome message confirmation once your register is successful !
    def send_welcome_email(self):
        ctx = {
            "user": self.username,
        }
        tpl = "user/welcome_email.html"
        html_message = render_to_string(tpl, ctx)
        send_mail(
            subject="Welcome to Simple Blog Family",
            message="",
            html_message=html_message,
            from_email="RET-ZURICHTEAM <noreply@ret-zurichteam.com>",
            recipient_list=[self.email],
        )

from django.db import models

# Create your models here.
