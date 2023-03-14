from django.urls import path
from main.views import HomePage
from user.views import my_blogs, CreateBlogView, UpdateBlogView, blog_publish, DraftListView, DeleteBlogView, add_a_comment, delete_comment

app_name = 'user'
urlpatterns = [
    path("",HomePage.as_view(), name='home'),
    path("myBlogs",my_blogs, name='myBlogs'),
    path("myDrafts", DraftListView.as_view(), name='myDrafts'),
    path("createBlog/<int:pk>",CreateBlogView.as_view(), name='createBlog'),
    path("edit/<int:pk>",UpdateBlogView.as_view(), name='editBlog'),
    path("publish/<int:pk>", blog_publish, name='publishBlog'),
    path("delete/<int:pk>", DeleteBlogView.as_view() , name='deleteBlog'),
    path("deleteComment/<int:pk>", delete_comment , name='deleteComment'),
    path("<str:uname>/comment/<int:pk>", add_a_comment, name='comment'),
]