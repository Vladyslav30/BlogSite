from django.shortcuts import render, get_object_or_404
from .models import Post
from datetime import date
# Create your views here.
def show_posts(request):
    posts = Post.objects.all()
    today_posts = [post for post in posts if post.post_date.date() == date.today()]
    count = len(today_posts)
    return render(request, 'blog/blog.html', {'posts':posts, 'count':count})

def post_details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_details.html', {'post':post})