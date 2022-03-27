from django import forms
from CustomUser.models import Users


class UsersCreationForm(forms.ModelForm):
    """Custom user creation form for CustomUser.models
    Includes email, first_name, last_name,etc...
    """
    password = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label='password2', widget=forms.PasswordInput)
    email = forms.EmailField(label="email")
    username = forms.CharField(max_length=60)

    class Meta:
        model: Users
        fields: ['first_name','last_name', 'birth_date']

    def __init__(self, *args, **kwargs):
        super( self, *args, **kwargs)
