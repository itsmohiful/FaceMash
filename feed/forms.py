from django.forms import ModelForm

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model= Post
        fields = ['title','description','post_image']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field, in self.fields.items():
            field.widget.attrs.update({'class' : 'form-control'})
        
        self.fields['description'].widget.attrs.update({'rows': '4'})
