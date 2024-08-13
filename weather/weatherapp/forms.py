from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm as DjangoPasswordChangeForm
from django.contrib.auth.models import User

class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class PasswordChangeForm(DjangoPasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
