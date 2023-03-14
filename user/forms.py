from django import forms
from user.models import Comment,Blog

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

class CreateBlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title','content')

        labels = {
            'title': '',
            'content': ''
        }

        widgets = {
            "title": forms.TextInput(attrs={
            'placeholder': "Enter Blog Title",
            'class': "form form-control text-center",
            'style': input_style,
            }),
            "content": forms.Textarea(attrs={
            'placeholder': "Type Your Content Here",
            'rows': 5,
            'style': f"resize:none;{input_style}",
            'class': "form form-control",
            })
        }