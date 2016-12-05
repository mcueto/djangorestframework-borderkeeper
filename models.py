# Just to keep things like ./manage.py test happy

from django.contrib.auth.models import Group
from django.db import models

class AbstractOrganization(models.Model):
    code = models.CharField(max_length=80, unique=True)
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

class Owner(AbstractOrganization):

    def __str__(self):
        return self.name

class Client(AbstractOrganization):

    def __str__(self):
        return self.name

class Instance(AbstractOrganization):
    client = models.ForeignKey(Client, blank=True, null=True)

    def __str__(self):
        return self.name
