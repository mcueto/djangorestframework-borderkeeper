from django.contrib import admin
from .models import (
    Owner,
    Client,
    Instance
)

admin.site.register(Owner)
admin.site.register(Client)
admin.site.register(Instance)
