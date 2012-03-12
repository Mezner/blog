from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from blog.models import Post

def index(request):
    return render_to_response('blog/index.html', {
        'posts': Post.objects.order_by('-posted')[:10]
    })

def view_post(request, slug):
    return render_to_response('blog/view_post.html',
    context_instance = RequestContext(request, {
        'post': get_object_or_404(Post, slug=slug),
        'posts': Post.objects.order_by('-posted')[:10]
    }))
