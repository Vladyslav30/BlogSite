from django.shortcuts import render

# Create your views here.
def show_posts(request):
    return render(request, 'blog/blog.html')
