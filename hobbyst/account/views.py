from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from account.forms import LoginForm

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('/board/')
    
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user :
                login(request, user)
                return redirect('/board/')
            else:
                print('로그인에 실패했습니다')

        context = {'form':form}
        return render(request, 'account/login.html', context)
    else:
        form = LoginForm()
        context = {'form':form}
        return render(request, 'account/login.html', context)