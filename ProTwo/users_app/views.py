from django.shortcuts import render
from users_app.models import User
# Create your views here.
def users(request):
    users_list = User.objects.order_by('name')
    users_dict = {'users_list': users_list}
    return render(request, 'users_app/users.html', context=users_dict)
