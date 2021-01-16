from django import forms
from user_app.models import MyUser


class UserEditForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['bio', 'profile_pyxz', 'tags']


class SignUpForm(forms.Form):

    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):

    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
