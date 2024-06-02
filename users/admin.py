from django.contrib import admin

# Register your models here.
from .models import CustomUser, Registrant

admin.site.register(CustomUser)
admin.site.register(Registrant)
