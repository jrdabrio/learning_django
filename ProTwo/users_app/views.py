from django.shortcuts import render
from users_app.models import User
from users_app import forms
# Create your views here.
def users(request):
    users_list = User.objects.order_by('name')
    users_dict = {'users_list': users_list}
    return render(request, 'users_app/users.html', context=users_dict)

def sign_up(request):
    sign_up_form = forms.FormSignUp()

    if request.method == 'POST':
        sign_up_form = forms.FormSignUp(request.POST)

        if sign_up_form.is_valid():
            new_user = User(name=sign_up_form.cleaned_data['name'],
                            last_name=sign_up_form.cleaned_data['last_name'],
                            email=sign_up_form.cleaned_data['email'])
            new_user.save()
    return render(request, 'users_app/sign_up.html', context={'form': sign_up_form})
