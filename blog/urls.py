from django.urls import path, re_path
from . import views
app_name = 'blog'
urlpatterns = [
    path('blog/', views.blog, name='blog'),

    re_path(r'^detail/(?P<slug>[^/]+)/?$',
            views.blog_detail, name='blog_detail'),
]
