from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from announcement.models import Announcement, City

# Register your models here.

class UserAdmin(AdminSite):
    login_form = AuthenticationForm

    def has_permission(self, request):
        return request.user.is_active


user_admin_site = UserAdmin(name='usersadmin')



class AnnouncementAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """ Restrict user to see other users """
        if not request.user.is_superuser:
            if db_field.name == "author":
                kwargs["queryset"] = User.objects.filter(pk=request.user.pk)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        """ Restrict user to see only their own announcements """
        qs = super(AnnouncementAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    def save_model(self, request, obj, form, change):
        """ Force saving user if not superuser """
        if not request.user.is_superuser:
            obj.author = request.user
        super().save_model(request, obj, form, change)


user_admin_site.register(Announcement, AnnouncementAdmin)
user_admin_site.register(City)
