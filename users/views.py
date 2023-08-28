from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import LoginForm,RegistrationForm,UserEditForm,ProfileEditForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from.models import Profile
from posts.models import PostModel


# Create your views here.
def UserLogin(request):
    if request.method=="POST":
        #LoginForm instance is created and populated with the POST data submitted by the user.
        form=LoginForm(request.POST)
        if form.is_valid():
            #This extracts cleaned data from the form
            data=form.cleaned_data

            #The authenticate function is used to verify the user's credentials (username and password) against the database. 
            # If the credentials are correct, it returns a user object. If they're not correct, it returns None
            user=authenticate(request,username=data['username'],password=data['password'])
            if user is not None:

                #The login function is called to log in the user. 
                # It takes the request and the authenticated user object as arguments.
                login(request,user)
                
                #If the user's credentials are verified and the login is successful, 
                # this line returns a simple HttpResponse indicating successful login.
                return redirect('index')
            else:
                return HttpResponse('Invalid credentials')
    else:
        form=LoginForm
    return render(request,'users/login.html',{'form':form})


# index page view
@login_required
def indexpage(request):
    current_user=request.user
    posts=PostModel.objects.filter(user=current_user)
    profile=Profile.objects.filter(user=current_user).first()
    return render(request,'users/index.html',{'posts':posts,'profile':profile})


#register page view
def registerPage(request):
    if request.method=='POST':
        user_form=RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)

            return render(request,'users/registerdone.html')
    else:
        user_form=RegistrationForm()
    return render(request,'users/register.html',{'user_form':user_form})

#edit page view
@login_required
def edit(request):
    if request.method=='POST':
        user_form=UserEditForm(instance=request.user,data=request.POST)
        profile_form=ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

    else:
        user_form=UserEditForm(instance=request.user)
        profile_form=ProfileEditForm(instance=request.user.profile)

    return render(request,'users/edit.html',{'user_form':user_form,'profile_form':profile_form})    
