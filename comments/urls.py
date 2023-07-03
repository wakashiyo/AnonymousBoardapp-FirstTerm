from django.urls import path
from . import views


app_name = 'comments'
urlpatterns = [
    path('', views.comments_index, name='index'),
    path('<int:comment_id>/', views.comments_show, name='show'),
    path('create/', views.comments_create, name='create'),
    path('<int:comment_id>/update/', views.comments_update, name='update'),
    path('<int:comment_id>/delete/', views.comments_delete, name='delete'),
    path('<int:comment_id>/reply/', views.comments_reply, name='reply'),
]