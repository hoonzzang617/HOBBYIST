from django.urls import path
from account.views import login_view, logout_view, signup, profile

app_name = 'account'
urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup),
    path('<int:user_id>/profile/', profile, name='profile'),
]