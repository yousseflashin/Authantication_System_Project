from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import UserAccountManager
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.



def registerView(request):
  return render(request,'register.html')

@csrf_protect
def loginView(request):
  username=request.POST.get('username')
  email = request.POST.get('email')
  password = request.POST.get('password')
  if request.method=="POST":
      User.objects.create_user(username=username,email=email,password=password)
  return render(request,'login.html')

@csrf_protect
def profileView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')  
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
     
        user_details = User.objects.get(email=request.user.email) if request.user.is_authenticated else None    
        context = {
            'email': user_details.email if user_details else None,
            'username': user_details.username if user_details else None,
        }
        return render(request, 'profile.html', context=context)



def logoutView(request):
    logout(request)
    return render(request , 'logout.html')





  
            
 