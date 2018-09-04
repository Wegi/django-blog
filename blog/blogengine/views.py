from django.shortcuts import render
from blogengine.models import Post
from django.core.paginator import Paginator

# Create your views here.
def all_posts(request):
    page = request.GET.get("page")
    paginator = Paginator(Post.objects.all().order_by("-pub_date"), 5)
    posts = paginator.get_page(page)
    return render(request, 'blogengine/post_overview.html', {'posts': posts})


def post(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "blogengine/post.html", {'post': post})