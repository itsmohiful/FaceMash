from django.forms import ModelForm

from .models import Comment, Post


class PostForm(ModelForm):
    class Meta:
        model= Post
        fields = ['title','description','post_image']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field, in self.fields.items():
            field.widget.attrs.update({'class' : 'form-control'})
        
        self.fields['description'].widget.attrs.update({'rows': '4'})


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field, in self.fields.items():
            field.widget.attrs.update({'class' : 'form-control'})
        
        self.fields['body'].widget.attrs.update({'rows': '3'})
