from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
from django.conf import settings
from blog.models import Post
from recaptcha.client import captcha

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

def add_comment(request, slug):
    if request.method == 'POST':
        response = captcha.submit(
            request.POST['recaptcha_challenge_field'],
            request.POST['recaptcha_response_field'],
            settings.RECAPTCHA_PRIVATE_KEY,
            request.META["REMOTE_ADDR"])
        if response.is_valid:
            return HttpResponse('form is valid')
        return HttpResponse('form is not valid')
    else:
        return HttpResponseBadRequest()
