from django.urls import path
from main.views import HomePage
from user.views import my_blogs, CreateBlogView, UpdateBlogView, blog_publish, DraftListView, DeleteBlogView, add_a_comment, delete_comment,CategoryView, like_blog

app_name = 'user'
urlpatterns = [
    path("",HomePage.as_view(), name='home'),
    path("<str:user>/myBlogs",my_blogs, name='myBlogs'),
    # path("myBlogs",MyBlogs.as_view(), name='myBlogs'),
    path("<str:user>/myDrafts", DraftListView.as_view(), name='myDrafts'),
    path("<str:user>/createBlog",CreateBlogView.as_view(), name='createBlog'),
    path("edit/<int:pk>",UpdateBlogView.as_view(), name='editBlog'),
    path("publish/<int:pk>", blog_publish, name='publishBlog'),
    path("like/<int:pk>", like_blog, name='likeBlog'),
    path("<str:user>/delete/<int:pk>", DeleteBlogView.as_view() , name='deleteBlog'),
    path("deleteComment/<int:pk>", delete_comment , name='deleteComment'),
    path("<str:uname>/comment/<int:pk>", add_a_comment, name='comment'),
    path("category/<str:category>", CategoryView, name='category'),
    path("<str:user>/<str:page>/<str:category>", CategoryView, name='category'),

]