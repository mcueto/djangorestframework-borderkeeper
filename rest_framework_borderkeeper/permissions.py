from __future__ import unicode_literals
from rest_framework.permissions import BasePermission
from .models import (
    Owner,
    Client,
    Instance
)

class IsOwner(BasePermission):

    def has_permission(self, request, view):

        if request.method == 'OPTIONS':
            return True

        owner = request.META.get('HTTP_OWNER_AUTHORIZATION')

        try:
            owner = Owner.objects.get(code=owner)

            if(owner):
                return True

        except Exception as e:
            return False

class IsClient(BasePermission):

    def has_permission(self, request, view):

        if request.method == 'OPTIONS':
            return True

        client = request.META.get('HTTP_CLIENT_AUTHORIZATION')

        try:
            client = Client.objects.get(code=client)

            if(client):
                return True

        except Exception as e:
            return False

class IsInstance(BasePermission):

    def has_permission(self, request, view):

        if request.method == 'OPTIONS':
            return True

        instance = request.META.get('HTTP_INSTANCE_AUTHORIZATION')

        try:
            instance = Instance.objects.get(code=instance)

            if(instance):
                return True

        except Exception as e:
            return False
