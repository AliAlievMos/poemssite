from django.db import models

class Bb(models.Model):
    author = models.CharField(max_length = 20)
    poem = models.TextField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
