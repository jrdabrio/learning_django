from django import forms
from users_app.models import User


class FormSignUp(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'
