# from django.urls import path
# from . import views
# from .views import user_signup, user_login

# urlpatterns = [
#     path('', views.home, name = 'home'),
#     path('signup/', user_signup, name='signup'),
#     path('login/', user_login, name='login'),
#     path('user_logout/',views.user_logout, name='user_logout'),
#     path('upload/', views.upload_post, name='upload_post'),
#     path('view_posts/', views.view_posts, name='view_posts'),
#     path('post/<int:pk>/', views.post_detail, name='post_detail'),
#     path('post/<int:pk>/update/', views.update_post, name='update_post'),
#     path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),
#     path('post/<int:post_id>/like/', views.like_post, name='like_post'),
#     path('post/<int:pk>/add_comment/', views.add_comment, name='add_comment'),
#     path('post/<int:pk>/view_comments/', views.view_comments, name='view_comments'),]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('upload/', views.upload_post, name='upload_post'),
    path('view_posts/', views.view_posts, name='view_posts'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/update/', views.update_post, name='update_post'),
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('post/<int:pk>/like/', views.like_post, name='like_post'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
    path('post/<int:pk>/comment/',views.add_comment, name='add_comment'),
    path('post/<int:pk>/comments/', views.view_comments, name='view_comments'),
]
