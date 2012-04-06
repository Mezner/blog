from django.contrib.syndication.views import Feed
from blog.models import Post

class LatestEntriesFeed(Feed):
    title = "Russell Myers - Blog"
    link = "http://russellmyers.com/blog/"
    description = "Latest technical blog posts by Russell Myers"

    def items(self):
        return Post.objects.order_by('-posted')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_link(self, item):
        return "http://russellmyers.com/blog/%s" % item.slug
