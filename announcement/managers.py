from django.db import models

class AnnouncentManager(models.Manager):
    def get_alive(self):
        return self.exclude(active=False)\
                    .exclude(header__isnull=True)\
                    .exclude(city__isnull=True)\
                    .exclude(author__first_name__exact='')

