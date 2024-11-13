from django.urls import path
from board.views import home, comment_add, comment_delete, post_add

urlpatterns = [
    path('', home, name='home'),
    path("comment_add/", comment_add),
    path("comments/<int:comment_id>/delete/", comment_delete),
    path("post_add/", post_add),
]