from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError("Please provide valid email address.")
        if not password:
            raise ValueError("Please provide a Password")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = None
    first_name = models.CharField(_("First Name"), max_length=255, null=True)
    last_name = models.CharField(_("Last Name"), max_length=255, null=True)
    phone = models.CharField(max_length=50, help_text="Office use only")
    email = models.EmailField(
        max_length=255, unique=True, null=True, help_text="Office use only"
    )
    is_staff = models.BooleanField(default=False)
    address = models.CharField(_("Address"), max_length=500, null=True)
    city = models.CharField(_("City"), max_length=255, null=True)
    state = models.CharField(_("State"), max_length=255, null=True)
    zip_code = models.CharField(_("Zip Code"), max_length=255, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    object = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = "user"
