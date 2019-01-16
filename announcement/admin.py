from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm

from .models import Announcement, City
# Register your models here.

admin.site.register(Announcement)
admin.site.register(City)