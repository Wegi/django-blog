from django.shortcuts import render
from blogengine.models import Post

# Create your views here.
def all_posts(request):
    return render(request, 'blogengine/post_overview.html', {'posts': Post.objects.all()})