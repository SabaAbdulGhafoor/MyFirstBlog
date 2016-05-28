from django.shortcuts import render

from django.utils import timezone
from .models import Post


# Create your views here.
def post_list(request):
    # from django.contrib.auth.models import User
    # User.objects.create(username='admin', password="pbkdf2_sha256$24000$ehewC577L0vp$7gbr6T/kqjtM6jUVVt26Y4hgM64phhMdhoCUFKWNLwE=", is_staff=True, is_superuser=True)
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "blog/post_list.html", {'posts': posts})
