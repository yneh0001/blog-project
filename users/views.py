from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():  #check the validity
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  #after regiestering, user is redirected to the home page
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        userForm = UserUpdateForm(request.POST, instance=request.user)
        profileForm = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            profileForm.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')     
            
            #if no new data, keep the old data in the form
    else:
        userForm = UserUpdateForm(instance=request.user)
        profileForm = ProfileUpdateForm(instance=request.user.profile)       

        #if no new data, keep the old data in the form

    context = {
        'userForm': userForm,
        'profileForm': profileForm
    }

    return render(request, 'users/profile.html', context)