from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy,reverse
from django.views import generic
from user.models import Blog, Comment, Category
from user.forms import CommentForm,CreateBlogForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


# # Create your views here.
# class MyBlogs(generic.ListView):
#     model = Blog
#     template_name = "user/myBlogs.html"
#     context_object_name = 'blogs'

#     def get_queryset(self, *args,**kwargs):
#         return Blog.objects.filter(author_id = self.kwargs.get('pk'))
    
@login_required
def my_blogs(request,user):

    # print(user)
    author = User.objects.filter(username=user)[0].pk
    # print(author)
    blogs = Blog.objects.all().filter(author=author, publish_date__isnull=False)
    return render(request, 'user/myBlogs.html', {'blogs':blogs,'page':'myBlogs','cat_list': Category.objects.all()})

class BlogDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
    model = Blog
    context_object_name = 'blog'
    template_name = 'user/blogDetail.html'

    def get_context_data(self, *args,**kwargs):
        contex =  super(BlogDetailView, self).get_context_data(*args,**kwargs)
        blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        liked = False
        if blog.likes.filter(pk=self.request.user.id).exists():
            liked = True
        if not blog.views.filter(pk=self.request.user.id).exists():
            blog.views.add(self.request.user)

        likes_count = blog.total_likes()
        contex['likes'] = likes_count
        contex['liked'] = liked

        return contex
    


class CreateBlogView(LoginRequiredMixin, generic.CreateView):
    login_url = '/login/'
    redirect_field_name = 'user/blogDetail.html'
    model = Blog
    template_name = 'user/createBlog.html'
    # fields = ('title','content')
    form_class = CreateBlogForm

    def form_valid(self,form):
        author_id = User.objects.filter(username = self.kwargs['user'])[0].pk
        form.instance.author_id = author_id
        return super().form_valid(form)

class UpdateBlogView(LoginRequiredMixin, generic.UpdateView):
    login_url = '/login/'
    redirect_field_name = 'user/blogDetail.html'
    model = Blog
    template_name = 'user/updateBlog.html'
    # fields = ('title','content')
    form_class = CreateBlogForm

class DraftListView(LoginRequiredMixin,generic.ListView):
    login_url = '/login/'
    # redirect_field_name = 'user/home.html'
    template_name = 'user/myBlogs.html'

    model = Blog
    context_object_name = 'blogs'

    def get_context_data(self,*args, **kwargs):
        contex =  super(DraftListView,self).get_context_data(*args,**kwargs)
        contex['cat_list'] = Category.objects.all()
        contex['page'] = "myDrafts"
        
        return contex

    def get_queryset(self):
        author = User.objects.filter(username = self.kwargs['user'])[0].pk
        # print(author)
        return Blog.objects.all().filter(author=author, publish_date__isnull=True)

class DeleteBlogView(LoginRequiredMixin,generic.DeleteView):
    model = Blog
    template_name = 'user/deleteBlog.html'
    def get_success_url(self):
        return reverse_lazy('user:myBlogs',kwargs={'user':self.kwargs['user']})
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


def CategoryView(request, category,user="",page=""):

    cat_list = Category.objects.all()
    if user != "":
        user_id = User.objects.filter(username = user)[0].pk
        data = []
        if page == "myBlogs":
            data = Blog.objects.filter(author=user_id,publish_date__isnull=False,category=category.title().replace("-"," "))
        else:
            data = Blog.objects.filter(author=user_id,publish_date__isnull=True,category=category.title().replace("-"," "))
        
        return render(request, 'user/category.html', {'category': category,'blogs':data,'cat_list':cat_list,'page':page})


    data = Blog.objects.filter(category=category.title().replace("-"," "))
    

    return render(request, 'user/category.html', {'category': category,'blogs':data,'cat_list':cat_list})

@login_required
def like_blog(request,pk):
    blog = get_object_or_404(Blog, id=pk)
    if blog.likes.filter(pk = request.user.id).exists():
        blog.likes.remove(request.user)
    else:
        blog.likes.add(request.user)

    return HttpResponseRedirect(reverse('blog-detail',kwargs={'pk':pk}))

@login_required
def profile_page(request,user):

    return render(request, 'user/profile.html', {'msg':f"Hello {user}"})