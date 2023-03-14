from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy,reverse
from django.views import generic
from user.models import Blog, Comment
from user.forms import CommentForm,CreateBlogForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


# Create your views here.
# class MyBlogs(generic.ListView):
#     model = Blog
#     template_name = "user/myBlogs.html"
#     context_object_name = 'blogs'

#     def get_queryset(self, *args,**kwargs):
#         return Blog.objects.filter(author = self.kwargs.get('pk'))
    
@login_required
def my_blogs(request):

    blogs = Blog.objects.all().filter(publish_date__isnull=False)
    return render(request, 'user/myBlogs.html', {'blogs':blogs})

class BlogDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
    model = Blog
    context_object_name = 'blog'
    template_name = 'user/blogDetail.html'
    


class CreateBlogView(LoginRequiredMixin, generic.CreateView):
    login_url = '/login/'
    redirect_field_name = 'user/blogDetail.html'
    model = Blog
    template_name = 'user/createBlog.html'
    # fields = ('title','content')
    form_class = CreateBlogForm

    def form_valid(self,form):
        form.instance.author_id = self.kwargs['pk']
        return super().form_valid(form)

class UpdateBlogView(LoginRequiredMixin, generic.UpdateView):
    login_url = '/login/'
    redirect_field_name = 'user/blogDetail.html'
    model = Blog
    template_name = 'user/createBlog.html'
    # fields = ('title','content')
    form_class = CreateBlogForm

class DraftListView(LoginRequiredMixin,generic.ListView):
    login_url = '/login/'
    # redirect_field_name = 'user/home.html'
    template_name = 'user/myBlogs.html'

    model = Blog
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(publish_date__isnull=True)

class DeleteBlogView(LoginRequiredMixin,generic.DeleteView):
    model = Blog
    template_name = 'user/deleteBlog.html'
    success_url = reverse_lazy('user:myBlogs')
    context_object_name = 'blog'

@login_required
def blog_publish(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.publish()
    blog.save()
    return redirect('user:home')

@login_required
def add_a_comment(request, pk,uname):
    # print(pk)
    # print(uname)
    form = CommentForm
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():

            author = User.objects.get(username = uname)
            blog = Blog.objects.get(pk = pk)
            sv = form.save(commit=False)
            sv.blog = blog
            sv.author = author
            sv.save()
            return HttpResponseRedirect(reverse('blog-detail', kwargs={'pk':pk}))
    return render(request, 'user/comment.html', {'form':form})

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    blog_pk = comment.blog.pk
    comment.delete()
    return HttpResponseRedirect(reverse('blog-detail',kwargs={'pk':blog_pk}))