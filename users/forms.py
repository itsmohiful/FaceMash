from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Profile


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})



class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})



class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name','date_of_birth','bio','profile_image','cover_photo']


    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

        self.fields['bio'].widget.attrs.update({'rows':'4'})
        self.fields['date_of_birth'].widget.input_type='date'
