from django.urls import path
from . import views


urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('articles/<int:article_pk>/comment-create/', views.comment_create, name='comment_create'),
    path('comments/<int:comment_pk>/', views.comment, name='comment'),
    path('articles/<int:article_pk>/comments/', views.article_comments, name='article_omment'),
    path('articles/<int:article_pk>/like/', views.like_article, name='like_article'),
    path('articles/<int:article_pk>/likes/', views.check_if_liked, name='check_if_liked'),
    path('comments/<int:comment_pk>/like/', views.like_comment, name='like_comment'),
    path('comments/<int:comment_pk>/likes/', views.check_comment_like, name='check_comment_like'),
]
