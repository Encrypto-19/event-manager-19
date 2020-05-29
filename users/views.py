from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm



# Create your views here.
class RegisterView(View):

    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form':form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print('form valid')
            form.save()
            return redirect('login')
        print('form invalid')
        return render(request, 'users/register.html', {'form':form})