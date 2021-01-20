from django import forms
from user_app.models import MyUser


class UserEditForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['bio', 'profile_pyxz', 'tags']



class SignUpForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'profile_pyxz', 'is_staff', 'is_superuser']



class LoginForm(forms.Form):

    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
