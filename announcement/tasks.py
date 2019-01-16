from celery import shared_task

from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.db.utils import IntegrityError

from .models import Announcement


@shared_task
def increment_announcement_view(user_id=None, session_key=None, announce_id=None):
    if user_id:
        instance = User.objects.get(user_id)
    else:
        instance = Session.objects.get(pk=session_key)
    announce = Announcement.objects.get(pk=announce_id)

    try:
        announce.views.add(instance)
        announce.views_count += 1
        announce.save()
    except IntegrityError:
        pass