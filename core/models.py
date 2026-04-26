from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    company = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
