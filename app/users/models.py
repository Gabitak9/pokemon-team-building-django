"""Users models."""

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """Profile model.

    Proxy model that extends the base data with other
    information.
    """
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    date_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        """Return username."""
        return self.user.username