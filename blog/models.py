from django.db import models
from tinymce import models as tinymce_models
from autoslug import AutoSlugField

class Post(models.Model):
    title = models.CharField(max_length=120, unique=True)
    slug = AutoSlugField(populate_from='title', max_length=50, unique=True)
    body = tinymce_models.HTMLField()
    posted = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.title
