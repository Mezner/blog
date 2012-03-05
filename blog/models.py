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

class Comment(models.Model):
    post = models.ForeignKey(Post)
    username = models.CharField(max_length=50)
    user_url = models.URLField()
    body = models.TextField()
    posted = models.DateField(auto_now=True)

    def __unicode__(self):
        return 'Post by %(username)s on %(posted)s' %\
        { "username" : self.username, "posted": self.posted }
