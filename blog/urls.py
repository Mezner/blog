from django.conf.urls.defaults import *
from blog.models import Post
from blog.feeds import LatestEntriesFeed

urlpatterns = patterns('',
    url(r'^$', 'blog.views.index'),
    url(r'^feed$', LatestEntriesFeed()),
    url(r'^(?P<slug>[^\.]+)', 'blog.views.view_post'),
)
