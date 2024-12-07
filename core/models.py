from django.db import models
from solo.models import SingletonModel



class Images(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="images/")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name if self.name else "no name"


class Contact(SingletonModel):
    address = models.CharField(max_length=255, blank=True, null=True)
    call_number = models.CharField(max_length=255, blank=True, null=True,
                                   help_text="If more than one call number, then split them with comma(,)")
    whatsap_number = models.CharField(max_length=255, blank=True, null=True,
                                      help_text="If more than one call number, then split them with comma(,)")
    map_address = models.URLField(null=True, blank=True, max_length=1000)

    def __str__(self):
        return "contact infos"


class Keyword(models.Model):
    keyword = models.CharField(max_length=200, unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.keyword
