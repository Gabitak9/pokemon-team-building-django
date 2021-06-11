"""Pokemon Team models."""

from django.contrib.auth.models import User
from django.db import models
import uuid


class Team(models.Model):
    """Pokemon Team model.

    """
    team_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    
    id_pokemon_1 = models.PositiveIntegerField(default=0)
    id_pokemon_2 = models.PositiveIntegerField(default=0)
    id_pokemon_3 = models.PositiveIntegerField(default=0)
    id_pokemon_4 = models.PositiveIntegerField(default=0)
    id_pokemon_5 = models.PositiveIntegerField(default=0)
    id_pokemon_6 = models.PositiveIntegerField(default=0)


    def __str__(self):
        """Return team id."""
        return self.team_uuid