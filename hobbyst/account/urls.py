from django.urls import path
from account.views import login_view

urlpatterns = [
    path('login/', login_view),
]