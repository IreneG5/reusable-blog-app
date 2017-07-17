from django.conf.urls import url
import views

urlpatterns = [
    # removed 'blog/' from the beginning of the URLs to create an installable App
    url(r'^$', views.post_list, name="post_list"),
    url(r'^$/', views.post_list, name="post_list"),
    url(r'^popular/$', views.popular_post_list, name="popular_post_lists"),
    url(r'^(?P<id>\d+)/$', views.post_detail, name="views-post-detail"),
    url(r'^post/new/$', views.new_post, name='new_post'),
    url(r'^(?P<id>\d+)/edit$', views.edit_post, name="edit_post"),

]
