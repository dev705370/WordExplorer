from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from DictonaryBuilder.models import Builder

class RegistrationForm(ModelForm):
        username = forms.CharField(label=(u'User Name'))
        email = forms.EmailField(label=(u'Email Address'))
        password = forms.CharField(label=(u'Password'), widget = forms.PasswordInput(render_value = False))
        password1 = forms.CharField(label=(u'Verify Password'), widget = forms.PasswordInput(render_value = False))
        
        class Meta:
            model = Builder
            exclude = ('user',)

        def clean_username(self):
            username = self.cleaned_data['username']
            try:
                User.objects.get(username = username)   
            except User.DoesNotExist:
                return username
            raise forms.ValidationError('Username already exist. Select something else.')

        def clean(self):
            password = self.cleaned_data['password']
            password1 = self.cleaned_data['password1']
            if password != password1 :
                forms.ValidationError('Passwords does not match. Please try again.')
            else :
                return self.cleaned_data


class LoginForm(forms.Form):
    username    = forms.CharField(label = (u'Username'))
    password    = forms.CharField(label = (u'Password'), widget = forms.PasswordInput(render_value = False))
