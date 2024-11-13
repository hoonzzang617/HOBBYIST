from django.shortcuts import render, redirect
from board.models import Post
# Create your views here.





def home(request):
    if not request.user.is_authenticated:
        return redirect('/account/login')
    posts = Post.objects.all()
    context = {'posts': posts}

    return render(request, 'board/home.html', context)

