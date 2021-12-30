from django.db import models


class Contact(models.Model):
    """A model to save the contact form"""

    full_name = models.CharField(max_length=60, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    subject = models.CharField(max_length=60, blank=False)
    message = models.CharField(blank=False, max_length=1500)

    def __str__(self):
        return self.full_name
