from .models import (
    Owner,
    Client,
    Instance
)

class OwnerQuerysetFilterMixin():

    def get_queryset(self):
        print("FILTERING BY OWNER :)")

        original_queryset = self.queryset

        try:
            owner_code = self.request.META.get('HTTP_OWNER_AUTHORIZATION')
            owner = Owner.objects.get(code = owner_code)

            queryset = original_queryset.filter(owner = owner)
        except Exception as e:
            queryset = []

        return queryset


class ClientQuerysetFilterMixin():

    def get_queryset(self):
        print("FILTERING BY CLIENT :)")

        original_queryset = self.queryset

        try:
            client_code = self.request.META.get('HTTP_CLIENT_AUTHORIZATION')
            client = Client.objects.get(code = client_code)

            queryset = original_queryset.filter(client = client)
        except Exception as e:
            queryset = []

        return queryset


class InstanceQuerysetFilterMixin():

    def get_queryset(self):
        print("FILTERING BY INSTANCE :)")

        original_queryset = self.queryset

        try:
            instance_code = self.request.META.get('HTTP_INSTANCE_AUTHORIZATION')
            instance = Instance.objects.get(code = instance_code)

            queryset = original_queryset.filter(instance = instance)
        except Exception as e:
            queryset = []

        return queryset
