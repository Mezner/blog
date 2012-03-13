from django.conf.urls.defaults import *
from blog.models import Post

urlpatterns = patterns('',
    url(r'^$', 'blog.views.index'),
    url(r'^add-comment/(?P<slug>[^\.]+)', 'blog.views.add_comment'),
    url(r'^(?P<slug>[^\.]+)', 'blog.views.view_post'),
)
