from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "posts/index.html", {'posts':posts})

def post_detail(request, id):
    return render(request, 'posts/detail.html')