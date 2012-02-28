from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Post

def index(request):
    return render_to_response('blog/index.html', {
        'posts': Post.objects.all()
    })

def view_post(request, slug):
    return render_to_response('blog/view_post.html', {
        'post': get_object_or_404(Post, slug=slug)
    })
