from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from blog.models import Post
from blog.forms import CommentForm

def index(request):
    return render_to_response('blog/index.html', {
        'posts': Post.objects.order_by('-posted')[:10]
    })

def view_post(request, slug):
    form = CommentForm()
    return render_to_response('blog/view_post.html',
    context_instance = RequestContext(request, {
        'form': form,
        'post': get_object_or_404(Post, slug=slug),
        'posts': Post.objects.order_by('-posted')[:10]
    }))
