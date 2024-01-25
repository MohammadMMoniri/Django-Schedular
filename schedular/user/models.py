from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, UserManager

USER_TYPE = (
    ("a", "admin"),
    ("n", "normal"),
)

class User(AbstractUser):
    user_type = models.CharField(choices=USER_TYPE, max_length=1, default='a')

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]
    objects = UserManager()

    def __str__(self):
        return self.username
