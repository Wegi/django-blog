from django.shortcuts import render
from blogengine.models import Post
from django.core.paginator import Paginator

# Create your views here.
def all_posts(request):
    page = request.GET.get("page")
    paginator = Paginator(Post.objects.all(), 5)
    posts = paginator.get_page(page)
    return render(request, 'blogengine/post_overview.html', {'posts': posts})