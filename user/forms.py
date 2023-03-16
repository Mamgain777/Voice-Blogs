from django import forms
from user.models import Comment,Blog, Category

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

        labels = {
            'text': '',
        }

        widgets ={
            'text': forms.Textarea(attrs= {
            'class': 'form form-control',
            'placeholder': 'Enter Your comment',
            'rows': 2,
            'style': 'resize:none;'
            })
        }



input_style = 'background-color: aliceblue; border: 1px solid black;'

category = Category.objects.all().values_list('name','name')
category_list = []

for item in category:
    category_list.append(item)

class CreateBlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title','title_tag', 'category','content')

        labels = {
            'title': '',
            'title_tag': '',
            'category': '',
            'content': 'Content'
        }

        widgets = {
            "title": forms.TextInput(attrs={
            'placeholder': "Enter Blog Title",
            'class': "form form-control text-center",
            'style': input_style,
            }),
            "title_tag": forms.TextInput(attrs={
            'placeholder': "Enter Blog Tag",
            'class': "form form-control text-center",
            'style': input_style,
            }),
            "category": forms.Select(choices= category_list,attrs={
            'class': "form form-select text-center",
            'style': input_style,
            }),
            "content": forms.Textarea(attrs={
            'style': f"resize:none;{input_style}",
            'class': "editable medium-editor-textarea form form-control",
            })
        }