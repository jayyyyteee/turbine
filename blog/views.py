from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model= Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        data = super().get_queryset()
        return data

# def starting_page(request):
#     latest_posts = Post.objects.all().order_by("-date")
#     return render(request, "blog/index.html", {
#         'posts': latest_posts
#     })

class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name="all_posts"
    
#  def posts(request):
#     all_posts=Post.objects.all().order_by("-date")
#     return render(request, "blog/all-posts.html", {
#         'posts': all_posts
#     })


class SinglePostView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["post_tags"]=self.object.tags.all()
        return context
# def post_detail(request, slug):
#     identified_post = get_object_or_404(Post, slug=slug)
#     return render(request, "blog/post-detail.html",
#                   {'post': identified_post,
#                    'post_tags': identified_post.tags.all()})