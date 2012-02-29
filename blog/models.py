from django.db import models
from tinymce import models as tinymce_models

class Post(models.Model):
    title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = tinymce_models.HTMLField()
    posted = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.title
