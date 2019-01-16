from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Announcement
from .tasks import increment_announcement_view

# Create your views here.

class AnnouncementList(ListView):
    model = Announcement

    def get_queryset(self):
        return Announcement.objects.get_alive()


class AnnouncementDetail(DetailView):
    model = Announcement
    queryset = Announcement.objects.select_related()

    def get_object(self):
        obj = super().get_object()

        if not self.request.session.session_key:
                self.request.session.create()
        increment_announcement_view.delay(self.request.user.pk, \
                                    self.request.session.session_key,\
                                    obj.pk)

        return obj
